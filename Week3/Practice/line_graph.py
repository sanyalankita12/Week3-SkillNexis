import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.plot(x,y)

plt.title("Sales")

plt.xlabel("Day")

plt.ylabel("Sales")

plt.grid(True)

plt.show()