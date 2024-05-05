package aula_extra_gravaArquivo_Regex;

import java.io.FileWriter;
import java.io.IOException;

public class gravar {
    public static void main(String[] args) {
        FileWriter escrever = null;
        try {
            escrever = new FileWriter("arquivo.txt");
            escrever.write("Raphael");
        } catch (IOException e) {
            e.printStackTrace();
        } finally{
            try{
                escrever.close();
            } catch(IOException e){
                e.printStackTrace();
            }
        }
    }
}
