class Programm:
	"""
	Programm 
	класс, который принимает входные значения
	и вызывает нужные методы
	"""
	def get_operands(self): 
		operands = []
		for i in range(5):
			try:
				value = int(input())
				if ((value < 0) or (value > 1)):
					 raise MyError("Неверный вид данных. Либо 0 (ложь), либо 1 (истина)")
			except ValueError:
				print("Неверный тип данных")
				break
			except MyError as error:
				print(error)
				break
			else:
				operands.append(value)
		return operands
	def give_operands(self, operands, need_op): # возвращает операнд, который мы укажем
		# операнды расставлены по порядку их добавления 
		op = {1: operands[0], 2: operands[1], 3: operands[2], 4: operands[3], 5: operands[4]}
		return op[need_op]
	def run_programm(self, operands):
		logic = Logic()

		self.a = operands[0]
		self.b = operands[1]
		self.c = operands[2]
		self.d = operands[3]
		self.e = operands[4]
		
		first_op = logic.implication(self.a, self.b)
		second_op = logic.equal(self.b, self.c)
		third_op = logic.implication(logic.implication(self.e, self.b), self.c)
		fourth_op = logic.equal(self.d, (not self.e))
		result = ((not first_op) or (second_op)) and ((third_op) or (fourth_op))
		if result:
			return result
		else:
			return 0

class MyError(Exception):
	"""Класс с моими исключениями"""
	def __init__(self, text):
		self.txt = text
		
class Logic:
	"""Logic - класс, хранящий в себе всю логику"""

	def implication(self, a, b): #следование
		if (not a) or b:
			return 1
		else:
			return 0
	def equal(self, a, b): #эквиваленция
		if not((not a and b) or (not b and a)):
			return 1
		else:
			return 0

print("************************")
print("~~~~Добро пожаловать~~~~")
print("************************")
print("Введите данные (0 либо 1). Я проделаю с ними следующие манипуляции:\nnot(A → B)or(B ↔ C)and(E → B → C)or(D ↔ (not E))")
print("И выведу таблицу истинности =))")
print("Только запомни: один раз ошибёшься и я обижусь")
programm = Programm()

while True:
	try:
		operands = programm.get_operands() #входящие данные
		result = programm.run_programm(operands) #запуск основной программы
	except IndexError:
		print("Попробуйте ещё раз =((")
	else:
		print("A: {0}, B: {1}, C: {2}, D: {3}, E: {4}, F: {5}"
		.format(
			programm.give_operands(operands, 1),
			programm.give_operands(operands, 2),
			programm.give_operands(operands, 3),
			programm.give_operands(operands, 4),
			programm.give_operands(operands, 5),
			result
		))
	finally:
		pass