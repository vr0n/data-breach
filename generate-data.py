# Generate random data breach info!
import ast
import random
import datetime

modNum = random.randint(0, 11)
month = list(range(1,12))
year = list(range(2000, int(datetime.datetime.now().strftime("%Y")) - 1))

state_codes = {
    'District of Columbia' : 'dc','Mississippi': 'MS', 'Oklahoma': 'OK', 
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR', 
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ', 
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT', 
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV', 
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND', 
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY', 
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD', 
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA', 
    'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX', 
    'Nevada': 'NV', 'Maine': 'ME'}

# let`s generate some functions!
# this one generates a random number base don a list size. We will be using this alot
def genNum(list):
  return random.randint(0, len(list) - 1) 

# we are going to create 6 breaches
# well... sometimes... It turns out the same
# date can be chosen twice, or even more times
# creating repeats
breaches = []

for i in range(0,6):
     breaches.append(str(datetime.date(year[genNum(year)], month[genNum(month)], 1).strftime("%Y-%m")))

# this one generates the data
def genData(fn, ln, i):
    breachDate = breaches[genNum(breaches)]
    changeDate = str(datetime.date(year[genNum(year)], month[genNum(month)], 1).strftime("%Y-%m"))
    state = states[genNum(states)]
    password = wordlist[genNum(wordlist)]
    stateCode = state_codes[state.title()]

    if i%5 != 0 and i%7 != 0:
        email = fn + "." + ln + str(nums[genNum(nums)]) + "@" + ext[genNum(ext)]  
    elif i%5 == 0:
        email = fn + "." + ln + "@" + ext[genNum(ext)]
    else:
        email = usernames[genNum(usernames)] + "@" + ext[genNum(ext)]

    data = "\n" + fn + "," + ln + "," + email + "," + password + "," + state + "," + stateCode + "," + breachDate + "," + changeDate

    return data

month = list(range(1,12))
year = list(range(2000, int(datetime.datetime.now().strftime("%Y")) - 1))

# import first names and generate variable for random generation
f = open('lists/first-names', 'rb')
first = ast.literal_eval(f.read().decode("utf-8"))
f.close()

# last name
f = open('lists/last-names', 'rb')
last = ast.literal_eval(f.read().decode("utf-8"))
f.close()

# numbers (though, this is dumb, I could have just generated them in this file
f = open('lists/numbers', 'rb')
nums = ast.literal_eval(f.read().decode("utf-8"))
f.close()

# email extensions
f = open('lists/email-extensions', 'rb')
ext = ast.literal_eval(f.read().decode("utf-8"))
f.close()

# passwords
f = open('lists/passwords', 'rb')
wordlist = ast.literal_eval(f.read().decode("utf-8"))
f.close()

# usernames
f = open('lists/usernames', 'rb')
usernames = ast.literal_eval(f.read().decode("utf-8"))

# and, finally, states. This one doesn't need to be translated to a literal list
f = open('lists/states', 'rb')
states = f.read().decode("utf-8").split("\n")[:-1]
f.close()

print("Imports complete. No issues so far.")

print("generating hot points...")



print("Opening file to write data too...")

dataFile = open('fake-breach-data/data.csv', 'w')
dataFile.write('First,Last,Email,Password,State of IP,State Code,Date of Breach,Date of Most Recent Password Change')

print("Entering loop to write data... This is the part that takes the longest...")

for i in range(0, 200000):
  fn = first[genNum(first)]
  ln = last[genNum(last)]

  line = genData(fn, ln, i)  

  dataFile.write(line)

dataFile.close()

print("All done! Enjoy!")
