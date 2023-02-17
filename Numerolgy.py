# A list of codes of all the letters 
t = [1, 2, 3, 4, 5, 8, 3, 5, 1, 1, 2, 3, 4, 5, 7, 8, 1, 2, 3, 4, 6, 6, 6, 5, 1, 7] 
# A function for sum of digits if in case the code is not single digit 
def sum_of_digits(n) : 
    while n >= 10 : 
          s = 0 
          for i in str(n) : 
               s += int(i) 
          n = s
    return n 
# Function to convert name to code : 
# Works as follows : 
# * Traverse through the name 
# * Add the respective code of each letters 
# * If the final result is not single digit, sum its 
# digits 
def encrypt(name) : 
      num = 0 
      for i in name : 
               num += t[ord(i) - ord('A')] 
      if num >= 10 : 
                num = sum_of_digits(num) 
      return num 
# Getting name input and print its respective code 
name = input("Enter the name : ") 
name = name.upper() 
print(name + " : " + str(encrypt(name))) 
# Function to print alternative name 
# Works as follows : 
# * A name and the code we want is passed as argument 
# * diff is the number that must be added to the original code of the name to get the code we desire 
# * Traverse through t and list all the letters with same code as diff 
# * Traverse through the name and find if any of the letter is present in the above list 
# * If then, then insert the letter another time in 
# the name 
def rename(name, num) : 
 # Ori - Original code of the name 
 ori = encrypt(name) 
 
 # diff is the number that must be added to ori to the 
# desired code 
 if ori > num : 
      diff = 9 + num - ori 
 else : 
      diff = num - ori 
 
 # Listing all the letters that have same code as diff 
 l = [] 
 for i in range(len(t)) : 
       if t[i] == diff : 
              l.append(chr(i + ord('A'))) 
 
 # Checking if any letters in the name match with the list above 
 # If , then that letter is inserted into the name 
 ln = [*name] 
 for i in range(len(ln)) : 
          if ln[i] in l : 
               ln.insert(i, ln[i]) 
               break 
 
 alt_name = "" 
 for x in ln : 
       alt_name += x 
 return alt_name 
# Printing all the names with codes from 1 to 10 
print("\nAlternative possible names : ") 
for i in range(1, 10) : 
       if rename(name, i) != name : 
                  print(str(i) + " : " + rename(name, i))