DROP TABLE IF EXISTS receipt_item CASCADE;
DROP TABLE IF EXISTS fetch_user CASCADE;
DROP TABLE IF EXISTS rewards_product_partner CASCADE;
DROP TABLE IF EXISTS brand CASCADE;
DROP TABLE IF EXISTS receipt CASCADE;
DROP TABLE IF EXISTS cpg CASCADE;
CREATE TABLE IF NOT EXISTS fetch_user (
	id TEXT PRIMARY KEY,
	user_state TEXT,
	created_date TIMESTAMP,
	last_login TIMESTAMP,
	user_role TEXT,
	sign_up_source TEXT,
	active BOOL
);


CREATE TABLE IF NOT EXISTS rewards_product_partner (
	id TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS receipt (
    id TEXT PRIMARY KEY,
    bonus_points_earned TEXT,
    bonus_points_earned_reason TEXT,
    create_date TIMESTAMP,
    date_scanned TIMESTAMP,
    finished_date TIMESTAMP,
    modify_date TIMESTAMP,
    points_awarded_date TIMESTAMP,
    points_earned TEXT,
    purchase_date TIMESTAMP,
    purchased_item_count TEXT,
    rewards_receipt_status TEXT,
    total_spent DOUBLE PRECISION,
	user_id TEXT
    --user_id TEXT REFERENCES fetch_user (id) - can't use because missing ids in fetch_user
);

CREATE INDEX IF NOT EXISTS i_user_id ON receipt(user_id);

CREATE TABLE IF NOT EXISTS receipt_item (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	receipt_id TEXT REFERENCES receipt (id),
    barcode TEXT,
    description TEXT,
    final_price TEXT,
    item_price TEXT,
	needs_fetch_review TEXT,
	partner_item_id TEXT,
	prevent_target_gap_points TEXT,
	quantity_purchased DOUBLE PRECISION,
	user_flagged_barcode TEXT,
	user_flagged_new_item TEXT,
	user_flagged_price TEXT,
	user_flagged_quantity DOUBLE PRECISION,
	needs_fetch_review_reason TEXT,
	points_not_awarded_reason TEXT,
	points_payer_id TEXT REFERENCES rewards_product_partner(id),
	rewards_group TEXT,
	rewards_product_partner_id TEXT REFERENCES rewards_product_partner (id),
	user_flagged_description TEXT,
	original_metabrite_barcode TEXT,
	original_metabrite_description TEXT,
	brand_code TEXT,
	competitor_rewards_group TEXT,
	discounted_item_price TEXT,
	original_receipt_item_text TEXT,
	item_number TEXT,
	original_metabrite_quantity_purchased DOUBLE PRECISION,
	points_earned TEXT,
	target_price TEXT,
	competitive_product TEXT,
	original_final_price TEXT,
	original_metabrite_item_price TEXT,
	deleted TEXT,
	price_after_coupon TEXT,
	metabrite_campaign_id TEXT
);

CREATE INDEX IF NOT EXISTS i_receipt_id ON receipt_item(receipt_id);

CREATE TABLE IF NOT EXISTS brand (
	id TEXT PRIMARY KEY,
    barcode TEXT,
    brand_code TEXT,
    category TEXT,
    category_code TEXT,
	cpg_id TEXT,
	top_brand TEXT,
	"name" TEXT
);

CREATE TABLE IF NOT EXISTS cpg (
	id TEXT PRIMARY KEY,
	"ref" TEXT
);