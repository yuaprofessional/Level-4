#Question
#Find the sum of digits of a number

#Logic
#create a variable
#Start a while loop 
#print variable

#Steps
# while a > 0:
#        Digit = N % 10
#    Count = Digit + Count
#    N = N // 10
#print Count

#Code
N = int(input("Num : "))
Count = 0
while N > 0:
    Digit = N % 10
    Count = Digit + Count
    N = N // 10
print(Count)