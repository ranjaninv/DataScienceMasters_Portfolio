## Wine Reviews - EDA

![image](https://user-images.githubusercontent.com/44445092/125156013-e3b28100-e128-11eb-8616-a9ec2f9ba832.png)

### Introduction

Wine, a much loved alcoholic drink has been produced and enjoyed since thousands of years. It is typically made from fermented grapes. Different varieties of grapes and strains of yeasts produce different styles of wine. This dataset consists of details of 129971 wines reviews produced across the globe by different wineries. I performed EDA on the wine reviews dataset by analyzing the variables in the dataset, also performed statistical functions to uncover some insights from the dataset.

### Data Understanding

- Dataset link - https://www.kaggle.com/mlg-ulb/creditcardfraud
- Wine reviews dataset has 14 columns and 129971 Rows.

### Data Cleanup



### EDA (Exploratory Data Analysis)

1. Scatter Plot of price and points of the wines.
    
    <img width="473" alt="image" src="https://user-images.githubusercontent.com/44445092/125156744-b23bb480-e12c-11eb-8e8d-140adaaa8d59.png">

2. Histogram of wine scores/price and comparison of US and French wines.

    <img width="574" alt="image" src="https://user-images.githubusercontent.com/44445092/125156632-15791700-e12c-11eb-95fd-1a81d10b8fff.png">

3. Below histogram suggests that most of the US Wines are having a score of 91.
  
    <img width="433" alt="image" src="https://user-images.githubusercontent.com/44445092/124867723-37379a00-df84-11eb-9db9-6cd02bd9fdd0.png">

4. Below histogram suggests that most of the US Wines are having a score of 91.

    <img width="582" alt="image" src="https://user-images.githubusercontent.com/44445092/125156670-53763b00-e12c-11eb-8455-7d7bb2a9177f.png">

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
