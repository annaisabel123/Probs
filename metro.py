import pandas as pd
import matplotlib.pyplot as plt

#general
df = pd.read_csv("metro.csv")
main_data = df.describe()

#figures
f1 = df["weather_main"].value_counts().plot(kind = "pie", title = "distribution of traffic according to weather")
f1.figure.savefig('weathervstraffic.pdf')
plt.close()

f2 = df.groupby(df["holiday"].notna())["traffic_volume"].mean().plot(kind="bar", title = "distribution of traffic holidays vs none holidays")
f2.figure.savefig('holiday.pdf')
plt.close()