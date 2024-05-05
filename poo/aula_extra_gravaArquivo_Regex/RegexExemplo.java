package aula_extra_gravaArquivo_Regex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class RegexExemplo {
    public static void main(String[] args) {
        String texto = "O professor da disciplina de Programação orientada a Objeto JAVA é o professor Raphael.";
        Pattern pattern = Pattern.compile("\\bRaphael\\b");
        Matcher matcher = pattern.matcher(texto);
        while (matcher.find()) {
            System.out.println("Encontrou a palavra 'Raphael' em: " + matcher.start());
        }
        // Texto de exemplo com um e-mail válido e um inválido
        String texto2 = "O e-mail do usuário é raphael@email.com e o outro é invalido@teste";

        // Expressão regular para validar e-mails
        String regexEmail = "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b";

        // Compilar a expressão regular em um padrão
        Pattern patternEmail = Pattern.compile(regexEmail);

        // Criar um matcher para encontrar correspondências na string de texto
        Matcher matcherEmail = patternEmail.matcher(texto2);

        // Iterar sobre as correspondências encontradas
        while (matcherEmail.find()) {
            System.out.println("E-mail encontrado: " + matcherEmail.group());
        }
    }
}
