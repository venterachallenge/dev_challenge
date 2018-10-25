# dev_challenge

	Readme

	The version of python that I used for this project is version 3.7.0
	
	the solution to the problem is done in two python files.  

	In the first python file, JsonConverter.py, the file takes a data.json file and converts it to the new style of json according to the spec.  This output file is called results.json.  

	To run this file just run "python JsonConverter.py" in a directory that contains data.json.  It will output a file called results.json

	The second part of this problem is done in the solutions.py file.  this file takes a json file called data-transformed.json and outputs the resulting calculations to output.txt.  
	
	to run this file just run "python solutions.py" in a directory that contains the data-transformed.json  For your convienience I have attached the sample files and my solutions to the problems in this file.

	for the solutions to these questions:
	Total revenue
	Vendor with the most revenue
	Quantity of hats sold
	ID of the customer that bought the most ice in October

	I used an interative approach by using loops to go through the json structure and store the data.  I used dictionaries to store the vendor with the most money and the custiomer id with the person who bought the most ice.  The rest of the data was easy to find and was stored inside variables.

	For the json converter, I used an iterative approach by going through the old json format and converting it to the new style.  I utilized a dictionary for the first level of data and a list of dictionaries to store the information about the orders themselves.  

	Some assumptions that I made while making this was that the files I would receive would be data.json and data-transformed.json, and that these two files would be fully functional json files with the layout specified in the problem specifications.

	I would also like to note that this implementation does not have any error checking.
