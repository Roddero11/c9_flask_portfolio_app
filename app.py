from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/<name>')
def profile(name):
	new_name = name + "likes to eat mangos"
	return render_template('index.html', name=new_name)


@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('add_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      total = 1
  	      try:
  	      	for str_num in request.form['text'].split():
  	      		total *= int(str_num)
  	      	return render_template('add_numbers.html', result=str(total))
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! 2 numbers with a space between them please"


@app.route('/shopping_list', methods=['GET','POST'])
def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          shop_list = []
          try:
            for item in request.form['text'].split():
              
              shop_list.append(item)

              
              
            return render_template('shopping_list.html', result="\n".join([str(item) for item in shop_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"
          
  	      
@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          for item in request.form['text'].split():
            answer = (datetime.datetime.now(pytz.timezone("Europe/Dublin")).strftime('Time = ' + '%H:%M:%S' + ' GMT ' + ' Year = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')

              
              
            return render_template('time.html', result=answer)

         

@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')


@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')


if __name__ == '__main__':
	app.run(debug=True)

# Program make a simple calculator 

# This function adds two numbers 
def add(x, y):
	return x + y
# This function subtracts two numbers
def subtract(x, y):
	return x - y
# This function multiples two numbers
def multiply(x, y):
	return x * y
# This function divides two numbers
def divide(x, y):
	return x/y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
	# take input from the user
	choice = input("Enter choice(1/2/3/4): ")
	
	# check if choice is one of the four options
	if choice in ("1", "2", "3", "4"):
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		
		if choice == "1":
			print(num1, "+", num2, "=", add(num1, num2))
			      
                elif choice == "2":
			      print(num1, "-", num2, "=", subtract(num1, num2))
			      
	        elif choice == "3":
			      print(num1, "*", num2, "=", multiply(num1, num2))
			      
                elif choice == "4":
			print(num1, "/", num2, "=", divide(num1, num2))
			
		# check if user wants another calculation
		# break the while loop if answer is no
		next_calculation = input("Let's do next calculation? (yes/no): ")
		if next_calculation == "no":
			break
		
		else:
			print("Invalid Input")
		
