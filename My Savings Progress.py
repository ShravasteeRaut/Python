import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
savings = [100, 150, 80, 200, 120]

plt.plot(days, savings)
plt.show()

plt.plot(days, savings)

plt.title('My Savings Progress')
plt.xlabel('Day of the Week')
plt.ylabel('Savings (₹)')
plt.grid(True)
plt.ylim(0, 250)

plt.show()

plt.plot(days, savings, color='blue', marker='o', linestyle='dashed', linewidth=2, markerfacecolor='red', markeredgecolor='black')

plt.title('My Savings Progress')
plt.xlabel('Day of the Week')
plt.ylabel('Savings (₹)')
plt.grid(True)
plt.ylim(0, 250)

plt.show()

plt.bar(days, savings, color='orange')

plt.title('My Savings Bar Chart')
plt.xlabel('Days of the Week')
plt.ylabel('Savings (₹)')
plt.ylim(0, 250)

plt.show()




