from domain.model.Pendencia import Pendencia

def test_pendencia():
    #arrange
    nome = "PendenciaEsperada"
    status = "pendente"
    # act
    pend = Pendencia(nome, status)
    # assert 
    assert pend.name == nome
    assert pend.status == status
    assert type(pend.name) == str
    
