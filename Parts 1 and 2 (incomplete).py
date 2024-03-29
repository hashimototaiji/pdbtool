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
if command == "help":
#List of valid commands
  print("atomfreq\nresfreq\nreslength\ntempcheck\noccupancy\nquit")
#Enter input for second command
  command_=input("Enter a command: ")
#Outputs of second command
  if command_ == "quit":
    quit()
  if command_ == "atomfreq":
    command_ = command_
  if command_ == "resfreq":
    command_ = command_
  if command_ == "reslength":
    command_ = command_
  if command_ == "tempcheck":
    command_ = command_
  if command_ == "occupancy":
    command_ = command
#Outputs for 'atomfreq', 'resfreq', 'reslength', 'tempcheck', 'occupancy'
if command == "atomfreq":
  command = command
if command == "resfreq":
  command = command
if command == "reslength":
  command = command
if command == "tempcheck":
  command = command
if command == "occupancy":
  command = command
