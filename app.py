from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


tasks = []
feedbacks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    if task_name:
        tasks.append({'name': task_name, 'completed': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:task_index>')
def complete_task(task_index):
    tasks[task_index]['completed'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:task_index>')
def delete_task(task_index):
    tasks.pop(task_index)
    return redirect(url_for('index'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        feedbacks.append({'name': name, 'email': email, 'message': message})

        return render_template('thank_you.html', name=name)

    return render_template('contact.html')


if __name__ == "__main__":
    app.run()
