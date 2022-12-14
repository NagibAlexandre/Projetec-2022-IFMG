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
      
  return render_template('loginindex.html')

@Site.route('/logout', methods=['GET','POST'])
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

@Site.route('/login')
def Site_Login():
    return render_template('loginindex.html', Titulo = 'Login')

@Site.route('/categorias')
def Site_categorias():
    return render_template('categorias.html', Titulo = 'Categorias')

@Site.route('/faleconosco')
def Site_faleconosco():
    return render_template('faleconosco.html', Titulo = 'Fale Conosco')

@Site.route('/recomendacoes')
def Site_recomendacoes():
    return render_template('recomendacoes.html', Titulo = 'Recomendacoes')

@Site.route('/quemsomos')
def Site_quemsomos():
    return render_template('quemsomos.html', Titulo = 'Quem Somos')

# Sub-sites da página categoria

@Site.route('/categorias/games')
def SiteCGames():
    return render_template('/subcategorias/games.html', Titulo= 'Games')
   
@Site.route('/categorias/culinaria')
def SiteCCulinaria():
    return render_template('/subcategorias/culinaria.html', Titulo= 'Culinaria')

@Site.route('/categorias/conversa')
def SiteCConversa():
    return render_template('/subcategorias/conversa.html', Titulo= 'Conversa')

@Site.route('/categorias/artes')
def SiteCArtes():
    return render_template('/subcategorias/artes.html', Titulo= 'Artes')

@Site.route('/categorias/musica')
def SiteCMusica():
    return render_template('/subcategorias/musica.html', Titulo= 'Musica')

@Site.route('/categorias/esporte')
def SiteCEsporte():
    return render_template('/subcategorias/esporte.html', Titulo= 'Esporte"')

# Esse código é para quando for rodar no Replit
#app.run(host='0.0.0.0', debug=True)

# Esse código é para quando for rodar em sua máquina
Site.run(debug=True)
