from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/dojo')
def success():
    return "¡Dojo!"

@app.route('/say/<string:name>')
def hola(name):
    return f"¡Hola, {name.capitalize()}!"

@app.route('/repeat/<int:times>/<string:message>') 
def message(times, message):
    msg = f"<h1> {message} <h1>" * times
    return f"{msg}"

@app.errorhandler(404)
def not_found(e):
    return "<h1>Página no encontrada <h1>", 404


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

