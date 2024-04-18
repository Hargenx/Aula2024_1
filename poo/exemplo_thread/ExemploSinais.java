import java.util.concurrent.Semaphore;

public class ExemploSinais {
    public static void main(String[] args) {
        // Cria um semáforo com uma permissão
        Semaphore semaphore = new Semaphore(1);

        // Cria e inicia as threads
        Thread t1 = new Thread(new Tarefa(semaphore, "Thread 1"));
        Thread t2 = new Thread(new Tarefa(semaphore, "Thread 2"));

        t1.start();
        t2.start();
    }
}

class Tarefa implements Runnable {
    private Semaphore semaphore;
    private String nome;

    public Tarefa(Semaphore semaphore, String nome) {
        this.semaphore = semaphore;
        this.nome = nome;
    }

    @Override
    public void run() {
        try {
            System.out.println(nome + " tentando adquirir a permissão.");
            semaphore.acquire();
            System.out.println(nome + " adquiriu a permissão.");

            // Simula um trabalho sendo feito pela thread
            Thread.sleep(2000);

        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            // Libera a permissão
            System.out.println(nome + " liberou a permissão.");
            semaphore.release();
        }
    }
}
