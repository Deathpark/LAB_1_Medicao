import requests
import pandas as pd
import os
import numpy as np
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

def exportar_para_csv(data, nome):
    if data:
        df = pd.DataFrame(data)

        df.to_csv(nome, index=False)

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

exportar_para_csv(dados_totais, 'dados_recebidos.csv')

dadosMetricas = []
for i in range(0, 1000):
  pacote = repositorios[i]
  projeto = pacote.split("/")
  os.system(f'git clone https://github.com/{pacote}')
  os.system(f'java -jar ./ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar ./{projeto[1]}/ true 0 true ./results/')
  os.system(f'rm -rf ./{pacote}')

  with open('./results/class.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    contador = 0
    cboSys = 0
    ditSys = 0
    lcomSys = 0
    for linha in linhas:
      if(contador > 0 and (not linha.isspace())):
        dados = linha.split(",")
        cbo = dados[3]
        cboModified = dados[4]
        dit = dados[8]
        lcom = dados[11]
        lcom2 = dados[12]
        
        if(cboSys < cbo):
          cboSys = cbo
        if(ditSys < dit):
          ditSys = dit
        if(lcomSys < lcom):
          lcomSys = lcom
    
    if(cboSys != 0 or ditSys != 0 or lcomSys != 0):
      metrica = "Projeto:" + pacote + ",CBO:" + cboSys + ",DIT:" + ditSys + ",LCOM:" + lcomSys
      dadosMetricas.append(metrica)

exportar_para_csv(dados_totais, 'metricas.csv')


with open('./metricas.csv', 'r') as dados:
  linhas = arquivo.readlines()
  cbo = []
  dit = []
  lcom = []

  for linha in linhas:
    dados = linha.split(",")
    cbo.append(dados[1].split(":")[1])
    dit.append(dados[2].split(":")[1])
    lcom.append(dados[3].split(":")[1])

print("CBO")
print(np.median(cbo))
print("DIT")
print(np.median(dit))
print("LCOM")
print(np.median(lcom))
