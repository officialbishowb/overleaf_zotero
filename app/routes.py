from flask import request, Response
from . import app
from pyzotero import zotero

from flask import request, Response
from . import app
from pyzotero import zotero
import bibtexparser

@app.route('/fetch_bibtex')
def fetch_bibtex():
    user_id = request.args.get('user_id')
    collection_key = request.args.get('collection_key')
    api_key = request.args.get('api_key')
    include_subcollections = request.args.get('include_subcollections', 'false').lower() == 'true'
    
    zot = zotero.Zotero(user_id, 'user', api_key)
    items = [] 
    
    main_collection_items = zot.collection_items(collection_key, format='bibtex')
    if main_collection_items:
        items.append(main_collection_items)
    
    if include_subcollections:
        subcollections = zot.collections_sub(collection_key)
        for sub in subcollections:
            sub_collection_items = zot.collection_items(sub['key'], format='bibtex')
            if sub_collection_items:
                items.append(sub_collection_items)
    
    combined_bibtex = '\n'.join([bibtexparser.dumps(item) for item in items])
    return Response(combined_bibtex, mimetype='text/plain')


@app.route('/')
def index():
    return "Hello, World!"