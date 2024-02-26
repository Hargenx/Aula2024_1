package seg_manha_poo.aula01;

class Pessoa {
    private String nome;
    private int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    @Override
    public String toString() {
        return "Nome: " + nome + "\nIdade: " + idade;
    }
}

class Aluno extends Pessoa {
    private int matricula;

    public Aluno(String nome, int idade, int matricula) {
        super(nome, idade);
        this.matricula = matricula;
    }

    public int getMatricula() {
        return matricula;
    }

    @Override
    public String toString() {
        return super.toString() + "\nMatrícula: " + matricula;
    }
}

class Professor extends Pessoa {
    private String disciplina;

    public Professor(String nome, int idade, String disciplina) {
        super(nome, idade);
        this.disciplina = disciplina;
    }

    public String getDisciplina() {
        return disciplina;
    }

    @Override
    public String toString() {
        return super.toString() + "\nDisciplina: " + disciplina;
    }
}

public class heranca {
    public static void main(String[] args) {
        Aluno aluno = new Aluno("Caroline", 30, 12345);
        Professor professor = new Professor("Raphael", 39, "Programação Orientada à Objetos em Java");

        System.out.println("Informações do Aluno:\n" + aluno.toString() + "\n");
        System.out.println("Informações do Professor:\n" + professor.toString());
    }
}
