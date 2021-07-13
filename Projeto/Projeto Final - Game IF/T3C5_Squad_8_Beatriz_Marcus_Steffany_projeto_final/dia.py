from asciis import Asciis

class Dia:
    def dia_bom_ruim(condicao_tempo):
        import time
        print()
        if condicao_tempo == '1':
            Asciis.diabom()
            print()
            string1 = ("Está um lindo dia de primavera, agradável, um céu sem nuvens.... perfeito para uma aventura... ")
            for ch in string1:
                time.sleep(0.1) 
                print(ch, end='', flush=True) 
        elif condicao_tempo == '2':
            Asciis.diafrio()
            print()
            string2 = ("É um dia chuvoso de início de inverno, está frio e nublado.... nada melhor que uma aventura para nos aquecer... " )
            for ch in string2:
                time.sleep(0.1) 
                print(ch, end='', flush=True)
        print()