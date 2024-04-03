
LAB 2: Um Estudo das Características de Qualidade de Sistemas Java

#### Introdução
A linguagem Java é definitivamente uma das linguagens mais utilizadas em todo o globo terrestre, sua criação e ferramentas foram tão impactantes na comunidade dev, solidificando paradigmas (Programação Orientada a Objeto) e sendo utilizada como base para outras ferramentas, tais como, **C#** e **Kotlin**.
Por conta de sua robustez e compatibilidade ela foi adotada por muitos times de desenvolvimento pelo mundo a fora, possuindo uma grande comunidade nos dias atuais, o objetivo desse trabalho é analisar se os maiores repositórios dessa tecnologias no github possuem bons índices de qualidade.

As seguintes perguntas foram definidas para essa pesquisa e a partir delas definimos hipóteses dos resultados

RQ 01: Qual a relação entre a popularidade dos repositórios e as suas características de qualidade?\
HI 01: Repositórios de Java mais populares, medidos pelo número de estrelas, forks e contribuidores, tendem a ter uma maior qualidade de código devido a maior contribuições da comunidade, resultando em menos defeitos e melhor documentação.

RQ 02: Qual a relação entre a maturidade do repositórios e as suas características de qualidade?\
HI 02: Repositórios de Java mais maduros, medidos pela idade desde sua criação,  provavelmente têm uma qualidade de código melhor, pois passaram por mais ciclos de desenvolvimento, revisões e refinamentos ao longo do tempo.

RQ 03: Qual a relação entre a atividade dos repositórios e as suas características de qualidade?\
HI 03: Repositórios de Java mais ativos, caracterizados por uma alta frequência de commits, issues abertos e resolvidos, e pull requests aceitos, provavelmente têm uma qualidade de código superior devido à constante manutenção e melhoria contínua do código fonte.

RQ 04: Qual a relação entre o tamanho dos repositórios e as suas características de qualidade?\
HI 04: Repositórios de Java com um maior número de linhas de código (LOC) podem ter uma qualidade de código variável. Embora repositórios maiores possam conter mais funcionalidades e soluções complexas, aumentando a probabilidade de bugs, mas ainda sim possuir uma robustez e boas práticas. Portanto, a qualidade de um repositório pode depender não apenas do tamanho absoluto, mas como isso está refletindo a clareza e a manutenibilidade do código.

#### Metodologia
**Ferramentas:**
* [Python](https://www.python.org/)
* [Github GraphQL API](https://docs.github.com/pt/graphql/reference/queries)
* [ck](https://github.com/mauricioaniche/ck)

A partir da query:

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

Foram recolhidos os repositórios desejados pela api do _github_ e armazenados em um arquivo de texto como uma tabela csv.

Com o link de cada repositório foi utilizado um script para calcular a qualidade do código com algumas métricas recolhidas pela ferramenta ck:

    dadosMetricas = []
    for i in range(0, 1000):
      pacote = repositorios[i]
      projeto = pacote.split("/")
      os.system(f'git clone https://github.com/{pacote}')
      os.system(f'java -jar ./ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar ./{projeto[1]}/ true 0 true ./results/')
      os.system(f'rm -rf ./{pacote}')
    
      # Lê os dados de class
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
          metrica = "Projeto: " + pacote + ", CBO: " + cboSys + ", DIT:" + ditSys + ", LCOM:" + lcomSys
          dadosMetricas.append(metrica)
    
    exportar_para_csv(dados_totais, 'metricas.csv')

 As métricas analisadas nesse trabalho foram:
* CBO: Coupling between objects
* DIT: Depth Inheritance Tree
* LCOM: Lack of Cohesion of Methods

(iii) os resultados obtidos para cada uma delas; 
(iv) a discussão sobre o que você esperava como resultado (suas hipóteses) e os valores obtidos.  

### Enunciation:

<Adicionar nessa parte o enunciado do laboratório prático>

## Integrantes do grupo:
### Group members

* Richbert Stephano de Faria Oliveira
* Sara Lourenço Iglesias
* Nelson Nolasco
* Yghor Ribas Gomes

## Artefatos:

* [Relatório](docs/README.md)
* [Scripts](scripts)
* [Conjunto de dados](scripts/dataset)
  

### Artifacts

* [Reports](docs/README.md)
* [Scripts](scripts)
* [Datasets](scripts/dataset)
  
