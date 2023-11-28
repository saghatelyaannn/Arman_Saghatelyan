'''

ex.7, ex.8, ex.9
write functions for the following string operations
startswith(str_obj, sub_string)
endswith(str_obj, sub_string)
is_in_str(str_obj, sub_string)
these functions should do the same as a builtin string functions do



'''

# startsWithObj
def startsWithObj(string, strObj):
	if string[:len(strObj)] == strObj:
		return True
	return False

# endsWithObj
def endsWithObj(string, strObj):
    if string[len(string) - len(strObj):] == strObj:
        return True
    return False

#isInString
def isInString(string, strObj):
	for i in range(len(string)):
		if string[i:i + len(strObj)] == strObj:
			return True
	return False


string = str(input("input the string: "))
strObj = str(input("input the object: "))

if startsWithObj(string, strObj):
	print(f"The string starts with {strObj}")
else:
	print(f"The string does NOT start with {strObj}")


if endsWithObj(string, strObj):
	print(f"The string ends with {strObj}")
else:
	print(f"The string does NOT ends with {strObj}")


if isInString(string, strObj):
	print(f"There is {strObj}")
else:
	print(f"There is NO {strObj}")












