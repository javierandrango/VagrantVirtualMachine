# append directory
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
flask_app_path = os.path.join(current_dir, '..', 'flask_app')
sys.path.append(flask_app_path)

# ORM modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DB setup module
from db_setup import Base, User, Categories, ItemCategory


# DB configuration
engine = create_engine('sqlite:///../catalogDBSetup.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# for the first time , if any error saving data in DB rise an exeption
user_1 = session.query(User).filter_by(id=1).one()
catnum='1'
try:
    new_category_1 = session.query(Categories).filter_by(id=int(catnum)).one()
except:
    new_category_1 = Categories(name='Climbing',user=user_1)
    session.add(new_category_1)
    session.commit()
    print("category {} added successfully".format(catnum))
    print("----------------")
else:
    print("category {} already exist".format(catnum))
    print("----------------")

# for the first time , if any error saving data in DB rise an exeption
item_catnum='1'
try:
    new_item_category_11 = session.query(ItemCategory).filter_by(item='Ascender').one()
except:
    new_item_itecategory_11 = ItemCategory(item='Ascender',
                                        description='''An ascender is a device (usually mechanical) 
                                            used for directly ascending a rope, or for facilitating  
                                        	protection with a fixed rope when climbing on very steep  
                                        	mountain terrain.
                                        	Ascenders can also be used as a braking component within a 
                                        	rope hauling system, often used in rescue situations.        
                                            ''',
                                        category=new_category_1,
                                        user=user_1)
    session.add(new_item_itecategory_11)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(item_catnum))


#adding more item categories
# item category 2
item_catnum='2'
try:
    new_item_category_12 = session.query(ItemCategory).filter_by(item='Auto belay').one()
except:
    new_item_category_12 = ItemCategory(item='Auto belay',
                              description='An auto belay (or autobelay) is a mechanical device used for \
                                belaying in indoor climbing walls, in both training and competition \
                                climbing formats. The device enables a climber to ascend indoor routes on \
                                a top rope but without the need for a human belaying partner. The device, \
                                which is permanently mounted in a fixed position at the top of the route, \
                                winds up a tape or steel wire to which the ascending climber is attached. \
                                When the ascending climber sits back, or falls, the auto belay \
                                automaticallybrakes and smoothly lowers the climber to the ground.',
                              category=new_category_1,
                              user=user_1,
                            )
    session.add(new_item_category_12)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(item_catnum))


# item category 3
item_catnum='3'
try:
    new_item_category_13 = session.query(ItemCategory).filter_by(item='Bachar ladder').one()    
except:
    new_item_category_13 = ItemCategory(item='Bachar ladder',
                              description='is a form of rope or metal ladder used as a training device by \
                                rock climbers to improve upper body strength.',
                              category=new_category_1,
                              user=user_1,
                            )
    session.add(new_item_category_13)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(item_catnum))

# item category 4
item_catnum='4'
try:
    new_item_category_14 = session.query(ItemCategory).filter_by(item='Belay device').one()
except:
    new_item_category_14 = ItemCategory(item='Belay device',
                              description=' is a mechanical piece of climbing equipment used to control a rope \
                                during belaying.[1] It is designed to improve belay safety for the climber by \
                                allowing the belayer to manage their duties with minimal physical effort. With \
                                the right belay device, a small, weak climber can easily arrest the fall of a \
                                much heavier partner. Belay devices act as a friction brake, so that when a \
                                climber falls with any slack in the rope, the fall is brought to a stop.',
                              category=new_category_1,
                              user=user_1,
                            )
    session.add(new_item_category_14)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(item_catnum))


# item category 5
item_catnum='5'
try:
    new_item_category_15 = session.query(ItemCategory).filter_by(item='Bouldering mat').one()
except:
    new_item_category_15 = ItemCategory(item='Bouldering mat',
                              description='A bouldering mat or crash pad is a foam pad used for protection when \
                                bouldering. Bouldering mats help prevent climbers from injuring themselves when \
                                falling from short heights.',
                              category=new_category_1,
                              user=user_1,
                            )
    session.add(new_item_category_15)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(item_catnum))



# new category 2
catnum='2'
try:
    new_category_2 = session.query(Categories).filter_by(id=int(catnum)).one()     
except:
    new_category_2 = Categories(name='Camping',user=user_1)
    session.add(new_category_2)
    session.commit()
    print("category {} added successfully".format(catnum))
    print("----------------")
else:
    print("category {} already exist".format(catnum))
    print("----------------")
# adding item categories
# new item 1 category 2
item_catnum = '1'
try:
    new_item_category_21 = session.query(ItemCategory).filter_by(item='Match').one()
except:
    new_item_category_21 = ItemCategory(item='Match',
                              description='A match is a tool for starting a fire. Typically, matches are made of \
                                small wooden sticks or stiff paper. One end is coated with a material that can \
                                be ignited by friction generated by striking the match against a suitable surface.',
                              category=new_category_2,
                              user=user_1,
                            )
    session.add(new_item_category_21)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("category {} already exist".format(catnum))
