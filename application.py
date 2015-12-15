from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import session as login_session
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catagory, Item

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



if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8000)