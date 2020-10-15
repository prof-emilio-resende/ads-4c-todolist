from domain.model.Pendencia import Pendencia
import pytest

def test_pendencia():
    #arrange
    # nome = "PendenciaEsperada"
    # status = "pendente"
    # # act
    # pend = Pendencia(nome, status)
    # # assert 
    # assert pend.name == nome
    # assert pend.status == status
    # assert type(pend.name) == str

    with pytest.raises(DadosMinimosException):
        pend = Pendencia()
        if not pent.name and not pend.status:
            raise Excpetion()
    
