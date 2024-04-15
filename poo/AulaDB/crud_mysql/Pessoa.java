public class Pessoa {
    private int id;
    private String nome;
    private int idade;
    private float altura;

    public Pessoa(int id, String nome, int idade, float altura) {
        this.id = id;
        this.nome = nome;
        this.idade = idade;
        this.altura = altura;
    }

    public Pessoa() {
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public float getAltura() {
        return altura;
    }

    @Override
    public String toString() {
        return "Pessoa [id=" + id + ", nome=" + nome + ", idade=" + idade + ", altura=" + altura + "]";
    }
}