import requests
import pandas as pd
import os
from spicy import stats

def consultar_repositorios(page):
    token = ''

    query = """
    query pesquisa($page: String){
      search(query: "stars:>100 language:Java fork:false sort:stars-desc", type: REPOSITORY, first: 20, after: $page) {
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
        global repositorios

        data = response.json()

        pagina = data['data']['search']['pageInfo']['endCursor']

        data = data['data']['search']['nodes']

        for repo in data:
          repositorios.append(repo['nameWithOwner'])

        return data
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
repositorios = []
for i in range(0, 1000, 20):
  dados = consultar_repositorios(pagina)
  if dados:
      dados_totais.append(dados)

pacote = repositorios[0]
os.system(f'cmd "git clone https://github.com/{pacote}"')
os.system(f'cmd "java -jar ./target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar ../{pacote}/ true 0 true ../../results/"')

exportar_para_csv(dados_totais)