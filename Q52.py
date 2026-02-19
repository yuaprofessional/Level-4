#Question
#	Reverse a number

#Logic
#create a variable
#Start a while loop 
#print variable

#Steps
# while a > 0:
#    digit = a % 10
#    REV = REV * 10 + digit
#    a = a // 10
#print REV

#Code
a = int(input("Num : "))
REV = 0
while a > 0:
    digit = a % 10
    REV = REV * 10 + digit
    a = a // 10
print(REV)