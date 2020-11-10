from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:

    try:
        dificuldade: int = int(input('Informe o nível de dificuldade desejado [1:default, 2, 3 ou 4]: '))
    except ValueError:
        dificuldade: int = 1

    if (dificuldade < 1) or (dificuldade > 4):
        dificuldade: int = 1

    calc: Calcular = Calcular(dificuldade)
    calc.mostrar_operacao()

    try:
        resultado: int = int(input())
    except ValueError:
        resultado: int = 0

    if calc.checar_resulado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    try:
        continuar: int = int(input('Deseja continuar o jogo? [1 - sim:default, 0 - não] '))
    except ValueError:
        continuar: int = 1

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
