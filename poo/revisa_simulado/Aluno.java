package revisa_simulado;

public class Aluno extends Pessoa {
    private int id;
    private String nome;
    private int matricula;
    private String email;
    private static String endereco;
    
    public Aluno(int id, String nome, int matricula, String email) {
        super(endereco);
        this.id = id;
        this.nome = nome;
        this.matricula = matricula;
        this.email = email;
    }

    public Aluno() {
        super(endereco);
    }
    

    public int getId() {
        return this.id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getMatricula() {
        return this.matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public String getEmail() {
        return this.email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

}
