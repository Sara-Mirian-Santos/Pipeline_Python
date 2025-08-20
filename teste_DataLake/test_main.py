from main import saudacao


def test_saudacao():
    assert saudacao("Jenkins") == "Olá, Jenkins!"
