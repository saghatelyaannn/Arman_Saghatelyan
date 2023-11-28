'''

ex.2
Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.

'''

string = str(input("Input the string: "))
n = int(input("Input the number of characters you want to remove: "))
print(string)
string = string[n::]
print(string)
	
