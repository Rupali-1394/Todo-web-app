from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self) ->str:
        return f"{self.sno} - {self.title}"

@app.route("/", methods=['GET','POST']) 
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        print(request.form['title'])
    # todo = Todo(title="Start studying hard for Microsoft", desc="You have to pass the exam")
    # db.session.add(todo)
    # db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route("/show")
def products():
    allTodo = Todo.query.filter_by(completed=False).all()
    print(allTodo)
    return 'this is products page'

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    todo = Todo.query.filter_by(sno=sno).first()  
    return render_template('update.html', todo=todo)

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    print(todo)
    return redirect('/')

@app.route("/complete/<int:sno>")
def complete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if todo:
        todo.completed = True
        db.session.commit()
    return redirect('/')
@app.route("/completed")
def completed_tasks():
    completed_todos =Todo.query.filter_by(completed=True).all()
    return render_template('completed.html', allTodo=completed_todos)
@app.route('/all_tasks')
def all_tasks():
    all_todos = Todo.query.all()
    return render_template('all_task.html', allTodo=all_todos)
if __name__ == '__main__':
    app.run(debug=True, port= 5000)