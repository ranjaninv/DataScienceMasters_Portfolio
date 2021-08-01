## Hotel Booking Analysis & Cancellation Prediction

![image](https://user-images.githubusercontent.com/44445092/127782200-a2c2a1da-62c3-4d4b-bdf5-bddfba4866a6.png)

### Introduction

  The hotel industry is subdivision of the hospitality industry that specializes in providing customers with lodging services. There are a variety of hotel types that typically can be categorized by size, function, service, and cost. Levels of service can usually be split into three options namely limited-service, mid-range service, and full-service. Booking of hotel room are done through various methods such as travel booking websites (such as Priceline, Kayak, Expedia, Booking.com), directly through hotel’s website, or various travel agents. Being an avid traveler, I choose to pick up a dataset in hotel bookings. Booking cancellations have significant impact on demand-management decisions in the hospitality industry. 

  Hotel industry faces a very high cancellation rate. With a global average of almost 40% cancellation rate, this trend produces a very negative impact on hotel revenue and distribution management strategies. To mitigate the effect of cancellations, hotels implement rigid cancellation policies and overbooking tactics, which in turn can have a negative impact on revenue and on the hotel reputation. To make things worse, during this covid crisis, hotel and hospitality industry has taken a massive hit in terms of less bookings and even more cancellations. The impact of COVID-19 on the travel industry so far has been multiple times worse than 9/11. Hotels were one of the first industries affected by the pandemic and it will be one of the last to recover. Therefore, it is more than ever necessary that using data science and ML, potential booking cancellations are identified in advance to allow hotel management allocate resources and plan accordingly. The aim of this project to not only find patterns and key insights related to hotel booking and cancellations but also to develop a few models for predicting a cancellation on a hotel room booking.


### Data Understanding

- Dataset link - https://www.kaggle.com/jessemostipak/hotel-booking-demand. 
- The dataset contains details of the videos uploaded on YouTube in US during 2018 and 2019.
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


