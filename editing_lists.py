numbers=[1, 2, 3, 5]
numbers.append(6)
numbers.insert(3, 4)#after third item in list, insert 4
numbers.remove(6)#remove item 6
print(numbers)
print(len(numbers))#prints the length of the list
numbers.clear()#clears the list
print(1 in numbers)#output is true or false (it will be false beacause the list is empty)