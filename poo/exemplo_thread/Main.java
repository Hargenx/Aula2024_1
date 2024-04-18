public class Main {
    public static void main(String[] args) {
        // Criando e iniciando a primeira thread
        Thread thread1 = new Thread(new MinhaThread("Thread 1"));
        thread1.start();

        // Criando e iniciando a segunda thread
        Thread thread2 = new Thread(new MinhaThread("Thread 2"));
        thread2.start();
    }
}

// Classe que implementa a interface Runnable
class MinhaThread implements Runnable {
    private String nome;

    // Construtor
    public MinhaThread(String nome) {
        this.nome = nome;
    }

    // Método run() que será executado pela thread
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(nome + ": Mensagem " + i);
            try {
                // Dormir a thread por um curto período de tempo para simular um trabalho
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}