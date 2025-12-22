import pandas as pd
import matplotlib.pyplot as plt

# payment methods ka data
pm = ["UPI", "Debit Card", "Credit Card", "Net Banking", "Wallet"]
tr = [450, 200, 150, 120, 80]

# dataframe banaya
df = pd.DataFrame()
df["Payment Method"] = pm
df["Transactions"] = tr

# data print kiya
print(df)

# simple statistics
print("\nStatistics:")
print(df["Transactions"].describe())

# pie chart
plt.pie(tr, labels=pm, autopct="%1.1f%%")
plt.title("Online Payment Methods")
plt.show()

# bar chart
plt.bar(pm, tr)
plt.xlabel("Payment Method")
plt.ylabel("Transactions")
plt.title("Transactions by Payment Method")
plt.show()
