# Interpreter for the Binary Turing Machine programming language
# Created by Jamie Large in 2022
import sys
from Machine import Machine

def process_code(code):
	m = Machine()
	for line in code:
		if line != "\n":
			m.process_command(line[:-1])

	m.run_machine()

if len(sys.argv) > 1:
	with open(sys.argv[1], "r") as f:
		lines = f.readlines()
		if len(lines) > 0 and lines[-1][-1] != "\n":
			lines[-1] += "\n"
		process_code(lines)
else:
	str_buf = []
	for line in sys.stdin:
		str_buf.append(line)
	process_code(str_buf)