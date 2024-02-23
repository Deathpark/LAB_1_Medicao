# Questão a ser resolvida:
RQ 03. Sistemas populares lançam releases com frequência?

Métrica: total de releases


# Query utilizada:
query {
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        releases {
          totalCount
        }
      }
    }
  }
}


# Resultado obtido: