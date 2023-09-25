# mwaa-test

## 環境構築
手順
```shell
$ sh install.sh
$ make init-db
$ make create-user
$ make up-web
```

別ターミナルで
```shell
$ make up-scheduler
```

## 画面の解説
- 参考: https://airflow.apache.org/docs/apache-airflow/stable/ui.html

|  TH  | TH |
| ---- |--|
|  DAGs Viwe  | DAG一覧 |
| Grid View   | 時間をまたがるDAGの棒グラフとグリッド表示。上段はDAG Runsの期間別チャート、下段はタスクインスタンス。 |
|  Graph View  | DAGの依存関係と、特定の実行における現在のステータス |
|  Calendar View  | DAG全体の履歴 |

## DAGの実行
[![Image from Gyazo](https://i.gyazo.com/c2c7f97970913b532dede01daf7d0cb6.png)](https://gyazo.com/c2c7f97970913b532dede01daf7d0cb6)

## ログの確認
[![Image from Gyazo](https://i.gyazo.com/d866fccf999a34478063eb88aa167677.png)](https://gyazo.com/d866fccf999a34478063eb88aa167677)

## 再集計
- タスクをクリアすると再実行される

# 参考
- [ApacheAirflowワークフロープログラミング入門](https://booth.pm/ja/items/3103934)
