import pytest 
from exception.DadosMinimosExcpetion import DadosMinimosExcepetion


def test_estrutura_pendencia():
      

  # arrange
  name = "Teste Pendencia"
  status = "Pendente"

  # act
  from domain.model import Pendencia
  pend = Pendencia(name, status)
  
  # assert
  assert pend.name == name
  assert pend.status == status

  try:
    pend = Pendencia()
  except:
    DadosMinimosExcepetion("Objeto instanciado sem parametros")
