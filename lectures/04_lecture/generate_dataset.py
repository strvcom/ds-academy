import numpy as np
import pandas as pd
import random

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


def generate_dataset(n_samples: int=1000, n_features: int=6, flip_y: float=0.2):
    """
    Function to generate data
    """
    random.seed(123)
    
    X, y = make_classification(
        n_samples=n_samples, n_features=n_features-1,
        n_classes=3, n_informative=3, flip_y=flip_y
    )

    # convert from numpy to pandas
    X = pd.DataFrame(X)
    y = pd.Series(y)

    # pick a few features at random to convert to categorical
    cat_cols = np.sort(
        np.random.choice(
            X.columns, size=int(len(X.columns)/3), replace=False
        )
    )

    # conver numerical features to categorical
    X.iloc[:, cat_cols] = X.iloc[:, cat_cols].apply(
        lambda col: np.round((col - min(col)) / (max(col) - min(col)) * 3, 0),
        axis=0
    )

    X.iloc[:, cat_cols] = X.iloc[:, cat_cols].values.astype(str)

    # convert column names to indicate whether numerical/categorical
    cat_rename_mapper = {
        column: f'categorical_{index}' for index, column in enumerate(cat_cols)
        }
    num_rename_mapper = {
        column: f'numerical_{index}' for index, column in enumerate(
            X.columns.symmetric_difference(cat_cols))
        }
    rename_maper = {**cat_rename_mapper, **num_rename_mapper}
    X.rename(columns=rename_maper, inplace=True)

    # split data in train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    return X_train, X_test, y_train, y_test