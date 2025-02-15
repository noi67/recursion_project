import markdown
import sys

if len(sys.argv) != 4:
    print('Error: Incorrect number of arguments')
    sys.exit()

command = sys.argv[1]

if (command != 'markdown'):
    print("Error: Unrecognized command '{}'.".format(command))
    sys.exit()

input_file = sys.argv[2]
output_file = sys.argv[3]

with open(input_file) as i_f:
    contents = i_f.read()

html = markdown.markdown(contents)

with open(output_file, 'w') as o_f:
    o_f.write(html)



