import argparse, math

class Income:
	def __init__(self, name, times_per_month, amt):
		self.name = name
		self.times_per_month = times_per_month
		self.amount = amt

	def review(self):
		print '\tIncome'
		print '\t\t' + self.name + ': ' + str(self.calculate())

	def calculate(self):
		return self.times_per_month * self.amount

class Investment:
	def __init__(self, name, p, r, n, t):
		self.name = name
		self.principle = p
		self.rate = r
		self.compound = n
		self.time_period = t

	# P(1 - r/n)^(n*t)
	def calculate(self):
		nt = self.time_period * self.compound / 12
		paren = 1 + (self.rate / self.compound)
		return self.principle * math.pow(paren, nt)

class Budget:
	def __init__(self):
		self.appt_gas = 0
		self.car_gas = 0
		self.groceries = 0
		self.rent = 0
		self.miscs = []

	def __init__(self, appt_gas, car_gas, groceries, rent, miscs):
		self.appt_gas = appt_gas
		self.car_gas = car_gas
		self.groceries = groceries
		self.rent = rent
		self.miscs = miscs

	def review(self):
		print '\tBudget'

		print '\t\tAppartment bills'
		print '\t\t\tGas: ' + str(self.appt_gas)
		print '\t\t\tRent: ' + str(self.rent)
		print '\t\t\tTotal: ' + str(self.appt_gas + self.rent)

		print '\t\tLife'
		print '\t\t\tGroceries: ' + str(self.groceries)
		print '\t\t\tCar Gas: ' + str(self.car_gas)
		print '\t\t\tTotal: ' + str(self.groceries + self.car_gas)

		for misc in self.miscs:
			misc.review()

		print '\t\tMonthly total: ' + str(self.calculate())

	def calculate(self):
		total = 0
		for misc in self.miscs:
			total = total + misc.calculate()
		return self.appt_gas + self.car_gas + self.rent + self.groceries + total

class Misc:
	def __init__(self, reason, amount):
		self.reasoning = reason
		self.amount = amount

	def review(self):
		print '\t'+ self.reasoning
		print '\t\t' + str(self.amount)

	def calculate(self):
		return self.amount

class Month:
	def __init__(self, name, budget, incomes):
		self.name = name
		self.budget = budget
		self.incomes = incomes

	def review(self, details):
		print self.name
		if details:
			for income in self.incomes:
				income.review()

			self.budget.review()

		print 'In the end...'
		print str(self.calculate())

	def calculate(self):
		total_income = 0
		for income in self.incomes:
			total_income = total_income + income.calculate()

		total_budget = self.budget.calculate()

		return total_income - total_budget

class Year:
	def __init__(self, months):
		self.months = months
		self.savings = 0
		self.checking = 0

	def add_month(self, month):
		self.months.append(month)

	def review(self, details):
		for month in self.months:
			month.review(details)

		print 'Overall: ' + str(self.calculate())

	def calculate(self):
		total = 0
		for month in self.months:
			total = total + month.calculate()

		return self.savings + self.checking + total


if __name__ == '__main__':
	# parse the parameters given
	parser = argparse.ArgumentParser()

	# optional
	parser.add_argument('--savings', help='amount in savings account at the beginning of the month')
	parser.add_argument('--checking', help='amount in checking account at the beginning of the month')

	args = parser.parse_args()
	savings = int(args.savings)
	checking = int(args.checking)


