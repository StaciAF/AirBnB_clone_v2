#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
import MySQLdb
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != "db", "Storage must be DB")
class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        pass

    def tearDown(self):
        """ Close connection at end of tests """
        try:
            self.curs.close()
            self.conc.close()
        except Exception:
            pass

    def test_aaa_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_aab_new(self):
        """ New object is correctly added to storage """
        new = State(**{'name': "Oklahoma"})
        storage.new(new)
        storage.save()
        self.assertTrue(new in storage.all().values())

    def test_aac_all(self):
        """ storage is properly returned """
        new = State(name="tmp")
        storage.new(new)
        storage.save()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    '''def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        storage.new(new)
        storage.save()
        storage.reload()
        _id = new.to_dict()['id']
        print("KEYS: ", storage.all())
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)'''
