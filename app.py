from flask import Flask, render_template, request, redirect, url_for, flash
from services.estoque_service import (
    inicializar_sheets, listar_estoque, obter_totais, obter_painel,
    registrar_entrada, dar_baixa, listar_historico
)

app = Flask(__name__)
app.secret_key = "entreirmaos_secreto"

with app.app_context():
    try:
        inicializar_sheets()
    except Exception as e:
        print("Erro ao inicializar sheets:", e)

@app.route("/")
def index():
    return redirect(url_for("painel"))

@app.route("/painel")
def painel():
    totais, produtos = obter_painel()
    return render_template("painel.html", totais=totais, produtos=produtos)

@app.route("/entrada", methods=["GET", "POST"])
def entrada():
    if request.method == "POST":
        dados = request.form.to_dict()
        resultado = registrar_entrada(dados)
        
        if resultado.get("sucesso"):
            flash(resultado["mensagem"], "success")
        else:
            flash(resultado.get("erro", "Erro ao registrar entrada."), "error")
            
        return redirect(url_for("entrada"))
        
    return render_template("entrada.html")

@app.route("/baixa", methods=["GET", "POST"])
def baixa():
    if request.method == "POST":
        dados = request.form.to_dict()
        resultado = dar_baixa(dados)
            
        if resultado.get("sucesso"):
            flash(resultado["mensagem"], "success")
        else:
            flash(resultado.get("erro", "Erro ao dar baixa."), "error")
            
        return redirect(url_for("baixa"))
        
    produtos = listar_estoque()
    return render_template("baixa.html", produtos=produtos)

@app.route("/historico")
def historico():
    filtro_tipo = request.args.get("tipo", "")
    filtro_mes  = request.args.get("mes", "")
    registros   = listar_historico(filtro_tipo, filtro_mes)
    return render_template("historico.html",
                           registros=registros,
                           filtro_tipo=filtro_tipo,
                           filtro_mes=filtro_mes)

if __name__ == "__main__":
    app.run(debug=True)
