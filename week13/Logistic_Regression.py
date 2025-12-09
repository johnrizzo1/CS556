import marimo

__generated_with = "0.18.1"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Classification with Logistic Regression and SVM

    We will be working with the [Titanic Data Set from Kaggle](https://www.kaggle.com/c/titanic). We'll be trying to predict a classification: survival or deceased.

     - **Variable Name -  Variable Description**
     - PassengerID - Passenger ID
     - Survived - Survival (0 = No; 1 = Yes)
     - Pclass - Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
     - Name	- Name
     - Sex - Sex
     - Age - Age in years
     - SibSp - Number of Siblings/Spouses Aboard
     - Parch - Number of Parents/Children Aboard
     - Ticket - Ticket Number
     - Fare - Passenger Fare
     - Cabin - Cabin number
     - Embarked - Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### a. Import Libraries

    Import all necessary libraries
    """)
    return


@app.cell
def _():
    import pandas as pd 
    import matplotlib.pyplot as plt
    import seaborn as sns

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression

    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import classification_report
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import precision_recall_fscore_support
    from sklearn.metrics import roc_curve, auc,precision_recall_curve

    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.calibration import CalibrationDisplay

    import numpy as np
    return (
        CalibrationDisplay,
        LogisticRegression,
        MinMaxScaler,
        accuracy_score,
        classification_report,
        pd,
        plt,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our target variable will be **survived**.  Use the rest of the fields mentioned above to predict whether a passenger survived the Titanic shipwreck.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### b.	Data Loading / Preprocessing
    #### i.	Loading
    1. Load the data <df_train.csv> and <df_test.csv> as a pandas dataframe using the `pandas.read_csv` function. The ‘df_test.csv’ has been preprocessed (i.e., null values have been dropped, certain columns etc. have been dropped) and should not be changed apart from splitting the dataframe into X_test and y_test.  The ‘df_train’ data has NOT been preprocessed and you will need to preprocess and prepare the ‘df_train’ dataframe. Note: Neither df_train nor df_test have been scaled. The next few steps will enumerate data preprocessing, scaling requirements we need to perform.
    """)
    return


@app.cell
def _(pd):
    df_train = pd.read_csv('df_train.csv')
    df_test = pd.read_csv('df_test.csv')
    return df_test, df_train


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    2. The resulting dataframe (i.e., df_train) should have the shape (712,12) indicating that there are 712 instances and 12 columns.
    """)
    return


@app.cell
def _(df_train):
    df_train.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    3. In df_train dataframe, currently you have 12 columns which are the following – PassengerID, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked and the Survived column (target variable).
    """)
    return


@app.cell
def _(df_train):
    df_train.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    4. Use the `pandas.isnull().sum()` function to check if there are any missing values in the df_train dataframe. Report which columns have missing (i.e., null) values and provide the number of the null values in the columns.
    """)
    return


@app.cell
def _(df_train):
    df_train.isnull().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    5. Use the `pandas.DataFrame.drop()` function to drop the ‘Cabin’, ‘PassengerID’, ‘Name’ and ‘Ticket’ columns.
    """)
    return


@app.cell
def _(df_train):
    df_train.drop(columns=['Cabin', 'PassengerId', 'Name', 'Ticket'], inplace=True)
    return


@app.cell
def _(df_train):
    df_train.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    6. Use the `pandas.DataFrame.fillna()` function to replace the NA values in the ‘Age’ column with the mean value of the ‘Age’ column. Note: This process is called **imputation** (i.e., filling null values with a pre-specified value) and we are employing one strategy called mean imputation, but other strategies can also be employed in general.
    Use the `dropna()` function to drop any remaining **rows** that consist of NA values.
    """)
    return


@app.cell
def _(df_train):
    # df_train['Age'].fillna(df_train['Age'].mean(), inplace=True)
    df_train.fillna({'Age': df_train['Age'].mean()}, inplace=True)
    return


@app.cell
def _(df_train):
    df_train.dropna(inplace=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    7. Your task is to use the feature columns to predict the target column. This can be cast as a classification problem.
    8. Create a pandas dataframe X_train of features (by dropping the ‘Survival’ column from the df_train dataframe). Create a pandas Series object of targets y_train (by only considering the ‘Survival’ column from the df_train dataframe). Moving forward, we will be working with X_train and y_train. At this point, also split the df_test into X_test and y_test by dropping the ‘Survival’ column and storing the features into X_test. Store the ‘Survival’ column in y_test.
    """)
    return


@app.cell
def _(df_train):
    X_train = df_train.drop(columns=['Survived'])
    return (X_train,)


@app.cell
def _(df_train):
    y_train = df_train['Survived']
    return (y_train,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### ii. Data Visualization

    1. Employ a scatter plot using `matplotlib.pyplot.scatter` between the age of the passengers and the price of their fare. Label the x-axis and the y-axis and also give the plot a title.
    """)
    return


@app.cell
def _(X_train, plt):
    plt.scatter(X_train['Age'], X_train['Fare'])
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.title('Age vs Fare')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    2. Use the df_train dataframe. Using matplotlib visualize the number of males and females that survived and their respective passenger classes on two separate bar chart plots using `matplotlib.pyplot.bar` (Passenger Class column)
    """)
    return


