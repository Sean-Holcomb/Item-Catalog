from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catagory, Item

from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

CLIENT_ID = json.loads(open('client_secret.json', 'r').read())['web']['client_id']
app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
@app.route("/catalog")
def catalog():
	catagories = session.query(Catagory).all()
	#propbally has problems with ordering
	items = session.query(Item).order_by(desc(Item.id)).limit(10).all()
	return render_template('main.html', catagories=catagories, items=items)

@app.route("/login")
def login():
	state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
	login_session['state'] = state
	return render_template('login.html', State = state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
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
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session['access_token']
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    if access_token is None:
 	print 'Access Token is None'
    	response = make_response(json.dumps('Current user not connected.'), 401)
    	response.headers['Content-Type'] = 'application/json'
    	return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
	del login_session['access_token']
    	del login_session['gplus_id']
    	del login_session['username']
    	del login_session['email']
    	del login_session['picture']
    	response = make_response(json.dumps('Successfully disconnected.'), 200)
    	response.headers['Content-Type'] = 'application/json'
    	return response
    else:

    	response = make_response(json.dumps('Failed to revoke token for given user.', 400))
    	response.headers['Content-Type'] = 'application/json'
    	return response

@app.route("/catalog/add", methods = ['GET', 'POST'])
def addItem():
	if request.method == 'POST':
		#probably has problem with drop down selector
		catagory = session.query(Catagory).filter_by(name = request.form['catagory']).one()
		newItem = Item(title = request.form['name'], description = request.form['description'], catagory = catagory)
		session.add(newItem)
		session.commit()
		return redirect(url_for('getItems', catagory_id = catagory.id))
	else:
		catagories = session.query(Catagory).all()
		return render_template('new.html', catagories=catagories)

#conflict between url and varible
@app.route("/catalog/<int:catagory_id>")
def getItems(catagory_id):
	catagories = session.query(Catagory).all()
	items = session.query(Item).filter_by(catagory_id = catagory_id).all()
	return render_template('main.html', catagories=catagories, items=items)

#conflict between url and varible
@app.route("/catalog/<int:catagory_id>/<int:item_id>/")
def getItem(catagory_id, item_id):
	item = session.query(Item).filter_by(id = item_id).one()
	return render_template('item.html', item = item)

#conflict between url and varible
@app.route("/catalog/<int:catagory_id>/<int:item_id>/edit", methods = ['GET', 'POST'])
def editItem(catagory_id, item_id):
	editItem = session.query(Item).filter_by(id = item_id).one()
	#probably has problem with drop down selector
	if request.method == 'POST':
		if request.form['name']:
			editItem.title = request.form['name']
		if request.form['description']:
			editItem.description = request.form['description']
		#if request.form['catagory']:
		#	catagory = session.query(Catagory).filter_by(name = request.form['catagory']).one()
		#	editItem.catagory = catagory
		session.add(editItem)
		session.commit()
		return redirect(url_for('getItems', catagory_id = editItem.catagory_id))
	else:
		catagories = session.query(Catagory).all()
		return render_template('edit.html', catagories=catagories, item = editItem)

#conflict between url and varible
@app.route("/catalog/<int:catagory_id>/<int:item_id>/delete", methods = ['GET', 'POST'])
def deleteItem(catagory_id, item_id):
	item = session.query(Item).filter_by(id = item_id).one()
	if request.method == 'POST':
		session.delete(item)
		session.commit()
		return redirect(url_for('getItems', catagory_id = item.catagory_id))
	else:
		return render_template('delete.html', item = item)

@app.route('/catalog.json')
def catalogJSON():
	json = { "Catagory" : [] }
	catagories = session.query(Catagory).all()
	for catagory in catagories:
		catdict = catagory.serialize
		items = session.query(Item).filter_by(catagory_id = catagory.id).all()
		if items:
			catdict['Item'] = []
			for item in items:
				catdict['Item'].append(item.serialize)
		json['Catagory'].append(catdict)


   	return jsonify(json)



if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=8000)