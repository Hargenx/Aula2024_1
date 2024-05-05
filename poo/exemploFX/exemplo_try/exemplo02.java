package exemploFX.exemplo_try;

public class exemplo02 {
    public static void main(String[] args) {
        Object objeto = "Raphael";

        if (objeto instanceof String string) {
            System.out.println("O objeto é uma String: " + string);
        } else {
            System.out.println("O objeto não é uma String.");
        }
    }
}
