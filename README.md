# Thank you, Christian!
This repository is inspired by your "20180929Python Library Lesson"!
The original is [Here](https://github.com/Yukiya025/26and1)
Repository name: 20180929CBLibraryPractice
# ようこそ
このリポジトリは、ロシアのМаксим Горький作、 Двадцать шесть и однаを読むためのものです。Djangoを使って公開することが目標。
まだ開発途中ですが、リポジトリ内のファイルの説明をします。

## 1. 26and1.csv
26and1.pyで生成されたファイル。Двадцать шесть и однаで単語が出た順に並んでいます。

## 2. 26and1.py
ロシア語では単語がさまざまな活用形となってでてきますが、活用されている単語をレマ化で認識後、登場回数をカウントするという自然言語処理を施しています。その後26and1.csvを生成。

## 3. 26and1.txt
Двадцать шесть и одна本文です。26and1.pyがこれを読み込みます。

## 4. 26and1_600.txt
Яндекс Переводчикで翻訳した日本語が入っている。

## 5. del_words.py
26and1.pyで拾ってほしくない単語 (前置詞や私がすでに覚えている単語など) を格納するためのファイル。どんどん追加予定。

## 6. addJP.py
26and1.csvに26and1_600.txtを追記する。

# 開発環境
- Python 3.6.6 (default, Sep 12 2018, 18:26:19) [GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
- Pycharm
- Linux Mint 19 "Tara" Cinnamon

# 参考サイト
[googletrans](https://py-googletrans.readthedocs.io/en/latest/)
- text (翻訳結果) のみを表示するのに役立つ。
