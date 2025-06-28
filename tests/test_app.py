from src.app import hello_world


def test_hello_world_default():
    assert hello_world() == "Hello, World!"


def test_hello_world_custom():
    assert hello_world("Jithin") == "Hello, Jithin!"


def test_hello_world_with_fixture(sample_name):
    assert hello_world(sample_name) == "Hello, OpenAI!"
