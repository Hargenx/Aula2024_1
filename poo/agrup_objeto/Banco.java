package agrup_objeto;
//Vamos criar um exemplo que envolve um agrupamento de objetos. Neste caso, vamos considerar um banco que possui várias contas bancárias e precisa realizar algumas operações em conjunto.
import java.util.ArrayList;
import java.util.List;

class Banco {
    private List<ContaBancaria> contas;

    public Banco() {
        this.contas = new ArrayList<>();
    }

    public void adicionarConta(ContaBancaria conta) {
        contas.add(conta);
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

    public static void main(String[] args) {
        Banco banco = new Banco();

        ContaBancaria contaCarol = new ContaBancaria("Carol", 6894, 14445, 48000.00);
        ContaBancaria contaGeorge = new ContaBancaria("George", 3924, 70240, 800.00);
        ContaBancaria contaJessica = new ContaBancaria("Jéssica", 3986, 12345, 1500.00);

        banco.adicionarConta(contaCarol);
        banco.adicionarConta(contaGeorge);
        banco.adicionarConta(contaJessica);

        // Exibindo informações iniciais
        banco.exibirInformacoesContas();
        System.out.println();

        // Realizando operações em conjunto
        banco.realizarOperacoes();

        // Exibindo informações após as operações
        banco.exibirInformacoesContas();
    }
}
