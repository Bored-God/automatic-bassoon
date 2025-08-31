# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# %%
training_data = pd.read_csv('/workspaces/automatic-bassoon/mnist_train.csv')
testing_data = pd.read_csv('/workspaces/automatic-bassoon/mnist_test.csv')

# %%
training_data.head()

# %%
a = training_data.iloc[4,1:].values  

# %%
a = a.reshape(28,28).astype('uint8')
plt.imshow(a)

# %%
#Creating the train and test splits.
df_train = training_data.iloc[:,1:]
train_labels = training_data.iloc[:, 0]
df_test = testing_data.iloc[:, 1:]
test_labels = testing_data.iloc[:10000, 0]
test_labels = test_labels.to_numpy()
test_labels

# %%
a = df_train.iloc[2,:].values
a = a.reshape(28,28).astype('uint8')
plt.imshow(a)

# %%
#call rf classifier
rf = RandomForestClassifier(n_estimators=100)

# %%
rf.fit(df_train,train_labels)


# %%
pred = rf.predict(df_test)

# %%
pred

# %%
pred == test_labels

# %%
#checking preds acc
pred = np.array(pred).ravel()
count = np.sum(pred == test_labels)
print(count, "out of", len(test_labels))
print(f"{count/len(test_labels)*100}%")



