from mrjob.job import MRJob
import re

palavras_regex = re.compile(r"[\w']+")

class QuantidadePalavras(MRJob):
    def mappear(self, _, linha):
        for palavra in palavras_regex.findall(linha):
            yield (palavra.lower(), 1)

    def reducer(self, palavra, quantidade):
        yield (palavra, sum(quantidade))

if __name__ == "__main__":
    QuantidadePalavras(args=["-r", "local"]).run()