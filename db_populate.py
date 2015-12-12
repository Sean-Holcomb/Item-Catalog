from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Catagory, Base, Item

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Catagories
catagory1 = Catagory(name="Snowboarding")
catagory2 = Catagory(name="Skiing")
catagory3 = Catagory(name="Surfing")
catagory4 = Catagory(name="Rock Climbing")
catagory5 = Catagory(name="Camping")
catagory6 = Catagory(name="Baseball")
catagory7 = Catagory(name="Football")
catagory8 = Catagory(name="Golf")

session.add(catagory1)
session.add(catagory2)
session.add(catagory3)
session.add(catagory4)
session.add(catagory5)
session.add(catagory6)
session.add(catagory7)
session.add(catagory8)
session.commit()

#Snowboarding items catagory1
item = Item(title="Snowboard", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item)
session.commit()

item = Item(title="Boots", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item)
session.commit()

item = Item(title="Snow Jacket", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item)
session.commit()

item = Item(title="Helmet", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item)
session.commit()

item = Item(title="Snow Gloves", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item)
session.commit()

item = Item(title="Snow Pants", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item)
session.commit()
#Skiiing items catagory 2
item = Item(title="Skis", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory2)
session.add(item)
session.commit()

item = Item(title="Ski Poles", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory2)
session.add(item)
session.commit()

item = Item(title="Goggles", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory2)
session.add(item)
session.commit()

item = Item(title="Ski Boots", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory2)
session.add(item)
session.commit()
#Surfing items catagory 3
item = Item(title="Surfboard", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory3)
session.add(item)
session.commit()

item = Item(title="Wetsuit", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory3)
session.add(item)
session.commit()

item = Item(title="Surf Wax", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory3)
session.add(item)
session.commit()

item = Item(title="Leash", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory3)
session.add(item)
session.commit()

item = Item(title="Stomp Pad", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory3)
session.add(item)
session.commit()
#Rock Climbing items catagory4
item = Item(title="Climbing Shoes", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory4)
session.add(item)
session.commit()

item = Item(title="Chalk bag", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory4)
session.add(item)
session.commit()

item = Item(title="Chalk", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory4)
session.add(item)
session.commit()

item = Item(title="Harness", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory4)
session.add(item)
session.commit()

item = Item(title="Rope", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory4)
session.add(item)
session.commit()
#Camping items catagory 5
item = Item(title="Tent", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory5)
session.add(item)
session.commit()

item = Item(title="Sleeping Bag", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory5)
session.add(item)
session.commit()

item = Item(title="Camp Fire", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory5)
session.add(item)
session.commit()

item = Item(title="Dining Kit", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory5)
session.add(item)
session.commit()
#Baseball items catagory 6
item = Item(title="Baseball Ball", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory6)
session.add(item)
session.commit()

item = Item(title="Baseball Bat", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory6)
session.add(item)
session.commit()

item = Item(title="Batting Helmet", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory6)
session.add(item)
session.commit()

item = Item(title="Catching Mit", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory6)
session.add(item)
session.commit()

item = Item(title="Chewing Tabaco", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory6)
session.add(item)
session.commit()
#Football items catagory 7
item = Item(title="Football Armor", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory7)
session.add(item)
session.commit()

item = Item(title="Cleets", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory7)
session.add(item)
session.commit()

item = Item(title="Football Ball", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory7)
session.add(item)
session.commit()

item = Item(title="Helmet", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory7)
session.add(item)
session.commit()
#Golf items catagory8
item = Item(title="Golf Bag", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item)
session.commit()

item = Item(title="Golf Club", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item)
session.commit()

item = Item(title="Driver", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item)
session.commit()

item = Item(title="Golf Cart", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item)
session.commit()

item = Item(title="Caddie", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item)
session.commit()

item = Item(title="Tees", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item)
session.commit()




print "added menu items!"