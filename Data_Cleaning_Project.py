import pandas as pd

# Data banaya ja raha hai
data = {
    'Day': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    'Sales': [5000, 7000, 4000, 6000, 9000, 12000, 8000]
}

# Data ko Pandas DataFrame mein convert kiya
df = pd.DataFrame(data)

# Calculations
total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()
highest_sales = df['Sales'].max()
highest_day = df.loc[df['Sales'].idxmax(), 'Day']
lowest_sales = df['Sales'].min()
lowest_day = df.loc[df['Sales'].idxmin(), 'Day']

print("===== WEEKLY SALES REPORT (Using Pandas) =====")
print(f"Total Sales: Rs. {total_sales}")
print(f"Average Daily Sales: Rs. {average_sales:.2f}")
print(f"Highest Sales: Rs. {highest_sales} ({highest_day})")
print(f"Lowest Sales: Rs. {lowest_sales} ({lowest_day})")
