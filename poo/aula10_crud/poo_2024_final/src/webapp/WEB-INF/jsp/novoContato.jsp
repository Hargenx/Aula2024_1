<!DOCTYPE html>
<html>

<head>
    <title>Novo Contato</title>
</head>

<body>
    <h1>Novo Contato</h1>
    <form action="/contatos" method="post">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required>
        <label for="telefone">Telefone:</label>
        <input type="text" id="telefone" name="telefone" required>
        <button type="submit">Salvar</button>
    </form>
</body>

</html>