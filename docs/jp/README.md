# FetchMark - セットアップガイド

FetchMarkは、GitHub PagesなどのWebサービスで公開されているMarkdownファイルを美しく表示するアプリです。

## 1. Markdownの公開
GitHub Pagesなどで、`.md`ファイルをWeb上に公開してください。

## 2. index.jsonの作成
アプリがファイルを認識するために、サーバーのルートディレクトリに `index.json` を作成する必要があります。

### JSONの形式
```json
[
  "README.md",
  {
    "docs": [
      "setup.md",
      "guide.md"
    ]
  }
]
```

## 3. 自動化ツールの利用
手動でJSONを作成する代わりに、Pythonスクリプトを使用できます。
1. `scripts/` フォルダを自分のリポジトリにコピーします。
2. `python3 scripts/generate_index.py` を実行します。

### GitHub Actions
`.github/workflows/generate-index.yml` ファイルを自分のリポジトリにコピーすると、プッシュするたびにインデックスが自動更新されるようになります。

## 4. カスタムCSS
- **ローカル**: 各フォルダに `style.css` を配置すると、そのフォルダ内に適用されます。
- **グローバル**: アプリのリポジトリ設定でCSSのURLを指定すると、全体に適用されます。
