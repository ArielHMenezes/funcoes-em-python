def funcao (investimento1, investimento2, investimento3, premio):
     custo_inicial_jogo = investimento1 + investimento2 + investimento3
     percetual_do_jogador1 = (100 * investimento1) / custo_inicial_jogo
     percetual_do_jogador2 = (100 * investimento2) / custo_inicial_jogo
     percetual_do_jogador3 = (100 * investimento3) / custo_inicial_jogo
     premio_jog1 = (premio*percetual_do_jogador1) / 100
     premio_jog2 = (premio*percetual_do_jogador2) / 100
     premio_jog3 = (premio*percetual_do_jogador3) / 100
     return premio_jog1, premio_jog2, premio_jog3