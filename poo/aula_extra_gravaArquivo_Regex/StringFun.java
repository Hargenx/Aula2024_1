package aula_extra_gravaArquivo_Regex;

public class StringFun {
    public static void main(String[] args) {
        String str = "Raphael";
        int length = str.length();
        String substring = str.substring(7);
        String replaced = str.replace("el", "");
        System.out.println("\tComprimento da string: " + length
         + "\n\tSubstring a partir do índice 4: " + substring
         + "\n\tSubstitui el por \"\": " + replaced);
    }
}