package agrup_objeto;

public class Pedido {
    private int numero;
    private String prato;

    public Pedido(int numero, String prato) {
        this.numero = numero;
        this.prato = prato;
    }

    public int getNumero() {
        return numero;
    }

    public String getPrato() {
        return prato;
    }

    @Override
    public String toString() {
        return "Pedido #" + numero + ": " + prato;
    }
}
