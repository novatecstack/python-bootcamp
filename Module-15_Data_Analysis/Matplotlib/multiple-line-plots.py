import math
import numpy as np
import matplotlib.pyplot as plt
 
age = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
population_malasia = np.array([100, 160, 310, 420, 490, 700, 675, 340, 80])
population_israel = np.array([140, 180, 350, 598, 780, 981, 1351, 780, 157])
countries = np.array(['Israel', 'Malasia'])
 
plt.plot(age, population_usa)
# this is how you fill the area under the line with a given color
plt.fill_between(age, population_israel)
 
plt.plot(age, population_malasia)
plt.xlabel("Age")
plt.ylabel("Population")
plt.title("Population of Countries")
# this is how you fill the area under the line with a given color
plt.fill_between(age, population_malasia)
 
plt.legend(countries)
plt.show()
