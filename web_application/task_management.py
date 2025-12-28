
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    completed_count = sum(1 for task in tasks if task["done"])
    pending_count = len(tasks) - completed_count
    return render_template( "task.html", tasks=tasks,completed_count=completed_count,pending_count=pending_count)

@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("task")
    if text:
        tasks.append({ "id": len(tasks) + 1,"text": text, "done": False})
    return redirect(url_for("index"))

@app.route("/toggle/<int:id>")
def toggle(id):
    for task in tasks:
        if task["id"] == id:
            task["done"] = not task["done"]
    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["POST"])
def edit(id):
    new_text = request.form.get("task")
    for task in tasks:
        if task["id"] == id:
            task["text"] = new_text
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)