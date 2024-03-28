import re
import logging
import os


def extrair_emails(texto: str) -> list:
    """
    Extrai emails de um texto.

    Parâmetros:
        texto (str): Texto do qual os emails serão extraídos.

    Retorna:
        list: Lista contendo os emails extraídos.
    """
    try:
        emails = re.findall(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", texto
        )
        return emails
    except Exception as e:
        logging.error(f"Erro ao extrair emails: {e}")
        return []


def salvar_emails_em_log(emails: list, nome_arquivo: str) -> None:
    """
    Salva emails em um arquivo de log.

    Parâmetros:
        emails (list): Lista de emails a serem salvos.
        nome_arquivo (str): Caminho completo do arquivo de log.

    Retorna:
        None
    """
    try:
        logging.basicConfig(filename=nome_arquivo, level=logging.INFO)
        for email in emails:
            logging.info(email)
        print(f"E-mails salvos em {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar em {nome_arquivo}: {e}")


if __name__ == "__main__":
    texto = "Olá, meu email é contato@example.com e o outro é contato2@example.com.br."
    emails = extrair_emails(texto)
    print(emails)
    if emails:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        nome_arquivo_saida = os.path.join(diretorio_atual, "emails.log")

        salvar_emails_em_log(emails, nome_arquivo_saida)