@app.cell
def _(df_train):
    df_train.head()
    return


@app.cell
def _(df_train, plt):
    plt.figure(figsize=(10,6))

    # First plot: Males survival by passenger class
    plt.subplot(1, 2, 1)
    male_data = df_train[df_train['Sex'] == 'male'].groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)
    male_data.plot(kind='bar', ax=plt.gca())
    plt.xlabel('Passenger Class')
    plt.ylabel('Count')
    plt.title('Male Survival by Passenger Class')
    plt.legend(['Did not survive', 'Survived'])

    # Second plot: Females survival by passenger class
    plt.subplot(1, 2, 2)
    female_data = df_train[df_train['Sex'] == 'female'].groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)
    female_data.plot(kind='bar', ax=plt.gca())
    plt.xlabel('Passenger Class')
    plt.ylabel('Count')
    plt.title('Female Survival by Passenger Class')
    plt.legend(['Did not survive', 'Survived'])

    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    3. Using the Target variable (Survived) in y_train plot a bar chart showing the distribution of the ‘Survived’ column.
    """)
    return


@app.cell
def _(plt, y_train):
    y_train.value_counts().plot(kind='bar')
    plt.xlabel('Survived')
    plt.ylabel('Count')
    plt.title('Distribution of Survived')
    plt.xticks(rotation=0)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    4. So far you should have successfully been able to load, preprocess and visualize your data. Use the `pd.get_dummies()` function to convert categorical data into dummy variables (‘Sex’ and ‘Embarked’). Make sure to pass `drop_first=True` to the `get_dummies()` function. (Perform this only on X_train and store the result back into X_train).
    """)
    return


@app.cell
def _(X_train, pd):
    X_train_1 = pd.get_dummies(X_train, columns=['Sex', 'Embarked'], drop_first=True)
    return (X_train_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### iii. Data Scaling

    1. Use MinMaxScaler to scale only the **continuous attributes** of X_train. Apply the `fit_transform()` function of the scaler to obtain the scaled data and store it back in X_train.
    """)
    return


@app.cell
def _(MinMaxScaler, X_train_1):
    scaler = MinMaxScaler()
    X_train_2 = scaler.fit_transform(X_train_1)
    return X_train_2, scaler


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    2. Scale the X_test using the scaler you have just fit, this time using the `transform()` function. Note: Store the scaled values back into X_test. At the end of this step, you must have X_train, X_test, all scaled according to the MinMaxScaler.
    """)
    return


@app.cell
def _(df_test, scaler):
    X_test = df_test.drop(columns=['Survived'])
    y_test = df_test['Survived']
    X_test = scaler.transform(X_test)
    return X_test, y_test


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### c. Modelling

    #### i. Modelling (Model Instantiation / Training) using Logistic Regression classifier

    1. Employ the Logistic Regression classifier from sklearn and instantiate the model. Label this model as ‘model_lr’
    """)
    return


@app.cell
def _(LogisticRegression):
    model_lr = LogisticRegression()
    return (model_lr,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    2. Once instantiated, `fit()` the model using the scaled X_train, y_train data.
    """)
    return


@app.cell
def _(X_train_2, model_lr, y_train):
    model_lr.fit(X_train_2, y_train)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    3. Employ the `predict()` function to obtain predictions on X_test and store this in a variable labeled as ‘y_pred_lr’.
    """)
    return


@app.cell
def _(X_test, model_lr):
    y_pred_lr = model_lr.predict(X_test)
    return (y_pred_lr,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    4. Employ the `accuracy_score` function by using the ‘y_pred_lr’ and ‘y_test’ variables as the functions parameters and print the accuracy of the Logistic Regression model.
    """)
    return


