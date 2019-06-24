import pytest
import monkeypatch
import mysql.connector
from helper_functions import handle_send_nano, add_history_record

class Message:
    pass


messages = [
    'great idea! !ntip 1',
    'great idea!\n !ntip 1',
    '!ntip 1 Great idea!',
    '!ntip 1USD great idea!',
    '/u/nano_tipper 1 great idea!\nGood call!',
    'u/nano_tipper 1 great idea!',
    '!nanocenter 1 tipbot awesome!',
    'awesome! \n!nanocenter 1 tipbot'
]

def send_nano():
    pass

def test_send_nano():
    def mock_history_record(*args, **kwargs):
        return 0

    def mock_mycursor_execute(*args, **kwargs):
        if True:
            return None
        else:
            return None

    def mock_commit(*args, **kwargs):
        return None


    monkeypatch.setattr('add_history_record', mock_history_record)
    monkeypatch.setattr(mycursor, 'add_history_record', mock_history_record)
    monkeypatch.setattr('add_history_record', mock_history_record)
