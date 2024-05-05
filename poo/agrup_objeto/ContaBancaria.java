package agrup_objeto;

public class ContaBancaria {
    private String nome;
    private int agencia;
    private int numeroConta;
    private double saldo;

    public ContaBancaria(String nome, int agencia, int numeroConta, double saldo) {
        this.nome = nome;
        this.agencia = agencia;
        this.numeroConta = numeroConta;
        this.saldo = saldo;
    }


    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getAgencia() {
        return this.agencia;
    }

    public void setAgencia(int agencia) {
        this.agencia = agencia;
    }

    public int getNumeroConta() {
        return this.numeroConta;
    }

    public void setNumeroConta(int numeroConta) {
        this.numeroConta = numeroConta;
    }

    public double getSaldo() {
        return this.saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
    
    
    
    public void exibirInformacoes() {
        System.out.println("Nome: " + nome);
        System.out.println("Agência: " + agencia);
        System.out.println("Nº da Conta: " + numeroConta);
        System.out.println("Saldo: R$ " + saldo);
    }

    public void realizarSaque(double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            System.out.println("Saque realizado com sucesso. Novo saldo: R$ " + saldo);
        } else {
            System.out.println("Saque não permitido. Saldo insuficiente.");
        }
    }

    public void realizarTransferencia(ContaBancaria destinatario, double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            destinatario.saldo += valor;
            System.out.println("Transferência realizada com sucesso. Novo saldo: R$ " + saldo);
        } else {
            System.out.println("Transferência não permitida. Saldo insuficiente.");
        }
    }
}
