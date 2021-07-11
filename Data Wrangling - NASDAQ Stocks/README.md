## NASDAQ Stocks - Data Wrangling

![image](https://user-images.githubusercontent.com/44445092/125187999-ee881700-e1f7-11eb-9882-6582eb426ff6.png)

### Introduction

Stocks are traded on stock exchages such as NYSE and NASDAQ. As a keen investor, I've always been intrigued by stocks, hence I decided to retrieve the stocks data for NASDAQ from various sources for data wrangling. As part of this project, I retrieved data from three different sources using three different methods, performed data cleanup, merged and add into a database, & apply data wrangling steps. 

### Data Understanding

- Data sources:
  - CSV file download - https://www.kaggle.com/suchitgupta60/s-p-500-companies-fundamentals-script
  - Web Scraping - 
  - API call - https://financialmodelingprep.com/api/v3/quotes/NASDAQ
- This dataset includes 40950 rows and 16 feature variables where each row corresponds to a unique video.
  
### EDA (Exploratory Data Analysis)

1. Below chart shows the days of the week which had the largest numbers of trending videos. There is a trend that on weekends, there are lesser videos being uploaded.

    <img width="697" alt="image" src="https://user-images.githubusercontent.com/44445092/125154396-73ebc880-e11f-11eb-8f7f-3da1b386d406.png">
 
2. Data and plot shows the trend that most of the videos are being uploaded on the weekdays, and over the weekends there is a significant drop in videos being published.

    <img width="544" alt="image" src="https://user-images.githubusercontent.com/44445092/125154498-e492e500-e11f-11eb-8c51-1c7dd411182f.png">

3. Below plot shows the trend that most of the videos are being uploaded between 14:00 and 16:00, highest number of videos being uploaded are around 16:00.
  
    <img width="543" alt="image" src="https://user-images.githubusercontent.com/44445092/125154619-74d12a00-e120-11eb-86ce-9fbf27d17d1b.png">
    
4. Entertainment category contains the largest number of trending videos with around 10,000 videos, second is Music category with around 6,200 videos, followed by How to & Style category with around 4,100 videos.

    <img width="599" alt="image" src="https://user-images.githubusercontent.com/44445092/125154654-a2b66e80-e120-11eb-83a1-7dec99a6a531.png">

5. Music and entertainment videos have the most number of likes.

    <img width="595" alt="image" src="https://user-images.githubusercontent.com/44445092/125154684-cd082c00-e120-11eb-819a-dfb9a9ed599c.png">

6. ESPN seem to have the greatest number of videos, followed by late night shows, mostly in entertainment category.

    <img width="809" alt="image" src="https://user-images.githubusercontent.com/44445092/125154713-ff198e00-e120-11eb-83c4-4d617419a231.png">

7. There seems to be positive correlation between the number of views and the no of likes of a video.

    <img width="502" alt="image" src="https://user-images.githubusercontent.com/44445092/125154775-6a636000-e121-11eb-8a46-a0236143706b.png">

8. Correlation matrix between views, likes, dislikes and number of comments on the video.

    <img width="640" alt="image" src="https://user-images.githubusercontent.com/44445092/125154807-8d8e0f80-e121-11eb-93d6-eaa7d51042b8.png">

    <img width="430" alt="image" src="https://user-images.githubusercontent.com/44445092/125154836-b2828280-e121-11eb-990a-de0cb54b8161.png">

9. Word cloud for the Description field, showing the most used words in the description.

    <img width="417" alt="image" src="https://user-images.githubusercontent.com/44445092/125154863-cd54f700-e121-11eb-8251-bd53f0bbb7f0.png">


### Modeling & Evaluation

1. As part of modeling, the intent is to build a model to predict number of likes and number of views on a video. Since both these values are continuous variables, therefore regression models are to be applied.

2. Results of linear Regression to predict number of likes. 

    <img width="644" alt="image" src="https://user-images.githubusercontent.com/44445092/125155036-e6aa7300-e122-11eb-8f14-3e4e54238de2.png">

3. Results of linear Regression to predict number of views. 

    <img width="640" alt="image" src="https://user-images.githubusercontent.com/44445092/125155085-36893a00-e123-11eb-98e1-6e384e604dcc.png">

4. Linear regression results shows that r-squared score of 0.76 which is not accurate enough. 

5. Random Forest Regressor model to predict number of views has a mean absolute error (MAE) of 220924 and score of 0.985.

    <img width="382" alt="image" src="https://user-images.githubusercontent.com/44445092/125155157-98e23a80-e123-11eb-8ff8-c6fc6c7094bc.png">

### Conclusion

1. Linear Regression is a good fit when modeling to predict number of likes.
2. To predict the number of views, Random Forest Regressor has better score than linear regression. 
3. Positive correlation between the number of views and the number of likes of a video. Like wise is the case with the number of views and the no of comments on a video.
4. The data set I worked with could have had few more attributes such comment text, length of the video, number of subscribers, etc. 


