# Generate random data breach info!
import ast
import random
import datetime

# let`s generate some functions!
# this one generates a random number
def genNum(list):
  return random.randint(0, len(list) - 1) 

# this one generates the data
def genData(fn, ln, i):
  if i%5 != 0 and i%7 != 0:  
    data = "\n" + fn + "," + ln + "," + (fn + "." + ln + str(nums[genNum(nums)]) + "@" + ext[genNum(ext)]) + "," + wordlist[genNum(wordlist)] + "," + states[genNum(states)] + "," + str(datetime.date(year[genNum(year)], month[genNum(month)], 1).strftime("%Y-%m")) + "," + str(datetime.date(year[genNum(year)], month[genNum(month)], 1).strftime("%Y-%m"))
  elif i%5 == 0:
    data = "\n" + fn + "," + ln + "," + (fn + "." + ln + "@" + ext[genNum(ext)]) + "," + wordlist[genNum(wordlist)] + "," + states[genNum(states)] + "," + str(datetime.date(year[genNum(year)], month[genNum(month)], 1).strftime("%Y-%m")) + "," + str(datetime.date(year[genNum(year)], month[genNum(month)], 1).strftime("%Y-%m"))
  else:
    data = "\n" + fn + "," + ln + "," + (usernames[genNum(usernames)] + "@" + ext[genNum(ext)]) + "," + wordlist[genNum(wordlist)] + "," + states[genNum(states)] + "," + str(datetime.date(year[genNum(year)], month[genNum(month)], 1).strftime("%Y-%m")) + "," + str(datetime.date(year[genNum(year)], month[genNum(month)], 1).strftime("%Y-%m"))  

  return data

month = list(range(1,12))
year = list(range(1990, int(datetime.datetime.now().strftime("%Y")) - 1))

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
states = f.read().decode("utf-8").split("\n")
f.close()

print("Imports complete. No issues so far.")
print("Opening file to write data too...")

dataFile = open('fake-breach-data/data.csv', 'w')
dataFile.write('First,Last,Email,Password,State of IP,Date of Breach,Date of Most Recent Password Change')

print("Entering loop to write data... This is the part that takes the longest...")

for i in range(0, 20000):
  fn = first[genNum(first)]
  ln = last[genNum(last)]

  line = genData(fn, ln, i)  

  dataFile.write(line)

dataFile.close()

print("All done! Enjoy!")
