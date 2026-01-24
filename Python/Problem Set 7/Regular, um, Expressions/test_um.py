from um import count

def test_count():
    assert count("um") == 1
    assert count("um, hello, um, world") == 2
    assert count("Um, thanks for the album.") == 1

def test_case_insensitivity():
    assert count("UM, thanks, um...") == 2

def test_whole_word():
    assert count("yummy") == 0
    assert count("instrumentation") == 0
