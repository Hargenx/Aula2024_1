package seg_manha_poo.aula02;

public class Main {
    public static void main(String[] args) {
        Pessoa aluno = new Aluno("Caroline", 30, 12345);
        Pessoa professor = new Professor("Raphael", 39, "POO");

        System.out.println("Informações da Pessoa 1:\n" + aluno.toString() + "\n");
        System.out.println("Informações da Pessoa 2:\n" + professor.toString());
        aluno.apresentar();
        professor.apresentar(professor.getIdade());
        professor.apresentar();

    }
}
