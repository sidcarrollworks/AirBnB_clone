#!/usr/bin/python3
'''
    Unique instance of filestorage
'''
from models.engine.file_storage import FileStorage



storage = FileStorage()
storage.reload()
