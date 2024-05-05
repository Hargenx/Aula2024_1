package exemplo_thread;

public class ExemploDemonUserThreads {
    public static void main(String[] args) {
        // Criando uma thread de usuário
        Thread threadUser = new Thread(new MinhaThread("Thread de Usuário"));
        // Definindo como user thread (padrão)
        threadUser.setDaemon(false);
        threadUser.start();

        // Criando uma thread demoníaca
        Thread threadDemon = new Thread(new MinhaThread("Thread Demoníaca"));
        // Definindo como daemon thread
        threadDemon.setDaemon(true);
        threadDemon.start();

        System.out.println("Fim do método main");
    }
}

class MinhaThread implements Runnable {
    private String nome;

    public MinhaThread(String nome) {
        this.nome = nome;
    }

    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(nome + ": Mensagem " + i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println(nome + " terminou.");
    }
}
