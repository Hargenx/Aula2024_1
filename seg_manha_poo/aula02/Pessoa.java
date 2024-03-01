package seg_manha_poo.aula02;

class Pessoa implements Apresentavel{
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
    public void apresentar() {
        System.out.println("Olá, eu sou " + nome + "!");
    }

    // Método sobrecarregado para apresentação com idade
    public void apresentar(int novaIdade) {
        System.out.println("Olá, eu sou " + nome + " e tenho " + novaIdade + " anos!");
    }

    @Override
    public String toString() {
        return "Nome: " + nome + "\nIdade: " + idade;
    }
}