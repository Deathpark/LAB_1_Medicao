# Questão a ser resolvida:
RQ 05. Sistemas populares são escritos nas linguagens mais populares?

Métrica: linguagem primária de cada um desses repositórios


# Query utilizada:
query {
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        primaryLanguage {
          name
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
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "EbookFoundation/free-programming-books",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "sindresorhus/awesome",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "public-apis/public-apis",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "jwasham/coding-interview-university",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "996icu/996.ICU",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "kamranahmedse/developer-roadmap",
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "donnemartin/system-design-primer",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "codecrafters-io/build-your-own-x",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "facebook/react",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "vuejs/vue",
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "vinta/awesome-python",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "tensorflow/tensorflow",
          "primaryLanguage": {
            "name": "C++"
          }
        },
        {
          "nameWithOwner": "trekhleb/javascript-algorithms",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "TheAlgorithms/Python",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "getify/You-Dont-Know-JS",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "CyC2018/CS-Notes",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "awesome-selfhosted/awesome-selfhosted",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "ohmyzsh/ohmyzsh",
          "primaryLanguage": {
            "name": "Shell"
          }
        },
        {
          "nameWithOwner": "twbs/bootstrap",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "torvalds/linux",
          "primaryLanguage": {
            "name": "C"
          }
        },
        {
          "nameWithOwner": "flutter/flutter",
          "primaryLanguage": {
            "name": "Dart"
          }
        },
        {
          "nameWithOwner": "ossu/computer-science",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "Significant-Gravitas/AutoGPT",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "practical-tutorials/project-based-learning",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "microsoft/vscode",
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "github/gitignore",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "jackfrued/Python-100-Days",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "jlevy/the-art-of-command-line",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "Snailclimb/JavaGuide",
          "primaryLanguage": {
            "name": "Java"
          }
        },
        {
          "nameWithOwner": "airbnb/javascript",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "ytdl-org/youtube-dl",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "trimstray/the-book-of-secret-knowledge",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "labuladong/fucking-algorithm",
          "primaryLanguage": {
            "name": "Markdown"
          }
        },
        {
          "nameWithOwner": "AUTOMATIC1111/stable-diffusion-webui",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "huggingface/transformers",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "vercel/next.js",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "Chalarangelo/30-seconds-of-code",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "golang/go",
          "primaryLanguage": {
            "name": "Go"
          }
        },
        {
          "nameWithOwner": "avelino/awesome-go",
          "primaryLanguage": {
            "name": "Go"
          }
        },
        {
          "nameWithOwner": "facebook/react-native",
          "primaryLanguage": {
            "name": "C++"
          }
        },
        {
          "nameWithOwner": "electron/electron",
          "primaryLanguage": {
            "name": "C++"
          }
        },
        {
          "nameWithOwner": "justjavac/free-programming-books-zh_CN",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "d3/d3",
          "primaryLanguage": {
            "name": "Shell"
          }
        },
        {
          "nameWithOwner": "yangshun/tech-interview-handbook",
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "kubernetes/kubernetes",
          "primaryLanguage": {
            "name": "Go"
          }
        },
        {
          "nameWithOwner": "axios/axios",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "microsoft/PowerToys",
          "primaryLanguage": {
            "name": "C#"
          }
        },
        {
          "nameWithOwner": "nodejs/node",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "facebook/create-react-app",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "f/awesome-chatgpt-prompts",
          "primaryLanguage": {
            "name": "HTML"
          }
        },
        {
          "nameWithOwner": "Genymobile/scrcpy",
          "primaryLanguage": {
            "name": "C"
          }
        },
        {
          "nameWithOwner": "mrdoob/three.js",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "microsoft/TypeScript",
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "goldbergyoni/nodebestpractices",
          "primaryLanguage": {
            "name": "Dockerfile"
          }
        },
        {
          "nameWithOwner": "angular/angular",
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "microsoft/terminal",
          "primaryLanguage": {
            "name": "C++"
          }
        },
        {
          "nameWithOwner": "denoland/deno",
          "primaryLanguage": {
            "name": "Rust"
          }
        },
        {
          "nameWithOwner": "mui/material-ui",
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "rust-lang/rust",
          "primaryLanguage": {
            "name": "Rust"
          }
        },
        {
          "nameWithOwner": "ant-design/ant-design",
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "ryanmcdermott/clean-code-javascript",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "puppeteer/puppeteer",
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "iluwatar/java-design-patterns",
          "primaryLanguage": {
            "name": "Java"
          }
        },
        {
          "nameWithOwner": "PanJiaChen/vue-element-admin",
          "primaryLanguage": {
            "name": "Vue"
          }
        },
        {
          "nameWithOwner": "GrowingGit/GitHub-Chinese-Top-Charts",
          "primaryLanguage": {
            "name": "Java"
          }
        },
        {
          "nameWithOwner": "521xueweihan/HelloGitHub",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "storybookjs/storybook",
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "papers-we-love/papers-we-love",
          "primaryLanguage": {
            "name": "Shell"
          }
        },
        {
          "nameWithOwner": "nvbn/thefuck",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "ripienaar/free-for-dev",
          "primaryLanguage": {
            "name": "HTML"
          }
        },
        {
          "nameWithOwner": "godotengine/godot",
          "primaryLanguage": {
            "name": "C++"
          }
        },
        {
          "nameWithOwner": "microsoft/Web-Dev-For-Beginners",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "animate-css/animate.css",
          "primaryLanguage": {
            "name": "CSS"
          }
        },
        {
          "nameWithOwner": "gothinkster/realworld",
          "primaryLanguage": {
            "name": "TypeScript"
          }
        },
        {
          "nameWithOwner": "fatedier/frp",
          "primaryLanguage": {
            "name": "Go"
          }
        },
        {
          "nameWithOwner": "langchain-ai/langchain",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "tensorflow/models",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "tailwindlabs/tailwindcss",
          "primaryLanguage": {
            "name": "HTML"
          }
        },
        {
          "nameWithOwner": "laravel/laravel",
          "primaryLanguage": {
            "name": "PHP"
          }
        },
        {
          "nameWithOwner": "iptv-org/iptv",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "mtdvio/every-programmer-should-know",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "django/django",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "pytorch/pytorch",
          "primaryLanguage": {
            "name": "Python"
          }
        },
        {
          "nameWithOwner": "sveltejs/svelte",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "tauri-apps/tauri",
          "primaryLanguage": {
            "name": "Rust"
          }
        },
        {
          "nameWithOwner": "Hack-with-Github/Awesome-Hacking",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "MisterBooo/LeetCodeAnimation",
          "primaryLanguage": {
            "name": "Java"
          }
        },
        {
          "nameWithOwner": "tonsky/FiraCode",
          "primaryLanguage": {
            "name": "Clojure"
          }
        },
        {
          "nameWithOwner": "gin-gonic/gin",
          "primaryLanguage": {
            "name": "Go"
          }
        },
        {
          "nameWithOwner": "neovim/neovim",
          "primaryLanguage": {
            "name": "Vim Script"
          }
        },
        {
          "nameWithOwner": "opencv/opencv",
          "primaryLanguage": {
            "name": "C++"
          }
        },
        {
          "nameWithOwner": "bitcoin/bitcoin",
          "primaryLanguage": {
            "name": "C++"
          }
        },
        {
          "nameWithOwner": "macrozheng/mall",
          "primaryLanguage": {
            "name": "Java"
          }
        },
        {
          "nameWithOwner": "nvm-sh/nvm",
          "primaryLanguage": {
            "name": "Shell"
          }
        },
        {
          "nameWithOwner": "florinpop17/app-ideas",
          "primaryLanguage": null
        },
        {
          "nameWithOwner": "doocs/advanced-java",
          "primaryLanguage": {
            "name": "Java"
          }
        },
        {
          "nameWithOwner": "FortAwesome/Font-Awesome",
          "primaryLanguage": {
            "name": "JavaScript"
          }
        },
        {
          "nameWithOwner": "spring-projects/spring-boot",
          "primaryLanguage": {
            "name": "Java"
          }
        },
        {
          "nameWithOwner": "gohugoio/hugo",
          "primaryLanguage": {
            "name": "Go"
          }
        }
      ]
    }
  }
}