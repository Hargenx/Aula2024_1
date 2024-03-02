package seg_manha_poo.agrup_objeto;

import java.util.ArrayList;
import java.util.List;

class Tarefa {
    private String descricao;
    private boolean concluida;

    public Tarefa(String descricao) {
        this.descricao = descricao;
        this.concluida = false;
    }

    public String getDescricao() {
        return descricao;
    }

    public boolean isConcluida() {
        return concluida;
    }

    public void concluir() {
        this.concluida = true;
        System.out.println("Tarefa concluída: " + descricao);
    }
}

class Funcionario {
    private String nome;

    public Funcionario(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }
}

class Projeto {
    private String nome;
    private List<Funcionario> equipe;
    private List<Tarefa> tarefas;

    public Projeto(String nome) {
        this.nome = nome;
        this.equipe = new ArrayList<>();
        this.tarefas = new ArrayList<>();
    }

    public void adicionarFuncionario(Funcionario funcionario) {
        equipe.add(funcionario);
    }

    public void adicionarTarefa(Tarefa tarefa) {
        tarefas.add(tarefa);
    }

    public void exibirInformacoes() {
        System.out.println("Projeto: " + nome);
        System.out.println("Equipe:");
        for (Funcionario funcionario : equipe) {
            System.out.println("  - " + funcionario.getNome());
        }

        System.out.println("Tarefas:");
        for (Tarefa tarefa : tarefas) {
            System.out.println("  - " + tarefa.getDescricao() + " (Concluída: " + tarefa.isConcluida() + ")");
        }
    }

    public static void main(String[] args) {
        // Criando funcionários
        Funcionario desenvolvedor1 = new Funcionario("Alice");
        Funcionario desenvolvedor2 = new Funcionario("Bob");

        // Criando tarefas
        Tarefa tarefa1 = new Tarefa("Implementar login");
        Tarefa tarefa2 = new Tarefa("Criar API REST");
        Tarefa tarefa3 = new Tarefa("Testar funcionalidades");

        // Criando projeto
        Projeto meuProjeto = new Projeto("Sistema de Gestão");

        // Adicionando funcionários ao projeto
        meuProjeto.adicionarFuncionario(desenvolvedor1);
        meuProjeto.adicionarFuncionario(desenvolvedor2);

        // Adicionando tarefas ao projeto
        meuProjeto.adicionarTarefa(tarefa1);
        meuProjeto.adicionarTarefa(tarefa2);
        meuProjeto.adicionarTarefa(tarefa3);

        // Exibindo informações do projeto
        meuProjeto.exibirInformacoes();

        // Concluindo uma tarefa
        tarefa1.concluir();

        // Exibindo informações do projeto após a conclusão da tarefa
        meuProjeto.exibirInformacoes();
    }
}
