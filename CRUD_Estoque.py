class GerenciamentoEstoque:
    def __init__(self):
        self.produtos = []  # Inicialmente, a lista de produtos está vazia.
    
    def AdicionarProduto(self, NomeProduto, quantidade, valor, categoria):

        codigo_produto = len(self.produtos) + 1 #Gerar ID auto incrementado
        
        if not isinstance(NomeProduto, str) or not isinstance(categoria, str): #Verifica se um valor tem o tipo definido
            raise ValueError('Nome ou a Categoria do produto possuem informações invalidas')
        
        NomeProduto = NomeProduto.upper()
        categoria = categoria.upper()

        if not isinstance(quantidade, int) or not isinstance(valor, (int,float)):
            try:
                quantidade = int(quantidade)
                valor = float(valor)
                if quantidade < 0 or valor < 0:
                    print('O valor precisa ser positivo')
            except ValueError:
                raise ValueError('Você forneceu valores negativos ou inválidos')

        novo_produto = {
            'Produto': NomeProduto,
            'Quantidade': quantidade,
            'Preco': round(float(valor), 2),
            'Categoria': categoria,
            'ID_Produto': codigo_produto
            } # Cria um de para com o nome das categorias

        self.produtos.append(novo_produto)
        print(f'O produto {NomeProduto} foi adicionado ao estoque')
   
    def VisualizarProdutos(self):
        if self.produtos:
            print("Produtos no estoque:")
            for produto in self.produtos:
                print(f"ID: {produto['ID_Produto']}, Produto: {produto['Produto']}, Quantidade: {produto['Quantidade']}, Preço: {produto['Preco']}, Categoria: {produto['Categoria']}")
        else:
            print('Nenhum produto encontrado no estoque.')

    def BuscarProdutoPorID(self, ID_produto):
        for produto in self.produtos:
            if produto['ID_Produto'] == ID_produto:
                return produto
        print(f' O produto com o código {ID_produto} não foi encontrado') #Precisa ser fora do IF pois senão iria parar no primeiro produto que nao possui match
    
    def RemoverProduto(self,ID_produto):  

        #Entrar na lista codigo_produto e procurar esse produto lá
        produto = self.BuscarProdutoPorID(ID_produto)
        NomeProduto = produto['Produto']
        if produto:
            self.produtos.remove(produto)
            print(f'O produto {NomeProduto} foi removido do estoque')
        else:
            print(f' O produto com o código fornecido {ID_produto} não foi encontrado') #Precisa ser fora do IF pois senão iria parar no primeiro produto que nao possui match
    
    def AtualizarProduto(self, ID_produto, Nova_Informacao):
        produto = self.BuscarProdutoPorID(ID_produto)

        if produto:
            print('Opcao que deseja atualizar:')
            print('1- Alterar quantidade de estoque')
            print('2- Alterar valor')
            print('3- Mudar Nome do Produto')
            print('4- Alterar Categoria')

            try:
                escolha = int(input('Escolha o número da opção: '))
            except ValueError:
                raise ValueError('Insira um número válido de 1 - 4')

            # Verifica se a escolha está dentro do intervalo válido
            if escolha not in [1, 2, 3, 4]:
                raise ValueError('Insira um número válido de 1 - 4')

            # Acessa o nome do produto diretamente do dicionário
            NomeProduto = produto['Produto']

            if escolha == 1:
                produto['quantidade'] = Nova_Informacao
                print(f'O produto {NomeProduto} agora possui {Nova_Informacao} de quantidade em estoque')

            elif escolha == 2:
                produto['valor'] = Nova_Informacao
                print(f'O produto {NomeProduto} agora possui o valor de: {Nova_Informacao}')

            elif escolha == 3:
                produto['NomeProduto'] = Nova_Informacao
                print(f'O nome do produto foi alterado para {Nova_Informacao} no estoque')

            elif escolha == 4:
                produto['categoria'] = Nova_Informacao
                print(f'A categoria do produto {NomeProduto} foi alterada para {Nova_Informacao}')

    def ExportarParaCSV(self, arquivo):
        df_produtos = pd.DataFrame(self.produtos)  # Criar DataFrame a partir da lista de produtos
        df_produtos.to_csv(arquivo, index=False)  # Exportar DataFrame para CSV

