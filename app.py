from flask import Flask,render_template,url_for,redirect,request,jsonify,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, MenuItem

##### Database Engine #####
engine = create_engine('postgresql://evans:evans123@localhost:5432/rest')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


##### Initialize Flask Application #####
app = Flask(__name__)


##### Web Application Page Handlers #####
@app.route('/')
@app.route('/restaurant/')
def show_restaurants():
    restaurants = session.query(Restaurant).order_by(Restaurant.name)
    return render_template('restaurants.html', restaurants=restaurants)


@app.route('/restaurant/new/', methods=['GET', 'POST'])
def new_restaurant():
    if request.method == 'POST':
        new_restaurant = Restaurant(name=request.form['restaurant-name'])
        session.add(new_restaurant)
        session.commit()
        flash("New restaurant created")
        return redirect(url_for('show_restaurants'))
    else:
        return render_template('newrestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
    edit_restaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).first()
    if request.method == 'POST':
        if request.form['restaurant-name']:
            edit_restaurant.name = request.form['restaurant-name']
        session.add(edit_restaurant)
        session.commit()
        flash("Restaurant successfully edited")
        return redirect(url_for('show_restaurants'))
    else:
        return render_template('editrestaurant.html',edit_restaurant=edit_restaurant)


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def delete_restaurant(restaurant_id):
    del_restaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).first()
    if request.method == 'POST':
        session.delete(del_restaurant)
        session.commit()
        flash("Restaurant successfully deleted")
        return redirect(url_for('show_restaurants'))
    else:
        return render_template('deleterestaurant.html',del_restaurant=del_restaurant)


# @app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def show_menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menu.html',items=items,restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/new/',
           methods=['GET', 'POST'])
def new_menu_item(restaurant_id):
    if request.method == 'POST':
        new_item = MenuItem(name=request.form['item-name'],description=request.form['description'],price=request.form['price'],restaurant_id=restaurant_id)
        session.add(new_item)
        session.commit()
        flash("New menu item created")
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/',
           methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_id):
    edit_item = session.query(MenuItem).filter_by(id=menu_id).first()
    if request.method == 'POST':
        edit_item.name = request.form['item-name']
        edit_item.description = request.form['description']
        edit_item.price = request.form['price']
        session.add(edit_item)
        session.commit()
        flash("Menu item successfully edited")
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html',
                               restaurant_id=restaurant_id,
                               edit_item=edit_item)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/',
           methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_id):
    del_item = session.query(MenuItem).filter_by(id=menu_id).first()
    if request.method == 'POST':
        session.delete(del_item)
        session.commit()
        flash("Menu item successfully deleted")
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', del_item=del_item)


##### API Endpoints #####
@app.route('/restaurant/JSON/')
def restaurant_list_json():
    restaurants = session.query(Restaurant).order_by(Restaurant.name)
    return jsonify(restaurants=[i.serialize for i in restaurants])


@app.route('/restaurant/<int:restaurant_id>/JSON/')
@app.route('/restaurant/<int:restaurant_id>/menu/JSON/')
def restaurant_menu_json(restaurant_id):
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(menu_items=[i.serialize for i in items])


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def menu_item_json(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id=menu_id).first()
    return jsonify(menu_item=[item.serialize])


##### Test Environment #####
if __name__ == '__main__':
    app.secret_key = 'secret_key_test'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
