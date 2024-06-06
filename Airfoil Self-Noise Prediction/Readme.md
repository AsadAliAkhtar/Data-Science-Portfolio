# Airfoil Noise Prediction Project

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Data Preprocessing](#data-preprocessing)
4. [Modeling](#modeling)
5. [Evaluation](#evaluation)
6. [Results](#results)
7. [Conclusion](#conclusion)
8. [Dependencies](#dependencies)

## Introduction
This project aims to predict scaled sound pressure levels of NACA 0012 airfoils at various wind tunnel speeds and angles of attack, using machine learning techniques. The NASA dataset comprises different size NACA 0012 airfoils at various wind tunnel speeds and angles of attack. The span of the airfoil and the observer position were the same in all of the experiments. The dataset was obtained from a series of aerodynamic and acoustic tests of two and three-dimensional airfoil blade sections conducted in an anechoic wind tunnel.

Predicting noise levels is crucial in designing quieter aircraft and assessing environmental impact. By leveraging this dataset, our goal is to develop a predictive model that can accurately estimate scaled sound pressure levels, aiding in the design and evaluation of airfoil configurations for reduced noise emissions.

## Dataset
The dataset used in this project includes features such as:
- Frequency
- Attack angle
- Chord length
- Free-stream velocity
- Suction side displacement thickness
- Scaled sound pressure (target variable)

The dataset was sourced from UCI Machine Learning Repository and contains *1503* **records** and  *6* **features**.

## Data Preprocessing
The data preprocessing steps include:
- Loading the dataset and assigning column names
- Checking for missing values (our dataset has no missing values)
- Exploring the correlation between features and target variable

## Modeling
In consideration of the non-linear relationship between features and the target, we opted for the **Random Forest Regressor** algorithm.

## Evaluation
We evaluated our model using Mean Absolute Error (MAE) on a validation set. The model outperformed the baseline, indicating its effectiveness in noise prediction.

## Results
The important features for noise prediction identified by our model include: ![Capture](https://github.com/AsadAliAkhtar/Data-Science-Portfolio/assets/170518936/974c2509-7cbb-43ac-9e9e-ad8ab71e383a)

The *model* has been saved for future use.

## Conclusion
This project demonstrates the application of machine learning in predicting airfoil noise levels. The results highlight the importance of feature engineering and model selection in achieving accurate predictions.

## Dependencies
The project requires the following dependencies:
- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook
