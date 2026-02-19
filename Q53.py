#Question
#Count digits in a number

#Logic
#create a variable
#Start a while loop 
#print variable

#Steps
# while a > 0:
#    Count = Count + 1
#    N = N // 10
#print Count

#Code
N = int(input("Num : "))
Count = 0
if N == 0:
    print("0")
while N > 0:
    Count = Count + 1
    N = N // 10

print(Count)