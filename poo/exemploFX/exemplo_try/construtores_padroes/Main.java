package exemploFX.exemplo_try.construtores_padroes;

public class Main {
    public static void main(String[] args) {
        try {
            throw new ExceptionPadrao("Ocorreu um erro personalizado");
        } catch (ExceptionPadrao e) {
            System.out.println("Exceção capturada: " + e.getMessage());
        }
    }
}
