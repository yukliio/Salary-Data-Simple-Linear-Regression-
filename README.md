
# Salary Prediction Based on Job Experience

This repository contains a simple linear regression model to predict salaries based on years of job experience. The project includes data preprocessing, model training, and visualization of the results.

# Data Preprocessing
The dataset used is `salary_data.csv`, which contains information about years of experience and corresponding salaries. The data preprocessing steps include:
- Importing necessary libraries: `numpy`, `pandas`, and `matplotlib`.
- Loading the dataset.
- Splitting the dataset into independent variable `X` (years of experience) and dependent variable `y` (salary).
- Splitting the data into training and test sets using `train_test_split` from `sklearn.model_selection`.

# Training the Model
A simple linear regression model is trained on the training set to establish the relationship between years of experience and salary.

# Predicting the Test Set Results
The model predicts the salaries for the test set based on the trained model to evaluate its performance.

# Visualizing the Results
The results are visualized using scatter plots and regression lines for both training and test sets, providing a clear view of how well the model fits the data.

# Getting Started
To run this project, clone the repository and ensure you have the necessary dependencies installed. You can install the required packages using a `requirements.txt` file and run the main script to see the predictions and visualizations.

```sh
git clone https://github.com/your-username/salary-prediction.git
cd salary-prediction
pip install -r requirements.txt
python script.py
```
