package poo.aula02.abstrato;

class Desenvolvedor extends Funcionario {
    private int horasTrabalhadas;
    private double salarioHora;

    public Desenvolvedor(String nome, int idade, int horasTrabalhadas, double salarioHora) {
        super(nome, idade);
        this.horasTrabalhadas = horasTrabalhadas;
        this.salarioHora = salarioHora;
    }

    @Override
    public double calcularSalario() {
        return horasTrabalhadas * salarioHora;
    }
}
