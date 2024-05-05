package aula02.exercicio02;

public class Main {
    public static void main(String[] args) {
        ContaBancaria conta1 = new ContaBancaria("Carol", 6894, 14445, 48000.00);
        ContaBancaria conta2 = new ContaBancaria("Gilson", 3924, 70240, 800.00);
        ContaBancaria conta3 = new ContaBancaria("Sara", 3986, 12345, 1500.00);

        System.out.println("Informações da Conta:");
        conta1.exibirInformacoes();
        System.out.println();

        System.out.println("Informações da Conta:");
        conta2.exibirInformacoes();
        System.out.println();

        System.out.println("Informações da Conta:");
        conta3.exibirInformacoes();
        System.out.println();

        conta1.realizarSaque(10000.00);
        System.out.println();

        conta2.realizarTransferencia(conta3, 300.00);
        System.out.println();

        conta3.realizarSaque(2000.00);
    }
}
