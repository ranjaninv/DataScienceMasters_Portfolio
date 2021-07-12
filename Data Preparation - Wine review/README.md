## Wine reviews - Data Preparation

![image](https://user-images.githubusercontent.com/44445092/125238453-e2aa5c80-e2ac-11eb-9b5b-0638c709ecff.png)

### Introduction

Wine, a much loved alcoholic drink has been produced and enjoyed since thousands of years. It is typically made from Sented grapes. Different varieties of grapes and strains of yeasts produce different styles of wine. As part of this project, the objective was to identify a dataset with wine reviews, clean it up and gain some insights using data preparation and analysis with R. 

### Data Understanding

* Dataset - [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews)

This dataset consists of details of 129971 wines reviews produced across the globe by different wineries. The dataset consists of country, wine description, designation, points, price, province, region_1, region_2, taster_name, taster_twitter_handle, title, variety, winery. We would be looking at various aspects of this data to uncover some insights. 

This dataset is not a clean dataset. Therefore, in order to clean up the dataset had to take various steps such as removing NAs, removing redundant fields, removing fields which had a lot of missing data, updating mean/median values to numeric fields which have missing data.

### EDA (Exploratory Data Analysis)

1. Best wine producing countries (points greater than 96).

    <img width="866" alt="image" src="https://user-images.githubusercontent.com/44445092/125235404-07e89c00-e2a8-11eb-88bf-db04fe51331d.png">

2. Countries producing costly wines.

    <img width="844" alt="image" src="https://user-images.githubusercontent.com/44445092/125235601-5433dc00-e2a8-11eb-8d5d-2d18626ef498.png">

3. Countries producing economical wines. 

    <img width="839" alt="image" src="https://user-images.githubusercontent.com/44445092/125235690-7a597c00-e2a8-11eb-9e22-9c745a057aad.png">

4. Countries producing Economical and high quality wines. 

    <img width="824" alt="image" src="https://user-images.githubusercontent.com/44445092/125235785-9e1cc200-e2a8-11eb-925f-c01a55fb0ca8.png">

5. States producing most wines.

    <img width="837" alt="image" src="https://user-images.githubusercontent.com/44445092/125235941-d7edc880-e2a8-11eb-96a1-f987c362692d.png">

6. Based on spearman correlation, it seems like there is strong positive correlation between points and price.
  
    <img width="513" alt="image" src="https://user-images.githubusercontent.com/44445092/125236146-171c1980-e2a9-11eb-9053-6511c6e4f425.png">

    <img width="839" alt="image" src="https://user-images.githubusercontent.com/44445092/125236213-32872480-e2a9-11eb-8aaa-ab22b3dd8ce3.png">

7. Points Distribution of the wines.

    <img width="839" alt="image" src="https://user-images.githubusercontent.com/44445092/125236731-13d55d80-e2aa-11eb-9d45-2919f87e2b26.png">

8. Price distribution of the wines.

    <img width="809" alt="image" src="https://user-images.githubusercontent.com/44445092/125236816-35364980-e2aa-11eb-9087-a3d8f1af9939.png">


### Conclusion

1. US, France, Italy, Portugal, Australia, Germany, Spain and Austria are the best wine producing coun- ties based on count of wines scoring more than 96 points with US topping the list.
2. France by far produces the costliest wines in the world.
3. US produces most economical wines.
4. US and Protugal are top 2 countries producing highly rated economical wines.
5. California, Washington, Bordeaux and Tuscany are most wine producing regions, with california top-
ping the list.
6. Austrian wines have the best mean scores and Chile has the lowest mean scores.
7. Price and points have a strong positive correlation.
