from main import Calculadora

def test_multiplicacao_simples():
    """
    Teste Unitário: Verifica se a operação complexa 
    está realmente multiplicando os valores.
    """
    calc = Calculadora()
    
    # CENÁRIO: 5 * 2 deve ser 10. 
    # Como o código atual faz 5 + 2, este teste vai falhar com 7 != 10.
    resultado = calc.operacao_complexa(5, 2)
    
    assert resultado == 10, f"Erro no cálculo: esperado 10, mas obteve {resultado}"

def test_multiplicacao_por_zero():
    calc = Calculadora()
    assert calc.operacao_complexa(10, 0) == 0