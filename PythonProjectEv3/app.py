from flask import Flask, render_template, request

app = Flask(__name__)

# RUTA PAGINA PRINCIPAL
@app.route('/')
def index():
    return render_template('index.html')

# RUTA EJERCICIO NUMERO 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        try:
            notas = [float(request.form['nota1']), float(request.form['nota2']), float(request.form['nota3'])]
            asistencia = float(request.form['asistencia'])
            promedio = sum(notas) / len(notas)
            estado = "Aprobado" if promedio >= 40 and asistencia >= 70 else "Reprobado"
            resultado = {'promedio': promedio, 'estado': estado}
        except ValueError:
            resultado = {'Error': ' Ingresar valores válidos.'}
    return render_template('ejercicio1.html', resultado=resultado)

# RUTA EJERCICIO NUMERO 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombres = [request.form['nombre1'], request.form['nombre2'], request.form['nombre3']]
        nombre_largo = max(nombres, key=len)
        resultado = {'nombre': nombre_largo, 'longitud': len(nombre_largo)}
    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)