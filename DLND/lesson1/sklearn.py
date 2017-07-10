from sklearn.model_selection import train_test_split

x_train, y_train, x_test, y_test = train_test_split(x, y, test_size= 0.25) #4 test if 16 total
#never use your testing data for training

#Medical Model

#Accuracy
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression

classifier = LinearRegression()
classifier.fit(x,y)

guesses = classifier.predict(x)

error = mean_absolute_error(y, guesses)

accuracy_score(y_true, y_pred)

#mean square error = R2 = 1 - 
# R2 is close to 1 = good model
# R2 is 0 = bad model, no better than taking the average.

#underfitting
#high bias vs overfitting