# new item 2 category 2
item_catnum='2'
try:
    new_item_category_22 = session.query(ItemCategory).filter_by(item='Canteen (bottle)').one()
except:
    new_item_category_22 = ItemCategory(item='Canteen (bottle)',
                              description='A canteen is a reusable drinking water bottle designed to be used by \
                                hikers, campers, soldiers, bush firefighters, and workers in the field. It is \
                                usually fitted with a shoulder strap or means for fastening it to a belt, and may \
                                be covered with a cloth bag and padding to protect the bottle and insulate the \
                                contents. If the padding is soaked with water, evaporative cooling can help keep \
                                the contents of the bottle cool. Many canteens also include a nested canteen cup.',
                              category=new_category_2,
                              user=user_1,
                            )
    session.add(new_item_category_22)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(item_catnum))
# new item 3 category 2
item_catnum='3'
try:
    new_item_category_23 = session.query(ItemCategory).filter_by(item='Tent').one()
except:
    new_item_category_23 = ItemCategory(item='Tent',
                              description='A tent is a shelter consisting of sheets of fabric or other material \
                                draped over, attached to a frame of poles or a supporting rope. While smaller \
                                tents may be free-standing or attached to the ground, large tents are usually \
                                anchored using guy ropes tied to stakes or tent pegs. First used as portable \
                                homes by nomads, tents are now more often used for recreational camping and as \
                                temporary shelters.',
                              category=new_category_2,
                              user=user_1,
                            )
    session.add(new_item_category_23)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(item_catnum))
# new item 4 category 2
item_catnum='4'
try:
    new_item_category_24 = session.query(ItemCategory).filter_by(item='Backpack').one()
except:
    new_item_category_24 = ItemCategory(item='Backpack',
                              description='A backpack—also called knapsack, rucksack, pack, booksack, bookbag, or \
                                backsack—is, in its simplest frameless form, a fabric sack carried on one\'s back \
                                and secured with two straps that go over the shoulders, but it can have an external \
                                frame, internal frame, and there are bodypacks.',
                              category=new_category_2,
                              user=user_1,
                            )
    session.add(new_item_category_24)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(item_catnum))



# new category 3
catnum=3
try:
    new_category_3 = session.query(Categories).filter_by(id=int(catnum)).one()       
except:
    new_category_3 = Categories(name='Skateboarding',user=user_1)
    session.add(new_category_3)
    session.commit()
    print("category {} added successfully".format(catnum))
    print("----------------")
else:
    print("category {} already exist".format(catnum))
    print("----------------")
# adding item categories
# new item 1 category 3
item_catnum='1'
try:
    new_item_category_31 = session.query(ItemCategory).filter_by(item='Elbow pad').one()    
except:
    new_item_category_31 = ItemCategory(item='Elbow pad',
                              description='Elbow pads are protective padded gear worn on the elbows to protect them \
                                against injury during a fall or a strike',
                              category=new_category_3,
                              user=user_1,
                            )
    session.add(new_item_category_31)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(catnum))
# new item 2 category 3
item_catnum='2'
try:
    new_item_category_32 = session.query(ItemCategory).filter_by(item='Caster board').one()
except:
    new_item_category_32 = ItemCategory(item='Caster board',
                              description='A caster board, vigorboard or waveboard is a two-wheeled, human-powered \
                                land vehicle. Other names are J-board and RipStik (sometimes written ripstick or rip \
                                stick), both of which are derived from commercial brands.',
                              category=new_category_3,
                              user=user_1,
                            )
    session.add(new_item_category_32)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(catnum))
# new item 3 category 3
item_catnum='3'
try:
    new_item_category_33 = session.query(ItemCategory).filter_by(item='Funbox').one()    
except:
    new_item_category_33 = ItemCategory(item='Funbox',
                              description='A funbox is a standard element of a skatepark. It generally consists of a \
                                box shape with a flat top and a ramp on two or more sides. A funbox may also include \
                                other elements that allow for more complicated skateboarding tricks',
                              category=new_category_3,
                              user=user_1,
                            )
    session.add(new_item_category_33)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(catnum))
# new item 4 category 3
item_catnum='4'
try:
    new_item_category_34 = session.query(ItemCategory).filter_by(item='Knee pad').one()
except:
    new_item_category_34 = ItemCategory(item='Knee pad',
                              description='Knee pads or kneepads are protective gear worn on knees to protect them against \
                                impact injury from falling to the ground or hitting an obstacle, or to provide padding for \
                                extended kneeling.Their primary purpose is to shield this vulnerable joint from potential \
                                impact injuries that may occur due to accidental falls, collisions with objects, or striking \
                                obstacles. By providing a cushioning barrier between the knees and the ground or other hard \
                                surfaces, knee pads help minimize the risk of severe damage or trauma.',
                              category=new_category_3,
                              user=user_1,
                            )
    session.add(new_item_category_34)
    session.commit()
    print("item category {} successfully added".format(item_catnum))
else:
    print("item category {} already exist".format(catnum))




#test_category = session.query(ItemCategory).filter_by(id=1).one()
#print("category item name:",test_category.item)
#print("category name:",test_category.category.name)

