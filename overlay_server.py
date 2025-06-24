from flask import Flask, render_template_string, request, send_from_directory
import os

app = Flask(__name__)

likes = {}

@app.route("/atualizar_like", methods=["POST"])
def atualizar_like():
    nome = request.form.get("nome")
    quantidade = int(request.form.get("quantidade", 0))
    if nome:
        likes[nome] = quantidade
    return "OK"

@app.route("/overlay")
def overlay():
    sorted_likes = sorted(likes.items(), key=lambda x: x[1], reverse=True)
    indexed_likes_list = list(enumerate(sorted_likes, start=1))
    html = """
    <!DOCTYPE html>
    <html lang='pt-BR'>
    <head>
        <meta charset='UTF-8'>
        <style>
            body {
                background: transparent;
                color: white;
                font-family: Arial, sans-serif;
                font-size: 24px;
            }
            .item {
                margin-bottom: 10px;
                display: flex;
                align-items: center;
            }
            .icon {
                width: 30px;
                height: 30px;
                margin-right: 10px;
            }
            .top1 {
                position: relative;
                width: 40px;
                height: 40px;
                margin-right: 10px;
            }
            .top1 img {
                position: absolute;
                width: 100%;
                height: 100%;
            }
        </style>
    </head>
    <body>
        {% for index, (name, count) in likes_list %}
            <div class='item'>
                {% if index == 1 %}
                    <div class='top1'>
                        <img src='/static/top1.png'>
                    </div>
                {% else %}
                    <img class='icon' src='/static/like.png'>
                {% endif %}
                {{ name }} - {{ count }} likes
            </div>
        {% endfor %}
    </body>
    </html>
    """
    return render_template_string(html, likes_list=indexed_likes_list)

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
