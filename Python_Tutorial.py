import streamlit as st 

# title
st.title("Python tutorial: Tricks to make your life easier.")
# header
st.header("Simple but effective tips for every python lovers")
# text
st.text("Here you have 10 tips to use in python to make easier your data science path")

#Tutorial
#subheader
# step 1 
st.header("1. Walrus operator")
txt = '''
The *Walrus** or **:=** operator is one of the latest additions to python 
3.8. It is an assignment operator that lets you assign value to a 
variable within an expression like conditional statements, loops, etc.
'''
st.write(txt)

st.subheader("Example:")

# A way to write code
code = '''Mylist = [1, 2, 3]
if(l := len(Mylist) > 2):
    print(l)

'''
#to export code
st.code(code, language = 'python')

#output
st.subheader("Output")
st.success("true")

# step 2
st.header("2. Splitting a string")
txt = '''
     If you want to split the components of a string into a list you
     can do that easily using the split() function in python. 
     This will make the string operations a lot easier!
     '''
st.write(txt)

st.subheader("Example:")

code = '''string = "hello world"

string.split()

print(string.split())
'''

#to export code
st.code(code, language = 'python')

#output
st.subheader("Output")
st.success("['hello', 'world']")

#step 3
st.header("3. Reversing a string")

txt = '''
     If you want to reverse a given string, you can do that with only 
     one line of code using the negative indexing of the string.
     '''
st.write(txt)

st.subheader("Example:")

code = '''str="hello world!"
a=str[::-1]
print(a)
'''

#to export code
st.code(code, language = 'python')

#output
st.subheader("Output")
st.success("!dlrow olleh")

#Step 4
st.header("4. Merging two dictionaries")

txt = '''
     This amazing trick will help you merge two dictionaries with just 1 line of code. 
     We just need to use ** in front of the name of the two dictionaries like below two 
     merge them into a single dictionary:
     '''
st.write(txt)

st.subheader("Example:")

code = '''d1 = {"a": 10, "b":20}
d2 = {"c": 30, "d":40}
d3 = {**d1, **d2}
print(d3)
'''

#to export code
st.code(code, language = 'python')

#output
st.subheader("Output")
st.success("{'a': 10, 'b': 20, 'c': 30, 'd': 40}")

#Step 5
st.header("5. The zip() function")

txt = '''
     The **zip()** function in python can make your life a lot easier when working with lists 
     and dictionaries. It is used to combine several lists of the same length.
     '''
st.write(txt)

st.subheader("Example:")

code = '''colour = ["red", "yellow", "green"]
fruits = ['apple', 'banana', 'mango']

for colour, fruits in zip(colour, fruits):
    print(colour, fruits)
'''

#to export code
st.code(code, language = 'python')

#output
st.subheader("Output")
st.success('''red apple\n
yellow banana\n
green mango ''')


txt = '''
     The **zip()** function can also be used for combining two lists into a dictionary. 
     This method can be really helpful while grouping data from the list.
     '''
st.write(txt)

st.subheader("Example:")

code = '''students = ["Rajesh", "kumar", "Kriti"]
marks = [87, 90, 88]

dictionary = dict(zip(students, marks))
print(dictionary)
'''

#to export code
st.code(code, language = 'python')

#output
st.subheader("Output")
st.success("{'Rajesh': 87, 'kumar': 90, 'Kriti': 88}")

#Step 6
st.header("6. Assigning multiple list values to a variable")

txt = '''
     If you want to assign some specific values of a list to a variable and all 
     the remaining values to another variable in a list format, you can use 
     the following technique:
     '''
st.write(txt)

st.subheader("Example:")

code = '''mylist = [1,2,3,4,5]
a,*b = mylist

print(f"a =",a) 

print(f"b =",b)
'''

#to export code
st.code(code, language = 'python')

#output
st.subheader("Output")
st.success('''a = 1\n
b = [2, 3, 4, 5]''')


txt = '''
 This process is also called list unpacking and you can apply this method for more than 2 variables also!
 '''
st.write(txt)

#Step 7
st.header("7. Remove duplicate list items")

txt = '''
     Do you have duplicate items in your list which you want to remove? You can do that with only one line of 
     code using the **set()** function.
     '''
st.write(txt)

st.subheader("Example:")

code = '''mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist)
'''

#to export code
st.code(code, language = 'python')

#output
st.subheader("Output")
st.success("{1, 2, 3, 4, 5, 6, 7, 8, 9}")

#Step 8
st.header("8. Lambda function")

txt = '''
     If you need a function that is not very complicated, it can be done easily in one line using **lambda**. 
     They are also called anonymous functions and are used heavily in data science and web development.
     '''
st.write(txt)

st.subheader("Example:")

code = '''mul = lambda a,b: a*b
mul(5,6)

print(mul(5,6))
'''

#to export code
st.code(code, language = 'python')

#output
st.subheader("Output")
st.success("30")

#Step 9
st.header("9. Swapping variable value")

txt = '''
     One of the first programs that we learn while learning about variables is swapping the values of two variables. 
     In python you can achieve that with one line of code:
     '''
st.write(txt)

st.subheader("Example:")

code = '''a = 100
b = 200
a,b = b,a
print(f'a = ',a) 
print(f'b = ',b)
'''

#to export code
st.code(code, language = 'python')

#output
st.subheader("Output")
st.success('''a =  200\n
b =  100''')

#Step 10
st.header("10. Use a password in your code")

txt = '''
    This python trick is amazing for securing your code with a password. 
    We will use the **getpass() function** from the **library getpass** which encodes your input. 
    This will prevent anyone from running the code without a password. Isn’t that cool!
     '''
st.write(txt)

st.subheader("Example:")

code = '''from getpass import getpass
password = getpass("password: ")
if password == "abcd":
    print("welcome strnger!")
else:
    print("wrong password")

'''

#to export code
st.code(code, language = 'python')

#output
st.subheader("Output")
st.success('''password: **** [abcd]\n
Welcome stranger!\n
Password: **** [abdc]\n
Wrong password''')

import streamlit as st 

txt = '''
Here is [a book](https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922?dchild=1&keywords=automate+the+boring+stuff+with+python&qid=1602697607&sr=8-2&linkCode=sl1&tag=pranjal20-20&linkId=71b2efa5db080e8f74068aebec7d7fb0&language=en_US&ref_=as_li_ss_tl)
on Python programming that I would definitely recommend for all beginners.
'''

st.write(txt)

st.subheader("Conclusions")

txt = '''
These were a few amazing Python tips and tricks which will make your work a lot easier while coding. 
There are many more shortcuts like these that you can explore from the official documentation or any other website.

**Note:** This article contains an affiliate link. This means that if you click on it and choose to buy 
the resource I linked above, a small portion of your subscription fee will go to me.

However, the recommended resource is experienced by me and helped me in my data science career journey.
'''

st.write(txt)