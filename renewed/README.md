# 久保琢也 ホームページ（新版）

旧blogdown / Hugoプロジェクトを保存したまま、`renewed/` に独立した新版を作成しています。
Python 3 の標準ライブラリのみでビルドできます。npm、R、Hugoは不要です。

## 内容の更新

`content.json` をUTF-8のテキストエディタで編集します。

- `affiliation`, `position`：所属、職位
- `description`：自己紹介
- `email`：掲載したい公開メールアドレス。空欄の場合はメールボタンを表示しません
- `career`, `education`, `committees`：経歴、学歴、委員歴
- `publications`, `talks`, `awards`, `funding`：研究業績。新しいものを配列の先頭に追加
- `tools`：ツール名、説明、URL、画像
- `courses`：学習資料

```sh
cd /Users/takuyakubo/Dropbox/myHomePage
python3 renewed/build.py
```

出力先は `renewed/dist/` です。生成済みHTMLを直接編集せず、内容は`content.json`、構成は`build.py`、デザインは`assets/site.css`を編集してください。

## プレビュー

```sh
cd /Users/takuyakubo/Dropbox/myHomePage/renewed/dist
python3 -m http.server 8765 --bind 127.0.0.1
```

ブラウザで http://127.0.0.1:8765/ を開きます。終了は Ctrl+C。

## 公開

`dist/` 全体を静的ホスティングに配置します。相対リンクなのでGitHub Pagesの`/HomePage/`配下でも動作します。
GitHub Pagesの場合は対象リポジトリの公開ブランチ／フォルダ、またはActionsからdistを配信してください。
公開前に既存ブログURLの継続方針を決め、移行先に旧ブログと関連画像を残してください。
旧サイトの`public/`を新版のdistで置き換える場合、旧ブログを別途保持しないと過去のリンクが失われます。
この作業では既存の公開サイトへのデプロイは行っていません。

## 情報源

プロフィール、追加業績、委員歴： https://researchmap.jp/kubotaku （2026年10月11日確認）
公開ツール、学習資料、資格・研修、旧業績：元プロジェクトのcontent/。
researchmapにメールアドレスの公開がなかったため、旧所属のメールは掲載していません。
資料は元サイト掲載順に「第N回の資料」としています。
外部アプリの稼働、SlideShareの閲覧可否は各サービスの運用状態に依存します。

サンプルのブログ記事、ダミーの企業情報、地図、コメントサービス等を新版には含めていません。
旧ファイルは削除していません。
