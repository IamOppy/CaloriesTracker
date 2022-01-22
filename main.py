from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from CalorieCalc import CalorieCalculator
from excelSheet import ExcelSheet
import os

Builder.load_file("screens.kv")


class MainScreen(Screen):

    def submit(self):
        name_query = self.manager.current_screen.ids.name.text
        height_query = self.manager.current_screen.ids.height_cm.text
        gender_query = self.manager.current_screen.ids.gender.text
        age_query = self.manager.current_screen.ids.age.text
        hours_query = self.manager.current_screen.ids.hours.text
        weight_query = self.manager.current_screen.ids.weight_kg.text
        Result = CalorieCalculator(name=name_query,
                                   height=height_query,
                                   gender=gender_query,
                                   age=age_query,
                                   weight=weight_query,
                                   hours=hours_query)

        save = ExcelSheet(calories_lost=int(Result.calculate_cals_lost()),
                          sleep_hours=hours_query)
        save.save_to_sheet()

        self.ids.result.text = "You lost" +" "+ str(int(Result.calculate_cals_lost())) + f" calories in {hours_query} hours last night"

    def open_records(self):
        file = 'RecentRecords.xlsx'
        try:
            os.startfile("RecentRecords.xlsx")

        except Exception:
           self.ids.result.text = "File not found. Made a new one."
           open(file, "a").close()

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()