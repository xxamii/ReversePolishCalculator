def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

operators = {
	'+': (1, add),
	'-': (1, subtract),
	'*': (2, multiply),
	'/': (2, divide)
}

def get_float_or_int(number : str):
	try:
		n = float(number)

		if n.is_integer():
			return int(n)
		else:
			return n

	except ValueError:
		print(f'Tried to parse an invalid number: {n}')
		return None

def parse_formula(formula : str) -> list:
	output_tokens = []
	current_number = ''

	for t in formula:
		if t.isnumeric():
			current_number += t
		elif not current_number == '':
			output_tokens.append(get_float_or_int(current_number))
			current_number = ''
		
		if t in operators.keys() or t in '()':
			output_tokens.append(t)

	if not current_number == '':
		output_tokens.append(get_float_or_int(current_number))
		current_number = ''

	return output_tokens


def parse_tokens(tokens : list) -> list:
	operators_stack = []
	output_tokens = []

	for t in tokens:
		if not type(t) is str:
			output_tokens.append(t)

		elif t in operators.keys():
			while len(operators_stack) > 0 and operators_stack[len(operators_stack) - 1] in operators.keys() and operators[operators_stack[len(operators_stack) - 1]][0] >= operators[t][0]:
				output_tokens.append(operators_stack.pop())

			operators_stack.append(t)

		elif t == '(':
			operators_stack.append(t)

		elif t == ')':
			el = operators_stack.pop()

			while not el == '(':
				output_tokens.append(el)
				el = operators_stack.pop()

	while len(operators_stack) > 0:
		output_tokens.append(operators_stack.pop())

	return output_tokens

def evaluate_tokens(tokens : list):
	stack = []

	for t in tokens:
		if not type(t) is str:
			stack.append(t)
		elif t in operators.keys():
			b = stack.pop()
			a = stack.pop()
			stack.append(operators[t][1](a, b))

	return get_float_or_int(str(stack[0]))

def main():
	tokens = parse_tokens(parse_formula(input('Enter formula: ')))
	print(evaluate_tokens(tokens))

if __name__ == '__main__':
	main()