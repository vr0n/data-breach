# vr0n
# 2019-09-23

This will hopefully becomes a fun way that others can learn about data analysis with Python.
I am writing this project as I learn myself, so things may not look as professional as they could.

Here's the idea:
	1) Create a script that automatically generates fake breach data
		a) I had thought about using real data from something like scylla.sh, but this felt potentially irresponsible
		b) This will make it so every experience with the project can have entirely different data
		c) Also, the scripts are very simple; so, everything is very customizable
	2) Introduce users to Python data visualization
	3) Have the users answer questions about the data using data visualization tools

Here's how I'm approaching each part of the idea:
	
	1) Create a scipt that automatiically gnerates fake breach data
		So, really I was learning about Python when I wrote this. There is no better evidence of this than
		checking out how I collected the data. This is a very inefficient use of Python, and I would like
		to go back and clean it up. When I do, I will update this README, so if you're reading this you
		are still working with the inefficient scripts.

		The scripts check different websites for data.
			The first-names script crawls a website for the top 1,000 last names of the past century.
			The last-names script grabs the top 100 male names and top 100 female names from SSA.GOV.
			The passwords are from an online dump of rockyou.txt
			The usernames are from a pastebin dump of an actual breach. Instead of using this data
			in the raw, I carved out the usernames and dumped the email extensions.

		These bits of data are drawn from the generate-values.py script. All you have to do is run:
			python generate-values.py
		And you will get all of the data from the aforementioned places.

		I've created a static dump of these lists in lists/ (which is what all of the other scripts call).
		The only reason I've decided to keep the generate-data.py script is in case the names get updated.
		I should probably have never used the generate-datay.py script the way I have, but I'm keeping it
		in as a historical artificat in case I need to reference it. Really, I'm only typing all this to 
		tell you to ignore that script and just use the lists/ folder.

		To actually generate fake data, you simply call:
			python generate-data.py
		The current setting is to generate 20,000 bits of data, however, I plan to change this so you can
		enter in a specific number of credentials you would like to generate as follows:
			python generate-data.py 1000000
		With the default (in case you don't enter a number) being 20,000

		This script currently generates the following metrics:
			FIRST NAME, LAST NAME, EMAIL, PASSWORD, STATE, DATE OF BREACH, DATE OF CLOSEST PASSWORD CHANGE
		There are other metrics I would like to add, like IP ADDRESS, however, I think this is enough for
		now.

	2) With these metrics, you can answer several questions with data visualization and analysis. With just a few
	pieces of information and an ability to Google questions, I think anyone could answer any of the questions I
	could ask. Ideally, I would introduce users to pandas, numpy, and seaborn. 

	3) I want users to answer a number of questions/requests with the given data:
		a) Create an ordered list of first and last names
			- This is more for interesting data purposes and understanding how to manipulate data
		b) Determine what email service suffered the most breaches
		c) Visualize the breaches by state
		d) Visualize the breaches by date
		e) How many passwords were all lowercase?
		f) How many passwords were all alphabetical characters only?
		g) How many passwords used uppercase, lowercase, numbers, and special characters?
		h) How many passwords have not been changes since the breach?
		i) use python to create a password generator for all of the users and save the emails and passwords into a csv file 
