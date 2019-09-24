from urllib.request import urlopen, Request
import pandas as pd

print('Collecting last names first...')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = 'https://names.mongabay.com/data/1000.html'

req = Request(url=reg_url, headers=headers)
data = urlopen(req).read()

raw = pd.read_html(data, skiprows=1)[0]
df = pd.DataFrame(raw)

names_raw = df[0].to_string(index=False)
names = names_raw.lower().split()

file = open('data-sources/last-names', 'w')
file.write(repr(names))
file.close()

print('Last names collected. Now collecting first names...')

reg_url = 'https://www.ssa.gov/OACT/babynames/decades/century.html'

req = Request(url=reg_url, headers=headers)
data = urlopen(req).read()

raw = pd.read_html(data)[0]
df = pd.DataFrame(raw)

male_names = df['Males']['Name'].to_string(index=False).rsplit("\n",1)[0]
female_names = df['Females']['Name'].to_string(index=False).rsplit("\n",1)[0]

names = (male_names + female_names).lower().split()

file = open('data-sources/first-names', 'w')
file.write(repr(names))
file.close()

print('Okay, we`ve collected the first names.')
print('Now for the hard part...')
print('Let`s collect the passwords...')

reg_url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-dup.txt'

req = Request(url=reg_url, headers=headers)
data = urlopen(req).read()

passwords = str(data).split('\\r\\n')

file = open('data-sources/passwords', 'w')
file.write(repr(passwords))
file.close()

print('Passwords have been collected (but, you should probably check the file anyway...)')

print('Now, let`s generate numbers for the email addresses...')
print('(The email extensions are hardcoded, so you can add to them if you like)')

numbers = []

for i in range(2,2200):
  numbers.append(i)

file = open('data-sources/numbers', 'w')
file.write(repr(numbers))
file.close()

print('Finally, let`s grab some weird emails that aren`t just names. Why? Because it looks more real...')

reg_url = 'https://pastebin.com/raw/gcXC6QH8'

req = Request(url=reg_url, headers=headers)
data = urlopen(req).read()

usernamesMid = data.decode("utf-8").split()
usernamesMid2 = []
usernames = []

for i in usernamesMid:
  if "@" in i:
    usernamesMid2.append(i)

for i in usernamesMid2:
  usernames.append(i.split('@',1)[0])

file = open('data-sources/usernames', 'w')
file.write(repr(usernames))
file.close()

print('Okay! That`s everything for now!')
print('Maybe in the future I will add zip codes as well, but this is a good start.')
print('Enjoy analyzing your fake data!')
