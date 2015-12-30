from flask import Flask, render_template
from flask import request, redirect, url_for, flash, jsonify
from flask.ext.seasurf import SeaSurf
from dict2xml import dict2xml as xmlify
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catagory, Item
import xml.etree.ElementTree as ET

from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())[
    'web']['client_id']
app = Flask(__name__)
csrf = SeaSurf(app)

engine = create_engine('sqlite:///itemscatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/")
@app.route("/catalog/")
def catalog():
    """
    Show user catalog page of website with most recent items showing
    """
    catagories = session.query(Catagory).all()
    items = session.query(Item).order_by(desc(Item.id)).limit(10).all()
    if 'username' not in login_session:
        state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                        for x in xrange(32))
        login_session['state'] = state
        return render_template('pub_main.html',
                               catagories=catagories,
                               items=items,
                               STATE=state)
    else:
        return render_template('main.html',
                               catagories=catagories,
                               items=items)


@csrf.exempt
@app.route('/gconnect', methods=['POST'])
def gconnect():
    """
    Validate user using Oauth2 from Google+
    """
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']

    return catalog()


@csrf.exempt
@app.route('/gdisconnect')
def gdisconnect():
    """
    Log user out from Google+ and delete fields on login_session,
    to remove user access
    """
    access_token = login_session['credentials']
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    if access_token is None:
        print 'Access Token is None'
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return catalog()
    else:
        response = make_response(
            json.dumps(
                'Failed to revoke token for given user.',
                400))
        response.headers['Content-Type'] = 'application/json'
        return catalog()


@app.route("/catalog/add", methods=['GET', 'POST'])
def addItem():
    """
    Take user to add item screen, POST method does not work if all required
     fields are not filled out.
    Post request adds new item to the database
    User redirected to home if not logged in.
    """

    if 'username' not in login_session:
        return catalog()
    if request.method == 'POST' and request.form['name'] and \
            request.form['description'] and request.form['catagory']:
        catagory = session.query(Catagory).filter_by(
            name=request.form['catagory']).one()
        newItem = Item(title=request.form['name'],
                       description=request.form['description'],
                       catagory=catagory)
        if request.form['image']:
            newItem.image = request.form['image']
        session.add(newItem)
        session.commit()
        return redirect(url_for('getItems', catagory_id=catagory.id))
    else:
        catagories = session.query(Catagory).all()
        return render_template('new.html', catagories=catagories)


@app.route("/catalog/<int:catagory_id>")
def getItems(catagory_id):
    """
    Show user catagory page with right side
    showing all items in the seclected catagory.
    Option to add item availible if user is logged in
    """
    catagories = session.query(Catagory).all()
    items = session.query(Item).filter_by(catagory_id=catagory_id).all()
    catagory = session.query(Catagory).filter_by(id=catagory_id).one()
    if 'username' not in login_session:
        state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                        for x in xrange(32))
        login_session['state'] = state
        return render_template('pub_catagory.html',
                               catagories=catagories,
                               items=items,
                               catagory=catagory,
                               length=len(items),
                               STATE=state)
    else:
        return render_template('catagory.html',
                               catagories=catagories,
                               items=items,
                               catagory=catagory,
                               length=len(items))


@app.route("/catalog/<int:catagory_id>/<int:item_id>/")
def getItem(catagory_id, item_id):
    """
    Take user to an item detail page.
    Option to edit and delete if user is logged in
    """
    item = session.query(Item).filter_by(id=item_id).one()
    if 'username' not in login_session:
        state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                        for x in xrange(32))
        login_session['state'] = state
        return render_template('pub_item.html', item=item, STATE=state)
    else:
        return render_template('item.html', item=item)


@app.route(
    "/catalog/<int:catagory_id>/<int:item_id>/edit",
    methods=[
        'GET',
        'POST'])
def editItem(catagory_id, item_id):
    """
    Display page to edit an item in the database.
    redirrected to home page if user is not logged in.
    """
    if 'username' not in login_session:
        return catalog()
    editItem = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editItem.title = request.form['name']
        if request.form['description']:
            editItem.description = request.form['description']
        if request.form['catagory']:
            catagory = session.query(Catagory).filter_by(
                name=request.form['catagory']).one()
            editItem.catagory = catagory
        if request.form['image']:
            editItem.image = request.form['image']
        session.add(editItem)
        session.commit()
        return redirect(url_for('getItems', catagory_id=editItem.catagory_id))
    else:
        catagories = session.query(Catagory).all()
        return render_template(
            'edit.html',
            catagories=catagories,
            item=editItem)

# conflict between url and varible


@app.route(
    "/catalog/<int:catagory_id>/<int:item_id>/delete",
    methods=[
        'GET',
        'POST'])
def deleteItem(catagory_id, item_id):
    """
    Display page to delete an item from database.
    redirrected to home page if user is not logged in.
    """
    if 'username' not in login_session:
        return catalog()
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('getItems', catagory_id=item.catagory_id))
    else:
        return render_template(
            'delete.html',
            item=item,
            nonce=login_session['state'])


@app.route('/catalog.json')
def catalogJSON():
    """
    Serialize database into a JSON object
    """
    json = buildDict()
    return jsonify(json)


@app.route('/catalog.xml')
def catalogXML():
    """
    Put data into xml format
    """
    data = buildDict()
    return xmlify(data, wrap="all", indent="  ")


def buildDict():
    """
    Return a python dictionary of database for use in API endpoints
    """
    dbDict = {"Catagory": []}
    catagories = session.query(Catagory).all()
    for catagory in catagories:
        catdict = catagory.serialize
        items = session.query(Item).filter_by(catagory_id=catagory.id).all()
        if items:
            catdict['Item'] = []
            for item in items:
                catdict['Item'].append(item.serialize)
        dbDict['Catagory'].append(catdict)
    return dbDict

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
