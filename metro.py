import pandas as pd
import matplotlib.pyplot as plt

#general
df = pd.read_csv("metro.csv")
main_data = df["traffic_volume"].describe()
daily_df = (
    df.groupby(pd.to_datetime(df["date_time"]).dt.date)
    .agg(
        traffic_volume=("traffic_volume", "sum"),
        weather_main=("weather_main", lambda x: x.mode()[0]),
        holiday = ("holiday", "first")
    )
    .reset_index()
)

print(daily_df.head(20))
# figures
f1 = daily_df["weather_main"].value_counts().plot(kind = "pie", title = "distribution of traffic according to weather")
f1.figure.savefig('weathervstraffic.pdf')
plt.close()

holiday_groups =(
    daily_df.groupby(daily_df["holiday"].notna())["traffic_volume"].mean()
.rename({True: "Holidays", False: "Regular Days"})
)
#extract numbers
avg_holi = holiday_groups["Holidays"]
avg_reg = holiday_groups["Regular Days"]
print(avg_holi, avg_reg)

f2= holiday_groups.plot(kind="bar", title = "Distribution of Traffic on Holidays vs Regular Days")
plt.ylabel("Average Traffic")
f2.figure.savefig('holiday.pdf')
plt.close()
