class GradeCalculator:

    def calculate_average(self, grade1, grade2, grade3):
        average = (grade1 + grade2 + grade3) / 3
        return average

    def get_result(self, average):
        if average >= 10:
            return "Passed"
        else:
            return "Failed"