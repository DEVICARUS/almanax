import json
from flask import ( Flask, render_template )

import almanax
from utility import getnsoup

app = Flask(__name__)

@app.route('/api/dofus')
def dofus():
    soup_almanax = getnsoup("http://www.krosmoz.com/en/almanax")
    return almanax.dofus(soup_almanax)

@app.route('/api/meridian')
def meridian():
    soup_almanax = getnsoup("http://www.krosmoz.com/en/almanax")
    return almanax.meridian(soup_almanax)
    
if __name__ == '__main__':
    app.run()