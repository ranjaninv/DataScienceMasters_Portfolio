## Fifa21 - Players Analysis & Prediction 

![image](https://user-images.githubusercontent.com/44445092/125036466-a4b4fa80-e058-11eb-801f-6d4d49780e7a.png)

### Introduction

FIFA (Fédération Internationale de Football Association) is the governing body of the association football. FIFA periodically releases players statistics. These statistics are very important and depicts every aspect of the players performance.

As part of this case study, I will be applying data mining and visualization techniques learnt during this course. With graph analysis, various trends and patterns related to players and their performance will be identified. Based on the various players performance data, I’ll try to predict if a player will be able to have an overall score of greater than 80. The intent is also to find which all features are most important in order to make that prediction. Player’s performance data is used by various soccer clubs to sign up new players or buy players contracts from other clubs. This prediction model can be used by club managers and recruiters to identify new players and predict if they will have high overall scores.

### Data Understanding

1. Source - https://www.kaggle.com/ekrembayar/fifa-21-complete-player-datasets
2. The data set has players data for 2021 season and contains 107 columns and 17125 rows.
3. This data set has players data for 2021 season and contains 107 columns and 17125 rows. The data describes players attributes like name, height, weight, age, club association, nationality, playing position, wage, contract details, and various performance data.

### EDA (Exploratory Data Analysis)

1. Below set of histograms show the distribution of players age, overall score (OVA), total stats, and potential (POT). It shows very trends such as maximum players are within age range of 20- 24.

      <img width="844" alt="image" src="https://user-images.githubusercontent.com/44445092/125153054-e3a98580-e116-11eb-9c5a-bf6b2153f9bf.png">

2. Below set of bar charts do show the comparison of counts for left foot vs right foot, Playing positions, International reputation, and Skills moves.

    <img width="851" alt="image" src="https://user-images.githubusercontent.com/44445092/125153074-0176ea80-e117-11eb-8d6c-8f0bbd81d9eb.png">

3. Below chart shows nation wise count of players and UK has the highest number of players.
  
    <img width="827" alt="image" src="https://user-images.githubusercontent.com/44445092/125153080-15225100-e117-11eb-8d30-841b929bd8fe.png">

4. Below stacked bar charts show how left foot vs right foot players are distributed across features of playing position, skills moves (SM), International reputation (IR).

    <img width="857" alt="image" src="https://user-images.githubusercontent.com/44445092/125153112-3a16c400-e117-11eb-9ffb-6aa59fb71f31.png">

### Modeling & Evaluation

1. Applied feature selection, 10 best features in my Fifa 21 dataset to predict if a player would have an overall score of more than 80.

    <img width="360" alt="image" src="https://user-images.githubusercontent.com/44445092/125153367-d392a580-e118-11eb-896f-07db5a7f4fdd.png">

2. Evaluated RandomForestClassifier, DecisionTreeClassifier, SGDClassifie & LogisticRegression. 
3. Based on AUROC score, RandomForestClassifier and LogisticRegression would be most accurate to predict if a player would have an overall score of more than 80.
4. Below is the result with logistical regression:

    <img width="592" alt="image" src="https://user-images.githubusercontent.com/44445092/125153515-d8a42480-e119-11eb-8f25-c8f414bed583.png">
    
5. Below is the result with Random Forest model:

    <img width="602" alt="image" src="https://user-images.githubusercontent.com/44445092/125153530-fa9da700-e119-11eb-9902-d22d0164f2e1.png">
    
### Conclusion

1. Highest number of players are within age range of 20-24.
2. It is evident here that a large percentage of players are right foot dominant and there are large number of midfielders compared to other playing positions.
3. International reputation of 3*/4* are not so common among players and very few have 5 * rating.
4. UK has the highest number of players based on Nation wise distribution.
5. When compared between models, logistical regression and random forest models were the best model.
6. And looking at the confusion matrix between logistical regression and random forest model, random forest model seems to have performed slightly better.
