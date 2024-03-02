package poo.aula02;

class Aluno extends Pessoa {
    private int matricula;

    public Aluno(String nome, int idade, int matricula) {
        super(nome, idade);
        this.matricula = matricula;
    }

    public int getMatricula() {
        return matricula;
    }

    // Sobreposição do método getInfoAdicional
    @Override
    public String getInfoAdicional() {
        return "Matrícula: " + matricula;
    }

    @Override
    public void apresentar() {
        System.out.println("Olá, eu sou o aluno " + getNome() + " e minha matrícula é " + matricula + "!");
    }
}