# Airline Fare Prediction Project

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Data Preprocessing](#data-preprocessing)
4. [Modeling](#modeling)
5. [Evaluation](#evaluation)
6. [Results](#results)
7. [Conclusion](#conclusion)
9. [Dependencies](#dependencies)

## Introduction
This project aims to predict airfare prices using machine learning techniques. Airfare prediction can help travelers make informed decisions and save money by booking flights at optimal times.

## Dataset
The dataset used in this project includes various features such as:
- Departure and arrival locations
- Flight duration
- Airline
- Flight day
- Date and time of departure and arrival
- Number of stops

The dataset was sourced from "Kaggle" and contains 10682 records and 13 features after data wrangling and feature engineering including the target variale "Price".

## Data Preprocessing
The data preprocessing steps include:
- Handling missing values
- Encoding categorical variables
- Feature scaling
- Feature engineering (e.g., extracting days, and month, etc. from date features)

## Modeling
Machine learning models was implemented:
- Random Forest Regressor

## Evaluation
The model was evaluated using metrics:
- Mean Absolute Error (MAE)

## Results
The model performed well as it beats the baseline MAE which was 3655, with the test data, Validation MAE was 1177.

## Conclusion
This project demonstrates the application of machine learning techniques to predict airfare prices. The top three most important feature for Prediction in this dataset was:
- Total Stops
- Duration Hour
- Travel Day

## Dependencies
The project requires the following dependencies:
- Python 3.x
- Pandas
- Scikit-learn
- Jupyter Notebook
