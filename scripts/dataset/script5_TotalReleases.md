# Questão a ser resolvida:
RQ 05. Sistemas populares são escritos nas linguagens mais populares?

Métrica: linguagem primária de cada um desses repositórios


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