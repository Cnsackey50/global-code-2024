name = input("What is your name")
age = input("what is your age?")
y = 'years' if int(age) < 10 else "you are a child"
print("hello"+" "+ name +" " +"! You are" +" " +age + " " +y+ " " + "old.")
# message to Cnsacky
if int(age) < 10:
    print('hello ' + name + ' you are a child')
elif 10 < int(age) < 18:
    print('hello ' + name + ' you are a teenager')
else:
    print('hello ' + name + ' you are an adult')
  
