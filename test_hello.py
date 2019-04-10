import hello

def test_says_world():
    assert hello.say_what() == 'world'

if __name__ == "__main__":
    test_says_world()
