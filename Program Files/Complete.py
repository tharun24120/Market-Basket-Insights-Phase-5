import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import matplotlib.pyplot as plt
data = pd.DataFrame({
    'TransactionID': [1, 2, 3, 4, 5],
    'Items': [
        'milk, bread, eggs',
        'bread, eggs',
        'milk, bread',
        'milk, eggs',
        'milk, bread, eggs, beer'
    ]
})
data['Items'] = data['Items'].str.split(', ')
data = pd.get_dummies(data['Items'].apply(pd.Series).stack()).sum(level=0)
frequent_itemsets = apriori(data, min_support=0.5, use_colnames=True)
association_rules_df = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
filtered_rules = association_rules_df[(association_rules_df['lift'] >= 1.0) & (association_rules_df['confidence'] >= 0.7)]
print(filtered_rules)
plt.scatter(filtered_rules['support'], filtered_rules['confidence'], alpha=0.5)
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.title('Support vs. Confidence')
plt.show()
