#!/usr/bin/python3
'''Defines a new engine using a sql db'''


class DBStorage:
    '''Contains the methods used in this engine'''
    __engine = None
    __session = None

    def __init__(self):
        '''Initializes the engine'''
        from sqlalchemy import create_engine
        from os import getenv
        user = getenv('HBNB_MYSQL_USER')
        pw = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://' + user + ':' + pw +
                                      '@' + host + ':3306/' + db,
                                      pool_pre_ping=True)
        conc = self.__engine.connect()
        if getenv('HBNB_ENV') == 'test':
            from models.base_model import Base
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        '''query on the current database session all objects depending
        on the class name'''
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place
        from models.user import User
        import console
        classes = {"Amenity": Amenity, "City": City,
                   "Place": Place, "Review": Review,
                   "State": State, "User": User}
        all_dict = {}
        for each in classes:
            if cls is None or cls == each:
                objects = self.__session.query(classes[each]).all()
                for obj in objects:
                    new_key = obj.__class__.__name__ + '.' + obj.id
                    all_dict[key] = obj
        return (all_dict)

    def new(self, obj):
        '''Adds an object to the database'''
        self.__session.add(obj)
        self.save()
        self.reload()

    def save(self):
        '''commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from the current database session obj if not None'''
        if obj is None:
            return
        self.__session.delete(obj)
        self.save()

    def reload(self):
        '''create all tables in the database'''
        from sqlalchemy.orm import scoped_session
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy import MetaData
        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ public method to close class Session """
        self.__session.close()
