from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catagory, Item

app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
@app.route("/catalog")
def catalog():
	catagories = session.query(Catagory).all()
	#propbally has problems with ordering
	items = session.query(Item).order_by(id.desc()).limit(10)
	return render_template('catalog.html', catagories=catagories, items=items)

@app.route("/catalog/add", methods = ['GET', 'POST'])
def addItem():
	if request.method == 'POST':
		#probably has problem with drop down selector
		catagory = session.query(Catagory)filter_by(name = request.form['catagory']).one()
		newItem = Item(title = request.form['name'], description = request.form['description'], catagory = catagory)
		session.add(newItem)
		session.commit()
		return redirect(url_for('getItems', catagory_id = catagory.id))
	else:
		catagories = session.query(Catagory).all()
		return render_template('new.html', catagories=catagories)

#conflict between url and varible
@app.route("/catalog/<string:catagory_name>")
def getItems(catagory_id):
	catagories = session.query(Catagory).all()
	items = session.query(Item).filter_by(cat_id = catagory_id).all()
	return render_template('catalog.html', catagories=catagories, items=items)

#conflict between url and varible
@app.route("/catalog/<string:catagory_name>/<string:item_name>")
def getItem(item_id):
	item = session.query(Item).filter_by(id = item_id).one()
	return render_template('item.html', item = item)

#conflict between url and varible
@app.route("/catalog/<string:catagory_name>/<string:item_name>/edit", methods = ['GET', 'POST'])
def editItem(item_id):
	editItem = session.query(Item).filter_by(id = item_id).one()
	#probably has problem with drop down selector
	if request.method == 'POST' and request.form['name'] and request.form['description'] and request.form['catagory']:
		catagory = session.query(Catagory)filter_by(name = request.form['catagory']).one()
		editItem.title = request.form['name']
		editItem.description = request.form['description']
		editItem.catagory = catagory)
		session.add(editItem)
		session.commit()
		return redirect(url_for('getItems', catagory_id = catagory.id))
	else:
		catagories = session.query(Catagory).all()
		return render_template('edit.html', catagories=catagories)

#conflict between url and varible
@app.route("/catalog/<string:catagory_name>/<string:item_name>/delete", methods = ['GET', 'POST'])
def deleteItem(item_id):
	item = session.query(Item).filter_by(id = item_id).one()
	if request.method == 'POST':
		session.delete(item)
		session.commit()
		return redirect(url_for('getItems', catagory_id = catagory.id))
	else:
		return render_template('delete.html', item = item)



if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8000)