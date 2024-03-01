package seg_manha_poo.aula02.abstrato;

class Gerente extends Funcionario {
    private double salarioMensal;

    public Gerente(String nome, int idade, double salarioMensal) {
        super(nome, idade);
        this.salarioMensal = salarioMensal;
    }

    @Override
    public double calcularSalario() {
        return salarioMensal;
    }
}