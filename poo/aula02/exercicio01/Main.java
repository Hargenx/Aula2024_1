package aula02.exercicio01;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            Inquilino q = new Inquilino();
            
            System.out.print("Insira o nome: ");
            q.setNome(scan.nextLine());
            
            System.out.print("Insira a idade: ");
            q.setIdade(scan.nextInt());
            
            // Consumir o caractere de nova linha pendente após o próximoInt()
            scan.nextLine();
            
            System.out.print("Insira o endereco: ");
            q.setEndereco(scan.nextLine());

            System.out.print("Insira o valor pago de alugel: R$");
            double aluguelPago = scan.nextDouble();

            System.out.print("Insira o valor pago do Condominio: R$");
            double condominioPago = scan.nextDouble();

            System.out.printf("\n%s tem %d anos, mora em %s e paga um aluguel de R$%.2f e R$%.2f de condominio.\n",  
                              q.getNome(), 
                              q.getIdade(), 
                              q.getEndereco(),  
                              aluguelPago,
                              condominioPago);

            q.pagou(aluguelPago, condominioPago);           
            
            System.out.println("\nDados da pessoa:\n");
            System.out.println(q.toString());
        } catch (Exception e) {
            System.err.println("Ocorreu um erro: " + e.getMessage());
        }
    }
}
