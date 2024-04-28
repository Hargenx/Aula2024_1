import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def main():
    # Dados de tempo até a extinção do vermelho e fertilidade azul
    tempo_extincao_vermelho = [132, 132, 105, 105, 164, 164, 204, 204, 191, 191, 155, 155, 105, 105, 84, 84, 160, 160, 150, 150, 103, 103, 99, 99, 83, 83, 137, 137, 79, 79, 81, 81, 196, 196, 87, 87, 86, 86, 71, 71, 54, 54, 68, 68, 49, 49, 80, 80, 44, 44, 47, 47, 63, 63, 74, 74, 63, 63, 61, 61, 69, 69, 54, 54, 41, 41, 45, 45, 108, 108, 64, 64, 46, 46, 41, 41, 67, 67, 52, 52, 36, 36, 35, 35, 57, 57, 59, 59, 36, 36, 30, 30, 39, 39, 35, 35, 34, 34, 47, 47, 44, 44, 30, 30, 37, 37, 38, 38, 37, 37, 43, 43, 37, 37, 32, 32, 33, 33, 53, 53, 42, 42, 36, 36, 37, 37, 32, 32, 31, 31, 24, 24, 39, 39, 31, 31, 34, 34, 25, 25, 25, 25, 26, 26, 37, 37, 32, 32, 24, 24, 34, 34, 26, 26, 33, 33, 26, 26, 46, 46, 22, 22, 25, 25, 34, 34, 22, 22, 24, 24, 26, 26, 22, 22, 19, 19, 23, 23, 17, 17, 22, 22, 37, 37, 30, 30, 25, 25, 24, 24, 21, 21, 33, 33, 25, 25, 22, 22, 19, 19, 22, 22, 15, 15, 17, 17, 20, 20, 21, 21, 21, 21, 20, 20, 22, 22, 21, 21, 21, 21, 20, 20, 28, 28, 22, 22, 17, 17, 18, 18, 19, 19, 16, 16, 24, 24, 20, 20, 22, 22, 15, 15, 17, 17, 21, 21, 20, 20, 17, 17, 20, 20, 17, 17, 22, 22, 17, 17, 21, 21, 21, 21, 18, 18, 16, 16, 13, 13, 22, 22, 19, 19, 19, 19, 16, 16, 20, 20, 16, 16, 17, 17, 18, 18, 16, 16, 20, 20, 14, 14, 15, 15, 27, 27, 17, 17, 19, 19, 13, 13, 17, 17, 13, 13, 16, 16, 26, 26, 15, 15, 17, 17, 19, 19, 16, 16, 12, 12, 20, 20, 17, 17, 18, 18, 16, 16, 15, 15, 17, 17, 18, 18, 13, 13, 17, 17, 13, 13, 21, 21, 21, 21, 19, 19, 16, 16, 15, 15, 14, 14, 16, 16, 18, 18, 17, 17, 17, 17, 12, 12, 15, 15, 15, 15, 13, 13, 15, 15, 16, 16, 23, 23, 15, 15, 19, 19, 16, 16, 18, 18, 12, 12, 16, 16, 12, 12, 12, 12, 19, 19, 12, 12, 18, 18, 15, 15, 16, 16, 17, 17, 12, 12, 14, 14, 15, 15, 12, 12, 8, 8, 13, 13, 10, 10, 13, 13, 13, 13, 12, 12, 11, 11, 15, 15, 12, 12, 16, 16, 12, 12, 11, 11, 16, 16, 11, 11, 14, 14, 14, 14, 14, 14, 15, 15, 13, 13, 10, 10, 12, 12, 15, 15, 11, 11, 12, 12, 9, 9, 12, 12, 13, 13, 9, 9, 13, 13, 14, 14, 9, 9, 13, 13, 12, 12, 16, 16, 10, 10, 13, 13, 12, 12, 10, 10, 13, 13, 15, 15, 9, 9, 9, 9, 13, 13, 11, 11, 10, 10, 10, 10, 13, 13, 14, 14, 10, 10, 11, 11, 14, 14, 10, 10, 10, 10, 12, 12, 9, 9, 13, 13, 11, 11, 9, 9, 11, 11, 13, 13, 15, 15, 10, 10, 10, 10, 10, 10, 15, 15, 10, 10, 13, 13, 9, 9, 10, 10, 12, 12, 8, 8, 13, 13, 11, 11, 10, 10, 13, 13, 10, 10, 10, 10, 11, 11, 12, 12, 12, 12, 15, 15, 10, 10, 10, 10, 16, 16, 9, 9, 11, 11, 9, 9, 12, 12, 10, 10, 9, 9, 10, 10, 11, 11, 9, 9, 9, 9, 14, 14, 10, 10]

    def remove_duplicatas_sequenciais(sequencia):
        nova_sequencia = []
        for i in range(len(sequencia)):
            if i % 2 == 0:
                nova_sequencia.append(sequencia[i])
        return nova_sequencia

    tempo_extincao_vermelho = remove_duplicatas_sequenciais(tempo_extincao_vermelho)
    # print(tempo_extincao_vermelho)

    fertilidade_azul = [ 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 2.3, 2.3, 2.3, 2.3, 2.3, 2.3, 2.3, 2.3, 2.3, 2.3, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.6, 2.6, 2.6, 2.6, 2.6, 2.6, 2.6, 2.6, 2.6, 2.6, 2.7, 2.7, 2.7, 2.7, 2.7, 2.7, 2.7, 2.7, 2.7, 2.7, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.4, 3.4, 3.4, 3.4, 3.4, 3.4, 3.4, 3.4, 3.4, 3.4, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.6, 4.6, 4.6, 4.6, 4.6, 4.6, 4.6, 4.6, 4.6, 4.6, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.9, 4.9, 4.9, 4.9, 4.9, 4.9, 4.9, 4.9, 4.9, 4.9, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]


    # Calcular média e desvio padrão
    media_tempo_extincao = np.mean(tempo_extincao_vermelho)
    desvio_padrao_tempo_extincao = np.std(tempo_extincao_vermelho)

    # Calcular a correlação entre as variáveis
    correlacao = np.corrcoef(fertilidade_azul, tempo_extincao_vermelho)[0, 1]

    # Visualização do tempo de extinção do vermelho
    st.header("Tempo até extinção do vermelho")
    st.write(f"Média: {media_tempo_extincao:.2f}")
    st.write(f"Desvio Padrão: {desvio_padrao_tempo_extincao:.2f}")
    st.write(f"Correlação com a fertilidade azul: {correlacao:.2f}")

    # Histograma do tempo de extinção do vermelho
    st.subheader("Histograma do Tempo até Extinção do Vermelho")
    plt.hist(tempo_extincao_vermelho, bins=30, density=True, alpha=0.6, color="g")
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, media_tempo_extincao, desvio_padrao_tempo_extincao)
    plt.plot(x, p, "k", linewidth=2)
    title = "Histograma do Tempo até Extinção do Vermelho"
    plt.title(title)
    plt.xlabel("Tempo até extinção do vermelho")
    plt.ylabel("Densidade")
    plt.grid(True)
    st.pyplot(plt)

    # Gráfico de dispersão da fertilidade azul versus tempo de extinção do vermelho
    st.header("Gráfico de Dispersão")
    st.write("Relação entre Fertilidade Azul e Tempo até Extinção do Vermelho")
    plt.figure(figsize=(8, 6))
    plt.plot(fertilidade_azul, tempo_extincao_vermelho, "bo", label="Dados")
    plt.xlabel("Fertilidade Azul")
    plt.ylabel("Tempo até extinção do vermelho")
    plt.title("Tempo até extinção do vermelho em relação à fertilidade azul")
    plt.grid(True)
    plt.legend()

    # Adicionar linha de tendência
    z = np.polyfit(fertilidade_azul, tempo_extincao_vermelho, 1)
    p = np.poly1d(z)
    plt.plot(fertilidade_azul, p(fertilidade_azul), "r--", label="Linha de Tendência")
    st.pyplot(plt)

if __name__ == "__main__":
    main()
