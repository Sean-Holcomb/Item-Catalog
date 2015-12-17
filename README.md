#Item Catalog
This is a web app built using Flask. It keeps track of items that fit into different catagories and dynamically creates pages for items. You can also add, edit and delete items from the database if you log in using Google+.
##How to install
1. Install Virtual Box and Vagrant using these <a href = https://www.udacity.com/wiki/ud197/install-vagrant>instruction</a> and the provided config file
2. Navigate to the the repository you just cloned and replace the catalog dirrectory with this repository.
3. From the command line navigate to the vagrant file and type the following commands:

	```
	vagrant up

	vagrant ssh

	cd /vagrant/catalog

	python database_setup.py

	python db_populate.py

	python application.py
	```
	The last three lines initialize the database, populate it with dummy data and begin the application

4. Go to <a href="localhost:8000">localhost:8000</a> to view the website
##Usage
* From the main page you can see all catagories and the ten most recently added items.
* Clicking on a catagory shows you all items in that catagory.
* Clicking on an item shows the details of that item.
* Login using the google plus button to gain access to the add, edit and delete functions.
* To add an item you must fill out all field except for the picture url
