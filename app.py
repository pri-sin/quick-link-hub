from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret_key"

DEFAULT_LINKS = [
    {"name": "YouTube", "url": "https://www.youtube.com"},
    {"name": "Google", "url": "https://www.google.com"},
    {"name": "Netflix", "url": "https://www.netflix.com"},
]

@app.route("/", methods=["GET", "POST"])
def home():
    if "links" not in session:
        session["links"] = DEFAULT_LINKS.copy()

    if request.method == "POST":
        if "add" in request.form:
            name = request.form.get("name").strip()
            url = request.form.get("url").strip()

            if name and url:
                session["links"].append({"name": name, "url": url})
                session.modified = True

        elif "delete" in request.form:
            index = int(request.form.get("delete"))
            if 0 <= index < len(session["links"]):
                del session["links"][index]
                session.modified = True

        return redirect("/")

    return render_template_string(HTML_TEMPLATE, links=session["links"])

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Personal Page</title>
    <style>
        body {
            background-color: #1B3A34; /* Dark green background */
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            width: 650px;
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        .emoji {
            font-size: 5rem;
            margin-bottom: 20px;
        }
        .link-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255, 255, 255, 0.2);
            padding: 10px 20px;
            margin: 10px 0;
            border-radius: 10px;
        }
        .link-container a {
            color: white;
            text-decoration: none;
            font-size: 1.2rem;
        }
        .link-container button {
            background: #D9534F;
            border: none;
            color: white;
            padding: 5px 10px;
            cursor: pointer;
            border-radius: 5px;
            font-size: 1rem;
        }
        .link-container button:hover {
            background: #c9302c;
        }
        .form-container {
            margin-top: 20px;
        }
        input, button {
            padding: 10px;
            margin: 5px;
            border-radius: 5px;
            border: none;
        }
        input {
            width: 200px;
        }
        button {
            background: #4CAF50;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="emoji">😎</div>
        <div class="links">
            {% for link in links %}
                <div class="link-container">
                    <a href="{{ link.url }}" target="_blank">{{ link.name }}</a>
                    <form method="POST">
                        <button type="submit" name="delete" value="{{ loop.index0 }}">🗑️</button>
                    </form>
                </div>
            {% endfor %}
        </div>

        <div class="form-container">
            <form method="POST">
                <input type="text" name="name" placeholder="Site Name" required>
                <input type="url" name="url" placeholder="https://example.com" required>
                <button type="submit" name="add">Add Link</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
