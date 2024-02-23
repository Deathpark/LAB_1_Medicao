# Questão a ser resolvida:
RQ 02. Sistemas populares recebem muita contribuição externa?

Métrica: total de pull requests aceitas


# Query utilizada:
query {
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        pullRequests {
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
          "pullRequests": {
            "totalCount": 35479
          }
        },
        {
          "nameWithOwner": "EbookFoundation/free-programming-books",
          "pullRequests": {
            "totalCount": 9842
          }
        },
        {
          "nameWithOwner": "sindresorhus/awesome",
          "pullRequests": {
            "totalCount": 1999
          }
        },
        {
          "nameWithOwner": "public-apis/public-apis",
          "pullRequests": {
            "totalCount": 3100
          }
        },
        {
          "nameWithOwner": "jwasham/coding-interview-university",
          "pullRequests": {
            "totalCount": 943
          }
        },
        {
          "nameWithOwner": "996icu/996.ICU",
          "pullRequests": {
            "totalCount": 1972
          }
        },
        {
          "nameWithOwner": "kamranahmedse/developer-roadmap",
          "pullRequests": {
            "totalCount": 2903
          }
        },
        {
          "nameWithOwner": "donnemartin/system-design-primer",
          "pullRequests": {
            "totalCount": 516
          }
        },
        {
          "nameWithOwner": "codecrafters-io/build-your-own-x",
          "pullRequests": {
            "totalCount": 374
          }
        },
        {
          "nameWithOwner": "facebook/react",
          "pullRequests": {
            "totalCount": 14550
          }
        },
        {
          "nameWithOwner": "vuejs/vue",
          "pullRequests": {
            "totalCount": 2508
          }
        },
        {
          "nameWithOwner": "vinta/awesome-python",
          "pullRequests": {
            "totalCount": 1886
          }
        },
        {
          "nameWithOwner": "tensorflow/tensorflow",
          "pullRequests": {
            "totalCount": 23687
          }
        },
        {
          "nameWithOwner": "trekhleb/javascript-algorithms",
          "pullRequests": {
            "totalCount": 717
          }
        },
        {
          "nameWithOwner": "TheAlgorithms/Python",
          "pullRequests": {
            "totalCount": 9327
          }
        },
        {
          "nameWithOwner": "getify/You-Dont-Know-JS",
          "pullRequests": {
            "totalCount": 889
          }
        },
        {
          "nameWithOwner": "CyC2018/CS-Notes",
          "pullRequests": {
            "totalCount": 610
          }
        },
        {
          "nameWithOwner": "awesome-selfhosted/awesome-selfhosted",
          "pullRequests": {
            "totalCount": 3037
          }
        },
        {
          "nameWithOwner": "ohmyzsh/ohmyzsh",
          "pullRequests": {
            "totalCount": 7114
          }
        },
        {
          "nameWithOwner": "twbs/bootstrap",
          "pullRequests": {
            "totalCount": 15027
          }
        },
        {
          "nameWithOwner": "torvalds/linux",
          "pullRequests": {
            "totalCount": 763
          }
        },
        {
          "nameWithOwner": "flutter/flutter",
          "pullRequests": {
            "totalCount": 51140
          }
        },
        {
          "nameWithOwner": "ossu/computer-science",
          "pullRequests": {
            "totalCount": 418
          }
        },
        {
          "nameWithOwner": "Significant-Gravitas/AutoGPT",
          "pullRequests": {
            "totalCount": 3602
          }
        },
        {
          "nameWithOwner": "practical-tutorials/project-based-learning",
          "pullRequests": {
            "totalCount": 374
          }
        },
        {
          "nameWithOwner": "microsoft/vscode",
          "pullRequests": {
            "totalCount": 27730
          }
        },
        {
          "nameWithOwner": "github/gitignore",
          "pullRequests": {
            "totalCount": 4325
          }
        },
        {
          "nameWithOwner": "jackfrued/Python-100-Days",
          "pullRequests": {
            "totalCount": 332
          }
        },
        {
          "nameWithOwner": "jlevy/the-art-of-command-line",
          "pullRequests": {
            "totalCount": 579
          }
        },
        {
          "nameWithOwner": "Snailclimb/JavaGuide",
          "pullRequests": {
            "totalCount": 1225
          }
        },
        {
          "nameWithOwner": "airbnb/javascript",
          "pullRequests": {
            "totalCount": 1514
          }
        },
        {
          "nameWithOwner": "ytdl-org/youtube-dl",
          "pullRequests": {
            "totalCount": 4896
          }
        },
        {
          "nameWithOwner": "trimstray/the-book-of-secret-knowledge",
          "pullRequests": {
            "totalCount": 258
          }
        },
        {
          "nameWithOwner": "labuladong/fucking-algorithm",
          "pullRequests": {
            "totalCount": 467
          }
        },
        {
          "nameWithOwner": "AUTOMATIC1111/stable-diffusion-webui",
          "pullRequests": {
            "totalCount": 2740
          }
        },
        {
          "nameWithOwner": "huggingface/transformers",
          "pullRequests": {
            "totalCount": 14787
          }
        },
        {
          "nameWithOwner": "vercel/next.js",
          "pullRequests": {
            "totalCount": 20313
          }
        },
        {
          "nameWithOwner": "Chalarangelo/30-seconds-of-code",
          "pullRequests": {
            "totalCount": 1603
          }
        },
        {
          "nameWithOwner": "golang/go",
          "pullRequests": {
            "totalCount": 3689
          }
        },
        {
          "nameWithOwner": "avelino/awesome-go",
          "pullRequests": {
            "totalCount": 4484
          }
        },
        {
          "nameWithOwner": "facebook/react-native",
          "pullRequests": {
            "totalCount": 15913
          }
        },
        {
          "nameWithOwner": "electron/electron",
          "pullRequests": {
            "totalCount": 21312
          }
        },
        {
          "nameWithOwner": "justjavac/free-programming-books-zh_CN",
          "pullRequests": {
            "totalCount": 460
          }
        },
        {
          "nameWithOwner": "d3/d3",
          "pullRequests": {
            "totalCount": 1167
          }
        },
        {
          "nameWithOwner": "yangshun/tech-interview-handbook",
          "pullRequests": {
            "totalCount": 530
          }
        },
        {
          "nameWithOwner": "kubernetes/kubernetes",
          "pullRequests": {
            "totalCount": 78473
          }
        },
        {
          "nameWithOwner": "axios/axios",
          "pullRequests": {
            "totalCount": 1555
          }
        },
        {
          "nameWithOwner": "microsoft/PowerToys",
          "pullRequests": {
            "totalCount": 5051
          }
        },
        {
          "nameWithOwner": "nodejs/node",
          "pullRequests": {
            "totalCount": 32680
          }
        },
        {
          "nameWithOwner": "facebook/create-react-app",
          "pullRequests": {
            "totalCount": 4249
          }
        },
        {
          "nameWithOwner": "f/awesome-chatgpt-prompts",
          "pullRequests": {
            "totalCount": 564
          }
        },
        {
          "nameWithOwner": "Genymobile/scrcpy",
          "pullRequests": {
            "totalCount": 419
          }
        },
        {
          "nameWithOwner": "mrdoob/three.js",
          "pullRequests": {
            "totalCount": 15449
          }
        },
        {
          "nameWithOwner": "microsoft/TypeScript",
          "pullRequests": {
            "totalCount": 17125
          }
        },
        {
          "nameWithOwner": "goldbergyoni/nodebestpractices",
          "pullRequests": {
            "totalCount": 953
          }
        },
        {
          "nameWithOwner": "angular/angular",
          "pullRequests": {
            "totalCount": 26404
          }
        },
        {
          "nameWithOwner": "microsoft/terminal",
          "pullRequests": {
            "totalCount": 4010
          }
        },
        {
          "nameWithOwner": "denoland/deno",
          "pullRequests": {
            "totalCount": 12153
          }
        },
        {
          "nameWithOwner": "mui/material-ui",
          "pullRequests": {
            "totalCount": 21470
          }
        },
        {
          "nameWithOwner": "rust-lang/rust",
          "pullRequests": {
            "totalCount": 69593
          }
        },
        {
          "nameWithOwner": "ant-design/ant-design",
          "pullRequests": {
            "totalCount": 16453
          }
        },
        {
          "nameWithOwner": "ryanmcdermott/clean-code-javascript",
          "pullRequests": {
            "totalCount": 281
          }
        },
        {
          "nameWithOwner": "puppeteer/puppeteer",
          "pullRequests": {
            "totalCount": 5298
          }
        },
        {
          "nameWithOwner": "iluwatar/java-design-patterns",
          "pullRequests": {
            "totalCount": 1879
          }
        },
        {
          "nameWithOwner": "PanJiaChen/vue-element-admin",
          "pullRequests": {
            "totalCount": 583
          }
        },
        {
          "nameWithOwner": "GrowingGit/GitHub-Chinese-Top-Charts",
          "pullRequests": {
            "totalCount": 19
          }
        },
        {
          "nameWithOwner": "521xueweihan/HelloGitHub",
          "pullRequests": {
            "totalCount": 39
          }
        },
        {
          "nameWithOwner": "storybookjs/storybook",
          "pullRequests": {
            "totalCount": 11876
          }
        },
        {
          "nameWithOwner": "papers-we-love/papers-we-love",
          "pullRequests": {
            "totalCount": 510
          }
        },
        {
          "nameWithOwner": "nvbn/thefuck",
          "pullRequests": {
            "totalCount": 687
          }
        },
        {
          "nameWithOwner": "ripienaar/free-for-dev",
          "pullRequests": {
            "totalCount": 3105
          }
        },
        {
          "nameWithOwner": "godotengine/godot",
          "pullRequests": {
            "totalCount": 39408
          }
        },
        {
          "nameWithOwner": "microsoft/Web-Dev-For-Beginners",
          "pullRequests": {
            "totalCount": 831
          }
        },
        {
          "nameWithOwner": "animate-css/animate.css",
          "pullRequests": {
            "totalCount": 839
          }
        },
        {
          "nameWithOwner": "gothinkster/realworld",
          "pullRequests": {
            "totalCount": 816
          }
        },
        {
          "nameWithOwner": "fatedier/frp",
          "pullRequests": {
            "totalCount": 807
          }
        },
        {
          "nameWithOwner": "langchain-ai/langchain",
          "pullRequests": {
            "totalCount": 10127
          }
        },
        {
          "nameWithOwner": "tensorflow/models",
          "pullRequests": {
            "totalCount": 3784
          }
        },
        {
          "nameWithOwner": "tailwindlabs/tailwindcss",
          "pullRequests": {
            "totalCount": 2471
          }
        },
        {
          "nameWithOwner": "laravel/laravel",
          "pullRequests": {
            "totalCount": 4685
          }
        },
        {
          "nameWithOwner": "iptv-org/iptv",
          "pullRequests": {
            "totalCount": 6757
          }
        },
        {
          "nameWithOwner": "mtdvio/every-programmer-should-know",
          "pullRequests": {
            "totalCount": 164
          }
        },
        {
          "nameWithOwner": "django/django",
          "pullRequests": {
            "totalCount": 17838
          }
        },
        {
          "nameWithOwner": "pytorch/pytorch",
          "pullRequests": {
            "totalCount": 80155
          }
        },
        {
          "nameWithOwner": "sveltejs/svelte",
          "pullRequests": {
            "totalCount": 4386
          }
        },
        {
          "nameWithOwner": "tauri-apps/tauri",
          "pullRequests": {
            "totalCount": 4123
          }
        },
        {
          "nameWithOwner": "Hack-with-Github/Awesome-Hacking",
          "pullRequests": {
            "totalCount": 100
          }
        },
        {
          "nameWithOwner": "MisterBooo/LeetCodeAnimation",
          "pullRequests": {
            "totalCount": 76
          }
        },
        {
          "nameWithOwner": "tonsky/FiraCode",
          "pullRequests": {
            "totalCount": 185
          }
        },
        {
          "nameWithOwner": "gin-gonic/gin",
          "pullRequests": {
            "totalCount": 1669
          }
        },
        {
          "nameWithOwner": "neovim/neovim",
          "pullRequests": {
            "totalCount": 16433
          }
        },
        {
          "nameWithOwner": "opencv/opencv",
          "pullRequests": {
            "totalCount": 14626
          }
        },
        {
          "nameWithOwner": "bitcoin/bitcoin",
          "pullRequests": {
            "totalCount": 20299
          }
        },
        {
          "nameWithOwner": "macrozheng/mall",
          "pullRequests": {
            "totalCount": 118
          }
        },
        {
          "nameWithOwner": "nvm-sh/nvm",
          "pullRequests": {
            "totalCount": 1060
          }
        },
        {
          "nameWithOwner": "florinpop17/app-ideas",
          "pullRequests": {
            "totalCount": 663
          }
        },
        {
          "nameWithOwner": "doocs/advanced-java",
          "pullRequests": {
            "totalCount": 118
          }
        },
        {
          "nameWithOwner": "FortAwesome/Font-Awesome",
          "pullRequests": {
            "totalCount": 681
          }
        },
        {
          "nameWithOwner": "spring-projects/spring-boot",
          "pullRequests": {
            "totalCount": 6106
          }
        },
        {
          "nameWithOwner": "gohugoio/hugo",
          "pullRequests": {
            "totalCount": 4952
          }
        }
      ]
    }
  }
}