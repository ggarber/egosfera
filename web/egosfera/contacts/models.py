from google.appengine.ext import db

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

class Contact(db.Model):
    user = db.ReferenceProperty(User)
    display_name = db.StringProperty()

class ContactIdentity(Identity):
    contact = db.ReferenceProperty(Contact)

