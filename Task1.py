def is_isogram(s: str) -> bool:
    
    if s == "": # In case of an empty string
        return True # The given string is an Isogram

    letters = [char for char in s.lower()] # Converting the given string to lower case and separating each letter
    
    for i in range(0,len(letters),1):
        value = letters[i]
        for j in range(i+1,len(letters),1):
            if (value == letters[j]):# Comparing letters to check if they are repeating
                return False # The given string is not an Isogram
    return True

print(is_isogram(""))
print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram("ααβγδ"))


