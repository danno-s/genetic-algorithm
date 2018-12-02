import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

n = input("número de reinas?")

sns.set()

data = pd.read_csv("{}q.csv".format(n))

fig, ax  = plt.subplots()

ax.set_title("Evolución del algoritmo para {} reinas".format(n))

sns.lineplot(x="Generación", y="Máximo", ci="sd", data = data, ax = ax)
sns.lineplot(x="Generación", y="Fitness", ci="sd", data = data, ax = ax)

ax.legend(["Máximo", "Promedio"], loc=4)

plt.show()

