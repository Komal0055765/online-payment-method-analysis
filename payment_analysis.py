 #Online Payment Method Analysis

import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Load CSV file
df = pd.read_csv("digital_payment.csv")

print("Dataset Loaded Successfully")
print(df.head())

# STEP 2: Analyze usage of payment methods
payment_usage = df["payment_type"].value_counts()

print("\nPayment Method Usage:")
print(payment_usage)

# STEP 3: Statistical Analysis
print("\nStatistical Analysis:")

print("Total Transactions:", df["transaction_amount"].count())
print("Total Amount:", df["transaction_amount"].sum())
print("Average Transaction Amount:", df["transaction_amount"].mean())
print("Maximum Transaction Amount:", df["transaction_amount"].max())
print("Minimum Transaction Amount:", df["transaction_amount"].min())

# STEP 4: Bar Chart
plt.figure()
payment_usage.plot(kind="bar")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.title("Usage of Online Payment Methods")
plt.show()

# STEP 5: Pie Chart
plt.figure()
payment_usage.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.ylabel("")
plt.title("Distribution of Online Payment Methods")
plt.show()

