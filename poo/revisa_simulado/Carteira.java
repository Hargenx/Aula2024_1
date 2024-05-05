package revisa_simulado;

class Carteira {
    private double quantidadeCriptomoeda;
    private Double depositar;

    public void depositar(Double depositar) {
        this.depositar = depositar;
    }

    public Double getDepositar() {
        return this.depositar;
    }

    public void setDepositar(Double depositar) {
        this.depositar = depositar;
    }

    public void retirar(double quantidade) throws QuantidadeInsuficiente {
        if (quantidade > quantidadeCriptomoeda) {
            throw new QuantidadeInsuficiente("Quantidade de criptomoeda insuficiente.");
        }
        quantidadeCriptomoeda -= quantidade;
    }
}

class QuantidadeInsuficiente extends Exception {
    public QuantidadeInsuficiente(String message) {
        super(message);
    }
}
