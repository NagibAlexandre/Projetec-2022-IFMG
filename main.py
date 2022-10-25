from flask import *
import usuarios

Site = Flask(__name__)
Site.secret_key= 'Projetec'

@Site.route('/')
def SiteIndex():
    return render_template('index.html',Titulo = 'Página Inicial')

@Site.route('/login', methods=['GET', 'POST'])
def PaginaLogin():
  if request.method == 'POST':
    email = request.form['email']
    senha = request.form['senha']
    usuario = usuarios.buscar(email, senha)
    if usuario is None:
      flash('Usuário/senha inválidos.')
    else:
      session['usuario_email'] = usuario.email
      session['usuario_nome'] = usuario.nome
      return redirect(url_for('SiteIndex'))
      
  return render_template('login.html')

@Site.route('/logout', methods=['POST'])
def PaginaLogout():
  session.pop('usuario_email', None)
  session.pop('usuario_nome', None)
  return redirect(url_for('SiteIndex'))

@Site.route('/loginfo')
def Login_info():
    return render_template('loginfo.html', Titulo = 'Sua página')

@Site.route('/noticias')
def Site_noticias():
    return render_template('noticias.html', Titulo = 'Noticias')



# Esse código é para quando for rodar no Replit
#app.run(host='0.0.0.0', debug=True)

# Esse código é para quando for rodar em sua máquina
Site.run(debug=True)
