
# Scripts


* Para usar os scripts nesta pasta inseridos, basta utilizar uma ferramenta que equivalente ao google colab e colar a query com a token gerada do seu github para pesquisa e executare o script para obter os resultados.
* -> Os resultados podem mudar de acordo com a época que é realizada a query. Todos os dados foram retirados no primeiro semestre de 2024. 
* -> O token utilizado foi omitido por questões de segurança

## Script:
import requests
import pandas as pd

def consultar_repositorios(page):
    token = ''

    query = """
    query pesquisa($page: String){
      search(query: "stars:>100 fork:false sort:stars-desc", type: REPOSITORY, first: 20, after: $page) {
        repositoryCount
        pageInfo {
          hasNextPage
          endCursor
        }
        nodes {
          ... on Repository {
            nameWithOwner
            createdAt
            pullRequests {
              totalCount
            }
            releases {
              totalCount
            }
            updatedAt
            primaryLanguage {
              name
            }
            issues (states: OPEN){
              totalCount
            }
            closedIssues: issues(states: CLOSED) {
              totalCount
            }
          }
        }
      }
    }
    """

    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    variables = {'page': page}

    response = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables}, headers=headers)

    if response.status_code == 200:
        global pagina

        data = response.json()

        pagina = data['data']['search']['pageInfo']['endCursor']
        return data['data']['search']['nodes']
    else:
        print('Erro ao fazer a solicitação:', response.status_code)
        return None

def exportar_para_csv(data):
    if data:
        df = pd.DataFrame(data)

        df.to_csv('dados_recebidos.csv', index=False)

        print("Dados exportados com sucesso para 'dados_recebidos.csv'")
    else:
        print("Não foi possível exportar os dados para CSV.")


## Fazer loop para pegar a página e fazer outras requisições
pagina = None
dados_totais = []
for i in range(0, 1000, 20):
  dados = consultar_repositorios(pagina)
  if dados:
      dados_totais.append(dados)

exportar_para_csv(dados_totais)

## Explicação do script