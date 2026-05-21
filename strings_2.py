##U CAN ADD A STRING TO ANOTHER STRING USING THE + OPERATOR
first_name='Adrian'
last_name='Oliden'
full_name=first_name + ' ' + last_name
print(full_name)
##BUT IF U WANT TO ADD A NUMBER TO A STRING U NEED TO CONVERT THE NUMBER TO A STRING FIRST
age=19
age_str=str(age)
msg='My name is ' + full_name + ' and I am ' + age_str + ' years old.'
print(msg)
##U CAN ALSO USE F-STRINGS TO CONCATENATE STRINGS AND VARIABLES
msg_f=f'My name is {full_name} and I am {age} years old.'
print(msg_f)
##AND U CAN SUME NUMBERS
num_1=10
num_2=20
print(f'The sum of {num_1} and {num_2} is {num_1 + num_2}')
