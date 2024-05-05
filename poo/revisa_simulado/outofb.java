package revisa_simulado;

public class outofb {
    public static void main(String[] args) {
        int mortesCovid [] ={2, 35, 57 ,80 , 28, 31};
        float soma = 0;
        for (int i = 0; i < mortesCovid.length; i++) {
            soma += mortesCovid[i];
        }
        float media = soma/mortesCovid.length;
        System.out.println("A média de mortes é:"+media);
        for(int i = 0; i < mortesCovid.length; i++){
            System.out.print(mortesCovid[i] + " ");
        }
    }
}