estoque = GerenciamentoEstoque() #Instancia de uma classe
estoque.AdicionarProduto('Caneta', 500, 2.50, 'Material Escolar')
estoque.AdicionarProduto('Lápis', 400, 1.50, 'Material Escolar')
estoque.AdicionarProduto('Borracha', 300, 1.00, 'Material Escolar')
estoque.AdicionarProduto('Tesoura', 150, 7.00, 'Material Escolar')
estoque.AdicionarProduto('Cola', 200, 4.00, 'Material Escolar')
estoque.AdicionarProduto('Grampeador', 50, 25.00, 'Material Escolar')
estoque.AdicionarProduto('Fita Adesiva', 180, 3.50, 'Material Escolar')
estoque.AdicionarProduto('Apontador', 250, 1.50, 'Material Escolar')
estoque.AdicionarProduto('Marcador de Texto', 100, 3.00, 'Material Escolar')
estoque.AdicionarProduto('Pasta', 90, 10.00, 'Material Escolar')

estoque.AdicionarProduto('Macarrão', 500, 5.00, 'Alimentos')
estoque.AdicionarProduto('Açúcar', 600, 4.00, 'Alimentos')
estoque.AdicionarProduto('Sal', 400, 2.00, 'Alimentos')
estoque.AdicionarProduto('Óleo de Soja', 350, 8.00, 'Alimentos')
estoque.AdicionarProduto('Farinha de Trigo', 300, 6.50, 'Alimentos')
estoque.AdicionarProduto('Leite', 700, 4.50, 'Alimentos')
estoque.AdicionarProduto('Café', 200, 15.00, 'Alimentos')
estoque.AdicionarProduto('Manteiga', 180, 8.00, 'Alimentos')
estoque.AdicionarProduto('Refrigerante', 400, 7.00, 'Alimentos')
estoque.AdicionarProduto('Molho de Tomate', 300, 3.00, 'Alimentos')

estoque.AdicionarProduto('Tênis', 60, 120.00, 'Vestuário')
estoque.AdicionarProduto('Casaco', 40, 150.00, 'Vestuário')
estoque.AdicionarProduto('Meia', 500, 5.00, 'Vestuário')
estoque.AdicionarProduto('Sapato', 70, 130.00, 'Vestuário')
estoque.AdicionarProduto('Camisa', 100, 30.00, 'Vestuário')
estoque.AdicionarProduto('Jaqueta', 30, 180.00, 'Vestuário')
estoque.AdicionarProduto('Saia', 50, 40.00, 'Vestuário')
estoque.AdicionarProduto('Vestido', 70, 80.00, 'Vestuário')
estoque.AdicionarProduto('Shorts', 90, 35.00, 'Vestuário')
estoque.AdicionarProduto('Sutiã', 120, 25.00, 'Vestuário')

estoque.AdicionarProduto('Celular', 30, 1500.00, 'Eletrônicos')
estoque.AdicionarProduto('Notebook', 20, 3000.00, 'Eletrônicos')
estoque.AdicionarProduto('Fone de Ouvido', 100, 150.00, 'Eletrônicos')
estoque.AdicionarProduto('Carregador', 80, 50.00, 'Eletrônicos')
estoque.AdicionarProduto('Mouse', 120, 40.00, 'Eletrônicos')
estoque.AdicionarProduto('Teclado', 100, 80.00, 'Eletrônicos')
estoque.AdicionarProduto('Monitor', 50, 700.00, 'Eletrônicos')
estoque.AdicionarProduto('Câmera', 40, 1200.00, 'Eletrônicos')
estoque.AdicionarProduto('Smartwatch', 60, 800.00, 'Eletrônicos')
estoque.AdicionarProduto('Impressora', 25, 600.00, 'Eletrônicos')

estoque.AdicionarProduto('Shampoo', 200, 20.00, 'Higiene')
estoque.AdicionarProduto('Condicionador', 180, 22.00, 'Higiene')
estoque.AdicionarProduto('Sabonete', 400, 3.00, 'Higiene')
estoque.AdicionarProduto('Pasta de Dente', 300, 5.00, 'Higiene')
estoque.AdicionarProduto('Escova de Dente', 250, 4.00, 'Higiene')
estoque.AdicionarProduto('Desodorante', 220, 10.00, 'Higiene')
estoque.AdicionarProduto('Creme Hidratante', 150, 25.00, 'Higiene')
estoque.AdicionarProduto('Papel Higiênico', 500, 12.00, 'Higiene')
estoque.AdicionarProduto('Álcool em Gel', 300, 8.00, 'Higiene')
estoque.AdicionarProduto('Perfume', 100, 100.00, 'Higiene')

estoque.ExportarParaCSV('estoque.csv')
