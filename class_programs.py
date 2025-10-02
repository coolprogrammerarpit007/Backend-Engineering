# Exercises: Level 1
# Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

class Statistics:
    def __init__(self,ages):
        self.ages = ages

    def count_numbers(self):
        return f"Count: {len(self.ages)}"

    def sum_numbers(self):
        total = 0
        for age in self.ages:
            total += age

        return f"Sum: {total}"

    def min_numbers(self):
        smallest = None

        for age in self.ages:
            if smallest is None or smallest > age:
                smallest = age

        return f"Min: {smallest}"

    def max_numbers(self):
        largest = None

        for age in self.ages:
            if largest is None or largest < age:
                largest = age

        return f"Max: {largest}"

    def range_numbers(self):
        largest = None
        smallest = None

        for age in self.ages:
            if largest is None or largest < age:
                largest = age

            if smallest is None or smallest > age:
                smallest = age


        range = largest - smallest
        return f"Range: {range}"

    def mean_numbers(self):
        avg_number = None

        total = sum(self.ages)
        avg_number = total/len(self.ages)
        return f"Mean: {avg_number}"

    def median(self):
        pass

    def mode(self):
        pass

    def standard_deviation(self):
        pass

    def variance(self):
        pass

    def freq_dist(self):
        pass

    def describe(self):
        pass


data = Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])
print(data.count_numbers())
print(data.sum_numbers())
print(data.min_numbers())
print(data.max_numbers())
print(data.range_numbers())
print(data.mean_numbers())



# Exercises: Level 2
# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.