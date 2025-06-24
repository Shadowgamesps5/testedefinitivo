from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Redireciona pra /overlay automaticamente
    return '<meta http-equiv="refresh" content="0; url=/overlay" />'

@app.route('/overlay')
def overlay():
    # Aqui vem o seu código do overlay que você já tem
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Overlay</title></head>
    <body>
        <h1 style="color:white; background:black;">Overlay Funcionando</h1>
        <!-- Aqui vai seu overlay real com os dados -->
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
