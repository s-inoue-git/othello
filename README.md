
# 操作方法

1. このディレクトリの中身を全て自分のプロジェクトフォルダへ移動

2. env/.envの「docker-init-env」部分をを自分のプロジェクト名に変更
```
COMPOSE_PROJECT_NAME=docker-init-env
```
3. 以下dockerコマンドを実行(image&containerの作成)
```bash
# move env dir
$ cd env
# imageの作成
$ docker-compose build
# containerの作成&起動
$ docker-compose up -d
# containerの中へ入る(docker-init-envは自分のプロジェクト名)
$ docker attach docker-init-env
```
環境構築完成！