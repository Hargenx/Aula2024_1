package exemplo_hash;

import java.util.HashMap;

/**
 *
 * @author Raphael
 */
public class Metodos {

    public static void incluir(int chave, int matricula, String nome, float nota) {
        HashMap<Integer, Estudante> hm = new HashMap<>();
        hm.put(chave, new Estudante(matricula, nome, nota));
                    /*if (option == 1) {
                // Create a new object

                System.out.println("Digite a Matricula: ");
                matricula = sc.nextInt();
                System.out.println("Digite o nome: ");
                nome = sc.next();
                System.out.println("Digite a nota: ");
                nota = sc.nextFloat();
                chave++;
                hm.put(chave, new Turma(matricula, nome, nota));
            } else if (option == 2) {
                if (hm.isEmpty()) {
                    hm.entrySet().stream().map(entry -> {
                        //System.out.print("Indice: " + entry.getKey());
                        return entry;
                    }).forEachOrdered(entry -> {
                        System.out.println("Matricula: " + entry.getValue().getMatricula());
                        System.out.println("Nome: " + entry.getValue().getNome());
                        System.out.println("Nota: " + entry.getValue().getNota());
                    });
                } else if (option == 3) {
                    System.out.println("Digite o nome do aluno que deseja alterar a nota: ");
                    //nome = sc.next();
                    hm.forEach((k, p) -> {
                        String nomePesquisa;
                        boolean existe = p.getNome().contains(nomePesquisa = sc.next());
                        if (existe == true) {
                            //System.out.println("O valor Raphael existe: " + existe);
                            System.out.println("Digite a nova nota: ");
                            float notaAlterada = sc.nextFloat();
                            p.setNota(notaAlterada);
                        }
                    });

                    System.out.println("Press one key to continue.");
                    sc.nextLine();
                } else if (option == 4) {

                } else {

                }
            }*/
    }

}