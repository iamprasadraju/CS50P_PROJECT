#importing required libraries for this project
import pyfiglet
import tabulate
import sys


font = pyfiglet.figlet_format("Password Manager",font = "small")
print(font)

print("list of commands:")
print("\n")
print("         V   --view all list of passwords")
print("         C   --create a New password") 
print("         D   --Delete a password")
print("         U   --Update the password")
