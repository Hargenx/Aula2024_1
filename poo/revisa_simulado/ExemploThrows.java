package revisa_simulado;

public class ExemploThrows {

    public static void main(String[] args) {
        try {
            dividir(10, 0);
        } catch (ArithmeticException e) {
            System.out.println("Erro: Divisão por zero!");
        }
    }

    public static void dividir(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("Divisão por zero não é permitida.");
        }
        int resultado = a / b;
        System.out.println("Resultado da divisão: " + resultado);
    }
}
