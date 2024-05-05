package aula01;

public class Main {
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
