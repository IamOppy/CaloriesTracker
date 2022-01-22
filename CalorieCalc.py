import excelSheet

class CalorieCalculator:
    def __init__(self, name, height, gender, age, weight, hours):
        self.name = name
        self.height = int(height)
        self.gender = gender
        self.age = int(age)
        self.weight = int(weight)
        self.hours = int(hours)

    def _calculate_BMR(self):
        if self.gender == "Male" or "male":
            BMRresult = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        if self.gender == "Female" or "female":
            BMRresult = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)

        return BMRresult

    def calculate_cals_lost(self):
        BMR_Result = self._calculate_BMR()
        cals_lost = (BMR_Result/24) * self.hours * 0.85
        return cals_lost


if __name__ == "__main__":
    obj1 = CalorieCalculator(name="Randolf", height=175, gender="Male", age=40, weight=195, hours=8)
    print(obj1.calculate_cals_lost())