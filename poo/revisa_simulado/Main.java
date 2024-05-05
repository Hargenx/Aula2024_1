package revisa_simulado;

public class Main {
    public static void main(String[] args) {
        Carteira minhaCarteira = new Carteira();
        minhaCarteira.setDepositar(100.0);

        try {
            minhaCarteira.retirar(150.0);
            System.out.println("Retirada realizada com sucesso.");
        } catch (QuantidadeInsuficiente e) {
            System.out.println(e.getMessage());
        }
    }
}
