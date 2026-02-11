import matplotlib.pyplot as plt
import seaborn as sns

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

# 1️. Line Chart using Matplotlib
plt.plot(months, sales, marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)

plt.show()
plt.savefig("line.png")

# 2.️ Bar Plot using Seaborn
sns.set_style("whitegrid")

sns.barplot(x=months, y=sales)

plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)

plt.show()
plt.savefig("bar.png")
