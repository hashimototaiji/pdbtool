#Prologue
#File opened
txt_file=open('pdbtool.pdb')
#Counting number of appearances of word 'ATOM'
count = 0
#Looping through each line in the text file
for line in txt_file:
  #Variable 'line' set as list of words
  line=line.split()
  #Seeing if first word is 'ATOM'
  if line[0] == 'ATOM':
    #Increase count by 1 if first word is 'ATOM'
    count+=1
#Print(text)
print("Welcome to the pdb program.\n")
print("To begin, try typing 'help' for the list of valid commands.\n")
print(count,"atoms recorded.\n\n")
#User Input
command=input("Enter a command: ")
#'quit' command to quit program
if command == "quit":
  quit()
#Outputs for command 'help'
elif command == "help":
#List of valid commands
  print("atomfreq\nresfreq\nreslength\ntempcheck\noccupancy\nquit")
#Enter input for second command
  command_=input("Enter a command: ")
#Outputs of second command
  if command_ == "quit":
    quit()
  elif command_ == "atomfreq":
    command_ = command_
  elif command_ == "resfreq":
    command_ = command_
  elif command_ == "reslength":
    command_ = command_
  elif command_ == "tempcheck":
    command_ = command_
  elif command_ == "occupancy":
    command_ = command_
#Outputs for 'atomfreq', 'resfreq', 'reslength', 'tempcheck', 'occupancy'
elif command == "atomfreq":
  command = command
elif command == "resfreq":
  command = command
elif command == "reslength":
  command = command
elif command == "tempcheck":
  command = command
elif command == "occupancy":
  command = command
#Output if an invalid command is entered
else:
#Prompt if invalid command entered
  print("Invalid command. Type 'help' for the list of valid commands")
#Help command entered AFTER invalid command given
  command_1=input("Enter a command: ")
  if command_1 == "help":
#List of valid commands (again)
    print("atomfreq\nresfreq\nreslength\ntempcheck\noccupancy\nquit")
#Enter input for command AFTER invalid command given
    command_2=input("Enter a command: ")
#Outputs of commands AFTER invalid command given
    if command_2 == "quit":
      quit()
    elif command_2 == "atomfreq":
      command_2 = command_2
    elif command_2 == "resfreq":
      command_2 = command_2
    elif command_2 == "reslength":
      command_2 = command_2
    elif command_2 == "tempcheck":
      command_2 = command_2
    elif command_2 == "occupancy":
      command_2 = command_2
