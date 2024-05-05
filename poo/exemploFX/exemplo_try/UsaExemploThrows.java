package exemploFX.exemplo_try;

import java.io.IOException;

public class UsaExemploThrows {
    void umMetodo(int num) throws IOException, ArithmeticException {
        if (num == 1) {
            throw new IOException("IOException");
        } else {
            throw new ArithmeticException("ArithmeticException");
        }
    }

    public static void main(String[] args) {
        try {
            UsaExemploThrows obj = new UsaExemploThrows();
            obj.umMetodo(1);
        } catch (IOException | ArithmeticException ex) {
            System.out.println(ex);
        }
    }
}