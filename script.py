import pandas as pd
import random
from datetime import datetime


def preprocessing():
    heart_rate_variability = []
    hrv_value = 60.00 # mean: 50 +- 16
    heart_rate = []
    hr_value = 60 # mean: 60-100, stress: can go up to 220
    temperature_gauge= []
    temp = 25.00 # mean: 15-35, firstdeg: 48, seconddeg: 55, thirddeg: 72

    unix_time = 1577836800 # 1 Jan 2020, 00:00:00
    firefighters = {"F1":"Hakim", "F2":"Vinod", "F3":"Bradley", "F4":"JunWei", "F5":"Kishore"}

    for f in firefighters:
        for i in range(172800):
            # 9AM to 9PM (both days)
            if 1577869200 <= unix_time <= 1577912400 or 1577955600 <= unix_time <= 1577998800:
                # 1st fire call (1pm to 2pm)
                if 1577883600 <= unix_time <= 1577887200:
                    hrv_range_fire = [round(random.randint(20, 30), 2) for x in range(3600)]
                    foo_hr = [round(random.randint(90, 180), 2) for x in range(3600)]
                    hr_range_fire = foo_hr[len(foo_hr) % 2::2] + foo_hr[::-2]
                    foo_temp = [round(random.randint(35, 45), 2) for x in range(3600)]
                    temp_range_fire = foo_temp[len(foo_temp) % 2::2] + foo_temp[::-2]
                    for num in range(3600):
                        ts = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
                        heart_rate_variability.append([ts, firefighters[f], hrv_range_fire[num]])
                        heart_rate.append([ts, firefighters[f], hr_range_fire[num]])
                        temperature_gauge.append([ts, firefighters[f], temp_range_fire[num]])
                        unix_time += 1
                    i += 3600
                # 2nd fire call (10am to 11am)
                elif 1577959200 <= unix_time <= 1577962800:
                    hrv_range_fire = [round(random.randint(20, 25), 2) for x in range(3600)]
                    foo_hr = [round(random.randint(100, 220), 2) for x in range(3600)]
                    hr_range_fire = foo_hr[len(foo_hr) % 2::2] + foo_hr[::-2]
                    foo_temp = [round(random.randint(35, 60), 2) for x in range(3600)]
                    temp_range_fire = foo_temp[len(foo_temp) % 2::2] + foo_temp[::-2]
                    for num in range(3600):
                        ts = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
                        heart_rate_variability.append([ts, firefighters[f], hrv_range_fire[num]])
                        heart_rate.append([ts, firefighters[f], hr_range_fire[num]])
                        temperature_gauge.append([ts, firefighters[f], temp_range_fire[num]])
                        unix_time += 1
                    i += 3600
                # non-call duty times
                else:
                    hrv_value = random.uniform(50, 65)
                    hr_value = random.randint(60, 70)
                    temp = random.uniform(25, 30)
                    ts = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
                    heart_rate_variability.append([ts, firefighters[f], hrv_value])
                    heart_rate.append([ts, firefighters[f], hr_value])
                    temperature_gauge.append([ts, firefighters[f], temp])
                    unix_time += 1
            # sleep time 9PM to 9AM (both days)
            else:
                hrv_value = random.uniform(60, 65)
                hr_value = random.randint(50, 55)
                temp = random.uniform(20, 25)
                ts = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
                heart_rate_variability.append([ts, firefighters[f], hrv_value])
                heart_rate.append([ts, firefighters[f], hr_value])
                temperature_gauge.append([ts, firefighters[f], temp])
                unix_time += 1
    return heart_rate_variability, heart_rate, temperature_gauge


def postprocessing(heart_rate_variability, heart_rate, temperature_gauge):
    df_hrv = pd.DataFrame(heart_rate_variability)
    df_hr = pd.DataFrame(heart_rate)
    df_temp = pd.DataFrame(temperature_gauge)
    df_hrv.to_csv('heart_rate_variability.csv', index=False)
    df_hr.to_csv('heart_rate.csv', index=False)
    df_temp.to_csv('temperature_gauge.csv', index=False)


if __name__ == '__main__':
    heart_rate_variability, heart_rate, temperature_gauge = preprocessing()
    postprocessing(heart_rate_variability, heart_rate, temperature_gauge)