package exercicios.exercicio01;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

class Pessoa {
    String nome;
    int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }
}

public class versao2 {
    public static void salvarEmTxt(List<Pessoa> pessoas, String nomeArquivo) {
        try (FileWriter arquivo = new FileWriter(nomeArquivo)) {
            for (Pessoa pessoa : pessoas) {
                arquivo.write("Nome: " + pessoa.nome + ", Idade: " + pessoa.idade + "\n");
            }
            System.out.println("Dados salvos em pessoas.txt: " + nomeArquivo);
        } catch (IOException e) {
            System.out.println("Erro ao salvar em pessoas.txt: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        List<Pessoa> pessoas = new ArrayList<>();
        pessoas.add(new Pessoa("Raphael", 39));
        pessoas.add(new Pessoa("Caroline", 30));
        String diretorioAtual = System.getProperty("user.dir") + System.getProperty("file.separator") + "pessoas2.txt";
        salvarEmTxt(pessoas, diretorioAtual);
    }
}
