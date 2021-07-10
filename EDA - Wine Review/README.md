## Wine Reviews - EDA

![image](https://user-images.githubusercontent.com/44445092/125156013-e3b28100-e128-11eb-8616-a9ec2f9ba832.png)

### Introduction

Wine, a much loved alcoholic drink has been produced and enjoyed since thousands of years. It is typically made from fermented grapes. Different varieties of grapes and strains of yeasts produce different styles of wine. This dataset consists of details of 129971 wines reviews produced across the globe by different wineries. We would be performing EDA on the wine reviews dataset by analyzing the variables in the dataset. We would be performing statistical functions to uncover some insights from the dataset.

### Data Understanding

- Dataset link - https://www.kaggle.com/mlg-ulb/creditcardfraud
- Wine reviews dataset has 14 columns and 129971 Rows.
The dataset contains transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. It contains only numerical input variables which are the result of a PCA transformation.
  
There are 29 decimal fields and 2 integer fields in the dataset.

The source dataset is clean and contains only numerical input variables which are the result of a PCA transformation. Hence, there wasn’t much scope with regards to data cleaning and preparation.

### EDA (Exploratory Data Analysis)

1. Distribution of fraudulent transactions amounts

    <img width="412" alt="image" src="https://user-images.githubusercontent.com/44445092/124867647-1bcc8f00-df84-11eb-811f-a02235b29dce.png">

2. Distribution of transaction times

    <img width="557" alt="image" src="https://user-images.githubusercontent.com/44445092/124867696-2ab34180-df84-11eb-8817-c997c49d9f96.png">

3. Fraud vs Non-Fraud
  
    <img width="433" alt="image" src="https://user-images.githubusercontent.com/44445092/124867723-37379a00-df84-11eb-9db9-6cd02bd9fdd0.png">


### Modeling & Evaluation

1. Target variable is "Class", therefore classification model will be applied. 
2. In order to overcome the challenges with imbalanced dataset, we applied oversampling technique called SMOTE. 
3. Identified all the key features using SelectKBest
4. Compared the models based roc_auc score. 

    <img width="218" alt="image" src="https://user-images.githubusercontent.com/44445092/124868006-bfb63a80-df84-11eb-843c-85512e616701.png">

### Conclusion

1. As proven by SelectKBest, transaction time does not have any influence on prediction of fraudulent transaction.
2. SMOTE oversampling technique helped overcome the Imbalanced datasets challenge.
3. Using Random Forest Model our model will correctly predict if the transaction was fraudulent or not 98.528% of the time.
4. Logistic Regression Model our model will correctly predict if the transaction was fraudulent or not 98.032% of the time.
5. Random forest model has less false positives than logistic regression making it a better model.
