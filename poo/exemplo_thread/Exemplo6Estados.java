package exemplo_thread;

public class Exemplo6Estados {
        public static void main(String[] args) {
            Thread thread = new Thread(new MinhaThread());
            // Estado: NEW (Nova) - A thread foi criada, mas ainda não foi iniciada
            System.out.println("Estado da thread: " + thread.getState());
            // Iniciando a thread
            thread.start();
            // Estado: RUNNABLE (Executável) - A thread está em execução ou pronta para ser
            // executada
            System.out.println("Estado da thread: " + thread.getState());
            try {
                // Espera a thread completar sua execução
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            // Estado: TERMINATED (Terminada) - A thread terminou sua execução
            System.out.println("Estado da thread: " + thread.getState());
        }
    }

    class MinhaThread implements Runnable {
        @Override
        public void run() {
            // Estado: RUNNABLE (Executável) - A thread está em execução
            System.out.println("Estado da thread: " + Thread.currentThread().getState());

            try {
                // Estado: TIMED_WAITING (Aguardando tempo determinado) - A thread está
                // esperando por um tempo determinado
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            // Estado: TERMINATED (Terminada) - A thread terminou sua execução
            System.out.println("Estado da thread: " + Thread.currentThread().getState());
        }
    }