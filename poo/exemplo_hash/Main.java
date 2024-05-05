package exemplo_hash;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        HashMap<Integer, Estudante> hm = new HashMap<>();
        hm.put(1, new Estudante(01062021, "Raphael", (float) 8.5));
        hm.put(2, new Estudante(01062021, "Caroline", 10));
        hm.put(3, new Estudante(02062020, "Gilson", 6));

        try (Scanner sc = new Scanner(System.in)) {
            int opcao = 0;
            int chave = 4;
            int matricula = 0;
            String nome = null;
            float nota = 0;
            System.out.println(chave);
            do {
                System.out.println("# # Escolha a opção # #");
                System.out.println("Opção 1 - Cadastro de aluno e nota");
                System.out.println("Opção 2 - Exibir alunos");
                System.out.println("Opção 3 - Alterar nota");
                System.out.println("Opção 4 - Excluir alunos");
                System.out.println("Option 0 - Exit program");
                System.out.println("_______________________");
                
                System.out.print("Digite a opção: ");
                opcao = sc.nextInt();
                
                switch (opcao) {
                    case 1:
                        System.out.println("Digite a Matricula: ");
                        matricula = sc.nextInt();
                        System.out.println("Digite o nome: ");
                        nome = sc.next();
                        System.out.println("Digite a nota: ");
                        nota = sc.nextFloat();
                        hm.put(chave, new Estudante(matricula, nome, nota));
                        chave++;
                        break;
                    case 2:
                        if (!hm.isEmpty()) {
                            hm.entrySet().stream().map(entry -> {
                                //System.out.print("Indice: " + entry.getKey());
                                return entry;
                            }).forEachOrdered(entry -> {
                                System.out.println("Matricula: " 
                                        + entry.getValue().getMatricula());
                                System.out.println("Nome: " + entry.getValue().getNome());
                                System.out.println("Nota: " + entry.getValue().getNota());
                                System.out.println("-----------------------------");
                            });
                        }
                        break;
                    case 3:
                        System.out.println("Digite o nome do aluno que deseja alterar a nota: ");
                        String nomePesquisa = sc.next();
                        hm.forEach((k, p) -> {
                            boolean existe = p.getNome().contains(nomePesquisa);
                            if (existe == true) {
                                //System.out.println("O valor Raphael existe: " + existe);
                                System.out.println("Digite a nova nota: ");
                                float notaAlterada = sc.nextFloat();
                                p.setNota(notaAlterada);
                            }
                        });
                        break;
                    case 4:
                        hm.entrySet().stream().map(entry -> {
                            //System.out.print("Indice: " + entry.getKey());
                            return entry;
                        }).forEachOrdered(entry -> {
                            System.out.println("ID: " + entry.getKey());
                            System.out.println("Matricula: " + entry.getValue().getMatricula());
                            System.out.println("Nome: " + entry.getValue().getNome());
                            System.out.println("Nota: " + entry.getValue().getNota());
                            System.out.println("-----------------------------");
                        });
                        System.out.println("Digite o id do aluno que deseja excluir: ");
                        int id = sc.nextInt();
                        hm.remove(id);
                        break;
                }
            } while (opcao != 0);
        }
        System.out.println("HashMap completo");
        hm.entrySet().stream().map(entry -> {
            //System.out.print("Indice: " + entry.getKey());
            return entry;
        }).forEachOrdered(entry -> {
            System.out.println("ID: " + entry.getKey());
            System.out.println("Matricula: " + entry.getValue().getMatricula());
            System.out.println("Nome: " + entry.getValue().getNome());
            System.out.println("Nota: " + entry.getValue().getNota());
        });

        hm.remove(3);
        System.out.println("HashMap apos deletar item 3");
        hm.entrySet().stream().map(entry -> {
            //System.out.print("Indice: " + entry.getKey());
            return entry;
        }).forEachOrdered(entry -> {
            System.out.println("Matricula: " + entry.getValue().getMatricula());
            System.out.println("Nome: " + entry.getValue().getNome());
            System.out.println("Nota: " + entry.getValue().getNota());
        });

        System.out.println("O HashMap está vazio: " + hm.isEmpty());
        System.out.println("Tamanho do mapa: " + hm.size());
        //System.out.println("O valor Raphael existe: " + hm.containsValue("Raphael"));
        //  In Java 8, you can loop a Map with forEach + lambda expression.
        hm.forEach((k, p) -> {
            boolean existe = p.getNome().contains("Raphael");
            if (existe == true) {
                //System.out.println("O valor Raphael existe: " + existe);
                p.setNota(5);
            }
        });

        hm.entrySet().stream().map(entry -> {
            //System.out.print("Indice: " + entry.getKey());
            return entry;
        }).forEachOrdered(entry -> {
            System.out.println("Matricula: " + entry.getValue().getMatricula());
            System.out.println("Nome: " + entry.getValue().getNome());
            System.out.println("Nota: " + entry.getValue().getNota());
        });
        System.out.println("A chave 3 existe: " + hm.containsKey(3));
        hm.clear();
        System.out.println("Elementos apos o clear(): " + hm);
    }
}
