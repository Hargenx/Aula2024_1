package com.aula2024;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import java.util.List;

public class AlunoDAO {
    public void salvar(Aluno aluno) {
        EntityManager entityManager = JPAUtil.getEntityManager();
        EntityTransaction transaction = entityManager.getTransaction();

        try {
            transaction.begin();
            entityManager.persist(aluno);
            transaction.commit();
        } catch (Exception e) {
            if (transaction != null) {
                transaction.rollback();
            }
            e.printStackTrace();
        } finally {
            entityManager.close();
        }
    }

    public List<Aluno> buscarTodos() {
        EntityManager entityManager = JPAUtil.getEntityManager();
        List<Aluno> alunos = entityManager.createQuery("SELECT a FROM Aluno a", Aluno.class).getResultList();
        entityManager.close();
        return alunos;
    }
}
