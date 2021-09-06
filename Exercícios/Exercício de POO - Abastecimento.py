# a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
  # I. tipoCombustivel.
  # II. valorLitro.
  # III. quantidadeCombustivel.
# b. A classe deve possuir no mínimo esses métodos:
  # I. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
  # foi colocada no veículo.
  # II. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
  # a ser pago pelo cliente.
  # III. alterarValor( ) – altera o valor do litro do combustível.
  # IV. alterarCombustivel( ) – altera o tipo do combustível.
  # V. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel:
    def __init__(self, TipoDeCombustivel, ValorDoLitro, QuantidadeDeCombustivel):
        self.TipoDeCombustivel = TipoDeCombustivel
        self.ValorDoLitro = ValorDoLitro
        self.QuantidadeDeCombustivel = QuantidadeDeCombustivel
    

    def abastecePorValor(self, valorabastecer):
        self.valorDoAbastecimento = 0
        valorabastecer = float(input("Informe o valor do abastecimento: R$" ).replace(",",".").strip())
   
    def abastecerPorLitro(self, litros):
        self.litrosAbastecidos = 0

    def alterarValor(self, valorlitro):
        self.novoValorDoLitro = 0        

    def alterarCombustivel(self, tipo):
        self.novoTipoCombustivel = 0

    def alterarQuantidadeCombustivel(self, quantidade):
        self.novaQuantidadeCombustivel = 0          

valorGasolina = 6.20
valorEtanol = 4.60
tipo1 = "Gasolina"
tipo2 = "Etanol"
