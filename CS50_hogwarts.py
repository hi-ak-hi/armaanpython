#{} = dictionary, comparing things
'''students={"hermonie":"grifindor",
     "harry":"grifindor",
     "ron":"grifindor",
     "draco":"slytherin"}'''
#indivisuily printing them
'''print(students["hermonie"])
print(students["harry"])
print(students["ron"])
print(students["draco"])'''
# printing them all togethor
'''for student in students:
    print(students[student])'''
#printing both 
'''for student in students:
    print(students,"is in",students[student])'''
#making longer dictionaries
students = [
    {"name":"hermione","house":"grifindor","patronus":"otter"},#make sure you have comas
    {"name":"harry","house":"grifindor","patronus":"stag"},#make sure you have comas
    {"name":"ron","house":"grifindor","patronus":"jack russell terrier"},#make sure you have comas
    {"name":"draco","house":"slytherin","patronus":None}#none litterly just means there is no information to put there
]

#printing it
for student in students:
    print(student["name"],"is in",student["house"] + ", and his/her patronus is a",student["patronus"])#use quotes