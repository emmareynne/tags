import sys
from os.path import join
sys.path.insert(1, sys.path[0])
from config import load_config, app_init
from datetime import datetime
from IPython import embed
from flask import request, redirect, render_template, g

app = app_init(__name__)

from tag import Tag # After app_init(), which sets db for the model

cfg = load_config(join(app.root_path, '../shared/config.yml'))

@app.route('/', methods=['GET'])
def show_tags():
    g.setdefault('image', cfg['awesome_image']) # Flask.g: a way to pass var to a template
    #embed()
    return "<html><head><link href=\"static/style.css\" rel=\"stylesheet\" type=\"text/css\"></head><body><h1>The Ultimate Tag Manager</h1><h1>Hello World!</h1><img src=\"%s\"><div>%s</div><div>%s</div></body></html>" % (cfg['awesome_image'],tags_html, form_html)

@app.route('/tags', methods=['POST'])
def add_tag():
    new_tag = request.form['tag-name']
    tag = Tag.where('tag', new_tag).first()
    if tag is None:
        tag = Tag.create(name=new_tag)

    return redirect('/')
