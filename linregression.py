import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

# function to show the scatter plot
def plot(x, xlabel, y, ylabel, color):
    plt.scatter(x, y, c=color, cmap='cividis', alpha=0.3)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar();
    plt.show()

# load in data from csv
data = np.genfromtxt('tetuan_power_consumption.csv', delimiter=',')

# drop the column names
data = np.delete(data, 0, 0)
# drop the date column
data = np.delete(data, 0, 1)

# adding new "time" column
rows = data.shape[0]
time = np.arange(rows)
time = time.reshape(-1, 1)
data = np.append(data, time, axis=1)

# specify training data
training_rows = np.int64(rows* 0.8)
training_data = np.array(data[:training_rows])

# specify test data
test_data = np.array(data[training_rows:])

# independent variable, time column
time = np.array(training_data[:,8])

# independent variable, temperature column (rounded to 2 digits)
temperature = np.array(training_data[:,0])
temperature = np.array([np.round(num, 2) for num in temperature])

# another independent variable, humidity
humidity = np.array(training_data[:,1])

# another independenet variable, diffuse flow
diffuse_flow = np.array(training_data[:,4])

# another independent variable, wind speed
wind_speed = np.array(training_data[:,2]) # needs classification instead of regression

# dependent variable, zone 1 power consumption
power_consumption = np.array(training_data[:,5])

# performing linear regression #

# assign x and y data
x = temperature.reshape((-1, 1)) # adjust x to column if necessary
y = power_consumption

# create the linear regression model, and fit it with x and y
model = LinearRegression().fit(x, y)

# assertain the accuracy of the model
r_squared = model.score(x, y)
print(f"coefficient of determination: {r_squared}") # only 0.17!!! so bad!
print(f"intercept: {model.intercept_}")

# plot the scatter
plot(x, "temp", y, "power consumption", humidity)

