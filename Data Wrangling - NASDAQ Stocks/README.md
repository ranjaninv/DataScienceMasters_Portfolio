## NASDAQ Stocks - Data Wrangling

![image](https://user-images.githubusercontent.com/44445092/125187999-ee881700-e1f7-11eb-9882-6582eb426ff6.png)

### Introduction

Stocks are traded on stock exchages such as NYSE and NASDAQ. As a keen investor, I've always been intrigued by stocks, hence I decided to retrieve the stocks data for NASDAQ from various sources for data wrangling. As part of this project, I retrieved data from three different sources using three different methods, performed data cleanup, merged and add into a database, & apply data wrangling steps. 

### Data Understanding
  
- Data sources:
  - [Kaggle](https://www.kaggle.com/suchitgupta60/s-p-500-companies-fundamentals-script) - This csv file contains extensive fundamentals data for 1781 stocks.
  - [Web Scraping](https://finance.yahoo.com/screener/unsaved/9cf4468e-7dc3-4be3-bc18-1db7ab68efcf?count=100&offset=1) - Stocks data from Yahoo Fianance was retreived by web scraping.   
  - [API call](https://financialmodelingprep.com/api/v3/quotes/NASDAQ) - Stocks performace data was retrieved by API call. 
 
### Process Outline
 
 - Downloaded the csv from Kaggle and loaded it into a dataframe.
 - To retrieve stocks data by web scraping, read the web page data, fetched and parsed the table contents into lists and eventually to the dataframe.
 - To retrieve data using API call, first API keys was retrieved. With the API keys, performed the API call which resulted in the response of json data. Parsed the JSON data to pick the desired attributes and loaded them in a csv file. The csv file was then loaded into a dataframe.
 - Once data from all three sources were available, loaded the data into SQLLite database in 3 different tables and eventually merged them in one table. 
 - Upon merging the data, performed EDA on the merged dataset. 
   
### EDA (Exploratory Data Analysis)

1. Top 10 earning companies in regards to net income.

    ![image](https://user-images.githubusercontent.com/44445092/125202382-fe741b00-e238-11eb-97ab-07d43fabbf79.png)

 
2. Top 10 companies when by total revenue.

    ![image](https://user-images.githubusercontent.com/44445092/125202536-9e31a900-e239-11eb-9d91-5e8ce3bfa016.png)

3. Scatterplot of Total assets vs liabilities of top 10 earning companies by revenue.
  
    <img width="411" alt="image" src="https://user-images.githubusercontent.com/44445092/125202814-f9b06680-e23a-11eb-8aec-b5fcbe926173.png">
    
4. Comparing Total revenue vs Net income of these top 10 earning companies.

    <img width="414" alt="image" src="https://user-images.githubusercontent.com/44445092/125202834-151b7180-e23b-11eb-9775-eea7645d2e9b.png">

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


