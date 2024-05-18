<!DOCTYPE html>
<html>

<head>
    <title>Editar Contato</title>
</head>

<body>
    <h1>Editar Contato</h1>
    <form action="/contatos/editar/${contato.id}" method="post">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" value="${contato.nome}" required>
        <label for="telefone">Telefone:</label>
        <input type="text" id="telefone" name="telefone" value="${contato.telefone}" required>
        <button type="submit">Atualizar</button>
    </form>
</body>

</html>