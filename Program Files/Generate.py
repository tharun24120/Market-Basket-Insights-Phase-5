association_rules_df = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
