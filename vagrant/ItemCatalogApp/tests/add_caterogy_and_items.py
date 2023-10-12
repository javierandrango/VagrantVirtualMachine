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
try:
    new_category_1 = session.query(Categories).filter_by(user_id=user_1.id).one()
    if (not new_category_1):
        new_category_1 = Categories(name='Climbing',user=user_1)
        session.add(new_category_1)
        session.commit()
        print("category added successfully")
except:
    print("error adding new category")
else:
    print("category already exist")

# for the first time , if any error saving data in DB rise an exeption
try:
    new_category_1 = session.query(Categories).filter_by(user_id=user_1.id).one()
    if (not new_category_1):
        new_itecategory_1 = ItemCategory(item='Ascender',
                                        description='''An ascender is a device (usually mechanical) 
                                            used for directly ascending a rope, or for facilitating  
                                        	protection with a fixed rope when climbing on very steep  
                                        	mountain terrain.
                                        	Ascenders can also be used as a braking component within a 
                                        	rope hauling system, often used in rescue situations.        
                                            ''',
                                            category=new_category_1,
                                            user=user_1)
        session.add(new_itecategory_1)
        session.commit()
        print("item category added successfully")
except:
    print("error adding item category")
else:
    print("item category already exist")


#adding more item categories
new_category_2 = ItemCategory(item='Auto belay',
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
session.add(new_category_2)
session.commit()

new_category_3 = ItemCategory(item='Bachar ladder',
                              description='is a form of rope or metal ladder used as a training device by \
                                rock climbers to improve upper body strength.',
                              category=new_category_1,
                              user=user_1,
                            )
session.add(new_category_3)
session.commit()

new_category_4 = ItemCategory(item='Belay device',
                              description=' is a mechanical piece of climbing equipment used to control a rope \
                                during belaying.[1] It is designed to improve belay safety for the climber by \
                                allowing the belayer to manage their duties with minimal physical effort. With \
                                the right belay device, a small, weak climber can easily arrest the fall of a \
                                much heavier partner. Belay devices act as a friction brake, so that when a \
                                climber falls with any slack in the rope, the fall is brought to a stop.',
                              category=new_category_1,
                              user=user_1,
                            )
session.add(new_category_4)
session.commit()

new_category_5 = ItemCategory(item='Bouldering mat',
                              description='A bouldering mat or crash pad is a foam pad used for protection when \
                                bouldering. Bouldering mats help prevent climbers from injuring themselves when \
                                falling from short heights.',
                              category=new_category_1,
                              user=user_1,
                            )
session.add(new_category_5)
session.commit()


#test_category = session.query(ItemCategory).filter_by(id=1).one()
#print("category item name:",test_category.item)
#print("category name:",test_category.category.name)

