from random import randint
from time import sleep


class Loteria:
    """
    A class used to represent a Lottery game.
    ...
    Attributes
    ----------
    jogos : list
        a list to store the numbers of a single lottery game
    jogos2 : list
        a list to store all the generated lottery games
    precos : dict
        a dictionary to store the price of the lottery games based on the number of chosen numbers
    Methods
    -------
    sortear_jogos(quant, num_numeros)
        Draws a specified number of lottery games, each containing a specified number of numbers.
    calcular_valor_aposta(num_numeros, quant)
        Calculates the total bet amount based on the number of chosen numbers and the number of bets.
    executar()
        Executes the lottery game by prompting the user for the number of games and the number of numbers per game.
    """

    def __init__(self):
        self.jogos = []
        self.jogos2 = []
        self.precos = {
            6: 5,
            7: 35,
            8: 140,
            9: 420,
            10: 1050,
            11: 2310,
            12: 4620,
            13: 8580,
            14: 15015,
            15: 25025,
            16: 40040,
            17: 61880,
            18: 92820,
            19: 135660,
            20: 193800,
        }

    def sortear_jogos(self, quant, num_numeros):
        """
        Sorteia uma quantidade especificada de jogos de loteria, cada um contendo um número especificado de números.

        Args:
            quant (int): A quantidade de jogos a serem sorteados.
            num_numeros (int): O número de números em cada jogo.

        Returns:
            None

        This method prints the sorted lottery games and appends them to the jogos2 list.
        """
        print(f'{" SORTEANDO JOGOS ":=^40}')
        for c in range(quant):
            for i in range(num_numeros):
                while True:
                    num = randint(1, 60)
                    if num not in self.jogos:
                        self.jogos.append(num)
                        break
            self.jogos.sort()
            self.jogos2.append(self.jogos[:])
            self.jogos.clear()
        for i, j in enumerate(self.jogos2):
            print(f"Jogo {i+1}: {j}")
            sleep(0.1)
        print(f'{" BOA SORTE! ":=^40}')

    def calcular_valor_aposta(self, num_numeros, quant):
        """
        Calcula o valor total da aposta com base no número de números escolhidos e na quantidade de apostas.

        Args:
            num_numeros (int): O número de números escolhidos na aposta.
            quant (int): A quantidade de apostas.

        Returns:
            None: Esta função imprime o valor total da aposta ou uma mensagem de erro se o número de apostas for inválido.
        """
        if num_numeros in self.precos:
            valor_total = self.precos[num_numeros] * quant
            print(f"O valor total da aposta é: R$ {valor_total:.2f}")
        else:
            print("Número de apostas inválido.")

    def executar(self):
        """
        Executes the lottery game by prompting the user for the number of games and the number of numbers per game.
        The method performs the following steps:
        1. Prints the game header.
        2. Prompts the user to input the number of games they want to play.
        3. Prompts the user to input the number of numbers per game (between 6 and 20).
        4. Validates the input for the number of numbers per game and prompts again if the input is invalid.
        5. Calls the method to draw the games with the specified parameters.
        6. Calls the method to calculate the total bet amount based on the number of numbers per game and the number of games.
        """
        print("-" * 30)
        print("      JOGO DA LOTERIA")
        print("-" * 30)

        quant = int(input("Quantos jogos você quer fazer? "))
        num_numeros = int(input("Você quer jogos de quantos números (6 a 20)? "))

        while num_numeros < 6 or num_numeros > 20:
            print("Escolha inválida! Por favor, escolha um número entre 6 e 20.")
            num_numeros = int(input("Você quer jogos de quantos números (6 a 20)? "))

        self.sortear_jogos(quant, num_numeros)
        self.calcular_valor_aposta(num_numeros, quant)


if __name__ == "__main__":
    loteria = Loteria()
    loteria.executar()
