import flask
from database.methods import *
from sqlalchemy.orm import Session


app = flask.Flask(__name__)

blueprint = flask.Blueprint(
    'api',
    __name__,
    url_prefix='/api/v1')


# path for getting all users
@blueprint.route('/users', methods=['GET'])
def get_users():
    """ Get all users from the database. """
    return flask.jsonify(get_all_users())
    


# path for getting a user by id
@blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user_id(user_id):
    """ Get a user from the database by id. """
    pass


# path for showing layout by id
@blueprint.route('/layouts/<int:layout_id>', methods=['GET'])
def get_layout_id(layout_id):
    """ Get a layout from the database by id. """
    pass


# path for saving a layout
@blueprint.route('/layouts', methods=['POST'])
def save_layout():
    """ Save a layout to the database. """
    pass


# path for showing the path between two points
@blueprint.route('/showpath', methods=['GET','POST'])
def show_path():
    """ Show the shortest path between two points. """
    data = flask.request.get_json()
    pass

# path for showing all pois
@blueprint.route('/pois', methods=['GET'])
def get_pois():
    """ Get all pois from the database. """
    return flask.jsonify(get_all_pois())