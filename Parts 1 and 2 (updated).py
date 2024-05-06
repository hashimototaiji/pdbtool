#!/usr/bin/env python3
#Prologue (indented comments)
  #Title: pdbtool
  #Authors: Adnan Prantoi, Iman Meawad, Taiji Hashimoto, Jayden Leung
  #Roles: J.L. (Parts 1 and 2), I.M. (Parts 3 and 4), T.H. (Parts 5 and 6), A.P. (parts 7 and 8)
  #Date of Creation: 03/29/24
  #Usage (command-usage): Commands 'help', 'atomfreq', 'resfreq', and 'quit' can be typed as they are
    #reslength-reslength <res_name> <chain_id> <res_seq_number>
    #tempcheck-tempcheck <decimal>
    #occupancy-occupancy <decimal>
  #Accepted Input (files): Only files containing the word 'ATOM' in the first index are accepted, since that's how the file is read when looking for specific information
  #Command Descriptions (Input-Output): 
    #help-lists all valid commands including itself
    #atomfreq-displays number of atoms for each element (Ex: C: 3201)
    #resfreq-displays the number of each residue in the file (Ex: ARG: 306)
    #reslength-displays the length of a residue if chain id and sequence number is given
    #tempcheck-displays the number of atoms that have a temperature factor at, above, or below a given value in terms of a fraction and percent
    #occupancy-displays the frequency of atoms at, above, or below a given value (factor)
    #quit-outputs a departing message (goodbye) then program ends
#Open file
txt_file=open('pdbtool.pdb')
#Define count
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
  print("goodbye")
  quit()
#Outputs for command 'help'
elif command == "help":
#List of valid commands
  print("help\natomfreq\nresfreq\nreslength\ntempcheck\noccupancy\nquit")
#Enter input for second command
  command_=input("Enter a command: ")
#Outputs of second command
  if command_ == "quit":
    print("goodbye")
    quit()
  elif command_ == "atomfreq":
    print("hello")
  elif command_ == "resfreq":
    print("hello")
  elif command_ == "reslength":
    print("hello")
  elif command_ == "tempcheck":
    print("hello")
  elif command_ == "occupancy":
    print("hello")
#Outputs for 'atomfreq', 'resfreq', 'reslength', 'tempcheck', 'occupancy'
elif command == "atomfreq":
  print("hello")
elif command == "resfreq":
  print("hello")
elif command == "reslength":
  print("hello")
elif command == "tempcheck":
  print("hello")
elif command == "occupancy":
  print("hello")
#Output if an invalid command is entered
else:
#Prompt if invalid command entered
  print("Invalid command. Type 'help' for the list of valid commands")
#Help command entered AFTER invalid command given
  command_1=input("Enter a command: ")
  if command_1 == "help":
#List of valid commands (again)
    print("help\natomfreq\nresfreq\nreslength\ntempcheck\noccupancy\nquit")
#Enter input for command AFTER invalid command given
    command_2=input("Enter a command: ")
#Outputs of commands AFTER invalid command given
    if command_2 == "quit":
      print("goodbye")
      quit()
    elif command_2 == "atomfreq":
      print("hello")
    elif command_2 == "resfreq":
      print("bye")
    elif command_2 == "reslength":
      print("hi")
    elif command_2 == "tempcheck":
      print("goodbye")
    elif command_2 == "occupancy":
      print("nice")