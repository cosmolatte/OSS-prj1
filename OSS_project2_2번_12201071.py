import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR


def sort_dataset(dataset_df):
    sort_data = dataset_df.sort_values('year', ascending=True)
    return sort_data


def split_dataset(dataset_df):
    x = data_df.drop(columns="salary", axis=1)
    y = dataset_df["salary"] * 0.001
    # y는 스케일링 시킨것
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=45, shuffle=True)
    return X_train, X_test, Y_train, Y_test


def extract_numerical_cols(dataset_df):
    num_cols = ['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR',
                       'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']
    return dataset_df[num_cols]


def train_predict_decision_tree(X_train, Y_train, X_test):
    dt_reg = DecisionTreeRegressor()
    dt_reg.fit(X_train, Y_train)
    predicted = dt_reg.predict(X_test)
    return predicted


def train_predict_random_forest(X_train, Y_train, X_test):

    rf_reg = RandomForestRegressor()
    rf_reg.fit(X_train, Y_train)
    predicted = rf_reg.predict(X_test)
    return predicted


def train_predict_svm(X_train, Y_train, X_test):
    svm_cls = SVR()
    #svc()가 문제였네 아 허탈해
    svm_cls.fit(X_train, Y_train)
    predicted = svm_cls.predict(X_test)
    return predicted


def calculate_RMSE(labels, predictions):
    return np.sqrt(np.mean((predictions - labels)**2))


if __name__ == '__main__':
    # DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
    data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

    sorted_df = sort_dataset(data_df)
    X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

    X_train = extract_numerical_cols(X_train)
    X_test = extract_numerical_cols(X_test)

    dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
    rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
    svm_predictions = train_predict_svm(X_train, Y_train, X_test)

    print("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))
    print("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))
    print("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))
