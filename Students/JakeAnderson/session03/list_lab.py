#this program will be asking people to add and remove items from a list
#making fruit
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print "The basket of fruit is full of the following" ,len(fruit), "delicious fruits:", fruit
#adding a fruit
new_fruit = raw_input("Which fruit would you like to add? ")
fruit.append(new_fruit.capitalize())
print "The basket has the following", len(fruit), "fruits:", fruit

F = raw_input("Which item number would you like to view? ")
print F, 'is', fruit[int(F) - 1]

fruit = ['Dragon'] + fruit
print fruit

fruit.insert(0, 'Pineapple')
print fruit

for f in fruit:
    if f.startswith("P"):
        print f
#deleting a fruit
print fruit
del fruit[-1]   
print fruit
R = raw_input("What fruit would you like to delete from the list? ")
fruit = fruit * 2


    
print fruit
while R.capitalize() in fruit:
    print "removing", R.capitalize()
    fruit.remove(R.capitalize())
    print fruit
    


for Bad_fruit in (fruit[:]):
    answer = raw_input("Do you like the fruit: %s " % (Bad_fruit))
    if answer[0].lower() == "n":
        fruit.remove(Bad_fruit)
        print "That was a rotting anyways"
    elif answer[0].lower() == "y":
        print "keeping this"
    else:
        print "That is not a valid answer, please answer yes or no"
print fruit

R_fruits = []
for f in fruit: 
    R_fruits.append(f[::-1])
print R_fruits
fruit.pop(-1)
print fruit












