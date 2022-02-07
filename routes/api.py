import flask
from database.methods import *
from sqlalchemy.orm import Session
from flask import jsonify, request


app = flask.Flask(__name__)

blueprint = flask.Blueprint(
    'api',
    __name__,
    url_prefix='/api/v1')


layout = [ 
    {
        'name': 'floor1',
        'pois': [
            {
                'name': 'Office1',
                'node_id': 1
            },
            {
                'name': 'Office2',
                'node_id': 2
            },
            {
                'name': 'Office3',
                'node_id': 3
            },
            {
                'name': 'Office4',
                'node_id': 4
            },
            {
                'name': 'Office5',
                'node_id': 5
            },
            {
                'name': 'Office6',
                'node_id': 6
            }
        ]
    }
    
    
]


# path for getting all users
@blueprint.route('/users', methods=['GET'])
def get_users():
    """ Get all users from the database. """
    pass
    


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
    start = request.args.get(int, None)
    end = request.args.get(int, None)
    return shortest_path(start, end)


# path for showing all pois
@blueprint.route('/pois', methods=['GET'])
def get_pois():
    """ Get all pois from the database. """
    return jsonify(layout)