import os

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from database_setup import User

engine = create_engine('postgresql://localhost/test')

Session = sessionmaker(bind=engine)

session = Session()

user = session.query(User).filter_by(username='admin').first()

if user.is_moderator:

return True

else:

return False
