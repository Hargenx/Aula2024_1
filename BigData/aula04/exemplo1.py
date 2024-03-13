from mrjob.job import MRJob
class VendasTotais(MRJob):
    def configure_args(self):
        super(VendasTotais, self).configure_args()
        self.add_passthru_arg('--output-format', choices=['json', 'csv'], default='csv', help='Escolha um formato de saída: json ou csv')
    def mapper(self, _, linha):
        if not linha.startswith("produto_id"): # Pula o cabeçalho
            produto_id, _, quantidade, preco_unitario = linha.split(',')
            total_venda = int(quantidade) * float(preco_unitario)
            yield produto_id, total_venda
    def reducer(self, produto_id, valores):
        yield produto_id, sum(valores)
if __name__ == "__main__":
    VendasTotais.run()
 
