from .db import *
from .models import *

def get_all_users() -> User:
    """
    Get all users from the database.
       
    RETURNS:
        The user object.
    """
    return session.query(User).all()
    
    

def get_user_by_id(user_id: int) -> User:
    """
    Get a user from the database by id.
    
    ARGS:
        user_id: The id of the user.
    
    RETURNS:
        The user object basedd on the id.
    """
    return session.query(User).filter_by(id=user_id).first()


def get_layout_by_id(layout_id: int) -> Layout:
    """
    Get a layout from the database by id.
    
    ARGS:
        layout_id: The id of the layout.
        
    RETURNS:
        The layout object basedd on the id.
    """
    return session.query(Layout).filter_by(id=layout_id).first()


def save_layout(layout: Layout) -> Layout:
    """
    Save a layout to the database.
    
    ARGS:
        layout: The layout object to save.
    
    RETURNS:
        The layout object.
    """
    layout = Layout(
        
    )
      
        
    
    session.add(layout)
    session.commit()
    return layout


def shortest_path(start: str, end: str) -> Path:
    """
    Show the shortest path between two points.
    
    ARGS:
        start: The start point.
        end: The end point.
    
    RETURNS:
        The shortest path between two points.
    """
    path = session.query(Path).filter_by(start=start, end=end).first()
    return path

def get_all_pois() -> Poi:
    """
    Get all pois from the database.
    
    RETURNS:
        The poi.
    """
    return session.query(Poi).all()
    