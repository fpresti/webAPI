from flask import Blueprint, request, session

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.post('/login')
def login():
    #get data from request.
    try :
        data = request.get_json()
        nombre = data.get("name")
        session['name'] = nombre    
        return f"Session: {session.get('name')}"
    except Exception as ex:
        return f"Error: {ex}"

@user_bp.get('/getsession')
def get_session():    
    try : 
        return f"Session: {session.get('name')}"
    except Exception as ex :
        return f"Error: {ex}"
    
@user_bp.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('name', None)    
    try :

        if session.get('name') is None :
            print('Session is None!')
        
        #another way of knowing if the session is None
        if not 'name' in session :
            print('Session is None!')

        return f"Session: {session.get('name')}"
    except Exception as ex :
        return f"Error: {ex}"