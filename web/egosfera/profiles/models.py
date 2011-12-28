from google.appengine.ext import db

EMAIL_NETWORK = "EMAIL"
PHONE_NETWORK = "PHONE"
TWITTER_NETWORK = "TWITTER"
FACEBOOK_NETWORK = "FACEBOOK"

class Identity(db.Model):
    identity = db.StringProperty()
    network = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)

class User(db.Model):
    display_name = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)

class UserIdentity(Identity):
    user = db.ReferenceProperty(User)
    confirmed = db.BooleanProperty()

class Card(db.Model):
    user = db.ReferenceProperty(User)
    confirmed = db.BooleanProperty()

class CardIdentity(db.Model)
    user = db.ReferenceProperty(User)
    identity = db.ReferenceProperty(UserIdentity)
