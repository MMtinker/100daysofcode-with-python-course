import re


data = 'Population is 2243603014. The phone number is 224-360-3014. Call me'

phoneRegex = re.compile(
    r'\d\d\d-\d\d\d-\d\d\d\d'
)

phoneRegex = re.compile(
    r'\d{3}-\d{3}-\d{4}'
)

findPhoneNUmber = phoneRegex.search(data)
phoneRegex.

print(findPhoneNUmber.group())

