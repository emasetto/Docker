import os
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'edher123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('auladoker.html')

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    valor = request.form['valor']
    categoria = request.form['categoria']
    if nome and valor and categoria:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tb_produto (nome, valor, categoria) VALUES (%s, %s, %s)', (nome, valor, categoria))
        conn.commit()
    return render_template('auladoker.html')

@app.route('/listar', methods = ['POST','GET'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select nome, valor, categoria from tb_produto')
    data = cursor.fetchall()
    conn.commit()
    return render_template('lista.html', datas = data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host = '0.0.0.0', port = port)