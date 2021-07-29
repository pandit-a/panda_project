from panda_project.lib import try_me

def test_try():
    ##assert len(hello_world()) != 0
    assert type(try_me("bullet")) == str
