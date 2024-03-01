package seg_manha_poo.aula02;

class Professor extends Pessoa {
    private String disciplina;

    public Professor(String nome, int idade, String disciplina) {
        super(nome, idade);
        this.disciplina = disciplina;
    }

    public String getDisciplina() {
        return disciplina;
    }

    // Sobreposição do método getInfoAdicional
    @Override
    public String getInfoAdicional() {
        return "Disciplina: " + disciplina;
    }
}