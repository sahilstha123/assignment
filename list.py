print("hello")
# to make a list we use symbol[]
a=[1,2,3]
print(a)

print(a[-1]) #it will print the last element of the index

print(a[0]) #it will print the first element of the index

b=[2,5,7]
b.insert(2,6) #used to insert the single element in any index list_name.insert(index_no,elemnt)
print(b)
print("\n")

# c=index no (0,1,2)
c=['dog','cat','mouse']
d=c.index('mouse') #it will print the index where your element is located
print("it will print the index where your element is located:",d) #output- 2
print("\n")

my_list=['dog','cat','mouse','horse','cow','mouse','lion','cat','dog']
# dog after the 1 index is searched
e=my_list.index('dog',1) 
print("dog after the 1 index is searched:",e)
print("\n")

# 'mouse' is search between the index 0 and 5 
f=my_list.index('mouse',0,5)
print("'Mouse' is search between the index 0 and 5:", f)
print("\n")

# to add the element in the list
op_list=['dog','cat','mouse']
op_list.append('rice')
print("before:['dog','cat','mouse'] \n after:",op_list)

#unpack
fruits=['apple','banana','cherry']
x,y,z=fruits
print(x,y,z)
print(y)
print(z)
 
 #to add multiple elements we use extend
a=['apple','banana','cherry']
a.extend(['cat','lion'])
print(a)
 
#  count
a=['apple','banana','cherry','apple','apple']
b=a.count('apple')
print(b)

# the pop() method uses the index odf an element to dlete it while the remove() method takes the value of the element as an input argument to delete the element
a=['apple','banana','cherry']
a.pop(2)
print(a)
a=['apple','banana','cherry']
a.remove('apple')
print(a)

# reveres
a=['apple','banana','cherry']
a.reverse()
print(a)

# sorted
a=['apple','dog','cherry']
a.sort()
print(a)

# copy
a=['apple','banana','cherry']
b=a.copy()
print(b)