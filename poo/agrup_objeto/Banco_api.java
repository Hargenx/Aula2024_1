package poo.agrup_objeto;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Banco_api {
    private List<ContaBancaria> contas;

    public Banco_api(List<ContaBancaria> contas) {
        this.contas = contas;
    }

    public void exibirInformacoesContas() {
        System.out.println("Informações de todas as Contas no Banco:");
        for (ContaBancaria conta : contas) {
            conta.exibirInformacoes();
            System.out.println();
        }
    }

    public void realizarOperacoes() {
        for (ContaBancaria conta : contas) {
            conta.realizarSaque(500.00);
            System.out.println();
        }

        // Transferir dinheiro da primeira conta para a segunda
        if (contas.size() >= 2) {
            contas.get(0).realizarTransferencia(contas.get(1), 1000.00);
            System.out.println();
        }
    }

    public void exibirSaldoPorAgencia() {
        // Agrupar contas por agência usando Collectors.groupingBy
        Map<Integer, List<ContaBancaria>> contasPorAgencia = contas.stream()
                .collect(Collectors.groupingBy(ContaBancaria::getAgencia, Collectors.toList()));

        System.out.println("Saldo por Agência:");
        contasPorAgencia.forEach((agencia, listaContas) -> {
            System.out.println("Agência: " + agencia);
            listaContas.forEach(conta -> System.out.println("   " + conta.getNome() + ": R$ " + conta.getSaldo()));
        });
    }
    

    public static void main(String[] args) {
        List<ContaBancaria> contas = List.of(
                new ContaBancaria("Carol", 6894, 14445, 48000.00),
                new ContaBancaria("George", 3924, 70240, 800.00),
                new ContaBancaria("Jéssica", 3986, 12345, 1500.00));

        Banco_api banco = new Banco_api(contas);

        // Exibindo informações iniciais
        banco.exibirInformacoesContas();
        System.out.println();

        // Realizando operações em conjunto
        banco.realizarOperacoes();

        // Exibindo informações após as operações
        banco.exibirInformacoesContas();

        // Exibindo o saldo por agência
        banco.exibirSaldoPorAgencia();
    }
}
