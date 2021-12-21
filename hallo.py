# This program says hello and asks for my name.
print('Hello world!')
print('What is your name?')
# ask for their name➌
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
# ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 5) + ' in 5 years.')


# Value that is passed to a function call is an argument .
# Notice that the quotes are not printed to the screen.
# They just mark where the string begins and ends; they
# are not part of the string value.
