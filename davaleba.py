#1
import math
leg1 = int(input('sheiyvanet ricxvi'))
leg2 = int(input('sheiyvanet ricxvi'))
hyp = math.sqrt(leg1**2 + leg2**2)
print(hyp)


#2

number = int(input('ricxvi'))
count = 0
while True:
    if number % 2 == 0:
        print(str(number)+'ლუწია ამიტომ ვყოფთ ორზე')
        number = number/2
    elif number != 1:
        print(str(number)+'კენტია ამიტომ ვაკეთებთ 3n+1')
        number = number * 3 + 1
    else:
        break
    count+=1
print('დაგვჭირდა'+str(count)+'სვლა')

#3

# a = int(input('ricxvi'))
# b = 0
#
# while b <= a:
#     p='a'*a
#     print(' '+p)
#    a -= 2






#4

sym = int(input('შეიყვანეთ სიმბოლო'))
highest = 0
lst=[]
while True:
    num = int(input('შეიყვანეთ რიცხვი'))
    lst.append(num)
    smallest=lst[0]
    for n in lst:
        if num > highest:
            highest=num
        elif n < smallest and n != sym:
            smallest = n
        elif len(lst) == 1 and lst[0] == sym:
            print('თქვენ შეიყვანეთ მარტო სიმბოლო')
    if num == sym:
            break
print(highest,smallest,)
