import sys

command = sys.argv[1]

if command == 'reverse' or command == 'copy':
    if len(sys.argv) != 4:
        print("Error: Incorrect number of arguments for '{}' command.".format(command))
        exit()
elif command == 'duplicate-contents':
    if len(sys.argv) != 4:
        print("Error: Incorrect number of arguments for 'duplicate-contents' command.")
        exit()
elif command == 'replace-string':
    if len(sys.argv) != 5:
        print("Error: Incorrect number of arguments for 'replace-string' command.")
        exit()
else:
    print("Error: Unrecognized command '{}'.".format(command))
    exit()

def reverse():
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    contents = ''

    with open(input_file) as i_f:
        contents = i_f.read()

    reversed_contents = contents[::-1]

    with open(output_file, 'w') as o_f:
        o_f.write(reversed_contents)

def copy():
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    contents = ''

    with open(input_file) as i_f:
        contents = i_f.read()

    with open(output_file, 'w') as o_f:
        o_f.write(contents)

def duplicate_contents():
    input_file = sys.argv[2]
    duplicate_count = int(sys.argv[3])
    contents = ''

    with open(input_file) as i_f:
        contents = i_f.read()

    duplicated_contents = contents * duplicate_count

    with open(input_file, 'w') as i_f:
        i_f.write(duplicated_contents)

def replace_string():
    input_file = sys.argv[2]
    replace_target = sys.argv[3]
    new_string = sys.argv[4]
    contents = ''

    with open(input_file) as i_f:
        contents = i_f.read()
        
    replaced_contents = contents.replace(replace_target, new_string)

    with open(input_file, 'w') as i_f:
        i_f.write(replaced_contents)



if (command == 'reverse'):
    reverse()
elif(command == 'copy'):
    copy()
elif(command == 'duplicate-contents'):
    duplicate_contents()
elif(command == 'replace-string'):
    replace_string()