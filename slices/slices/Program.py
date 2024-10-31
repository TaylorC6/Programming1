list1 = [1,2,3,4,5]
front = list1[0:3]
back = list1[3:len(list1)]
print(front)
print(back)
print(front + back)

hello = "Hello, world!"
substr = hello[:5]
print(substr)
print(hello[-1])
print(hello[-6:-1]) # [start:stop:step)
print(hello[::-1]) # [0:len(hello):-1] # print backwards
print(hello == hello[::-1])
taco = "tacocat"
print(taco == taco[::-1])

input()