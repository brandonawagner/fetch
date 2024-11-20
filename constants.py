users_column_mapping = {
    '_id': 'id',
    'active': 'active',
    'createdDate': 'created_date',
    'lastLogin': 'last_login',
    'role': 'user_role',
    'signUpSource': 'sign_up_source',
    'state': 'user_state'
}

reciept_column_mapping = {
    '_id': 'id',
    'bonusPointsEarned': 'bonus_points_earned',
    'bonusPointsEarnedReason': 'bonus_points_earned_reason',
    'createDate': 'create_date',
    'dateScanned': 'date_scanned',
    'finishedDate': 'finished_date',
    'modifyDate': 'modify_date',
    'pointsAwardedDate': 'points_awarded_date',
    'pointsEarned': 'points_earned',
    'purchaseDate': 'purchase_date',
    'purchasedItemCount': 'purchased_item_count',
    'rewardsReceiptStatus': 'rewards_receipt_status',
    'totalSpent': 'total_spent',
    'userId': 'user_id'
}

reciept_item_column_mapping = {
    '_id': 'receipt_id',
    'barcode': 'barcode',
    'description': 'description',
    'finalPrice': 'final_price',
    'itemPrice': 'item_price',
    'needsFetchReview': 'needs_fetch_review',
    'partnerItemId': 'partner_item_id',
    'preventTargetGapPoints': 'prevent_target_gap_points',
    'quantityPurchased': 'quantity_purchased',
    'userFlaggedBarcode': 'user_flagged_barcode',
    'userFlaggedNewItem': 'user_flagged_new_item',
    'userFlaggedPrice': 'user_flagged_price',
    'userFlaggedQuantity': 'user_flagged_quantity',
    'needsFetchReviewReason': 'needs_fetch_review_reason',
    'pointsNotAwardedReason': 'points_not_awarded_reason',
    'pointsPayerId': 'points_payer_id',
    'rewardsGroup': 'rewards_group',
    'rewardsProductPartnerId': 'rewards_product_partner_id',
    'userFlaggedDescription': 'user_flagged_description',
    'originalMetaBriteBarcode': 'original_metabrite_barcode',
    'originalMetaBriteDescription': 'original_metabrite_description',
    'brandCode': 'brand_code',
    'competitorRewardsGroup': 'competitor_rewards_group',
    'discountedItemPrice': 'discounted_item_price',
    'originalReceiptItemText': 'original_receipt_item_text',
    'itemNumber': 'item_number',
    'originalMetaBriteQuantityPurchased': 'original_metabrite_quantity_purchased',
    'pointsEarned': 'points_earned',
    'targetPrice': 'target_price',
    'competitiveProduct': 'competitive_product',
    'originalFinalPrice': 'original_final_price',
    'originalMetaBriteItemPrice': 'original_metabrite_item_price',
    'deleted': 'deleted',
    'priceAfterCoupon': 'price_after_coupon',
    'metabriteCampaignId': 'metabrite_campaign_id'
}
cpg_column_mapping = {
    '$id.$oid': 'id',
    '$ref': 'ref'
}

rewards_product_partner_column_mapping = {
    'rewardsProductPartnerId': 'id'
}

brand_column_mapping = {
    '_id': 'id',
    'barcode': 'barcode',
    'category': 'category',
    'categoryCode': 'category_code',
    'name': 'name',
    'topBrand': 'top_brand',
    'brandCode': 'brand_code',
    '$id.$oid': 'cpg_id',
}