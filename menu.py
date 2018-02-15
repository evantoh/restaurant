from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Base, MenuItem

engine = create_engine('postgresql://evans:evans123@localhost:5432/rest')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Menu for UrbanBurger
restaurant1 = Restaurant(name="Urban Burger")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="ksh250", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(name="French Fries", description="with garlic and parmesan",
                     price="ksh299", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     price="ksh550", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Chocolate Cake", description="fresh baked and served with ice cream",
                     price="ksh399", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Sirloin Burger", description="Made with grade A beef",
                     price="ksh799", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Root Beer", description="16oz of refreshing goodness",
                     price="ksh199", course="Beverage", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Iced Tea", description="with Lemon",
                     price="ksh99", course="Beverage", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
                     price="ksh349", course="Entree", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                     price="ksh599", course="Entree", restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                     price="ksh799", course="Entree", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    name="Peking Duck", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="$25", course="Entree", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     price="ksh 15", course="Entree", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="ksh 12", course="Entree", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     price="ksh 14", course="Entree", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     price="ksh 120", course="Entree", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant1 = Restaurant(name="Panda Garden")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     price="ksh 899", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     price="ksh 699", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
                     price="ksh 995", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     price="ksh 699", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="ksh 950", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Thyme for that
restaurant1 = Restaurant(name="Thyme for That Vegetarian Cuisine ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="ksh 299", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     price="ksh 599", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                     price="ksh 450", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="ksh 695", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="ksh 795", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="ksh 680", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Tony's Bistro
restaurant1 = Restaurant(name="kaguto")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="ksh 400", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken and Rice", description="Chicken... and rice",
                     price="ksh 495", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="ksh 695", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="ksh 395", course="Dessert", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Tonkomo", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     price="ksh 795", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for Andala's
restaurant1 = Restaurant(name="Andala")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="ksh 995", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="ksh 795", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="ksh 650", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="ksh 675", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="ksh 700", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Auntie Ann's
restaurant1 = Restaurant(name="Auntie Diner' ")

session.add(restaurant1)
session.commit()

menuItem9 = MenuItem(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                     price="ksh 899", course="Entree", restaurant=restaurant1)

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     price="ksh 299", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="ksh 1095", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
                     price="ksh 750", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     price="ksh 895", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="ksh 950", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="ksh 199", course="Dessert", restaurant=restaurant1)

session.add(menuItem10)
session.commit()


# Menu for Cocina Y Amor
restaurant1 = Restaurant(name="Cocina Y Amor ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                     price="ksh 595", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="ksh 799", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


restaurant1 = Restaurant(name="State Bird Provisions")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     price="ksh 595", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit

menuItem1 = MenuItem(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
                     price="ksh 695", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                     price="ksh 425", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


print ("added menu items!")