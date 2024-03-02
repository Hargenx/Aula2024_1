package poo.aula02.abstrato;

public class Main {
    public static void main(String[] args) {
        Desenvolvedor desenvolvedor = new Desenvolvedor("Raphael", 39, 80, 450.0);
        Gerente gerente = new Gerente("Karl Franz", 35, 18000.0);

        
        System.out.println("Informações do Desenvolvedor:\n" + desenvolvedor.toString());
        System.out.println("Salário do Desenvolvedor: $" + desenvolvedor.calcularSalario());

        System.out.println();

        System.out.println("Informações do Gerente:\n" + gerente.toString());
        System.out.println("Salário do Gerente: $" + gerente.calcularSalario());
    }
}
