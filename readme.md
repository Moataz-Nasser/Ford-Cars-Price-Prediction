# Ford Card Price Prediction Using Linear Regression

## Dataset

Name: Ford Car Price Prediction  
Description: This dataset contains information about various Ford car models and their characteristics, along with their market prices. It is designed for predicting car prices based on features such as production year, mileage, fuel type, and engine specifications.  
Target Variable: Price  
Link: https://www.kaggle.com/datasets/adhurimquku/ford-car-price-prediction

## EDA Summary

- Data did not include any missing
- Data contained 17,966 rows and 9 columns
- Dropped 154 duplicate rows
- Trimmed all column names to remove spaces
- Converted categorical columns “model”, “fuelType”, and “transmission” to string type
- Trimmed all strings in categorical columns
- Replaced “Other” in fuelType with “Hybrid”
- Corrected year 2060 to 2015 for a specific car
- Replaced 201.8 MPG for Kuga Hybrid with max MPG of other hybrids
- Dropped rows with tax > 200
- Removed outliers in price and mileage using IQR method

## Visualizations

- Shows the number of cars available for each Ford model.
- Displays how many cars use each fuel type.
- Compares the frequency of manual, semi-automatic, and automatic cars.
- Visualizes relationships between numeric features like price, mileage, and engine size.
- Compares the mean car price for each production year.
- Shows how closely predicted prices match actual prices.
- Displays the distribution of prediction errors.

## Model Implementation Steps

- Split the data into a train and a test dataset. The train dataset is 70% of the original one, while the test dataset is 30%.
- Applied log transformation to the target column “price” to stabilize variance.
- Applied one-hot encoding to categorical features and aligned input features with training columns.
- Trained a Linear Regression model using the training dataset.
- Predicted car prices on the test dataset and reversed the log transformation.
- Measured model performance using Mean Square Errors (MSE), Root Mean Square Errors (RMSE), and Mean Absolute Percentage Error (MAPE).

## Evaluation Metrics

- Mean Square Errors (MSE): 2,128,869.33
- Root Mean Square Errors (RMSE): 1,459.06
- Mean Absolute Percentage Error (MAPE): 9.38%

## Interpretation of Results

The linear regression model shows a Mean Squared Error (MSE) of 2,128,869.33 and a Root Mean Squared Error (RMSE) of 1,459.06. Compared to the prices in the cleaned dataset, which range from $1,294 to $24,690 with a mean of $12,294, this indicates that the predicted car prices deviate on average by about $1,459. While this error is not negligible, it is relatively small compared to the overall price range. The Mean Absolute Percentage Error (MAPE) of 9.38% further suggests that the model provides reasonably accurate predictions and captures the general trend of Ford car prices based on the input features.
