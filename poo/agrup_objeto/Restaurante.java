package poo.agrup_objeto;

import java.util.ArrayList;
import java.util.Deque;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;

public class Restaurante {
    public static void main(String[] args) {
        // Usando Set para armazenar os pratos únicos pedidos
        Set<String> pratosUnicos = new HashSet<>();

        // Usando List para armazenar a ordem dos pedidos
        List<Pedido> pedidos = new ArrayList<>();

        // Usando Queue para simular a fila de pedidos
        Queue<Pedido> filaPedidos = new LinkedList<>();

        // Usando Deque para simular as ações do chef (retirar da fila e preparar)
        Deque<Pedido> acoesChef = new LinkedList<>();

        // Adicionando alguns pedidos
        Pedido pedido1 = new Pedido(1, "Pizza Margherita");
        Pedido pedido2 = new Pedido(2, "Hamburguer com batatas fritas");
        Pedido pedido3 = new Pedido(3, "Salada Caesar");

        pratosUnicos.add(pedido1.getPrato());
        pratosUnicos.add(pedido2.getPrato());
        pratosUnicos.add(pedido3.getPrato());

        pedidos.add(pedido1);
        pedidos.add(pedido2);
        pedidos.add(pedido3);

        filaPedidos.add(pedido1);
        filaPedidos.add(pedido2);
        filaPedidos.add(pedido3);

        // Simulando a ação do chef retirando da fila e preparando
        // Retira o primeiro pedido da fila e coloca na ação do chef
        acoesChef.offer(filaPedidos.poll()); 
        // Retira o segundo pedido da fila e coloca na ação do chef
        acoesChef.offer(filaPedidos.poll()); 

        // Exibindo informações
        System.out.println("Pratos Únicos Pedidos: " + pratosUnicos);
        System.out.println("Ordem dos Pedidos: " + pedidos);
        System.out.println("Fila de Pedidos: " + filaPedidos);
        System.out.println("Ações do Chef: " + acoesChef);
    }
}
