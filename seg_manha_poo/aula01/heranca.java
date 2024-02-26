package seg_manha_poo.aula01;


class Pessoa {
    private String nome;
    private int idade;

    public Pessoa(){}

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

    public void setNome(String nome){
        this.nome = nome;
    }

    public void setIdade(int  idade){
        this.idade = idade;
    }

    // Método polimórfico de sobreposição
    public String getInfoAdicional() {
        return "N/A";  // Implementação padrão
    }

    @Override
    public String toString() {
        return "Nome: " + nome + "\nIdade: " + idade + "\nInformação Adicional: " + getInfoAdicional();
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

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    // Sobreposição do método getInfoAdicional
    @Override
    public String getInfoAdicional() {
        return "Matricula: " + matricula;
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

    public void  setDisciplina(String disciplina) {
        this.disciplina = disciplina;
    }

    // Sobreposição do método getInfoAdicional
    @Override
    public String getInfoAdicional() {
        return "Disciplina: " + disciplina;
    }
}

public class heranca {
    public static void main(String[] args) {
        Aluno aluno = new Aluno("Caroline", 30, 12345);
        Professor professor = new Professor("Raphael", 39, "Programação Orientada à Objetos em Java");

        System.out.println("Informações do Aluno:\n" + aluno.toString() + "\n");
        System.out.println("Informações do Professor:\n" + professor.toString());

        Aluno[] alunos = new Aluno[2];
        alunos[0] = new Aluno("Carol", 18, 67889);
        alunos[1] = new Aluno("Raphael", 19,  67890);

        for (Aluno a : alunos){
            System.out.println(a.toString());
        }
    }
}
