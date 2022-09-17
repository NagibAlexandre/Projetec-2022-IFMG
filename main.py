from flask import *

Site = Flask(__name__)

@Site.route('/')
def SiteIndex():
    return render_template('index.html',Titulo = 'IndexPlaceholder')

# Esse código é para quando for rodar no Replit
#app.run(host='0.0.0.0', debug=True)

# Esse código é para quando for rodar em sua máquina
Site.run(debug=True)
