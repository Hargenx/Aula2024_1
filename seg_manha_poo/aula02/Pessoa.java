package seg_manha_poo.aula02;

class Pessoa {
    private String nome;
    private int idade;

    public Pessoa() {
    }

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    // Método polimórfico de sobreposição
    public String getInfoAdicional() {
        return "N/A"; // Implementação padrão
    }

    @Override
    public String toString() {
        return "Nome: " + nome + "\nIdade: " + idade;
    }
}