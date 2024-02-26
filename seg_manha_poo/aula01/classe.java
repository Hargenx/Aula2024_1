package seg_manha_poo.aula01;

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

    @Override
    public String toString() {
        return "Nome: " + nome + "\nIdade: " + idade;
    }
    

    public static void main(String[] args) {
        Pessoa p1 = new Pessoa("Caroline", 30);
        System.out.println(p1.toString());
        Pessoa pessoa = new Pessoa();
        pessoa.setNome("Raphael");
        pessoa.setIdade(39);

        System.out.println("Nome: " + pessoa.getNome());
        System.out.println("Idade: " + pessoa.getIdade());

    }
}