import pandas as pd
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import constants as c


def to_date(x):
    """
    Convert dataframe date from Unix timestamp  into a human-readable date.

    Args:
        x (object): The JSON object column

    Returns:
        date: human-readable date or None
    """
    try:
        return pd.to_datetime(x['$date'], unit='ms', errors='coerce')
    except TypeError:
        return None


def truncate_all(eng):
    """
    Convert dataframe date column date into a human readability date.

    Args:
        eng (object): SQL engine object

    Returns:
        None
    """
    with eng.begin() as con:
        con.execute(text('TRUNCATE TABLE fetch_user RESTART IDENTITY CASCADE'))
        con.execute(text('TRUNCATE TABLE receipt_item RESTART IDENTITY CASCADE'))
        con.execute(text('TRUNCATE TABLE receipt RESTART IDENTITY CASCADE'))
        con.execute(text('TRUNCATE TABLE cpg RESTART IDENTITY CASCADE'))
        con.execute(text('TRUNCATE TABLE brand RESTART IDENTITY CASCADE'))
        con.execute(text('TRUNCATE TABLE rewards_product_partner RESTART IDENTITY CASCADE'))


if __name__ == '__main__':
    load_dotenv(os.path.abspath('./.env'))

    db_user = os.environ['DB_USER']
    db_password = os.environ['DB_PASSWORD']
    db_host = os.environ['DB_HOST']
    db_port = os.environ['DB_PORT']
    db_name = os.environ['DB_NAME']

    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    # load files
    brands = pd.read_json('./files/brands.json.gz', compression='gzip', lines=True)
    receipts = pd.read_json('./files/receipts.json.gz', compression='gzip', lines=True)

    # there was an issue extracting gzip in code for users
    users = pd.read_json('./files/users.json', lines=True)

    # truncate all tables before appending
    truncate_all(engine)

    # user
    users['_id'] = users['_id'].apply(lambda x: x['$oid'])
    users['createdDate'] = users['createdDate'].apply(lambda x: to_date(x))
    users['lastLogin'] = users['lastLogin'].apply(lambda x: to_date(x))

    # duplicates keys exists
    users = users.drop_duplicates()
    users = users.rename(columns=c.users_column_mapping)

    users.to_sql('fetch_user', engine, if_exists='append', index=False)

    # rewards product partner and receipt
    receipts_list = receipts.explode('rewardsReceiptItemList')
    receipts_list = pd.json_normalize(receipts_list['rewardsReceiptItemList'])

    # rewards_product_partner
    rpp = receipts_list[receipts_list['rewardsProductPartnerId'].notna()]
    rpp = rpp[['rewardsProductPartnerId']]
    rpp = rpp.rename(columns=c.rewards_product_partner_column_mapping)

    rpp = rpp.drop_duplicates()
    rpp.to_sql('rewards_product_partner', engine, if_exists='append', index=False)

    # receipt and receipt item
    receipts_item = receipts.explode('rewardsReceiptItemList')
    receipts = receipts.drop('rewardsReceiptItemList', axis=1)

    receipts['_id'] = receipts['_id'].apply(lambda x: x['$oid'])
    receipts['createDate'] = receipts['createDate'].apply(lambda x: to_date(x))
    receipts['dateScanned'] = receipts['dateScanned'].apply(lambda x: to_date(x))
    receipts['finishedDate'] = receipts['finishedDate'].apply(lambda x: to_date(x))
    receipts['modifyDate'] = receipts['modifyDate'].apply(lambda x: to_date(x))
    receipts['pointsAwardedDate'] = receipts['pointsAwardedDate'].apply(lambda x: to_date(x))
    receipts['purchaseDate'] = receipts['purchaseDate'].apply(lambda x: to_date(x))

    receipts_item = pd.json_normalize(receipts_item['rewardsReceiptItemList'])
    receipts_item = pd.concat([receipts[['_id']], receipts_item], axis=1)

    receipts = receipts.rename(columns=c.reciept_column_mapping)
    receipts.to_sql('receipt', engine, if_exists='append', index=False)

    receipts_item = receipts_item.rename(columns=c.reciept_item_column_mapping)
    receipts_item.to_sql('receipt_item', engine, if_exists='append', index=False)

    # cpg and brands
    brands['_id'] = brands['_id'].apply(lambda x: x['$oid'])
    cpg = pd.json_normalize(brands['cpg'])
    brands = pd.concat([brands, cpg], axis=1)
    brands = brands.drop('cpg', axis=1)
    brands = brands.drop('$ref', axis=1)

    brands = brands.rename(columns=c.brand_column_mapping)
    brands.to_sql('brand', engine, if_exists='append', index=False)

    cpg = cpg.rename(columns=c.cpg_column_mapping)
    cpg = cpg.drop_duplicates(subset='id')

    cpg.to_sql('cpg', engine, if_exists='append', index=False)
