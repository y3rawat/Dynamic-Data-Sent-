from flask import Flask, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# Global variables to track the status
current_function = 1

# Define your functions
def function_1():
    # Simulate some processing
    return "Function 1 completed"

def function_2():
    # Simulate some processing
    return "Function 2 completed"

def function_3():
    # Simulate some processing
    return "Function 3 completed"

def function_4():
    # Simulate some processing
    return "Function 4 completed"

# Routes to execute functions and show their completion
@app.route('/')
def index():
    global current_function
    # Start with the first function
    return redirect(url_for('execute_function'))

@app.route('/execute_function')
def execute_function():
    global current_function
    
    if current_function == 1:
        result = function_1()
        current_function += 1
        return render_template('function1.html', result=result)
    elif current_function == 2:
        result = function_2()
        current_function += 1
        return render_template('function2.html', result=result)
    elif current_function == 3:
        result = function_3()
        current_function += 1
        return render_template('function3.html', result=result)
    elif current_function == 4:
        result = function_4()
        current_function = 1  # Reset or end
        return render_template('function4.html', result=result)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    # This is only used for local development
    app.run(debug=True)
