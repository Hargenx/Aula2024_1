import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class gerenciamento_arquivo {
    public static String lerArquivo(String nomeArquivo) throws Exception_Leitura_Arquivo {
        BufferedReader leitura = null;
        try {
            leitura = new BufferedReader(new FileReader(nomeArquivo));
            StringBuilder conteudo = new StringBuilder();
            String linha;
            while ((linha = leitura.readLine()) != null) {
                conteudo.append(linha).append("\n");
            }
            return conteudo.toString();
        } catch (IOException e) {
            throw new Exception_Leitura_Arquivo("Erro ao ler o arquivo", e);
        } finally {
            if (leitura != null) {
                try {
                    leitura.close();
                } catch (IOException e) {
                    System.err.println("Erro ao fechar o arquivo: " + e.getMessage());
                }
            }
        }
    }

    public static void main(String[] args) {
        try {
            String conteudo = lerArquivo("Arquivo.txt");
            System.out.println("Conteúdo do arquivo:");
            System.out.println(conteudo);
        } catch (Exception_Leitura_Arquivo e) {
            System.err.println("Erro ao ler o arquivo: " + e.getMessage());
        }
    }
}

class Exception_Leitura_Arquivo extends Exception {
    public Exception_Leitura_Arquivo(String message, Throwable cause) {
        super(message, cause);
    }
}
