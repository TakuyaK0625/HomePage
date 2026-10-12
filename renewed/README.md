# サイトの更新

文章と経歴はcontent.json、ページ構成はbuild.py、デザインはassets/site.cssを編集します。

```sh
LC_ALL=en_US.UTF-8 python3 renewed/build.py
```

生成先はrenewed/dist/です。dist/の内容をリポジトリのルートへ配置してGitHub Pagesで公開します。
プロフィールの趣味や人材育成の文章は現在build.pyに記載しています。
