package aula02.exercicio01;
import java.util.Objects;

public class Inquilino extends Pessoa {
    protected String endereco;

    public Inquilino(){}

    public Inquilino(String nome, int idade, String endereco){
        super(nome,idade);
        this.endereco = endereco;
    }


    public Inquilino(String endereco) {
        this.endereco = endereco;
    }

    public String getEndereco() {
        return this.endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public Inquilino endereco(String endereco) {
        setEndereco(endereco);
        return this;
    }

    public double pagarAluguel(double valor) {
        System.out.println(getNome() + " pagou R$ " + valor + " de aluguel.");
        return valor;
    }

    public double pagarCondominio(double valor) {
        System.out.println(getNome() + " pagou R$ " + valor + " de condomínio.");
        return valor;
    }
    public void pagou(double pagamentoAluguel, double pagamentoCondominio){
        if (pagamentoAluguel + pagamentoCondominio > 2000){
            double valor_total = pagamentoAluguel+pagamentoCondominio;
            System.out.printf("Pagamento realizado.\n\tR$:%.2f", valor_total);
        }else{
            System.out.println("Pagamento ainda não realizado.");
        }
    }
        

    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Inquilino)) {
            return false;
        }
        Inquilino inquilino = (Inquilino) o;
        return Objects.equals(endereco, inquilino.endereco);
    }

    @Override
    public String toString() {
        return "O morador "+ getNome() + " possui " + getIdade() + " e vive na " + endereco;
    }
    
}
