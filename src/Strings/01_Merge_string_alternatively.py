def merge_strings_alternatively(str1: str, str2: str) -> str:
    result = []
    #length of the longer string
    max_len = max(len(str1), len(str2))
    
    for i in range(max_len):
        if i < len(str1):
            result.append(str1[i])
        if i < len(str2):
            result.append(str2[i])

    return ''.join(result)


'''Sample test'''

str1 = "abcde"
str2 = "123456789"
output = merge_strings_alternatively(str1, str2)
print(output)