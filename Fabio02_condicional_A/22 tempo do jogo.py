"""
22. Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia seguinte.
"""
def main():
    hora1, minuto1 = map(int, input('Digite a hora e o min do começo do jogo: ').split(':'))
    hora2, minuto2 = map(int, input('Digite a hora e o min do fim do jogo: ').split(':'))

    duracao_jogo(hora1, hora2, minuto1, minuto2)

def duracao_jogo(h_inicio, h_fim, m_inicio, m_fim):
    if h_inicio > h_fim:
        duracao_h = (24 - h_inicio) + h_fim
    else:
        duracao_h = h_inicio - h_fim
        
    if m_inicio > m_fim:
        duracao_m = (60 - m_inicio) + m_fim
    else:
        duracao_m = m_inicio - m_fim

    print(f'A duração do jogo é de {duracao_h} horas e {duracao_m} minutos')


main()
