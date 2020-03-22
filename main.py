import json
from flask import ( Flask, render_template )

from almanax import dofus

app = Flask(__name__)

@app.route('/api')
def api():
    return dofus()
    
if __name__ == '__main__':
    app.run()