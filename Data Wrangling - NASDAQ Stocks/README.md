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

5. Ploted the Kernel Density function of Percentage change of the prices.

    <img width="414" alt="image" src="https://user-images.githubusercontent.com/44445092/125203038-3d57a000-e23c-11eb-9992-3cf014bde3c3.png">

6. Histogram of stock prices listed in the merged dataset.

    <img width="395" alt="image" src="https://user-images.githubusercontent.com/44445092/125202905-7a6f6280-e23b-11eb-8dbe-35ff1c8016c9.png">


### Conclusion

1. Stocks data retrived from 3 different sources using different methods and loaded into database tables. 
2. Looking at the EDA results, Apple Inc is the top earning company on NASDAQ. 
3. Apple Inc has the highest revenue. 
4. There seems to be no coorelation between Assets and Liabilities. 

