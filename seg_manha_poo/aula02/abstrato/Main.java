package seg_manha_poo.aula02.abstrato;

public class Main {
    public static void main(String[] args) {
        Desenvolvedor desenvolvedor = new Desenvolvedor("Alice", 28, 160, 30.0);
        Gerente gerente = new Gerente("Bob", 35, 5000.0);

        // Usando métodos da classe Funcionario
        System.out.println("Informações do Desenvolvedor:\n" + desenvolvedor.toString());
        System.out.println("Salário do Desenvolvedor: $" + desenvolvedor.calcularSalario());

        System.out.println(); // Adicionando uma linha em branco para separar os exemplos

        System.out.println("Informações do Gerente:\n" + gerente.toString());
        System.out.println("Salário do Gerente: $" + gerente.calcularSalario());
    }
}
