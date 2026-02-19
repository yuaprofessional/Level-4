#Question
#Check whether a number is a palindrome

#Logic
#create a variable
#Start a while loop 
#print variable

#Steps
# while a > 0:
#    digit = a % 10
#    REV = REV * 10 + digit
#    a = a // 10
#print Count

#Code
a = int(input("Num : "))
b = a 
REV = 0
while a > 0:
    digit = a % 10
    REV = REV * 10 + digit
    a = a // 10
print(REV)
if(REV == b):
    print(f"{b} is a palindrome") 
else:
    print(f"{b} is not a palindrome")   
