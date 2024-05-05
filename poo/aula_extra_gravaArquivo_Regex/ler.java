package aula_extra_gravaArquivo_Regex;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ler {
    public static void main(String[] args) {
        // Chama a função para ler o arquivo
        String diretorioAtual = System.getProperty("user.dir") + System.getProperty("file.separator") + "arquivo.txt";
        lerArquivo(diretorioAtual);
    }

    public static void lerArquivo(String nomeArquivo) {
        try (BufferedReader reader = new BufferedReader(new FileReader(nomeArquivo))) {
            String linha;
            while ((linha = reader.readLine()) != null) {
                System.out.println(linha);
            }
        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo: " + e.getMessage());
        }
    }
}