@app.cell
def _(accuracy_score, y_pred_lr, y_test):
    accuracy = accuracy_score(y_test, y_pred_lr)
    print(f'Accuracy of Logistic Regression model: {accuracy}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### ii. Modelling Logistic Regression Classifier with the addition of noise on the target variable.

    In the data repository you should see three noisy datasets – `df_train_noise20`, `df_train_noise40`, and `df_train_noise60`. These datasets have already been preprocessed. In each dataset `df_train_noise<integer>`, the integer indicates the percentage of noise injected into the target variable in that training set. The noise can be considered a result of incorrect class labelling of a particular instance. For example, in `df_train_noise20`, 20% of the instances have an incorrect target label in the training set. Our goal will be to train a set of classification models on such noisy training data and test on a clean test set (i.e., same as what we have been using so far `df_test`).

    Load the `df_train_noise<nl>` (nl means noise level and is a place holder for the integer percentage) datasets and split the data into `X_train_<nl>` and `y_train_<nl>` (e.g., if working with `df_train_noise20` we would split the data and store it in variables named `X_train_20`, `y_train_20`). `X_train_<nl>` should store the features and `y_train_<nl>` should store the target variable.

    **Repeat the following steps (c. i. 1 – 4) for the 20%, 40%, 60% noise level datasets.**
    Train a new Logistic Regression model on the new training and use the pre-existing `X_test` and `y_test` to evaluate your model. Label this model as `model_lr_noise_<nl>`. Specifically, do the following:
    1. Employ a new Logistic Regression classifier from sklearn and instantiate the model. Label this model as `model_lr_noise<nl>`
    2. Once instantiated, `fit()` the model using the `X_train_<nl>` and `y_train_<nl>` data.
    3. Employ the `predict()` function to obtain predictions on `X_test` and store this in a variable labeled as `y_pred_lr_noise<nl>`.
    4. Employ the `accuracy_score` function and print the accuracy of the new Logistic Regression model.
    """)
    return


@app.cell
def _(LogisticRegression, MinMaxScaler, X_test, accuracy_score, pd, y_test):
    df_train_noise20 = pd.read_csv(f'df_train_noise20.csv')
    X_train_20 = df_train_noise20.drop(columns=['Survived'])
    y_train_20 = df_train_noise20['Survived']
    X_train_20 = MinMaxScaler().fit_transform(X_train_20)
    model_lr_noise_20 = LogisticRegression()
    model_lr_noise_20.fit(X_train_20, y_train_20)
    y_pred_lr_noise20 = model_lr_noise_20.predict(X_test)
    accuracy_noise20 = accuracy_score(y_test, y_pred_lr_noise20)
    print(f'Accuracy of Logistic Regression model with 20% noise: {accuracy_noise20}')
    return (y_pred_lr_noise20,)


@app.cell
def _(LogisticRegression, MinMaxScaler, X_test, accuracy_score, pd, y_test):
    df_train_noise40 = pd.read_csv(f'df_train_noise40.csv')
    X_train_40 = df_train_noise40.drop(columns=['Survived'])
    y_train_40 = df_train_noise40['Survived']
    X_train_40 = MinMaxScaler().fit_transform(X_train_40)
    model_lr_noise_40 = LogisticRegression()
    model_lr_noise_40.fit(X_train_40, y_train_40)
    y_pred_lr_noise40 = model_lr_noise_40.predict(X_test)
    accuracy_noise40 = accuracy_score(y_test, y_pred_lr_noise40)
    print(f'Accuracy of Logistic Regression model with 40% noise: {accuracy_noise40}')
    return (y_pred_lr_noise40,)


@app.cell
def _(LogisticRegression, MinMaxScaler, X_test, accuracy_score, pd, y_test):
    df_train_noise60 = pd.read_csv(f'df_train_noise60.csv')
    X_train_60 = df_train_noise60.drop(columns=['Survived'])
    y_train_60 = df_train_noise60['Survived']
    X_train_60 = MinMaxScaler().fit_transform(X_train_60)
    model_lr_noise_60 = LogisticRegression()
    model_lr_noise_60.fit(X_train_60, y_train_60)
    y_pred_lr_noise60 = model_lr_noise_60.predict(X_test)
    accuracy_noise60 = accuracy_score(y_test, y_pred_lr_noise60)
    print(f'Accuracy of Logistic Regression model with 60% noise: {accuracy_noise60}')
    return (y_pred_lr_noise60,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### d. Evaluation

    #### i. Report F1 Score, Precision, Recall, Accuracy (All on the test set X_test, y_test)

    1. Use `classification_report()` function from sklearn.metrics to report the precision, recall, and f1 score for each class for the `model_lr` model, along with a confusion matrix.
    """)
    return


@app.cell
def _(classification_report, y_pred_lr, y_test):
    print("Classification Reports: Logistic Regression without noise:")
    print(classification_report(y_test, y_pred_lr))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### ii. Report the accuracy and classification report for each of the three noisy models (`model_lr_noise<nl>`)
    """)
    return


@app.cell
def _(
    classification_report,
    y_pred_lr_noise20,
    y_pred_lr_noise40,
    y_pred_lr_noise60,
    y_test,
):
    print("Classification Reports: Logistic Regression with noise 20%:")
    print(classification_report(y_test, y_pred_lr_noise20))
    print("Classification Reports: Logistic Regression with noise 40%:")
    print(classification_report(y_test, y_pred_lr_noise40))
    print("Classification Reports: Logistic Regression with noise 60%:")
    print(classification_report(y_test, y_pred_lr_noise60))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### iii. Make a calibration plot for `model_lr`

    Use the `CalibrationDisplay` class from sklearn.calibration to make your plot.
    """)
    return


@app.cell
def _(CalibrationDisplay, X_test, model_lr, plt, y_test):
    calibration_display = CalibrationDisplay.from_estimator(
        model_lr, X_test, y_test, name="Logistic Regression"
    )
    plt.show()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
