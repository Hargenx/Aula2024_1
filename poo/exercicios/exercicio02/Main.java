package exercicios.exercicio02;

import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        Pessoa[] dados = {
                new Pessoa("Raphael", 39, "Rio de Janeiro"),
                new Pessoa("Marcia", 49, "Rio Grande do Sul")
        };
        salvarEmJson(dados);
    }

    public static void salvarEmJson(Pessoa[] dados) {
        try (FileWriter arquivo = new FileWriter("dados.json")) {
            arquivo.write("[");
            for (int i = 0; i < dados.length; i++) {
                arquivo.write("{");
                arquivo.write("\"nome\": \"" + dados[i].nome + "\", ");
                arquivo.write("\"idade\": " + dados[i].idade + ", ");
                arquivo.write("\"cidade\": \"" + dados[i].cidade + "\"");
                arquivo.write("}");
                if (i < dados.length - 1) {
                    arquivo.write(", ");
                }
            }
            arquivo.write("]");
            System.out.println("Dados salvos em dados.json");
        } catch (IOException e) {
            System.out.println("Erro ao salvar em dados.json: " + e.getMessage());
        }
    }

    static class Pessoa {
        String nome;
        int idade;
        String cidade;

        public Pessoa(String nome, int idade, String cidade) {
            this.nome = nome;
            this.idade = idade;
            this.cidade = cidade;
        }
    }
}
