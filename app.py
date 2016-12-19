import json
from flask import Flask, request, jsonify
from flask import render_template
from lib.bisection import Bisection
from lib.fixed_point import FixedPoint
from lib.gauss import Gauss
from lib.horner import Horner
from lib.jacobi import Jacobi
from lib.newton_raphson import NewtonRaphson
from lib.regula_falsi import RegulaFalsi
from lib.secant import Secant

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/biseccion')
def biseccion():
    return render_template('biseccion.html')


@app.route('/calcular_biseccion', methods=['POST'])
def calcular_biseccion():
    equation = str(request.form['equation'])
    a = float(request.form['a'])
    b = float(request.form['b'])
    e = float(request.form['error'])
    bs = Bisection(equation, 'x')
    bs.solve_bisection(a, b, e)
    return jsonify(data=bs.sections)


@app.route('/regula_falsi')
def regula_falsi():
    return render_template('regula_falsi.html')


@app.route('/calcular_regula', methods=['POST'])
def calcular_regula_falsi():
    equation = str(request.form['equation'])
    a = float(request.form['a'])
    b = float(request.form['b'])
    e = float(request.form['error'])
    rf = RegulaFalsi(equation, 'x')
    rf.solve_regula(a, b, e)
    return jsonify(data=rf.sections)


@app.route('/newton_raphson')
def nraphson():
    return render_template('newton_raphson.html')


@app.route('/calcular_nraphson', methods=['POST'])
def calcular_nraphson():
    equation = str(request.form['equation'])
    x = float(request.form['x'])
    e = float(request.form['error'])
    nr = NewtonRaphson(equation, 'x')
    nr.solve_newton(x, e)
    return jsonify(data=nr.sections)


@app.route('/secante')
def secante():
    return render_template('secante.html')


@app.route('/calcular_secante', methods=['POST'])
def calcular_secante():
    equation = str(request.form['equation'])
    a = float(request.form['a'])
    b = float(request.form['b'])
    e = float(request.form['error'])
    se = Secant(equation, 'x')
    se.solve_secant(a, b, e)
    return jsonify(data=se.sections)


@app.route('/punto_fijo')
def punto_fijo():
    return render_template('punto_fijo.html')


@app.route('/calcular_punto_fijo', methods=['POST'])
def calcular_punto_fijo():
    equation = str(request.form['equation'])
    x = float(request.form['x'])
    e = float(request.form['error'])
    fp = FixedPoint(equation, 'x')
    fp.solve_fixed(x, e)
    return jsonify(data=fp.sections)


@app.route('/horner')
def horner():
    return render_template('horner.html')


@app.route('/calcular_horner', methods=['POST'])
def calcular_horner():
    a = str(request.form['equation_a'])
    b = str(request.form['equation_b'])
    hrn = Horner(a, b, 'x')
    hrn.solve_horner()
    return jsonify(data={'quotient': str(hrn.quotient.as_expr()), 'residue': str(hrn.residue.as_expr())})


@app.route('/gauss')
def gauss():
    return render_template('gauss.html')


@app.route('/calcular_gauss', methods=['POST'])
def calcular_gauss():
    eqs = str(request.form['equations']).split('\n')
    gss = Gauss(eqs, var='x')
    gss.solve_gauss()
    return jsonify(sections=str(gss.sections), eqc=str(gss.eq_coeffs))


@app.route('/jacobi')
def jacobi():
    return render_template('jacobi.html')


@app.route('/calcular_jacobi', methods=['POST'])
def calcular_jacobi():
    eqs = str(request.form['equations']).split('\n')
    limit = int(request.form['limit'])
    jcb = Jacobi(eqs, limit=limit, var='x')
    jcb.solve_jacobi()
    return jsonify(sections=str(jcb.sections), eqc=str(jcb.eq_coeffs))


@app.route('/lagrange_poli')
def lagrange_poli():
    return render_template('lagrange_poli.html')


@app.route('/diferencia_finita')
def diferencia_finita():
    return render_template('diferencia_finita.html')


@app.route('/trapecio')
def trapecio():
    return render_template('trapecio.html')


@app.route('/simpson')
def simpson():
    return render_template('simpson.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
