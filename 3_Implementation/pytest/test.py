from test_main import *

def test_addsongs():
    assert addsongs() == SUCCESS

def test_deletesongs():
    assert deletesong() == SUCCESS

def test_play():
    assert Play() == SUCCESS

def test_pause():
    assert Pause() == SUCCESS

def test_stop():
    assert Stop() == SUCCESS

def test_resume():
    assert Resume() == SUCCESS

def test_previous():
    assert Previous() == SUCCESS

def test_next():
    assert Next() == SUCCESS

def test_player():
    assert player() == SUCCESS

def test_login():
    assert login_page() == SUCCESS

def test_signup():
    assert signUpPage() == SUCCESS

def test_start():
    assert start() == SUCCESS
