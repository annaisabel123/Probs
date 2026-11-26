import pandas as pd
import matplotlib.pyplot as plt

#general
df = pd.read_csv("metro.csv")
main_data = df["traffic_volume"].describe()
daily_df = (
    df.drop_duplicates(subset=["date_time"])
    .groupby(pd.to_datetime(df["date_time"]).dt.date)
    .agg(
        traffic_volume=("traffic_volume", "sum"),
        weather_main=("weather_main", lambda x: x.mode()[0]),
        holiday = ("holiday", "first")
    )
    .reset_index()
)


# figures

f1 = (
    daily_df.groupby("weather_main")["traffic_volume"]
    .mean()
    .sort_values()
    .plot(kind="bar", title="Distribution of Traffic According to Weather")
)

plt.xlabel("Weather Condition")
plt.ylabel("Average Daily Traffic Volume")

f1.figure.savefig("weathervstraffic.pdf", bbox_inches="tight")
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
