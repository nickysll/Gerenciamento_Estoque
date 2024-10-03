# Sistema de Gerenciamento de Estoque

## Descrição
Este projeto consiste em um sistema que permite adicionar, remover e atualizar produtos em um estoque. Cada produto possui atributos como nome, quantidade, preço, categoria, entre outros. O sistema oferece funcionalidades para gerenciar o estoque e gerar relatórios.

## Funcionalidades
- **CRUD de produtos:** Permite criar, ler, atualizar e deletar produtos do estoque.
- **Relatórios de estoque baixo:** Gera relatórios com produtos que estão com estoque baixo.
- **Cálculo do valor total do estoque:** Calcula e exibe o valor total do estoque com base nos produtos cadastrados.
- **Exportação de relatórios:** Possibilita a exportação de relatórios em formatos CSV ou Excel.

## Requisitos
O sistema precisa oferecer as seguintes funcionalidades:
1. **Adicionar Produto:** Adicionar um novo produto ao estoque com nome, quantidade, preço, categoria e código do produto.
2. **Remover Produto:** Remover um produto existente digitando seu código. O sistema exibirá as informações do produto e solicitará a confirmação da exclusão.
3. **Atualizar Produto:** Atualizar as informações de um produto existente com base no código do produto.
4. **Relatórios Analíticos:** Gerar relatórios que mostrem itens em estoque, ticket médio de venda, etc.
5. **Exportação de Dados:** Permitir a exportação de dados para CSV ou Excel, além de possibilitar a importação de informações de uma planilha.

## Como Usar
### Adicionar Produto
Para adicionar um produto, utilize o método `AdicionarProduto` e forneça os seguintes parâmetros:
- `NomeProduto`: Nome do produto.
- `quantidade`: Quantidade do produto em estoque.
- `valor`: Preço do produto.
- `categoria`: Categoria do produto.

### Remover Produto
Para remover um produto, utilize o método `RemoverProduto` e forneça o código do produto.

### Atualizar Produto
Para atualizar um produto, utilize o método `AtualizarProduto` e forneça o código do produto e a nova informação desejada.

### Exportar para CSV
Para exportar o estoque atual para um arquivo CSV, utilize o método `ExportarParaCSV` e forneça o nome do arquivo.

## Ferramentas de Armazenamento
Os dados do estoque são armazenados em um arquivo CSV. Você pode facilmente importar e exportar esses dados conforme necessário.

## Dependências
Este projeto utiliza as seguintes bibliotecas:
- `pandas` para manipulação de dados.
- `matplotlib` e `plotly` para visualização de dados.
- `streamlit` para a interface gráfica do usuário (GUI).

## Exemplo de Uso
Abaixo está um exemplo de como utilizar o sistema:

```python
estoque = GerenciamentoEstoque()
estoque.AdicionarProduto('Caneta', 500, 2.50, 'Material Escolar')
estoque.VisualizarProdutos()
estoque.RemoverProduto(1)
estoque.AtualizarProduto(2, {'Quantidade': 300})
estoque.ExportarParaCSV('estoque.csv')
