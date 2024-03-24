public class ExceptionPadrao extends Exception {

    public ExceptionPadrao() {
        super();
    }

    public ExceptionPadrao(String message) {
        super(message);
    }

    public ExceptionPadrao(String message, Throwable cause) {
        super(message, cause);
    }

    public ExceptionPadrao(Throwable cause) {
        super(cause);
    }
    
}
