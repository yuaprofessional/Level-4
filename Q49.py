#Question
#Find the factorial of a number

#Logic
#create a variable with starting value as 1
#Take input
#Start a loop from 1 to N, -1
#print variable

#Steps
# N = mm
# F = 1
# (N,1,-1)
# F = i * F
#print i

#Code
N = int(input("Num : "))
F = 1
for i in range(N,0,-1):
    if(N > 0):
        F = i * F
    else:
        print(".")
print(F)
