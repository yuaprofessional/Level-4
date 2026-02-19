#Question
#Find the sum of even numbers from 1 to N

#Logic
#create a variable
#Start a loop from 1 to a
#print variable

#Steps
# for i (1,a+1)
#print i

#Code
a = int(input("Num : "))
c = 0
for i in range(2,a + 1,2):
    c = c + i
print(c)