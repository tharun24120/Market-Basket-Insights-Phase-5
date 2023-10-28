data['Items'] = data['Items'].str.split(', ')
data = pd.get_dummies(data['Items'].apply(pd.Series).stack()).sum(level=0)
