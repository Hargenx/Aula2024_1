public class throws_exemplo {

    public static double divide(double dividendo, double divisor) throws ArithmeticException {
        if (divisor == 0) {
            throw new ArithmeticException("Não pode ser dividido por zero");
        }
        return dividendo / divisor;
    }

    public static void main(String[] args) {
        double resultado;
        try {
            resultado = divide(10, 0);
            System.out.println("resultadoado da divisão: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Exceção capturada: " + e.getMessage());
        }
    }
}
