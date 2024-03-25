import java.io.IOException;

public class ExemploThrows {
    void umMetodo(int num) throws IOException, ArithmeticException{
        if (num == 1){
            throw new IOException("IOException");
        }else{
            throw new ArithmeticException("ArithmeticException");
        }
    }
}
public class Main {
    public static void main(String[] args) {
        try{
            ExemploThrows obj = new ExemploThrows();
            obj.umMetodo(1);
        }catch(IOException | ArithmeticException ex){
            System.out.println(ex);
        }
    }    
}
