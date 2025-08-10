from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task_text = request.form.get("task")
    if task_text:
        tasks.append({"text": task_text, "completed": False})
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect("/")

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = not tasks[task_id]["completed"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
