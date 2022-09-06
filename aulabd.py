import os
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'edher123'
app.config['MYSQL_DATABASE_DB'] = 'banco'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.0'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('auladoker.html')

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    if nome and cpf and email:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tb_cadastro (user_nome, user_cpf, user_email) VALUES (%s, %s, %s)', (nome, cpf, email))
        conn.commit()
    return render_template('auladoker.html')

@app.route('/listar', methods = ['POST','GET'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select user_nome, user_cpf, user_email from tb_cadastro')
    data = cursor.fetchall()
    conn.commit()
    return render_template('lista.html', datas = data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host = '0.0.0.0', port = port)