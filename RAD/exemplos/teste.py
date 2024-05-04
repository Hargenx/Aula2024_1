dados = str(input("digite algo: ")  or 'N/A')

print(dados)

def limpaArray(arrayA: list, arrayB: list) -> list:
    """
    Takes two lists, `arrayA` and `arrayB`, and returns a new list containing the unique elements from both lists, sorted in ascending order.

    Parameters:
        arrayA (list): The first list.
        arrayB (list): The second list.

    Returns:
        list: A new list containing the unique elements from both `arrayA` and `arrayB`, sorted in ascending order.
    """
    return sorted(set(arrayA + arrayB))

a = [1, 2, 3, 3, 2, 1]
b = [7, 8, 9, 9, 8, 7]

c = limpaArray(a, b)

print(c)

lista = [
    "www.cade.com.br",
    "www.yahoo.com",
    "www.google.com.br",
    "www.altavista.com"
]

def tira_www(links: list) -> list[str]:
    """
    Removes the "www." prefix from each URL in the given list.

    Parameters:
        links (list): A list of URLs.

    Returns:
        list[str]: A new list with the "www." prefix removed from each URL.
    """
    return [url.removeprefix("www.") for url in links]


sem_www = tira_www(lista)
print(sem_www)
