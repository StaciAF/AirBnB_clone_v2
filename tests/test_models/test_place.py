#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        dct = {'number_rooms': 0, 'number_bathrooms': 5,
               'description': 'None', 'max_guest': 1,
               'price_by_night': 80, 'latitude': 1.1, 'longitude': 2.2,
               'name': 'TestPlace'}
        state = State(**{'name': 'Teststate'})
        city = City(**{'name': 'TestCity', 'state_id': state.id})
        user = User(**{'email': 'examplemail', 'password': 'test_pwd',
                       'first_name': 'John', 'last_name': 'Smith'})
        dct.update({'city_id': city.id, 'user_id': user.id})
        self.args = dct

    def test_city_id(self):
        """ """
        new = self.value(**self.args)
        print("BUGCHECK")
        print("CITY:", hasattr(new, 'city_id'), getattr(new, 'city_id'), type(getattr(new, 'city_id')))
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.amenity_ids), list)
