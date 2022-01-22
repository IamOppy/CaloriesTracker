import pandas as pd
import datetime


class ExcelSheet:
    df = pd.read_excel('RecentRecords.xlsx')
    def __init__(self, calories_lost, sleep_hours):
        self.date_today = datetime.datetime.now().strftime("%Y-%m-%d")
        self.calories_lost = calories_lost
        self.sleep_hours = sleep_hours

    def save_to_sheet(self):
        df = self.df.append({"DATE":self.date_today,
                             "CALORIES LOST":self.calories_lost,
                            "SLEEP HOURS":self.sleep_hours},
                            ignore_index=True)
        df.to_excel("RecentRecords.xlsx", index=False)

if __name__ == "__main__":
    obj1 = ExcelSheet(calories_lost=833, sleep_hours=8)
    obj1.save_to_sheet()