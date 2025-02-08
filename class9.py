# class no 9

name="pkistan"
print(name)

# capitalize
print(name.capitalize())
# length
newName="my name is fatima and my nationality of pakistani"
print(newName)
print(len(newName))
# replace
print(newName.replace('pakistani','america'))
# index
print(newName.index('my'))
# # find
print(newName.find('aisha'))


# list methods

my_list=['aisha','eman']
print(my_list)

# append
(my_list.append('yoha'))
print(my_list)

# insert
(my_list.insert(1,'fatima'))
print(my_list)

# reverse
(my_list.reverse())
print(my_list)

# pop
my_list.pop(1)
print(my_list)

# sort
num_list=[5,8,9,1,2]
num_list.sort()
print(num_list)

# extand
my_list=["aisha","eman","yoha",]
new_list=["ali","aneeq","abdullah"]
my_list.extend(new_list)
print(my_list)

# remove
my_list.remove('ali')
print(my_list)

# dictionary methods

student={
       "name":"husnain",
       "age": 22,
       "course": "AI"

}
print(student)
# get
print(student.get("name"))
print(student["name"])

# print(student["salary"])
print(student.get("salary"))
print(student.get("salary",'apney kam sey kam rakho'))

# keys methods
print(student.keys())
# values methods
print(student.values())
# loop keys
print(student.keys())
for key in student.keys():
    print(key)
# items       
print(student.items())
# loops items
for item in student.items():
    print(item)
for key,value in student.items():
    print(f'key {key} and value {value}')

# update method
student.update ({"age":29})
print(student)

# clear
student.clear()
print(student)