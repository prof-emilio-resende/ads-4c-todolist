def test_estrutura_pendencia():
  # arrange
  nome = "Teste Pendencia"
  status = "Pendente"

  # act
  from domain.model import Pendencia
  pend = Pendencia(nome, status)
  
  # assert
  assert pend.nome == nome
  assert pend.status == status