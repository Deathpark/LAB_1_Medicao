# Questão a ser resolvida:
RQ 06. Sistemas populares possuem um alto percentual de issues fechadas?

Métrica: razão entre número de issues fechadas pelo total de issues


# Query utilizada:
query {
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
				issues (states: OPEN){
          totalCount
        }
        closedIssues: issues(states:CLOSED) {
          totalCount
        }
      }
    }
  }
}


# Resultado obtido:
{
  "data": {
    "search": {
      "nodes": [
        {
          "nameWithOwner": "freeCodeCamp/freeCodeCamp",
          "issues": {
            "totalCount": 267
          },
          "closedIssues": {
            "totalCount": 17403
          }
        },
        {
          "nameWithOwner": "EbookFoundation/free-programming-books",
          "issues": {
            "totalCount": 24
          },
          "closedIssues": {
            "totalCount": 1038
          }
        },
        {
          "nameWithOwner": "sindresorhus/awesome",
          "issues": {
            "totalCount": 22
          },
          "closedIssues": {
            "totalCount": 312
          }
        },
        {
          "nameWithOwner": "public-apis/public-apis",
          "issues": {
            "totalCount": 9
          },
          "closedIssues": {
            "totalCount": 547
          }
        },
        {
          "nameWithOwner": "jwasham/coding-interview-university",
          "issues": {
            "totalCount": 45
          },
          "closedIssues": {
            "totalCount": 369
          }
        },
        {
          "nameWithOwner": "996icu/996.ICU",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 0
          }
        },
        {
          "nameWithOwner": "kamranahmedse/developer-roadmap",
          "issues": {
            "totalCount": 723
          },
          "closedIssues": {
            "totalCount": 1068
          }
        },
        {
          "nameWithOwner": "codecrafters-io/build-your-own-x",
          "issues": {
            "totalCount": 176
          },
          "closedIssues": {
            "totalCount": 426
          }
        },
        {
          "nameWithOwner": "donnemartin/system-design-primer",
          "issues": {
            "totalCount": 197
          },
          "closedIssues": {
            "totalCount": 80
          }
        },
        {
          "nameWithOwner": "facebook/react",
          "issues": {
            "totalCount": 1167
          },
          "closedIssues": {
            "totalCount": 11547
          }
        },
        {
          "nameWithOwner": "vuejs/vue",
          "issues": {
            "totalCount": 356
          },
          "closedIssues": {
            "totalCount": 9657
          }
        },
        {
          "nameWithOwner": "vinta/awesome-python",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 0
          }
        },
        {
          "nameWithOwner": "tensorflow/tensorflow",
          "issues": {
            "totalCount": 1901
          },
          "closedIssues": {
            "totalCount": 36860
          }
        },
        {
          "nameWithOwner": "trekhleb/javascript-algorithms",
          "issues": {
            "totalCount": 124
          },
          "closedIssues": {
            "totalCount": 215
          }
        },
        {
          "nameWithOwner": "TheAlgorithms/Python",
          "issues": {
            "totalCount": 28
          },
          "closedIssues": {
            "totalCount": 1411
          }
        },
        {
          "nameWithOwner": "getify/You-Dont-Know-JS",
          "issues": {
            "totalCount": 80
          },
          "closedIssues": {
            "totalCount": 844
          }
        },
        {
          "nameWithOwner": "CyC2018/CS-Notes",
          "issues": {
            "totalCount": 129
          },
          "closedIssues": {
            "totalCount": 446
          }
        },
        {
          "nameWithOwner": "awesome-selfhosted/awesome-selfhosted",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 804
          }
        },
        {
          "nameWithOwner": "ohmyzsh/ohmyzsh",
          "issues": {
            "totalCount": 123
          },
          "closedIssues": {
            "totalCount": 4514
          }
        },
        {
          "nameWithOwner": "twbs/bootstrap",
          "issues": {
            "totalCount": 395
          },
          "closedIssues": {
            "totalCount": 21899
          }
        },
        {
          "nameWithOwner": "torvalds/linux",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 0
          }
        },
        {
          "nameWithOwner": "flutter/flutter",
          "issues": {
            "totalCount": 12217
          },
          "closedIssues": {
            "totalCount": 80002
          }
        },
        {
          "nameWithOwner": "ossu/computer-science",
          "issues": {
            "totalCount": 16
          },
          "closedIssues": {
            "totalCount": 613
          }
        },
        {
          "nameWithOwner": "Significant-Gravitas/AutoGPT",
          "issues": {
            "totalCount": 86
          },
          "closedIssues": {
            "totalCount": 2071
          }
        },
        {
          "nameWithOwner": "practical-tutorials/project-based-learning",
          "issues": {
            "totalCount": 52
          },
          "closedIssues": {
            "totalCount": 63
          }
        },
        {
          "nameWithOwner": "microsoft/vscode",
          "issues": {
            "totalCount": 7405
          },
          "closedIssues": {
            "totalCount": 164700
          }
        },
        {
          "nameWithOwner": "github/gitignore",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 0
          }
        },
        {
          "nameWithOwner": "jackfrued/Python-100-Days",
          "issues": {
            "totalCount": 523
          },
          "closedIssues": {
            "totalCount": 106
          }
        },
        {
          "nameWithOwner": "jlevy/the-art-of-command-line",
          "issues": {
            "totalCount": 108
          },
          "closedIssues": {
            "totalCount": 131
          }
        },
        {
          "nameWithOwner": "Snailclimb/JavaGuide",
          "issues": {
            "totalCount": 57
          },
          "closedIssues": {
            "totalCount": 917
          }
        },
        {
          "nameWithOwner": "airbnb/javascript",
          "issues": {
            "totalCount": 89
          },
          "closedIssues": {
            "totalCount": 1201
          }
        },
        {
          "nameWithOwner": "ytdl-org/youtube-dl",
          "issues": {
            "totalCount": 3763
          },
          "closedIssues": {
            "totalCount": 22708
          }
        },
        {
          "nameWithOwner": "trimstray/the-book-of-secret-knowledge",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 0
          }
        },
        {
          "nameWithOwner": "AUTOMATIC1111/stable-diffusion-webui",
          "issues": {
            "totalCount": 1890
          },
          "closedIssues": {
            "totalCount": 5190
          }
        },
        {
          "nameWithOwner": "labuladong/fucking-algorithm",
          "issues": {
            "totalCount": 358
          },
          "closedIssues": {
            "totalCount": 452
          }
        },
        {
          "nameWithOwner": "huggingface/transformers",
          "issues": {
            "totalCount": 754
          },
          "closedIssues": {
            "totalCount": 13385
          }
        },
        {
          "nameWithOwner": "vercel/next.js",
          "issues": {
            "totalCount": 2505
          },
          "closedIssues": {
            "totalCount": 17065
          }
        },
        {
          "nameWithOwner": "Chalarangelo/30-seconds-of-code",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 294
          }
        },
        {
          "nameWithOwner": "golang/go",
          "issues": {
            "totalCount": 8656
          },
          "closedIssues": {
            "totalCount": 51828
          }
        },
        {
          "nameWithOwner": "avelino/awesome-go",
          "issues": {
            "totalCount": 1
          },
          "closedIssues": {
            "totalCount": 620
          }
        },
        {
          "nameWithOwner": "facebook/react-native",
          "issues": {
            "totalCount": 838
          },
          "closedIssues": {
            "totalCount": 24622
          }
        },
        {
          "nameWithOwner": "electron/electron",
          "issues": {
            "totalCount": 855
          },
          "closedIssues": {
            "totalCount": 18506
          }
        },
        {
          "nameWithOwner": "justjavac/free-programming-books-zh_CN",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 0
          }
        },
        {
          "nameWithOwner": "yangshun/tech-interview-handbook",
          "issues": {
            "totalCount": 28
          },
          "closedIssues": {
            "totalCount": 60
          }
        },
        {
          "nameWithOwner": "d3/d3",
          "issues": {
            "totalCount": 6
          },
          "closedIssues": {
            "totalCount": 2181
          }
        },
        {
          "nameWithOwner": "kubernetes/kubernetes",
          "issues": {
            "totalCount": 1938
          },
          "closedIssues": {
            "totalCount": 42739
          }
        },
        {
          "nameWithOwner": "axios/axios",
          "issues": {
            "totalCount": 505
          },
          "closedIssues": {
            "totalCount": 3975
          }
        },
        {
          "nameWithOwner": "microsoft/PowerToys",
          "issues": {
            "totalCount": 5504
          },
          "closedIssues": {
            "totalCount": 20908
          }
        },
        {
          "nameWithOwner": "nodejs/node",
          "issues": {
            "totalCount": 1522
          },
          "closedIssues": {
            "totalCount": 15747
          }
        },
        {
          "nameWithOwner": "facebook/create-react-app",
          "issues": {
            "totalCount": 1702
          },
          "closedIssues": {
            "totalCount": 6528
          }
        },
        {
          "nameWithOwner": "f/awesome-chatgpt-prompts",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 0
          }
        },
        {
          "nameWithOwner": "Genymobile/scrcpy",
          "issues": {
            "totalCount": 1672
          },
          "closedIssues": {
            "totalCount": 2552
          }
        },
        {
          "nameWithOwner": "mrdoob/three.js",
          "issues": {
            "totalCount": 360
          },
          "closedIssues": {
            "totalCount": 11810
          }
        },
        {
          "nameWithOwner": "microsoft/TypeScript",
          "issues": {
            "totalCount": 5571
          },
          "closedIssues": {
            "totalCount": 33836
          }
        },
        {
          "nameWithOwner": "goldbergyoni/nodebestpractices",
          "issues": {
            "totalCount": 33
          },
          "closedIssues": {
            "totalCount": 283
          }
        },
        {
          "nameWithOwner": "angular/angular",
          "issues": {
            "totalCount": 1389
          },
          "closedIssues": {
            "totalCount": 25513
          }
        },
        {
          "nameWithOwner": "microsoft/terminal",
          "issues": {
            "totalCount": 1473
          },
          "closedIssues": {
            "totalCount": 10642
          }
        },
        {
          "nameWithOwner": "denoland/deno",
          "issues": {
            "totalCount": 1789
          },
          "closedIssues": {
            "totalCount": 7589
          }
        },
        {
          "nameWithOwner": "mui/material-ui",
          "issues": {
            "totalCount": 1578
          },
          "closedIssues": {
            "totalCount": 17099
          }
        },
        {
          "nameWithOwner": "rust-lang/rust",
          "issues": {
            "totalCount": 9067
          },
          "closedIssues": {
            "totalCount": 42579
          }
        },
        {
          "nameWithOwner": "ant-design/ant-design",
          "issues": {
            "totalCount": 967
          },
          "closedIssues": {
            "totalCount": 27782
          }
        },
        {
          "nameWithOwner": "ryanmcdermott/clean-code-javascript",
          "issues": {
            "totalCount": 68
          },
          "closedIssues": {
            "totalCount": 83
          }
        },
        {
          "nameWithOwner": "puppeteer/puppeteer",
          "issues": {
            "totalCount": 296
          },
          "closedIssues": {
            "totalCount": 6258
          }
        },
        {
          "nameWithOwner": "iluwatar/java-design-patterns",
          "issues": {
            "totalCount": 200
          },
          "closedIssues": {
            "totalCount": 699
          }
        },
        {
          "nameWithOwner": "PanJiaChen/vue-element-admin",
          "issues": {
            "totalCount": 1224
          },
          "closedIssues": {
            "totalCount": 2346
          }
        },
        {
          "nameWithOwner": "GrowingGit/GitHub-Chinese-Top-Charts",
          "issues": {
            "totalCount": 148
          },
          "closedIssues": {
            "totalCount": 154
          }
        },
        {
          "nameWithOwner": "521xueweihan/HelloGitHub",
          "issues": {
            "totalCount": 93
          },
          "closedIssues": {
            "totalCount": 2491
          }
        },
        {
          "nameWithOwner": "storybookjs/storybook",
          "issues": {
            "totalCount": 1696
          },
          "closedIssues": {
            "totalCount": 10378
          }
        },
        {
          "nameWithOwner": "papers-we-love/papers-we-love",
          "issues": {
            "totalCount": 17
          },
          "closedIssues": {
            "totalCount": 217
          }
        },
        {
          "nameWithOwner": "nvbn/thefuck",
          "issues": {
            "totalCount": 243
          },
          "closedIssues": {
            "totalCount": 467
          }
        },
        {
          "nameWithOwner": "ripienaar/free-for-dev",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 0
          }
        },
        {
          "nameWithOwner": "godotengine/godot",
          "issues": {
            "totalCount": 9675
          },
          "closedIssues": {
            "totalCount": 38691
          }
        },
        {
          "nameWithOwner": "microsoft/Web-Dev-For-Beginners",
          "issues": {
            "totalCount": 52
          },
          "closedIssues": {
            "totalCount": 237
          }
        },
        {
          "nameWithOwner": "animate-css/animate.css",
          "issues": {
            "totalCount": 26
          },
          "closedIssues": {
            "totalCount": 832
          }
        },
        {
          "nameWithOwner": "gothinkster/realworld",
          "issues": {
            "totalCount": 54
          },
          "closedIssues": {
            "totalCount": 472
          }
        },
        {
          "nameWithOwner": "langchain-ai/langchain",
          "issues": {
            "totalCount": 1305
          },
          "closedIssues": {
            "totalCount": 4842
          }
        },
        {
          "nameWithOwner": "fatedier/frp",
          "issues": {
            "totalCount": 88
          },
          "closedIssues": {
            "totalCount": 3108
          }
        },
        {
          "nameWithOwner": "tailwindlabs/tailwindcss",
          "issues": {
            "totalCount": 8
          },
          "closedIssues": {
            "totalCount": 3115
          }
        },
        {
          "nameWithOwner": "tensorflow/models",
          "issues": {
            "totalCount": 1044
          },
          "closedIssues": {
            "totalCount": 6188
          }
        },
        {
          "nameWithOwner": "iptv-org/iptv",
          "issues": {
            "totalCount": 12
          },
          "closedIssues": {
            "totalCount": 7404
          }
        },
        {
          "nameWithOwner": "laravel/laravel",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 0
          }
        },
        {
          "nameWithOwner": "pytorch/pytorch",
          "issues": {
            "totalCount": 12690
          },
          "closedIssues": {
            "totalCount": 27421
          }
        },
        {
          "nameWithOwner": "mtdvio/every-programmer-should-know",
          "issues": {
            "totalCount": 24
          },
          "closedIssues": {
            "totalCount": 18
          }
        },
        {
          "nameWithOwner": "django/django",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 0
          }
        },
        {
          "nameWithOwner": "sveltejs/svelte",
          "issues": {
            "totalCount": 919
          },
          "closedIssues": {
            "totalCount": 5067
          }
        },
        {
          "nameWithOwner": "tauri-apps/tauri",
          "issues": {
            "totalCount": 679
          },
          "closedIssues": {
            "totalCount": 2873
          }
        },
        {
          "nameWithOwner": "Hack-with-Github/Awesome-Hacking",
          "issues": {
            "totalCount": 0
          },
          "closedIssues": {
            "totalCount": 0
          }
        },
        {
          "nameWithOwner": "MisterBooo/LeetCodeAnimation",
          "issues": {
            "totalCount": 17
          },
          "closedIssues": {
            "totalCount": 42
          }
        },
        {
          "nameWithOwner": "tonsky/FiraCode",
          "issues": {
            "totalCount": 376
          },
          "closedIssues": {
            "totalCount": 929
          }
        },
        {
          "nameWithOwner": "gin-gonic/gin",
          "issues": {
            "totalCount": 575
          },
          "closedIssues": {
            "totalCount": 1581
          }
        },
        {
          "nameWithOwner": "neovim/neovim",
          "issues": {
            "totalCount": 1416
          },
          "closedIssues": {
            "totalCount": 9468
          }
        },
        {
          "nameWithOwner": "opencv/opencv",
          "issues": {
            "totalCount": 2421
          },
          "closedIssues": {
            "totalCount": 7915
          }
        },
        {
          "nameWithOwner": "bitcoin/bitcoin",
          "issues": {
            "totalCount": 363
          },
          "closedIssues": {
            "totalCount": 7445
          }
        },
        {
          "nameWithOwner": "macrozheng/mall",
          "issues": {
            "totalCount": 26
          },
          "closedIssues": {
            "totalCount": 458
          }
        },
        {
          "nameWithOwner": "nvm-sh/nvm",
          "issues": {
            "totalCount": 347
          },
          "closedIssues": {
            "totalCount": 1743
          }
        },
        {
          "nameWithOwner": "florinpop17/app-ideas",
          "issues": {
            "totalCount": 103
          },
          "closedIssues": {
            "totalCount": 41
          }
        },
        {
          "nameWithOwner": "doocs/advanced-java",
          "issues": {
            "totalCount": 3
          },
          "closedIssues": {
            "totalCount": 141
          }
        },
        {
          "nameWithOwner": "FortAwesome/Font-Awesome",
          "issues": {
            "totalCount": 5456
          },
          "closedIssues": {
            "totalCount": 13787
          }
        },
        {
          "nameWithOwner": "spring-projects/spring-boot",
          "issues": {
            "totalCount": 583
          },
          "closedIssues": {
            "totalCount": 32638
          }
        },
        {
          "nameWithOwner": "gohugoio/hugo",
          "issues": {
            "totalCount": 446
          },
          "closedIssues": {
            "totalCount": 6574
          }
        }
      ]
    }
  }
}