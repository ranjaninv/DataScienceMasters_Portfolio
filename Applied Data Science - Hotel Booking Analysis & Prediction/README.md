## Hotel Booking Analysis & Cancellation Prediction

![image](https://user-images.githubusercontent.com/44445092/127782200-a2c2a1da-62c3-4d4b-bdf5-bddfba4866a6.png)

### Introduction

  The hotel industry is subdivision of the hospitality industry that specializes in providing customers with lodging services. There are a variety of hotel types that typically can be categorized by size, function, service, and cost. Levels of service can usually be split into three options namely limited-service, mid-range service, and full-service. Booking of hotel room are done through various methods such as travel booking websites (such as Priceline, Kayak, Expedia, Booking.com), directly through hotel’s website, or various travel agents. Being an avid traveler, I choose to pick up a dataset in hotel bookings. Booking cancellations have significant impact on demand-management decisions in the hospitality industry. 

  Hotel industry faces a very high cancellation rate. With a global average of almost 40% cancellation rate, this trend produces a very negative impact on hotel revenue and distribution management strategies. To mitigate the effect of cancellations, hotels implement rigid cancellation policies and overbooking tactics, which in turn can have a negative impact on revenue and on the hotel reputation. To make things worse, during this covid crisis, hotel and hospitality industry has taken a massive hit in terms of less bookings and even more cancellations. The impact of COVID-19 on the travel industry so far has been multiple times worse than 9/11. Hotels were one of the first industries affected by the pandemic and it will be one of the last to recover. Therefore, it is more than ever necessary that using data science and ML, potential booking cancellations are identified in advance to allow hotel management allocate resources and plan accordingly. The aim of this project to not only find patterns and key insights related to hotel booking and cancellations but also to develop a few models for predicting a cancellation on a hotel room booking.


### Data Understanding

- [Explore Dataset in Kaggle](https://www.kaggle.com/jessemostipak/hotel-booking-demand)
- This dataset includes 119391 rows and 32 feature variables. 
- This data set contains booking information for a city hotel and a resort hotel, and also includes information such as when the booking was made, length of stay, the number of adults, children, and/or babies, and the number of available parking spaces, among other things.
  
### EDA (Exploratory Data Analysis)

1. Below plot shows the comparison of cancellation of bookings for Resort Hotel and City Hotel.

    <img width="257" alt="image" src="https://user-images.githubusercontent.com/44445092/127786351-6808d6a9-d38c-46bc-abf8-7d2b6db94b50.png">
 
2. Below pie chart shows the distribution of the Reservation Status.

    <img width="468" alt="image" src="https://user-images.githubusercontent.com/44445092/127786370-68de63cb-07ca-4634-8ffb-b42cb143593a.png">

3. Below plot shows the distribution and highest concentration points.
  
    <img width="354" alt="image" src="https://user-images.githubusercontent.com/44445092/127786381-f98f5477-5d48-4c5d-92ec-59e0344e3f0e.png">
    
4. Below plot shows the distribution of bookings over the weeks of the year.

    <img width="422" alt="image" src="https://user-images.githubusercontent.com/44445092/127786885-18901571-9b4f-40b6-a1b9-33565070c39e.png">

5. Below plot the demonstrates the distribution of average daily rates for different room types.

    <img width="468" alt="image" src="https://user-images.githubusercontent.com/44445092/127786902-68e3e7b5-aaf8-4bc3-967e-7c9432093a9f.png">

6. Below plot shows the comparison of booking price of room over a period of time.

    <img width="468" alt="image" src="https://user-images.githubusercontent.com/44445092/127787007-dcf8ac1e-e5dc-4840-8719-1cc244c0c57f.png">

7. Below plot shows the comparison of total guests per month.

    <img width="468" alt="image" src="https://user-images.githubusercontent.com/44445092/127787016-2d312a5c-58ba-45cb-9525-90a8bf81a03d.png">

8. Plot showing distribution of Market Segment by different Hotel Types.

    <img width="468" alt="image" src="https://user-images.githubusercontent.com/44445092/127787084-97a5cc62-e16a-43ef-bb9a-24db2f5bb503.png">

    <img width="640" alt="image" src="https://user-images.githubusercontent.com/44445092/125154807-8d8e0f80-e121-11eb-93d6-eaa7d51042b8.png">

9. Heatmap of the correlation.

    <img width="468" alt="image" src="https://user-images.githubusercontent.com/44445092/127787133-4c2813a8-809f-4422-a7e3-7b7f95322e2c.png">


### Modeling & Evaluation

1. As part of modeling, the intent is to build a model to predict if a hotel booking will be cancelled. Since booking cancellation is a categorical variables, therefore classification models are to be applied.

2. Results of Random Forest Classifier. 

    <img width="331" alt="image" src="https://user-images.githubusercontent.com/44445092/127787308-2ee74d7b-e2ad-441f-bd79-be0b9eed2eb5.png">
    
    <img width="225" alt="image" src="https://user-images.githubusercontent.com/44445092/127787312-07173c72-d6f9-471b-a314-a8912c5e7991.png">

3. Results of Logistic Regression. 

    <img width="330" alt="image" src="https://user-images.githubusercontent.com/44445092/127787330-c3e9f9f1-0ab1-46ee-bd4b-ee9554038035.png">

    <img width="225" alt="image" src="https://user-images.githubusercontent.com/44445092/127787335-84d562ee-c790-45ee-b900-c714fc90e8cd.png">

4. Results of Decision Tree Classification model. 

    <img width="305" alt="image" src="https://user-images.githubusercontent.com/44445092/127787362-9bb53a6b-890b-418f-bc03-0574764d9220.png">

    <img width="225" alt="image" src="https://user-images.githubusercontent.com/44445092/127787364-14b015bf-29a8-4c0c-8cb7-1243788d6fe0.png">         

5. Results of KNN Classification model.

    <img width="325" alt="image" src="https://user-images.githubusercontent.com/44445092/127787397-b5048a0a-e739-4f7a-90a7-646fcf29fff6.png">

    <img width="225" alt="image" src="https://user-images.githubusercontent.com/44445092/127787402-4a601fb3-0846-4c4c-bc90-2490add0d3e0.png">

### Conclusion

1. Booking cancellations has strongest positive correlation with lead time and average daily rates. Therefore, hotels should look at this and try to adjust their pricing and cancellation strategies accordingly. 
2. Random oversampling technique helped overcome the Imbalanced datasets challenge. 
3. Using Random Forest Model our model will correctly predict if a hotel room booking will be cancelled or not 93.78% of the time.
4. Decision Tree Model our model will correctly predict if a hotel room booking will be cancelled or not 92.91% of the time.
5.Random forest model has less false positives than Decision Tree making it a better model.



