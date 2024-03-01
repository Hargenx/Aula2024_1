package seg_manha_poo.aula02;

public class Main {
    public static void main(String[] args) {
        Pessoa pessoa1 = new Aluno("Caroline", 30, 12345);
        Pessoa pessoa2 = new Professor("Raphael", 39, "POO");

        System.out.println("Informações da Pessoa 1:\n" + pessoa1.toString() + "\n");
        System.out.println("Informações da Pessoa 2:\n" + pessoa2.toString());
    }
}
