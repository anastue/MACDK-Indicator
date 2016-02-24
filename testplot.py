#set up matplotlib and the figure
import matplotlib.pyplot as plt
plt.figure
 
#create data
x_series = [0,1,2,3,4,5]
y_series_1 = [x**2 for x in x_series]
y_series_2 = [x**3 for x in x_series]
 
#plot data
plt.plot(x_series, y_series_1, label="x^2")
plt.plot(x_series, y_series_2, label="x^3")
 
#add in labels and title
plt.xlabel("Small X Interval")
plt.ylabel("Calculated Data")
plt.title("Our Fantastic Graph")
 
#add limits to the x and y axis
plt.xlim(0, 6)
plt.ylim(-5, 80) 
 
#create legend
plt.legend(loc="upper left")
 
#save figure to png
plt.savefig("example.png")
