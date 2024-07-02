#STRING METHODS

#name = "vedant"

#print (name)                                    #prints the string as is
#print (type(name))                              #prints string, boolean, or int, etc.
#print (len(name))                               #prints the number of characters in the string
#print (name.find("e"))                          #index of letter in question
#print (name.capitalize())                       #Capitalizes teh first letter of forst word
#print (name.upper())                            #Makes all capital
#print (name.lower())                            #Makes all lowercase
#print (name.isdigit())                          #boolean true if only digits
#print (name.isalpha())                          #boolean true if only alphabet
#print (name.count("e"))                         #returns number of specified characters
#print (name.replace("v","w"))       #Replaces old w new letter
#print (name*5)                                  #multiplies string by number


#------------------------------------------------------------------------------------------------------------
#TYPE CAST

#x=1
#y=2.8
#z="22"

#x=str(x)        #convert int to string when trying to concatanate with other strings
#y=int(y)        #int f(x) on float drops decimal
#z=float(z)      #str*3 would be strstrstr, while int*3 would give actual value

#print (x)
#print (y)
#print (z*3)

#--------------------------------------------------------------------------------------------------------------
#CONCATENATION

#name = input("What is your name?:")             #accepts input only as strings; we have to cast str as int if we want to use int
#age = int (input("How old are you?:"))          #if decimal, cast as float
#age = age +1

#print ("Hello "+name)
#print ("you are "+ str(age) + " years old")     #remember, we can only use str in concatenation

#--------------------------------------------------------------------------------------------------------------
#MATH FXN

#import math

#pi =3.14
#x= 1
#e=78

#print (round(pi))       #round to nearest whole integer
#print (math.ceil(pi))   #round up to nearest whole integer
#print (math.floor(pi))  #round down to nearest whole integer
#print (abs(pi))         #abs value
#print (pow(pi, 2))      #raises first to the second value
#print (math.sqrt(pi))   #sqrt
#print (max (x,pi,e))    #gives max value in the vars entered
#print (min (x,pi,e))    #gives min value in the vars entered

#------------------------------------------------------------------------------------------------------------------
#SLICING

#name = "Vedant Talati"
#sname = name[0:6]       #gives value between 0 to 6 exclusive
#nmane = name[7::2]      #gives value between 7 and end, stepping by 2
#rname = name[::-1]      #reverses the full str
#print (sname)
#print (nmane)
#print (rname)

#website = "http://google.com"
#website2 = "http://wikipedia.org"
#slice = slice(7,-4,)    #deletes http:// and the .com, even if the name of site is diff length (this is a new f(x))

#print (website[slice])
#print (website2[slice])

#------------------------------------------------------------------------------------------------------------------
# IF ELIF AND ELSE STATEMENTS

#age= int(input("How old are you?: "))

#if age>=18:
    #print("You are an adult!")
#elif age<0:
    #print( "You haven't been born yet!")
#else:
    #print("child detected")

# ------------------------------------------------------------------------------------------------------------------
# AND OR NOT OPERATORS

#temp = int(input("What is the temperature outside?: "))

#if temp >= 0 and temp <= 30:           #Both conditions have to be true to execute
 #   print("Cool Weather")
#elif temp<0 or temp >30:               #One or the other has to be true to execute
 #   print("EXTREME WEATHER BRO")

 #------------------------------------------------------------------------------------------------------------------
# WHILE LOOPS

#name= ""

#while len(name) == 0:                  #As long as condition is satisfied, while loops will execute for infinity
    #name = str(input("What is ur name bro "))

#nam = None

#while not nam:
   # nam = input("Enter your name: ")

#print("Hello "+nam)

#---------------------------------------------------------------------------------------------------------------------
# FOR LOOPS
#
# While Loop: Infinite
# For Loops: Finite

#for index in range(10):     #indexing begins at 0, so 10 is not printed normally
#    print(index+1)

#for i in range(50,100):     #50 inclusive to 100 exclusive
   # print (i)

#for i in range(50,100,2):    #50 to 100(exclusive), with step of 2
  #  print (i)

#for i in "Vedant Talati":   # strings can also be used instead of range fxn
   # print (i)

#import time                  #imports the time class

#for i in range (10,0,-1):
  #  print (i)
  #  time.sleep(1)            #makes code delay for 1 second before reexecuting the loop
#print ("Happy New Year!")

#--------------------------------------------------------------------------------------------------------------------
#NESTED LOOPS

#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol= input ("write ur symbol bro: ") + " "

#for i in range (rows):           #row 1, row 2, row 3, etc.
 #   for j in range (columns):    #column 1, column 2, column 3, etc.
 #       print (symbol, end = "")   #prints symbol, and stops from making new line
 #   print ()          #goes down one line

#-------------------------------------------------------------------------------------------------------------------
#LOOP CONTROL STATEMENTs

#break - used to terminate loops entirely
#continue - skips to the next iteration of the loop
#pass= does nothing, acts as a placeholder

#while True:
    #name = input("name bro ")
    #if name != "":
        #break                  #breaks out of nearest enclosed loop

#phonenum="123-456-7890"

#for i in phonenum:
    #if i == "-":
        #continue                #skips over the dash, and doesn't print it
    #print(i, end="")

#for i in range(1,21):
    #if i == 13:
        #pass                   #acts as a placeholder to write future code; skips over it for now
    #else:
        #print (i)

#------------------------------------------------------------------------------------------------------------------
#LISTS

#food = ["pizza", "roti", "pasta", "pizza"]

#food[0] = "sushi"                            #sets index value = to something else

#food.append("ice cream")                    #adds ice cream to the end of the list
#food.remove("roti")                         #removes the specific value from list
#food.pop()                                  #removes last item from list
#food.insert(0,"cake")                       #adds obj at specified index
#food.sort()                                 #sorts the list alphabetically
#food.clear()                                #clears everything in a list

#print (food[0])

#for x in food:
    #print (x, end=" ")

#-------------------------------------------------------------------------------------------------------------------
#2D LISTS

#breakfast = ["milk","cereal","cookies"]
#lunch = ["Pizza","Juice","Doritos"]
#dinner = ["Gordita Crunch","Bean Burrito","Baja Blast"]

#food = [breakfast, lunch, dinner]

#print (food[0][2])                      #first index specifies list, and second the value within that list

#--------------------------------------------------------------------------------------------------------------------
#TUPLES -  immutable lists

#student = ("Vedant",15,"male")

#print(student.count("Vedant"))
#print(student.index("male"))

#for z in student:
    #print (z)

#if "Vedant" in student:
    #print("present")

#--------------------------------------------------------------------------------------------------------------------
#SETS - unordered, unindexed ---- NO DUPLICATE VALUES

#u = {"spoon","fork","knife"}
#d = {"bowl","plate","cup"}

#u.add("napikin")
#u.remove("fork")
#u.clear()
#u.update(d)                         #add all elements in D to U
#D_U = u.union(d)                     #makes new set using the union function

#for x in u:
    #print(x)

#print(u.difference(d))                  #what does u have that d doesn't
#print(u.intersection(d))                #what do both have similar

#---------------------------------------------------------------------------------------------------------------------
#DICTIONARIES - A changeable, unordered collection of unique key:value pairs
#               Fast because they use hashing,allowing us to access values quickly

#capitals = {'USA':'Washington DC',
#            'India':'New Delhi',
#            'China':'Beijing',
#            'Russia':'Moscow'}

#print(capitals['Russia'])               #instead of calling an index, call the key to recieve definition

#print(capitals.get('Germany'))          #get method is a way to check if a value is there w/o getting errors
