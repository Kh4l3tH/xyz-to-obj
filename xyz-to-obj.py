import os
import sys

edge_length = 0.1

if len(sys.argv) == 2:
	input_file = sys.argv[1]
elif len(sys.argv) == 3:
	input_file = sys.argv[1]
	edge_length = float(sys.argv[2])
else:
	print('Usage: xyz-to-obj.py input_file edge_length', 'asd')
	exit()

output_file = os.path.splitext(input_file)[0] + '.obj'

with open(output_file, 'a') as output_file:
	with open(input_file) as input_file:
		for i, line in enumerate(input_file):
			n = i*8

			line = line.split(' ')
			x = float(line[0])
			y = float(line[1])
			z = float(line[2])

			output_file.write('v {0:.6f} {1:.6f} {2:.6f}\n'.format(x+edge_length, y+edge_length, z+edge_length))
			output_file.write('v {0:.6f} {1:.6f} {2:.6f}\n'.format(x-edge_length, y+edge_length, z+edge_length))
			output_file.write('v {0:.6f} {1:.6f} {2:.6f}\n'.format(x-edge_length, y-edge_length, z+edge_length))
			output_file.write('v {0:.6f} {1:.6f} {2:.6f}\n'.format(x+edge_length, y-edge_length, z+edge_length))
			output_file.write('v {0:.6f} {1:.6f} {2:.6f}\n'.format(x+edge_length, y+edge_length, z-edge_length))
			output_file.write('v {0:.6f} {1:.6f} {2:.6f}\n'.format(x-edge_length, y+edge_length, z-edge_length))
			output_file.write('v {0:.6f} {1:.6f} {2:.6f}\n'.format(x-edge_length, y-edge_length, z-edge_length))
			output_file.write('v {0:.6f} {1:.6f} {2:.6f}\n'.format(x+edge_length, y-edge_length, z-edge_length))

			output_file.write('f {0} {1} {2} {3}\n'.format(n+1, n+2, n+3, n+4))
			output_file.write('f {0} {1} {2} {3}\n'.format(n+5, n+6, n+7, n+8))
			output_file.write('f {0} {1} {2} {3}\n'.format(n+1, n+2, n+6, n+5))
			output_file.write('f {0} {1} {2} {3}\n'.format(n+2, n+3, n+7, n+6))
			output_file.write('f {0} {1} {2} {3}\n'.format(n+3, n+4, n+8, n+7))
			output_file.write('f {0} {1} {2} {3}\n'.format(n+4, n+1, n+5, n+8))
