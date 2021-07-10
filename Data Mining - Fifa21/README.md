## Fifa21 - Players Analysis & Prediction 

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

1. Highest number of players are within age range of 20-24.
2. It is evident here that a large percentage of players are right foot dominant and there are large number of midfielders compared to other playing positions.
3. International reputation of 3*/4* are not so common among players and very few have 5 * rating.
4. UK has the highest number of players based on Nation wise distribution.
5. When compared between models, logistical regression and random forest models were the best model.
6. And looking at the confusion matrix between logistical regression and random forest model, random forest model seems to have performed slightly better.
