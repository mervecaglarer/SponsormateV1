import sys
import pandas as pd
import numpy as np

np.set_printoptions(threshold=sys.maxsize)

from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import hamming_loss
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.ensemble import RandomForestClassifier

dict_for_df = {
    'KNN': [],
    'DTC': [],
    'ETC': [],
    'RFC': [],
}


def return_metrics(X, y, classifier):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    if classifier == "KNN":
        clf = MultiOutputClassifier(KNeighborsClassifier()).fit(X_train, y_train)
    elif classifier == "DTC":
        clf = MultiOutputClassifier(DecisionTreeClassifier()).fit(X_train, y_train)
    elif classifier == "ETC":
        clf = MultiOutputClassifier(ExtraTreeClassifier()).fit(X_train, y_train)
    elif classifier == "RFC":
        clf = MultiOutputClassifier(RandomForestClassifier()).fit(X_train, y_train)
    else:
        clf = MultiOutputClassifier(KNeighborsClassifier()).fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = 0
    shape = y_pred.shape
    for idxRow in range(shape[0]):
        trueValCount = 0
        size = 0
        for idxCol in range(shape[1]):
            if y_test[idxRow][idxCol] == 1 or y_pred[idxRow][idxCol] == 1:
                size += 1
        for idxCol in range(shape[1]):
            if y_test[idxRow][idxCol] == y_pred[idxRow][idxCol] and (
                    y_test[idxRow][idxCol] == 1 or y_pred[idxRow][idxCol] == 1):
                trueValCount += 1
        lineAccuracy = trueValCount / size if trueValCount > 0 else 0
        accuracy += lineAccuracy
        # print('{0} -> {1} -> {2}/{3}'.format(idxRow,lineAccuracy,trueValCount,size))
        # print(y_test[idxRow])
        # print(y_pred[idxRow])
    print("AVG Accuracy")
    print(accuracy / shape[0] if accuracy > 0 else 0)
    print("Hamming Loss")
    print(hamming_loss(y_test, y_pred))

    def return_metrics2(X, y, classifier):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        if classifier == "KNN":
            clf = MultiOutputClassifier(KNeighborsClassifier()).fit(X_train, y_train)
        elif classifier == "DTC":
            clf = MultiOutputClassifier(DecisionTreeClassifier()).fit(X_train, y_train)
        elif classifier == "ETC":
            clf = MultiOutputClassifier(ExtraTreeClassifier()).fit(X_train, y_train)
        elif classifier == "RFC":
            clf = MultiOutputClassifier(RandomForestClassifier()).fit(X_train, y_train)
        else:
            clf = MultiOutputClassifier(KNeighborsClassifier()).fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = 0
        shape = y_pred.shape
        for idxRow in range(shape[0]):
            trueValCount = 0
            size = 0
            for idxCol in range(shape[1]):
                if y_test[idxRow][idxCol] == y_pred[idxRow][idxCol]:
                    trueValCount += 1
            lineAccuracy = trueValCount / shape[1] if (trueValCount > 0) else 0
            accuracy += lineAccuracy
            # print('{0} -> {1} -> {2}/{3}'.format(idxRow,lineAccuracy,trueValCount,size))
            # print(y_test[idxRow])
            # print(y_pred[idxRow])
        print("AVG Accuracy")
        print(accuracy / shape[0] if accuracy > 0 else 0)
        print("Hamming Loss")
        print(hamming_loss(y_test, y_pred))
        return hamming_loss(y_test, y_pred) * 100

    X1 = pd.read_csv('data_encoded.csv')
    X2 = pd.read_csv('data_encoded_2.csv')
    y = pd.read_csv('y.csv')
    y = y.to_numpy()

    return_metrics(X1, y, 'KNN')
    return_metrics(X1, y, 'DTC')
    return_metrics(X1, y, 'ETC')
    return_metrics(X1, y, 'RFC')

    dict_for_df['KNN'].append(return_metrics2(X1, y, 'KNN'))
    dict_for_df['DTC'].append(return_metrics2(X1, y, 'DTC'))


    dict_for_df['ETC'].append(return_metrics2(X1, y, 'ETC'))
    dict_for_df['RFC'].append(return_metrics2(X1, y, 'RFC'))

    for i in range(20):
        dict_for_df['KNN'].append(return_metrics2(X1, y, 'KNN'))
        dict_for_df['DTC'].append(return_metrics2(X1, y, 'DTC'))
        dict_for_df['ETC'].append(return_metrics2(X1, y, 'ETC'))
        dict_for_df['RFC'].append(return_metrics2(X1, y, 'RFC'))

    # data_encoded.csv
    return_metrics(X2, y, 'KNN')
    return_metrics(X2, y, 'DTC')
    return_metrics(X2, y, 'ETC')
    return_metrics(X2, y, 'RFC')

    # data_encoded2.csv
    return_metrics2(X2, y, 'KNN')
    return_metrics2(X2, y, 'DTC')
    return_metrics2(X2, y, 'ETC')
    return_metrics2(X2, y, 'RFC')

    # Hamming Loss
    dict_for_df

    df = pd.DataFrame.from_dict(dict_for_df)
    graph = df.boxplot()
    graph.set_ylabel('Hamming Loss (%)')
