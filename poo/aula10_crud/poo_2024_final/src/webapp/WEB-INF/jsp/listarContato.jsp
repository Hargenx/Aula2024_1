<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
    <!DOCTYPE html>
    <html>

    <head>
        <title>Lista de Contatos</title>
        <link rel="stylesheet" href="<c:url value='/css/style.css' />">
    </head>

    <body>
        <h1>Lista de Contatos</h1>
        <a href="/contatos/novo">Novo Contato</a>
        <ul>
            <c:forEach var="contato" items="${contatos}">
                <li>${contato.nome} - ${contato.telefone}
                    <a href="/contatos/editar/${contato.id}">Editar</a>
                    <a href="/contatos/excluir/${contato.id}">Excluir</a>
                </li>
            </c:forEach>
        </ul>
    </body>

    </html>