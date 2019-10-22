name = "Yevhen"
height = "197"
weight = "72"
married = False

print(name)
print(height + height)
print("My name is " + name)
print(name + " is " + str(height) + " cm and " + str(weight) + " kg")
print("name is {} and height {}".format(name, height))


a = 4
b = 6.5
c = "2.5"
print(a + b)


age = 12

if (age < 10):
    print("child")
elif (age <= 19):
    if(age < 13):
        print("small")
    print("teenager")
elif (age < 65):
    print("adult")
else:
    print("retiree")

lis = [12, 44.3, 'a', ['h', 'i']]
print(lis[3])
print(lis[3][0])
print(lis)
lis.append("new")
print(lis)