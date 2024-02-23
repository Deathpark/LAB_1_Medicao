# Questão a ser resolvida:
RQ 04. Sistemas populares são atualizados com frequência?

Métrica: tempo até a última atualização (calculado a partir da data de última atualização)


# Query utilizada:
query {
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        createdAt
      }
    }
  }
}