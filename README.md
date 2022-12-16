# tetouan_power_consumption
Linear regression with sklearn on a large dataset

Various weather data from 2017 collected from Tetouan, Morocco. Source: https://archive.ics.uci.edu/ml/datasets/Power+consumption+of+Tetouan+city.

This code is playing with the linear regression function from scikit-learn, and plotting various aspects of the dataset with matplotlib.

The whole dataset was split for training (first 80% of the rows, roughly 42,000 datapoints) and testing (the last 20%, roughly 10,000). The training data
was plotted using temperature on the horizontal axis and humidity as a color scale, and power consumption as the dependent variable:
![image](https://user-images.githubusercontent.com/65456795/208005924-790aed04-9ed7-40bb-8c92-131662297876.png)

The testing dataset was plotted in the same way:
![image](https://user-images.githubusercontent.com/65456795/208006165-9b708e0a-0bd3-418a-a0d2-d6f6b4308cfd.png)

Results...
Coefficient of determination with training data: 0.1989
Coefficient of determination with testing data: 0.0806
Equation: power_consumption = -188.79*temperature + -0.1*humidity + -3.45*diffuse_flow + -29.95*time + 660.4*wind_speed

So the there is a linear correlation between the independent variables and power consumption, but the equation does not have great predictive reliability.
