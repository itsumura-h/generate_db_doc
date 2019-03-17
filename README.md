generate_db_doc
===

DB周りのドキュメントを作るためのツールです

## 使い方
venvを作り、pipenvを使ってpipfileからプラグインをインストールしてください

```
python -m venv .venv
sourve .venv/bin/activate
pip install pipenv
pipenv install
```

### setup
```
python generate_db_doc.py setup
```
inputとoutputという名前のディレクトリが作られます

### md_to_html
```
python generate_db_doc.py md_to_html input/db.md
```
inputディレクトリ以下にマークダウンファイルを置きます。input/db.mdを読み込んで、output/db.htmlというファイルが出力されます