## Credit Card Fraud Prediction

### Introduction

Credit cards and electronic payments make overall functioning in a global marketplace much easier. Each year financial institutions lost a chunk of money as a result of credit card fraud. In year 2018, a total of $24.26 Billion was lost due to payment card fraud across the globe and United States being the most fraud prone country. Credit card fraud was ranked number one type of identity theft fraud. Credit card fraud increased by 18.4 percent in 2018 and is still climbing. Credit card fraud includes fraudulent transactions on a credit card or debit card. One of the challenges behind fraud detection is that frauds are far less common as compared to legal transactions. After initial struggle to find a good dataset, came across the dataset on Kaggle which was considerably good to be able to build and train our model. As part of this project, built a few models for fraud detection using anonymized credit card transaction data.

### Data Understanding

Dataset link - https://www.kaggle.com/mlg-ulb/creditcardfraud

The dataset contains transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. It contains only numerical input variables which are the result of a PCA transformation.

Attribute Information:
  1) Time-Numberofsecondselapsedbetweenthistransactionandthefirst transaction in the dataset.
  2) V1- V28 – These are the result of a PCA Dimensionality reduction to protect user identities and sensitive features.
  3) Amount–Transactionamount
  4) Class – This is a response variable and has the values of 1 for fraudulent transactions, and 0 for non-fraudulent transactions.
  
There are 29 decimal fields and 2 integer fields in the dataset.

The source dataset is clean and contains only numerical input variables which are the result of a PCA transformation. Hence, there wasn’t much scope with regards to data cleaning and preparation.

### Modeling

This dataset is severely imbalanced as most of the transactions are non-fraudulent. So, the algorithms are much likely to classify new observations to the majority class and high accuracy won't tell us anything. To address the problem of imbalanced dataset, we choose to use oversampling data approach technique. Oversampling increases the number of minority class members in the training set. In order to make our data set balanced, we are using a type of oversampling called SMOTE (Synthetic Minority Oversampling Technique) and by doing that we are not losing any information from the original training set as all the observations from the minority and majority classes are retained. SMOTE works by utilizing a k-nearest neighbor algorithm to create synthetic data.

Using the new balanced dataset, performed feature selection which helped to select the features in our dataset which contributes most to the target variable. Using SelectKBest technique, determined 10 best features for the model. This step helps to improve the model accuracy and reduces training time.

For the model selection, compared 4 models namely logistic regression, Random Forest classifier, decision tree classifier and SGD classifier. Based on their roc_auc scores, selected randon forest and logistic regression models. 

### Conclusion

1. As proven by SelectKBest, transaction time does not have any influence on prediction of fraudulent transaction.
2. SMOTE oversampling technique helped overcome the Imbalanced datasets challenge.
3. Using Random Forest Model our model will correctly predict if the transaction was fraudulent or not 98.528% of the time.
4. Logistic Regression Model our model will correctly predict if the transaction was fraudulent or not 98.032% of the time.
5. Random forest model has less false positives than logistic regression making it a better model.
