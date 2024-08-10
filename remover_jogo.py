def remover_jogo(biblioteca, nome_jogo):
    for jogo in biblioteca:
        if jogo == nome_jogo:
            biblioteca.remove(jogo)
            print(f"jogo: {jogo} removido com sucesso!")
            return
            print(f"jogo: {jogo} não encontrado!")