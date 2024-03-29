# Machine for the Binary Turing Machine programming language
# Created by Jamie Large in 2022
BLANK = 0
INITIAL_STATE = 0
INPUT_STATE = 1
OUTPUT_STATE = 2

class Machine:
	def __init__(self):
		self.tape = []
		self.rules = {}
		self.current_rule = []

	# Process a binary command
	def process_command(self, command):
		if len(command) < 1 or command[-1] not in ("?", "!") or not all(c == "0" or c == "1" for c in command[:-2]):
			raise SyntaxError("Invalid command: " + command);

		# New part of rule
		if command[-1] == "!":
			# Add this to the current rule
			try:
				self.current_rule.append(int(command[:-1], 2))
			except:
				raise SyntaxError(f"Invalid command: {command}")

			# if the previous rule is now complete, add it to the rules
			if len(self.current_rule) == 5:
				self.rules[(self.current_rule[0], self.current_rule[1])] = (self.current_rule[2], self.current_rule[3], self.current_rule[4])
				self.current_rule = []
			
		# New input
		elif command[-1] == "?":
			# Add this to the tape
			try:
				self.tape.append(int(command[:-1], 2))
			except:
				raise SyntaxError(f"Invalid command: {command}")

	# Run the Turing Machine on the specified input
	def run_machine(self):
		# for rule in self.rules:
		# 	print(f"{rule} => {self.rules[rule]}")
		# print(self.tape)
		index = 0
		state = INITIAL_STATE
		if len(self.tape) == 0:
			self.tape.append(BLANK)
		c_symbol = self.tape[index]
		while (state, c_symbol) in self.rules or state in (INPUT_STATE, OUTPUT_STATE):
			# print(f"{(state, c_symbol)}, {index}, {self.tape}")
			# INPUT STATE
			if state == INPUT_STATE:
				user_input = input()
				try:
					int_input = ord(user_input)
					self.tape[index] = int_input
				except:
					int_input = 0
					for c in user_input:
						int_input += ord(c)
					self.tape[index] = int_input
				state = INITIAL_STATE
				index += 1

			# OUTPUT STATE
			elif state == OUTPUT_STATE:
				if c_symbol != BLANK:
					try:
						p_symbol = chr(c_symbol)
						print(p_symbol, end='')
					except:
						print(c_symbol, end='')
					index += 1
				else:
					state = INITIAL_STATE
					index += 1

			# OTHER STATE
			else:
				state, n_symbol, direction = self.rules[(state, c_symbol)]
				self.tape[index] = n_symbol
				index = max(index + (1 if direction % 2 == 0 else -1), 0)

			if index == len(self.tape):
				self.tape.append(0)
			c_symbol = self.tape[index]