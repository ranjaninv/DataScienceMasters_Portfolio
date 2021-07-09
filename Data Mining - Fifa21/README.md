## Fifa21 - Players Analysis 

![image](https://user-images.githubusercontent.com/44445092/125036466-a4b4fa80-e058-11eb-801f-6d4d49780e7a.png)

### Introduction


### Data Understanding

1. Source - https://www.kaggle.com/ekrembayar/fifa-21-complete-player-datasets
2. The data set has players data for 2021 season and contains 107 columns and 17125 rows.
3. This data set has players data for 2021 season and contains 107 columns and 17125 rows. The data describes players attributes like name, height, weight, age, club association, nationality, playing position, wage, contract details, and various performance data.

### EDA (Exploratory Data Analysis)

1. Below set of histograms show the distribution of players age, overall score (OVA), total stats, and potential (POT). It shows very trends such as maximum players are within age range of 20- 24.

      

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
