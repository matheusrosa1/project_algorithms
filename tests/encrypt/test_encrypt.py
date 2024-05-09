import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Hello", "invalid_key")

    # Testa com mensagem inválida
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(12345, 2)

    assert encrypt_message("XABLAU", 2) == "UALB_AX"
    assert encrypt_message("Hello", 10) == "olleH"
    assert encrypt_message("Hello", 4) == "o_lleH"
    assert encrypt_message("Hello", 3) == "leH_ol"
