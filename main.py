from flask import *

Site = Flask(__name__)

@Site.route('/')
def SiteIndex():
    return render_template('index.html')

# Quando rodar por meio de sites (Replit por exemplo)
#app.run(host='0.0.0.0', debug=True)

# Quando rodar por meio da própria máquina (VsCode, PyCharm etc)
Site.run(debug=True)
