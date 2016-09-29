string = '"hello"'

print string[-1]

if ((string[0] == '"' and string[-1] == '"') or (string[0] == "'" and string[-1] == "'")):
    string = string[1 : len(string)-1]
    
print string