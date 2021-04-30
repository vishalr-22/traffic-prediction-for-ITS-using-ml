import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score

class dbservice:
    def svm(self,junction, vehicles):
        # Importing the dataset
        dataset = pd.read_csv('trafficc.csv')           
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, -1].values

        # Splitting the dataset into the Training set and Test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
        print(X_train)
        print(X_test)
        print(y_test)

        # Feature Scaling
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        print(X_train)
        print(X_test)

        #Training the SVM model on the Training set
        classifier1 = SVC(kernel = 'linear', random_state = 0)
        classifier1.fit(X_train, y_train)
        
        # Predicting a new result
        print(classifier1.predict(sc.transform([[junction,vehicles]])))

        # Predicting the Test set results
        y_pred = classifier1.predict(X_test)
        
        # Making the Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        print(cm)
        print(accuracy_score(y_test, y_pred))

        #returning the predicted value
        return classifier1.predict(sc.transform([[junction,vehicles]])) 


    