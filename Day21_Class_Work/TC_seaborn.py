import seaborn as sns
import matplotlib.pyplot as plt

mark=[50,60,70,80,90,65]

sns.set_style("whitegrid")
sns.histplot(mark,bins=5)
plt.title("Marks")
plt.show()
