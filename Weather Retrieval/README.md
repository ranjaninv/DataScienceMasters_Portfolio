## Weather Retrieval

![image](https://user-images.githubusercontent.com/44445092/125156013-e3b28100-e128-11eb-8616-a9ec2f9ba832.png)

### Introduction

Wine, a much loved alcoholic drink has been produced and enjoyed since thousands of years. It is typically made from fermented grapes. Different varieties of grapes and strains of yeasts produce different styles of wine. This dataset consists of details of 129971 wines reviews produced across the globe by different wineries. I performed EDA on the wine reviews dataset by analyzing the variables in the dataset, also performed statistical functions to uncover some insights from the dataset.

### Data Understanding

- Dataset link - https://www.kaggle.com/mlg-ulb/creditcardfraud
- Wine reviews dataset has 14 columns and 129971 Rows.

### Data Cleanup

- Below is the snapshot of missing data in the dataset:
    - There are 9 columns that have missing values.
    - There is 1 column having greater than 50% missing values.
    - There is 1 column having greater than 40% missing values.
    - There is 1 column having greater than 30% missing values.
    - There are 4 columns having greater than 20% missing values. 
    - There are 5 columns having greater than 10% missing values.

- There are duplicates in the description field, therefore we need to remove them.
- First variable “"Unnamed: 0” in the data frame is just the serial #, therefore it is safe to remove
them as there is no benefit of it to provide insight about data.
- We also need to remove the region2 from data frame since majority of it is not having any value.
- We also need to null values from the dataframe.
- There are 47660 rows and 11 columns, after all the cleanup and removing all rows with null
values.

### EDA (Exploratory Data Analysis)

1. Scatter Plot of price and points of the wines.
    
    <img width="473" alt="image" src="https://user-images.githubusercontent.com/44445092/125156744-b23bb480-e12c-11eb-8e8d-140adaaa8d59.png">

2. Histogram of wine scores/price and comparison of US and French wines.

    <img width="574" alt="image" src="https://user-images.githubusercontent.com/44445092/125156632-15791700-e12c-11eb-95fd-1a81d10b8fff.png">

3. Below histogram suggests that most of the US Wines are having a score of 91.
  
    <img width="580" alt="image" src="https://user-images.githubusercontent.com/44445092/125156785-ee6f1500-e12c-11eb-96fb-a8a23d58cbd2.png">

4. Below histogram suggests that most of the French wines are having a score of 88.5.

    <img width="594" alt="image" src="https://user-images.githubusercontent.com/44445092/125156813-0f376a80-e12d-11eb-8e02-d4d098010804.png">

5. PMF of wine scores.

    <img width="574" alt="image" src="https://user-images.githubusercontent.com/44445092/125156845-4148cc80-e12d-11eb-94c1-a2825d4e8f81.png">

6. CDF of price between US and French wines which have score greater than 90.

    <img width="561" alt="image" src="https://user-images.githubusercontent.com/44445092/125156894-866cfe80-e12d-11eb-94ff-7d82ea6bbf42.png">

    

### Modeling & Evaluation

1. Created a model to predict the price of the wine based on the score of the wine. And based on it, tried to predict what might be the price of a wine which has a score of 97.

    <img width="547" alt="image" src="https://user-images.githubusercontent.com/44445092/125156959-d2b83e80-e12d-11eb-9bcc-0a184fa05a49.png">

### Conclusion

- One of the biggest challenge I faced was that I only had 2 numeric variables (price and points) to play with.
