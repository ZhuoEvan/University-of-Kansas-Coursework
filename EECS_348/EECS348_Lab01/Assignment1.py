#Read and React to the Command Function
def read_command(command_list):
    for command in command_list:
        print(command[0])

#Opening and Extracting File Content Function
def split_file(filename):
    #Local Variables
    file_content = []
    
    #Opening the file
    with open(filename, 'r') as file_opened:
        for line in file_opened:
            file_content.append(line.strip().split(','))
    
    return file_content

#Main Function
def main():
    filename = 'Assignment1_Test_File.txt'
    command_list = split_file(filename)
    read_command(command_list)

main()