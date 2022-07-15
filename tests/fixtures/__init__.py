import pytest


@pytest.fixture
def criar_jogo():
    from app.bo.bo_jogo import Jogo

    return Jogo()
