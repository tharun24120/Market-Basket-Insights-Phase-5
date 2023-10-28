filtered_rules = association_rules_df[(association_rules_df['lift'] >= 1.0) & (association_rules_df['confidence'] >= 0.7)]
print(filtered_rules)
plt.scatter(filtered_rules['support'], filtered_rules['confidence'], alpha=0.5)
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.title('Support vs. Confidence')
plt.show()