# friend-clone-bot
友達とのトーク履歴からクローンを作成して、応答するLineBotです。

# コンテナの起動

docker-compose up

# コンテナの起動(image のサイビルド)

docker-compose up --build

# コンテナの中に入る

docker container exec -it backend_web_1 bash

# マイグレーションファイルの作成(変更するときだけで大丈夫)

python manage.py makemigrations

# マイグレーションの実行

python manage.py migrate
