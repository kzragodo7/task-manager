from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data for tasks and contact feedback (use a database in production)
tasks = []
feedbacks = []

# Route to display tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to handle task addition
@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    if task_name:
        tasks.append({'name': task_name, 'completed': False})
    return redirect(url_for('index'))

# Route to mark a task as completed
@app.route('/complete/<int:task_index>')
def complete_task(task_index):
    tasks[task_index]['completed'] = True
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<int:task_index>')
def delete_task(task_index):
    tasks.pop(task_index)
    return redirect(url_for('index'))

# Route to show the contact form and handle form submission
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get user input from form
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Store feedback (in-memory, can be replaced by a database)
        feedbacks.append({'name': name, 'email': email, 'message': message})

        # Redirect to a thank-you page or show a success message
        return render_template('thank_you.html', name=name)

    return render_template('contact.html')


if __name__ == "__main__":
    app.run()
