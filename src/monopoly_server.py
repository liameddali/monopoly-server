import os
from flask import Flask, request, redirect, render_template, url_for, flash, make_response, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_socketio import SocketIO, emit
import random
import string

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'monopoly-server.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

socketio = SocketIO(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    game_in_progress = db.Column(db.Boolean, default=False)
    current_game_id = db.Column(db.String(5))
    balance = db.Column(db.Integer, default=2000, nullable=False)
    user_cookie = db.Column(db.String(5))

    def __repr__(self):
        return f"<User {self.id} {self.username} {self.password} {self.game_in_progress} {self.current_game_id} {self.balance}>"

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    level = db.Column(db.Integer, default=0, nullable=False)
    game_id = db.Column(db.String(5), nullable=False)
    image_filename = db.Column(db.String(100), nullable=False)  # New column for image filename

    def __repr__(self):
        return f"<Property {self.name} Owner: {self.owner_id} Level: {self.level} Image: {self.image_filename}>"

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    user_cookie = request.cookies.get('user_cookie')
    user = User.query.filter_by(user_cookie=user_cookie).first()

    if user:
        return redirect('/active-user')
    else:
        resp = make_response(redirect('/log-in'))
        resp.set_cookie('user_cookie', '', expires=0)
        return resp

@app.route('/active-user')
def active_user():
    user_cookie = request.cookies.get('user_cookie')
    user = User.query.filter_by(user_cookie=user_cookie).first()
    username = user.username
    gip = user.game_in_progress
    return render_template('active-user.html', username=username, game_in_progress=gip)

@app.route('/create-a-game', methods=['POST', 'GET'])
def create_a_game():
    user_cookie = request.cookies.get('user_cookie')
    user = User.query.filter_by(user_cookie=user_cookie).first()
    username = user.username
    new_game_id = ''
    while new_game_id == '':
        new_game_id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        test_user = User.query.filter_by(current_game_id=new_game_id).first()
        if test_user:
            new_game_id = ''

    if request.method == 'POST':
        new_game_id = request.form.get('new_game_id')
        if user.game_in_progress == 0:
            user.current_game_id = new_game_id
            user.game_in_progress = 1
            db.session.commit()
        else:
            user.current_game_id = new_game_id
            user.balance = 2000
            db.session.commit()

        # Create properties for the new game
        properties_data = [
            {"name": "Mediterranean Avenue", "image": "mediterranean_avenue.svg"},
            {"name": "Baltic Avenue", "image": "baltic_avenue.svg"},
            {"name": "Oriental Avenue", "image": "oriental_avenue.svg"},
            {"name": "Vermont Avenue", "image": "vermont_avenue.svg"},
            {"name": "Connecticut Avenue", "image": "connecticut_avenue.svg"},
            {"name": "St. Charles Place", "image": "st_charles_place.svg"},
            {"name": "States Avenue", "image": "states_avenue.svg"},
            {"name": "Virginia Avenue", "image": "virginia_avenue.svg"},
            {"name": "St. James Place", "image": "st_james_place.svg"},
            {"name": "Tennessee Avenue", "image": "tennessee_avenue.svg"},
            {"name": "New York Avenue", "image": "new_york_avenue.svg"},
            {"name": "Kentucky Avenue", "image": "kentucky_avenue.svg"},
            {"name": "Indiana Avenue", "image": "indiana_avenue.svg"},
            {"name": "Illinois Avenue", "image": "illinois_avenue.svg"},
            {"name": "Atlantic Avenue", "image": "atlantic_avenue.svg"},
            {"name": "Ventnor Avenue", "image": "ventnor_avenue.svg"},
            {"name": "Marvin Gardens", "image": "marvin_gardens.svg"},
            {"name": "Pacific Avenue", "image": "pacific_avenue.svg"},
            {"name": "North Carolina Avenue", "image": "north_carolina_avenue.svg"},
            {"name": "Pennsylvania Avenue", "image": "pennsylvania_avenue.svg"},
            {"name": "Park Place", "image": "blue_1.svg"},
            {"name": "Boardwalk", "image": "boardwalk.svg"}
        ]

        for property_data in properties_data:
            new_property = Property(
                name=property_data["name"],
                game_id=new_game_id,
                image_filename=property_data["image"]
            )
            db.session.add(new_property)
        db.session.commit()

        flash(f'You created the game {new_game_id} and joined it! Properties have been initialized.', 'info')
        return redirect('/dashboard-wallet')

    return render_template('create-a-game.html', username=username, new_game_id=new_game_id)

@app.route('/create-or-join-a-game')
def create_or_join_a_game():
    user_cookie = request.cookies.get('user_cookie')
    user = User.query.filter_by(user_cookie=user_cookie).first()
    username = user.username
    return render_template('create-or-join-a-game.html', username=username)

@app.route('/current-or-new-game')
def current_or_new_game():
    user_cookie = request.cookies.get('user_cookie')
    user = User.query.filter_by(user_cookie=user_cookie).first()
    username = user.username
    idgame = user.current_game_id
    return render_template('current-or-new-game.html', username=username, game_id=idgame)

@app.route('/dashboard-account')
def dashboard_account():
    user_cookie = request.cookies.get('user_cookie')
    user = User.query.filter_by(user_cookie=user_cookie).first()
    username = user.username
    idgame = user.current_game_id
    return render_template('dashboard-account.html', username=username, game_id=idgame)

@app.route('/dashboard-properties')
def dashboard_properties():
    user_cookie = request.cookies.get('user_cookie')
    user = User.query.filter_by(user_cookie=user_cookie).first()
    username = user.username
    idgame = user.current_game_id

    # Assuming you have a Property model with fields: name, owner_id, level, and game_id
    properties_query = Property.query.filter_by(game_id=idgame).all()
    properties = {
        prop.name: {
            'owner': User.query.get(prop.owner_id).username if prop.owner_id else 'Bank',
            'level': prop.level,
            'image': prop.image_filename
        }
        for prop in properties_query
    }

    print(properties)
    if not properties:
        flash(f'No properties found for this game. {properties} ', 'info')

    return render_template('dashboard-properties.html', username=username, game_id=idgame, properties=properties)

@app.route('/dashboard-wallet', methods=['GET', 'POST'])
def dashboard_wallet():
    user_cookie = request.cookies.get('user_cookie')
    user = User.query.filter_by(user_cookie=user_cookie).first()
    username = user.username

    if user is None:
        return redirect(url_for('login'))

    idgame = user.current_game_id
    balance = user.balance

    potential_player = User.query.filter_by(current_game_id=idgame).all()
    potential_player = [u for u in potential_player if u.username != username]

    redirect_target = request.args.get('redirect')
    
    if request.method == 'POST':
        if redirect_target == 'send':
            amount_send = request.form.get('amount_send')
            recipient = request.form.get('recipient_username')
            recipient = User.query.filter_by(username=recipient).first()
            if recipient is None and not amount_send:
                flash('Fields are empty!', 'error')
            else:
                if recipient is None:
                    flash('Select a recipient!', 'error')
                else:
                    if not amount_send:
                        flash('Select an amount!', 'error')
                    else:
                        amount_send = int(amount_send)
                        if balance < amount_send:
                            flash('Not enough money to do this!', 'warning')
                        elif amount_send < 0:
                            flash('The amount must be greater than 0!', 'error')
                        else:
                            recipient.balance += amount_send
                            user.balance -= amount_send
                            db.session.commit()
                            flash(f'You sent {amount_send} $ to {recipient.username}.', 'success')

            return redirect ('/dashboard-wallet')
                
        elif redirect_target == 'ask':
            amount_asked = request.form.get('amount_asked')
            giver = request.form.get('giver_username')
            giver = User.query.filter_by(username=giver).first()
            if giver is None and not amount_asked:
                flash('Fields are empty!', 'error')
            else:
                if giver is None:
                    flash('Select a giver!', 'error')
                else:
                    if not amount_asked:
                        flash('Select an amount!', 'error')
                    else:
                        amount_asked = int(amount_asked)
                        flash(f'You asked {amount_asked} $ to {giver.username}.', 'success')
                        
            return redirect ('/dashboard-wallet')
        
    return render_template('dashboard-wallet.html', username=username, game_id=idgame, balance=user.balance, players=potential_player)

@app.route('/join-a-game', methods=['GET', 'POST'])
def join_a_game():
    user_cookie = request.cookies.get('user_cookie')
    user = User.query.filter_by(user_cookie=user_cookie).first()
    username = user.username
    if request.method == 'POST':
        asked_game_id = request.form.get('game_id')
        test_user = User.query.filter_by(current_game_id=asked_game_id).first()
        if test_user:
            if user.game_in_progress == 0:
                user.current_game_id = asked_game_id
                user.game_in_progress = 1
                db.session.commit()
            else:
                user.current_game_id = asked_game_id
                user.balance = 2000
                db.session.commit()
            flash(f'You joined the game {asked_game_id} !', 'info')
            return redirect ('/dashboard-wallet')
        else:
            flash('The game ID you entered does not exist! It normally contains five characters.')
            

    return render_template('join-a-game.html', username=username)

@app.route('/log-in', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('passwd')
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            flash('Logged in successfully!', 'success')
            gip = user.game_in_progress

            if gip == 0:
                resp = make_response(redirect('/create-or-join-a-game'))
            else:
                resp = make_response(redirect('/current-or-new-game'))
            user_cookie = user.user_cookie
            resp.set_cookie('user_cookie', user_cookie)
            return resp
        else:
            if not username and not password:
                flash('Fields are empty!', 'warning')
            elif not username or not password:
                if not username:
                    flash('Username field is empty!', 'warning')
                if not password:
                    flash('Password field is empty!', 'warning')
            else:
                flash('Invalid credentials, please try again.', 'error')
            
    return render_template('log-in.html')

@app.route('/log-out')
def logout():
    redirect_target = request.args.get('redirect', 'login')

    if redirect_target == 'register':
        redirect_url = '/sign-up'
    else:
        redirect_url = '/log-in'

    resp = make_response(redirect(redirect_url))
    resp.set_cookie('user_cookie', '', expires=0)
    flash('You have been logged out.', 'success')
    return resp

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password1 = request.form['passwd1']
        password2 = request.form['passwd2']

        if not username and not password1 and not password2:
            flash('Fields are empty!', 'warning')
        else:
            if not username or not password1 or not password2:
                if not username:
                    flash('Username field is empty!', 'warning')
                if not password1 and not password2:
                    flash('Password fields are empty!', 'warning')
                else:
                    if not password1:
                        flash('First password field is empty!', 'warning')
                    if not password2:
                        flash('Second password field is empty!', 'warning')
            else:
                user = User.query.filter_by(username=username).first()
                if user:
                    flash('Username already exists. Please choose a different one.', 'warning')
                else:
                    if password1 == password2:
                        hashed_password = generate_password_hash(password1, method='pbkdf2:sha256')
                        user_cookie = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                        new_user = User(username=username, password=hashed_password, user_cookie=user_cookie)
                        db.session.add(new_user)
                        db.session.commit()
                        flash('Registration successful! Please login.', 'success')
                        return redirect('/log-in')
                    else:
                        flash('The two passwords do not match!', 'warning')
    return render_template('sign-up.html')

# Événement lorsque le client envoie de l'argent
@socketio.on('send_money')
def handle_send_money(data):
    # Émettre l'événement send_money_transaction à tous les clients
    socketio.emit('send_money_transaction', data)

# Événement lorsque le client demande de l'argent
@socketio.on('ask_money')
def handle_ask_money(data):
    # Émettre l'événement ask_money_transaction à tous les clients
    socketio.emit('ask_money_transaction', data)

# Événement lorsque le client rejoin une partie
@socketio.on('player_join_game')
def handle_player_join_game(data):
    # Émettre l'événement player_join_game à tous les clients
    socketio.emit('player_join_game', data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)