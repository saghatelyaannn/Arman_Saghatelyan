'''

write a function that returns the number of non-overlapping occurrences of substring sub in string S
i.e. write a function that does the same as a builtin str.count() function does
function signature: count_sub_in_str(string_obj, substring)

'''

def stringCount(string, strObj):
	result = 0
	for i in range(len(string)):
		if string[i:i + len(strObj)] == strObj:
			result += 1
	return result

string = str(input("input the string: "))
strObj = str(input("input the object: "))
print(stringCount(string, strObj))
