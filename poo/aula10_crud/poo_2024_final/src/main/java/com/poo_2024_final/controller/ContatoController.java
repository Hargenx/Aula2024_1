package com.poo_2024_final.controller;

import com.poo_2024_final.model.Contato;
import com.poo_2024_final.service.ContatoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class ContatoController {

    @Autowired
    private ContatoService contatoService;

    @GetMapping("/contatos")
    public String listarContatos(Model model) {
        List<Contato> contatos = contatoService.listarContatos();
        model.addAttribute("contatos", contatos);
        return "listarContatos";
    }

    @GetMapping("/contatos/novo")
    public String novoContatoForm(Model model) {
        model.addAttribute("contato", new Contato());
        return "incluirContato"; // Mudança para corresponder ao nome correto do arquivo JSP
    }

    @PostMapping("/contatos")
    public String adicionarContato(@ModelAttribute Contato contato) {
        contatoService.adicionarContato(contato);
        return "redirect:/contatos";
    }

    @GetMapping("/contatos/editar/{id}")
    public String editarContatoForm(@PathVariable int id, Model model) {
        Contato contato = contatoService.listarContatos().stream().filter(c -> c.getId() == id).findFirst()
                .orElse(null);
        if (contato != null) {
            model.addAttribute("contato", contato);
            return "editarContato"; // Mudança para corresponder ao nome correto do arquivo JSP
        }
        return "redirect:/contatos";
    }

    @PostMapping("/contatos/editar/{id}")
    public String atualizarContato(@PathVariable int id, @ModelAttribute Contato contato) {
        contato.setId(id);
        contatoService.atualizarContato(contato);
        return "redirect:/contatos";
    }

    @GetMapping("/contatos/excluir/{id}")
    public String excluirContato(@PathVariable int id) {
        contatoService.excluirContato(id);
        return "redirect:/contatos";
    }
}
