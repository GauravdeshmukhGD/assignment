'''
#question 1
becon=22
becon+1 
becon+=1 #It increment the value of becon
print(becon)

#question 2

'spam' * 3
print('spam')

#it does not multiply the value

#question 3

difference between break and continue
break
break will break the loop when certain condition become true, it will break the loop
continue
in continue statement, it will skip the value when certain condition become true
it does not break the loop

#question 4

4) In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
range function
range function is use in loop

for i in range(10):
    print(i)
# it will start from 0 and end at 9

for i in range(0,10):
    print(i)
#it will itrate same like range(10)

for i in range(0,10,1):
    print(i)# it will itrate like range(10) function


#question 5
#print the no. from 1 to 10 using for loop
for i in range(1,11):
    print(i)

#print the no. from 1 to 10 using while loop
i=1
while i<11:
    print(i)
    i+=1

#question 6
    #given no. is armstrong or not
num=int(input("enter a no."))
sum=0
temp=num
while(temp>0):
    digit = temp%10
    sum+= digit** 3
    temp //= 10
if(num==sum):
  print('yes',num)
else:
    print('no',num)


#print all even no. between 1 to 100
for i in range(1,100):
    if(i%2==0):
        print(i)
    else:
        print('not a even no.')

#sum of all element in list
total=0
list=[10,12,13]
for ele in range(0,len(list)):
    total=total+list[ele]

print('sum of element',total)

'''
#write a program to reverse word in a given string in python
s='hello everone my name is gaurav deshmukh'
words=s.split()
words=list(reversed(words))
print(''.join(words))


