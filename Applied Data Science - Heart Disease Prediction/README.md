## Heart Disease Prediction

![image](https://user-images.githubusercontent.com/44445092/128667156-3b9752b8-6882-4b90-b347-70727859628f.png)

### Introduction

  Heart disease is one of the most significant health crisis that the world is facing today. It is not only the leading cause of the death in the United States but also a major cause of disability. According to WHO, an estimated 17.9 million people died from heart diseases in 2019, representing 32% of all global deaths. Of these deaths, 85% were due to heart attack and stroke. Heart disease is the leading cause of death for men, women, and people of most racial and ethnic groups in the United States. On average, someone dies of CVD every 36 seconds in the US. There are 2,380 deaths from CVD each day, based on 2018 data. Heart disease costs the United States about $219 billion each year from 2014 to 2015. This includes the cost of health care services, medicines, and lost productivity due to death. The early prognosis of heart diseases can help in making decisions on lifestyle changes in high-risk patients and in turn reduce the complications, fatalities, and overall healthcare cost on economy. 
  
  There are many things that can raise your risk for heart disease, and they are referred as risk factors. A large percentage of heart diseases can be prevented. Cardiovascular disease prediction is a critical challenge in the clinical data analysis. Machine learning (ML) has been showing an effective assistance in making decisions and predictions from the large quantity of data produced by the healthcare industries and hospitals. 
  
  As part of this project, I’ll be looking at a few patterns and insights in the heart disease dataset. I’ll also be developing a few models for predicting the 10 year coronary heart disease based on the associated risk factors in the dataset. 


### Data Understanding

- [Explore Dataset in Kaggle](https://www.kaggle.com/dileep070/heart-disease-prediction-using-logistic-regression)
- This dataset includes 4238 rows and 15 feature variables. 
- Each attribute is a potential risk factor. There are both demographic, behavioral, and medical risk factors in the dataset.
  
### EDA (Exploratory Data Analysis)

1. Below plots shows the distribution of all the Boolean attributes of the dataset.

    <img width="429" alt="image" src="https://user-images.githubusercontent.com/44445092/128668377-3a028f61-f80b-4593-a187-f5f250be918d.png">
 
2. Below set of plots show the distribution of all the continuous variables in the dataset. 

    <img width="385" alt="image" src="https://user-images.githubusercontent.com/44445092/128668414-81cc50af-ba20-4096-b253-10d84428dd9d.png">

3. As we can see in below plot, most of the people who don't have a 10-year risk of coronary heart disease are female while the ones who have the risk are generally male.
  
    <img width="212" alt="image" src="https://user-images.githubusercontent.com/44445092/128668451-fb6bdfb5-e64a-495a-9124-535a2c6feab9.png">
    
4. Below plot demonstrates that smoking status has insignificant effect on the risk in the data.

    <img width="241" alt="image" src="https://user-images.githubusercontent.com/44445092/128668504-39508ba9-a2ff-4d3a-9bbf-08f390d65a56.png">

5. Below chart shows the distribution of smokers by age.

    <img width="307" alt="image" src="https://user-images.githubusercontent.com/44445092/128668542-d565ec53-857a-480d-8900-17989bfaeb43.png">

6. Below is the box and whisker plot of distribution of Glucose, Total Cholesterol, Systolic blood pressure, Siastolic blood pressure, Heart rate against TenYearCHD. 

    <img width="468" alt="image" src="https://user-images.githubusercontent.com/44445092/128668607-dade5dd1-8fb0-4f1f-b85c-a9a7c53504c7.png">

7. Below plot shows the line graph comparison of totChol, cigPerDay & glucose. 

    <img width="312" alt="image" src="https://user-images.githubusercontent.com/44445092/128668632-a1592f16-f9ac-45c1-9b65-6da26f9e20dc.png">

8. Below box-whisker plot helps to identify the outliers in the dataset. 

    <img width="386" alt="image" src="https://user-images.githubusercontent.com/44445092/128668747-9d46aee2-2da8-4aab-ab51-bfd7a1fa6e0d.png">

9. Heatmap of the correlation.

    <img width="336" alt="image" src="https://user-images.githubusercontent.com/44445092/128668683-8d739ab5-c72b-4038-80a0-66257765883b.png">
    
    <img width="468" alt="image" src="https://user-images.githubusercontent.com/44445092/128668700-6eebfb11-233f-48df-8169-14a7ba4908d2.png">

    <img width="187" alt="image" src="https://user-images.githubusercontent.com/44445092/128668724-f42f2b28-8405-4a82-9e6c-d5049fa1fccd.png">


### Modeling & Evaluation

1. As part of modeling, the intent is to build a model to predict if a person is at risk of getting heart disease in 10 years. Since TenYearCHD is a categorical variables, therefore classification models are to be applied.

2. Results of Random Forest Classifier. 

    <img width="268" alt="image" src="https://user-images.githubusercontent.com/44445092/128667781-ac8411ec-f11c-4304-a8fc-0cf40d45933d.png">
    
    <img width="199" alt="image" src="https://user-images.githubusercontent.com/44445092/128667794-b5c4ebd8-bc9d-4a33-879b-53f7a43507d8.png">

3. Results of Logistic Regression. 

    <img width="257" alt="image" src="https://user-images.githubusercontent.com/44445092/128667807-eb6fcb11-41ff-40e9-8d94-bb1446f5633a.png">

    <img width="191" alt="image" src="https://user-images.githubusercontent.com/44445092/128667823-808ba64f-341b-4a3f-bc2b-ad96b500a573.png">

4. Results of Decision Tree Classification model. 

    <img width="234" alt="image" src="https://user-images.githubusercontent.com/44445092/128667839-dcdfbdb8-359c-4a59-bd69-b1c7cc74143f.png">

    <img width="196" alt="image" src="https://user-images.githubusercontent.com/44445092/128667859-b31253f7-493f-4472-8e94-7ba3b0b120a2.png">        

5. Results of KNN Classification model.

    <img width="260" alt="image" src="https://user-images.githubusercontent.com/44445092/128667870-f28b2279-b1c7-4c36-ad0c-90918a86e0eb.png">

    <img width="199" alt="image" src="https://user-images.githubusercontent.com/44445092/128667884-748a604c-3faf-4c10-9b55-d967ea7d361d.png">
    
6. Results of SVC Classification model.

    •	SVM with Gamma = 0.1, and C = 1.0
    
    <img width="292" alt="image" src="https://user-images.githubusercontent.com/44445092/128668144-48f82806-0ad8-4c12-8553-4a735d9924d5.png">
    
    •	SVM with Gamma = 0.01, and C = 1.0
    
    <img width="292" alt="image" src="https://user-images.githubusercontent.com/44445092/128668160-6593c879-45c9-4a19-b9dd-4e3fa92b4e4b.png">
    
    •	SVM with Gamma = 0.001, and C = 1.0
    
    <img width="292" alt="image" src="https://user-images.githubusercontent.com/44445092/128668181-f1d9ec27-9bec-47f8-b25c-d6f24b4fd637.png">

    •	SVM with Gamma = 0.1, and C = 80
    
    <img width="292" alt="image" src="https://user-images.githubusercontent.com/44445092/128668233-7ba7b78f-bfbe-476d-bb58-e20e95e3c2d7.png">

7. Comparison of all the implemented models:

    <img width="442" alt="image" src="https://user-images.githubusercontent.com/44445092/128668292-57a502b1-6a57-426c-913c-9de86601a136.png">

### Conclusion

•	The strongest positive correlations of TenYearCHD are with age and sysBP.
•	Performed Standardization technique to scale the data before running it through the ML algorithms. 
•	Since the training dataset was moderately imbalanced, applied Random oversampling technique to overcome the imbalanced datasets challenge. 
•	Based on the accuracy of the implemented classification models to predict TenYearCHD, SVM classification model shows highest accuracy followed by Random Forest classification model.




