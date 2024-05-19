package com.poo_2024_final.service;

import com.poo_2024_final.model.Contato;
import com.poo_2024_final.repository.ContatoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ContatoService {
    @Autowired
    private ContatoRepository contatoRepository;

    public List<Contato> listarContatos() {
        return contatoRepository.findAll();
    }

    public Contato adicionarContato(Contato contato) {
        return contatoRepository.save(contato);
    }

    public Contato atualizarContato(Contato contato) {
        return contatoRepository.save(contato);
    }

    public void excluirContato(int id) {
        contatoRepository.deleteById(id);
    }
}