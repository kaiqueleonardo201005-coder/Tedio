import itertools
import time
import os

ARQUIVO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "01_Site_Senha",
    "senha_teste.txt"
)

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print("╔══════════════════════════════════════╗")
    print("║          PASSWORD CRACKER V2         ║")
    print("╠══════════════════════════════════════╣")
    print("║          LABORATÓRIO LOCAL           ║")
    print("╚══════════════════════════════════════╝")
    print()

def escolher_caracteres():
    print("CONJUNTO DE CARACTERES")
    print()
    print("[1] Apenas números")
    print("[2] Apenas letras minúsculas")
    print("[3] Letras + números")
    print("[4] Personalizado")
    print()

    escolha = input("Escolha: ")

    if escolha == "1":
        return "0123456789"

    if escolha == "2":
        return "abcdefghijklmnopqrstuvwxyz"

    if escolha == "3":
        return "abcdefghijklmnopqrstuvwxyz0123456789"

    if escolha == "4":
        caracteres = input("Digite os caracteres: ")

        if caracteres:
            return caracteres

    print("Opção inválida.")
    return None

def ler_tamanho():
    while True:
        try:
            tamanho = int(input("Tamanho máximo da senha (1-6): "))

            if 1 <= tamanho <= 6:
                return tamanho

        except ValueError:
            pass

        print("Digite um número entre 1 e 6.")

def carregar_senha():
    if not os.path.exists(ARQUIVO):
        return None

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return arquivo.read().strip()

def quebrar(senha, caracteres, tamanho_maximo):

    tentativas = 0
    inicio = time.perf_counter()

    for tamanho in range(1, tamanho_maximo + 1):

        total = len(caracteres) ** tamanho

        for combinacao in itertools.product(
            caracteres,
            repeat=tamanho
        ):

            tentativa = "".join(combinacao)
            tentativas += 1

            if tentativa == senha:

                tempo = time.perf_counter() - inicio

                if tempo <= 0:
                    tempo = 0.000001

                velocidade = tentativas / tempo

                limpar()

                print("╔══════════════════════════════════════╗")
                print("║        PASSWORD ENCONTRADA!          ║")
                print("╠══════════════════════════════════════╣")
                print(f"║ Senha: {tentativa:<29}║")
                print(f"║ Tentativas: {tentativas:<24}║")
                print(f"║ Velocidade: {velocidade:,.0f}/s")
                print(f"║ Tempo: {tempo:.2f}s")
                print("╚══════════════════════════════════════╝")

                return

            tempo = time.perf_counter() - inicio

            if tempo <= 0:
                tempo = 0.000001

            velocidade = tentativas / tempo

            print(
                f"\rTentativas: {tentativas:,} | "
                f"{velocidade:,.0f}/s | "
                f"Tempo: {tempo:.2f}s | "
                f"Tentando: {tentativa}",
                end="",
                flush=True
            )

    print()
    print()
    print("SENHA NÃO ENCONTRADA.")

def main():

    limpar()
    banner()

    senha = carregar_senha()

    if senha is None:
        print("Nenhuma senha foi criada.")
        print()
        print("Abra o projeto 01 e salve uma senha primeiro.")
        return

    print("Senha carregada: " + "*" * len(senha))
    print()

    caracteres = escolher_caracteres()

    if caracteres is None:
        return

    print()

    tamanho_maximo = ler_tamanho()

    if len(senha) > tamanho_maximo:
        print()
        print("A senha de teste é maior que o tamanho escolhido.")
        return

    print()
    print("Configuração:")
    print(f"Caracteres: {len(caracteres)}")
    print(f"Tamanho máximo: {tamanho_maximo}")
    print()
    input("Pressione ENTER para iniciar...")

    limpar()
    banner()

    quebrar(
        senha,
        caracteres,
        tamanho_maximo
    )

if __name__ == "__main__":
    main()