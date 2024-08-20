from flask import Flask
from configuration import configure_all
# Inicializaçao
app = Flask(__name__)

configure_all(app)

# Execuçao
app.run(debug=True)