from calculator import Calculator
from grade_calculator import GradeCalculator

# ماشین حساب
calc = Calculator()

print("جمع:", calc.add(10, 5))
print("تفریق:", calc.subtract(10, 5))
print("ضرب:", calc.multiply(10, 5))
print("تقسیم:", calc.divide(10, 5))

# محاسبه معدل
grade = GradeCalculator()

average = grade.calculate_average(18, 16, 14)

print("معدل:", average)
print("نتیجه:", grade.get_result(average))