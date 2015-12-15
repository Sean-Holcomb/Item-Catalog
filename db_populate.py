from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Catagory, Base, Item

engine = create_engine('sqlite:///itemcatalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Clear Tables (Does ot reset auto increment)
#session.query(Catagory).delete()
#session.query(Item).delete()

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
item1 = Item(title="Snowboard", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item1)
session.commit()

item2 = Item(title="Boots", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item2)
session.commit()

item3 = Item(title="Snow Jacket", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item3)
session.commit()

item4 = Item(title="Helmet", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item4)
session.commit()

item5= Item(title="Snow Gloves", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item5)
session.commit()

item6 = Item(title="Snow Pants", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory1)
session.add(item6)
session.commit()
#Skiiing items catagory 2
item7 = Item(title="Skis", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory2)
session.add(item7)
session.commit()

item8 = Item(title="Ski Poles", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory2)
session.add(item8)
session.commit()

item9 = Item(title="Goggles", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory2)
session.add(item9)
session.commit()

item10 = Item(title="Ski Boots", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory2)
session.add(item10)
session.commit()
#Surfing items catagory 3
item11 = Item(title="Surfboard", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory3)
session.add(item11)
session.commit()

item12 = Item(title="Wetsuit", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory3)
session.add(item12)
session.commit()

item13 = Item(title="Surf Wax", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory3)
session.add(item13)
session.commit()

item14 = Item(title="Leash", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory3)
session.add(item14)
session.commit()

item15 = Item(title="Stomp Pad", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory3)
session.add(item15)
session.commit()
#Rock Climbing items catagory4
item16 = Item(title="Climbing Shoes", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory4)
session.add(item16)
session.commit()

item17 = Item(title="Chalk bag", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory4)
session.add(item17)
session.commit()

item18 = Item(title="Chalk", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory4)
session.add(item18)
session.commit()

item19 = Item(title="Harness", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory4)
session.add(item19)
session.commit()

item20 = Item(title="Rope", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory4)
session.add(item20)
session.commit()
#Camping items catagory 5
item21 = Item(title="Tent", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory5)
session.add(item21)
session.commit()

item22 = Item(title="Sleeping Bag", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory5)
session.add(item22)
session.commit()

item23 = Item(title="Camp Fire", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory5)
session.add(item23)
session.commit()

item24 = Item(title="Dining Kit", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory5)
session.add(item24)
session.commit()
#Baseball items catagory 6
item25 = Item(title="Baseball Ball", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory6)
session.add(item25)
session.commit()

item26 = Item(title="Baseball Bat", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory6)
session.add(item26)
session.commit()

item27 = Item(title="Batting Helmet", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory6)
session.add(item27)
session.commit()

item28 = Item(title="Catching Mit", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory6)
session.add(item28)
session.commit()

item29 = Item(title="Chewing Tabaco", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory6)
session.add(item29)
session.commit()
#Football items catagory 7
item30 = Item(title="Football Armor", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory7)
session.add(item30)
session.commit()

item31 = Item(title="Cleets", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory7)
session.add(item31)
session.commit()

item32 = Item(title="Football Ball", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory7)
session.add(item32)
session.commit()

item33 = Item(title="Helmet", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory7)
session.add(item33)
session.commit()
#Golf items catagory8
item34 = Item(title="Golf Bag", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item34)
session.commit()

item35 = Item(title="Golf Club", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item35)
session.commit()

item36 = Item(title="Driver", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item36)
session.commit()

item37 = Item(title="Golf Cart", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item37)
session.commit()

item38 = Item(title="Caddie", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item38)
session.commit()

item39 = Item(title="Tees", description = "Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem Ipsum lorem", catagory = catagory8)
session.add(item39)
session.commit()

print "added menu items!"