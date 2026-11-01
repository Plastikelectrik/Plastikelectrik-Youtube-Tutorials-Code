import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def load_data(file_name):
    # Load data from file
    data = np.loadtxt(file_name)
    return data

def predict_handwriting_style(data):
    # Train model and make predictions
    X_train, X_test, y_train, y_test = train_test_split(data[:, :-1], data[:, -1], test_size=0.2, random_state=42)
    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)
    return lr_model.predict(X_test)

def main():
    # Load and predict handwriting style
    data = load_data('handwriting_data.csv')
    predictions = predict_handwriting_style(data)
    print(predictions)
if __name__ == '__main__':
    main()
