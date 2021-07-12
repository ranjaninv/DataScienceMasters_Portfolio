## Wine reviews - Data Preparation

![Winery1](https://user-images.githubusercontent.com/44445092/125221602-0f02b080-e28e-11eb-8b57-9e27b12a841e.jpeg)

### Introduction

Wine, a much loved alcoholic drink has been produced and enjoyed since thousands of years. It is typically made from Sented grapes. Different varieties of grapes and strains of yeasts produce different styles of wine. As part of this project, the objective was to identify a dataset with wine reviews, clean it up and gain some insights using data preparation and analysis with R. 

### Data Understanding

* Dataset - [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews)

This dataset consists of details of 129971 wines reviews produced across the globe by different wineries. The dataset consists of country, wine description, designation, points, price, province, region_1, region_2, taster_name, taster_twitter_handle, title, variety, winery. We would be looking at various aspects of this data to uncover some insights. 

This dataset is not a clean dataset. Therefore, in order to clean up the dataset had to take various steps such as removing NAs, removing redundant fields, removing fields which had a lot of missing data, updating mean/median values to numeric fields which have missing data.

### Problem Statements

1. Determine which countries/region produces best wines? 
2. Determine which wineries produces best wines?
3. Determine which countries/region produces costly wines?
4. Determine which countries/region produces economical wines?
5. Determine which countries/region produces economical and high quality wines?
6. Determine which states are producing most wines?
7. Determine which countries are producing best and worst wines?
8. Establish corelation between a price of wines and points scored by the wine?

### Conclusion

1. Answered problem statement in form of graphs/charts.
5. Based on spearman correlation, it seems like there is strong positive correlation between points and price. 
