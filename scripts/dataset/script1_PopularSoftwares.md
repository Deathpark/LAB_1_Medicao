# Questão a ser resolvida:
RQ 01. Sistemas populares são maduros/antigos?

Métrica: idade do repositório (calculado a partir da data de sua criação)


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



# Resultado obtido:
{
  "data": {
    "search": {
      "nodes": [
        {
          "nameWithOwner": "freeCodeCamp/freeCodeCamp",
          "createdAt": "2014-12-24T17:49:19Z"
        },
        {
          "nameWithOwner": "EbookFoundation/free-programming-books",
          "createdAt": "2013-10-11T06:50:37Z"
        },
        {
          "nameWithOwner": "sindresorhus/awesome",
          "createdAt": "2014-07-11T13:42:37Z"
        },
        {
          "nameWithOwner": "public-apis/public-apis",
          "createdAt": "2016-03-20T23:49:42Z"
        },
        {
          "nameWithOwner": "jwasham/coding-interview-university",
          "createdAt": "2016-06-06T02:34:12Z"
        },
        {
          "nameWithOwner": "996icu/996.ICU",
          "createdAt": "2019-03-26T07:31:14Z"
        },
        {
          "nameWithOwner": "kamranahmedse/developer-roadmap",
          "createdAt": "2017-03-15T13:45:52Z"
        },
        {
          "nameWithOwner": "donnemartin/system-design-primer",
          "createdAt": "2017-02-26T16:15:28Z"
        },
        {
          "nameWithOwner": "codecrafters-io/build-your-own-x",
          "createdAt": "2018-05-09T12:03:18Z"
        },
        {
          "nameWithOwner": "facebook/react",
          "createdAt": "2013-05-24T16:15:54Z"
        },
        {
          "nameWithOwner": "vuejs/vue",
          "createdAt": "2013-07-29T03:24:51Z"
        },
        {
          "nameWithOwner": "vinta/awesome-python",
          "createdAt": "2014-06-27T21:00:06Z"
        },
        {
          "nameWithOwner": "tensorflow/tensorflow",
          "createdAt": "2015-11-07T01:19:20Z"
        },
        {
          "nameWithOwner": "trekhleb/javascript-algorithms",
          "createdAt": "2018-03-24T07:47:04Z"
        },
        {
          "nameWithOwner": "TheAlgorithms/Python",
          "createdAt": "2016-07-16T09:44:01Z"
        },
        {
          "nameWithOwner": "getify/You-Dont-Know-JS",
          "createdAt": "2013-11-16T02:37:24Z"
        },
        {
          "nameWithOwner": "CyC2018/CS-Notes",
          "createdAt": "2018-02-13T14:56:24Z"
        },
        {
          "nameWithOwner": "awesome-selfhosted/awesome-selfhosted",
          "createdAt": "2015-06-01T02:33:17Z"
        },
        {
          "nameWithOwner": "ohmyzsh/ohmyzsh",
          "createdAt": "2009-08-28T18:15:37Z"
        },
        {
          "nameWithOwner": "twbs/bootstrap",
          "createdAt": "2011-07-29T21:19:00Z"
        },
        {
          "nameWithOwner": "torvalds/linux",
          "createdAt": "2011-09-04T22:48:12Z"
        },
        {
          "nameWithOwner": "flutter/flutter",
          "createdAt": "2015-03-06T22:54:58Z"
        },
        {
          "nameWithOwner": "ossu/computer-science",
          "createdAt": "2014-05-04T00:18:39Z"
        },
        {
          "nameWithOwner": "Significant-Gravitas/AutoGPT",
          "createdAt": "2023-03-16T09:21:07Z"
        },
        {
          "nameWithOwner": "practical-tutorials/project-based-learning",
          "createdAt": "2017-04-12T05:07:46Z"
        },
        {
          "nameWithOwner": "microsoft/vscode",
          "createdAt": "2015-09-03T20:23:38Z"
        },
        {
          "nameWithOwner": "github/gitignore",
          "createdAt": "2010-11-08T20:17:14Z"
        },
        {
          "nameWithOwner": "jackfrued/Python-100-Days",
          "createdAt": "2018-03-01T16:05:52Z"
        },
        {
          "nameWithOwner": "jlevy/the-art-of-command-line",
          "createdAt": "2015-05-20T15:11:03Z"
        },
        {
          "nameWithOwner": "Snailclimb/JavaGuide",
          "createdAt": "2018-05-07T13:27:00Z"
        },
        {
          "nameWithOwner": "airbnb/javascript",
          "createdAt": "2012-11-01T23:13:50Z"
        },
        {
          "nameWithOwner": "ytdl-org/youtube-dl",
          "createdAt": "2010-10-31T14:35:07Z"
        },
        {
          "nameWithOwner": "trimstray/the-book-of-secret-knowledge",
          "createdAt": "2018-06-23T10:43:14Z"
        },
        {
          "nameWithOwner": "labuladong/fucking-algorithm",
          "createdAt": "2020-02-19T09:01:23Z"
        },
        {
          "nameWithOwner": "AUTOMATIC1111/stable-diffusion-webui",
          "createdAt": "2022-08-22T14:05:26Z"
        },
        {
          "nameWithOwner": "huggingface/transformers",
          "createdAt": "2018-10-29T13:56:00Z"
        },
        {
          "nameWithOwner": "vercel/next.js",
          "createdAt": "2016-10-05T23:32:51Z"
        },
        {
          "nameWithOwner": "Chalarangelo/30-seconds-of-code",
          "createdAt": "2017-11-29T17:35:03Z"
        },
        {
          "nameWithOwner": "golang/go",
          "createdAt": "2014-08-19T04:33:40Z"
        },
        {
          "nameWithOwner": "avelino/awesome-go",
          "createdAt": "2014-07-06T13:42:15Z"
        },
        {
          "nameWithOwner": "facebook/react-native",
          "createdAt": "2015-01-09T18:10:16Z"
        },
        {
          "nameWithOwner": "electron/electron",
          "createdAt": "2013-04-12T01:47:36Z"
        },
        {
          "nameWithOwner": "justjavac/free-programming-books-zh_CN",
          "createdAt": "2013-11-04T01:59:19Z"
        },
        {
          "nameWithOwner": "d3/d3",
          "createdAt": "2010-09-27T17:22:42Z"
        },
        {
          "nameWithOwner": "yangshun/tech-interview-handbook",
          "createdAt": "2016-07-05T05:00:48Z"
        },
        {
          "nameWithOwner": "kubernetes/kubernetes",
          "createdAt": "2014-06-06T22:56:04Z"
        },
        {
          "nameWithOwner": "axios/axios",
          "createdAt": "2014-08-18T22:30:27Z"
        },
        {
          "nameWithOwner": "microsoft/PowerToys",
          "createdAt": "2019-05-01T17:44:02Z"
        },
        {
          "nameWithOwner": "nodejs/node",
          "createdAt": "2014-11-26T19:57:11Z"
        },
        {
          "nameWithOwner": "facebook/create-react-app",
          "createdAt": "2016-07-17T14:55:11Z"
        },
        {
          "nameWithOwner": "f/awesome-chatgpt-prompts",
          "createdAt": "2022-12-05T13:54:13Z"
        },
        {
          "nameWithOwner": "Genymobile/scrcpy",
          "createdAt": "2017-11-21T18:00:27Z"
        },
        {
          "nameWithOwner": "mrdoob/three.js",
          "createdAt": "2010-03-23T18:58:01Z"
        },
        {
          "nameWithOwner": "microsoft/TypeScript",
          "createdAt": "2014-06-17T15:28:39Z"
        },
        {
          "nameWithOwner": "goldbergyoni/nodebestpractices",
          "createdAt": "2017-09-15T08:33:19Z"
        },
        {
          "nameWithOwner": "angular/angular",
          "createdAt": "2014-09-18T16:12:01Z"
        },
        {
          "nameWithOwner": "microsoft/terminal",
          "createdAt": "2017-08-11T18:38:22Z"
        },
        {
          "nameWithOwner": "denoland/deno",
          "createdAt": "2018-05-15T01:34:26Z"
        },
        {
          "nameWithOwner": "mui/material-ui",
          "createdAt": "2014-08-18T19:11:54Z"
        },
        {
          "nameWithOwner": "rust-lang/rust",
          "createdAt": "2010-06-16T20:39:03Z"
        },
        {
          "nameWithOwner": "ant-design/ant-design",
          "createdAt": "2015-04-24T15:37:24Z"
        },
        {
          "nameWithOwner": "ryanmcdermott/clean-code-javascript",
          "createdAt": "2016-11-25T22:25:41Z"
        },
        {
          "nameWithOwner": "puppeteer/puppeteer",
          "createdAt": "2017-05-09T22:16:13Z"
        },
        {
          "nameWithOwner": "iluwatar/java-design-patterns",
          "createdAt": "2014-08-09T16:45:18Z"
        },
        {
          "nameWithOwner": "PanJiaChen/vue-element-admin",
          "createdAt": "2017-04-17T03:35:49Z"
        },
        {
          "nameWithOwner": "GrowingGit/GitHub-Chinese-Top-Charts",
          "createdAt": "2019-09-05T03:01:56Z"
        },
        {
          "nameWithOwner": "521xueweihan/HelloGitHub",
          "createdAt": "2016-05-04T06:24:11Z"
        },
        {
          "nameWithOwner": "storybookjs/storybook",
          "createdAt": "2016-03-18T04:23:44Z"
        },
        {
          "nameWithOwner": "papers-we-love/papers-we-love",
          "createdAt": "2013-12-15T14:31:41Z"
        },
        {
          "nameWithOwner": "nvbn/thefuck",
          "createdAt": "2015-04-08T15:08:04Z"
        },
        {
          "nameWithOwner": "ripienaar/free-for-dev",
          "createdAt": "2015-03-18T21:06:26Z"
        },
        {
          "nameWithOwner": "godotengine/godot",
          "createdAt": "2014-01-04T16:05:36Z"
        },
        {
          "nameWithOwner": "microsoft/Web-Dev-For-Beginners",
          "createdAt": "2020-11-10T02:44:00Z"
        },
        {
          "nameWithOwner": "animate-css/animate.css",
          "createdAt": "2011-10-12T10:07:38Z"
        },
        {
          "nameWithOwner": "gothinkster/realworld",
          "createdAt": "2016-02-26T20:49:53Z"
        },
        {
          "nameWithOwner": "fatedier/frp",
          "createdAt": "2015-12-21T15:24:59Z"
        },
        {
          "nameWithOwner": "langchain-ai/langchain",
          "createdAt": "2022-10-17T02:58:36Z"
        },
        {
          "nameWithOwner": "tensorflow/models",
          "createdAt": "2016-02-05T01:15:20Z"
        },
        {
          "nameWithOwner": "tailwindlabs/tailwindcss",
          "createdAt": "2017-10-06T14:59:14Z"
        },
        {
          "nameWithOwner": "laravel/laravel",
          "createdAt": "2011-06-08T03:06:08Z"
        },
        {
          "nameWithOwner": "iptv-org/iptv",
          "createdAt": "2018-11-14T22:00:57Z"
        },
        {
          "nameWithOwner": "mtdvio/every-programmer-should-know",
          "createdAt": "2017-08-24T13:18:26Z"
        },
        {
          "nameWithOwner": "django/django",
          "createdAt": "2012-04-28T02:47:18Z"
        },
        {
          "nameWithOwner": "pytorch/pytorch",
          "createdAt": "2016-08-13T05:26:41Z"
        },
        {
          "nameWithOwner": "sveltejs/svelte",
          "createdAt": "2016-11-20T18:13:05Z"
        },
        {
          "nameWithOwner": "tauri-apps/tauri",
          "createdAt": "2019-07-13T09:09:37Z"
        },
        {
          "nameWithOwner": "Hack-with-Github/Awesome-Hacking",
          "createdAt": "2016-03-30T15:47:10Z"
        },
        {
          "nameWithOwner": "MisterBooo/LeetCodeAnimation",
          "createdAt": "2018-12-06T08:01:22Z"
        },
        {
          "nameWithOwner": "tonsky/FiraCode",
          "createdAt": "2014-11-11T19:32:38Z"
        },
        {
          "nameWithOwner": "gin-gonic/gin",
          "createdAt": "2014-06-16T23:57:25Z"
        },
        {
          "nameWithOwner": "neovim/neovim",
          "createdAt": "2014-01-31T13:39:22Z"
        },
        {
          "nameWithOwner": "opencv/opencv",
          "createdAt": "2012-07-19T09:40:17Z"
        },
        {
          "nameWithOwner": "bitcoin/bitcoin",
          "createdAt": "2010-12-19T15:16:43Z"
        },
        {
          "nameWithOwner": "macrozheng/mall",
          "createdAt": "2018-04-04T01:11:44Z"
        },
        {
          "nameWithOwner": "nvm-sh/nvm",
          "createdAt": "2010-04-15T17:47:47Z"
        },
        {
          "nameWithOwner": "florinpop17/app-ideas",
          "createdAt": "2019-02-25T18:36:56Z"
        },
        {
          "nameWithOwner": "doocs/advanced-java",
          "createdAt": "2018-10-06T11:38:30Z"
        },
        {
          "nameWithOwner": "FortAwesome/Font-Awesome",
          "createdAt": "2012-02-17T14:19:43Z"
        },
        {
          "nameWithOwner": "spring-projects/spring-boot",
          "createdAt": "2012-10-19T15:02:57Z"
        },
        {
          "nameWithOwner": "gohugoio/hugo",
          "createdAt": "2013-07-04T15:26:26Z"
        }
      ]
    }
  }
}