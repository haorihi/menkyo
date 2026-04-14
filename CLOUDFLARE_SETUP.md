# Cloudflare Pages + KV 同期環境のセットアップ手順

GitHubリポジトリへのプッシュが完了しました。以下の手順でCloudflare側にデプロイし、同期機能を有効化してください。

---

## 1. KV（データベース）の作成

Cloudflareダッシュボード上で、同期データを保存するための場所（KV）を準備します。

1. [Cloudflareダッシュボード](https://dash.cloudflare.com/)にログインします。
2. 左メニューの **[Workers & Pages]** > **[KV]** を選択します。
3. **[Create a namespace]** をクリックし、名前に `HISTORY_KV` と入力して作成します。
4. 一覧に表示された `HISTORY_KV` の **[ID]** （32桁の英数字）をコピーしておきます。

---

## 2. Pagesプロジェクトの作成

リポジトリと連携してサイトを公開します。

1. **[Workers & Pages]** > **[Overview]** から **[Create application]** > **[Pages]** を開きます。
2. **[Connect to Git]** をクリックし、リポジトリ（`haorihi/menkyo`）を選択します。
3. **[Begin setup]** をクリックします。
4. **[Build settings]** は以下の通りに設定します（基本的にそのままでOKです）。
   - **Framework preset**: `None`
   - **Build command**: （空欄のまま）
   - **Build output directory**: `.`
5. **[Save and Deploy]** をクリックします（この時点ではまだ同期は動きません）。

---

## 3. KVと環境変数の紐付け（重要）

デプロイされたサイトにデータベースとパスワードを持たせます。

1. Pagesプロジェクトの管理画面で、 **[Settings]** > **[Functions]** タブを開きます。
2. **[KV namespace bindings]** セクションを探し、 **[Add binding]** をクリックします。
   - **Variable name**: `HISTORY_KV`
   - **KV namespace**: 手順1で作った `HISTORY_KV` を選択します。
3. 次に、 **[Settings]** > **[Environment variables]** タブを開きます。
4. **[Add variable]** をクリックします（ProductionとPreviewの両方に設定することをお勧めします）。
   - **Variable name**: `SYNC_TOKEN`
   - **Value**: **自分だけの合言葉**（例: `my-secret-1234`）を入力して保存します。
5. **[Deployments]** タブに戻り、最新のデプロイの横にある「...」から **[Retry deployment]** を行い、設定を反映させます。

---

## 4. マルチデバイス同期の使い方

設定完了後、PCやスマホから「合言葉つきのURL」で1回だけアクセスします。

### 初回アクセスURL
`https://(あなたのプロジェクト名).pages.dev/?token=(決めた合言葉)`

> [!IMPORTANT]
> - このURLでアクセスするのは、**各端末で最初の一回だけ**で大丈夫です。
> - アクセスするとアプリが合言葉を覚え、自動的にURLから `?token=...` が消えます。
> - 以降は、ブックマーク等から普通にアクセスするだけで、裏側で勝手にクラウドと同期されます。

これで設定はすべて完了です！
別の端末でも同じURL（`?token=...` 付き）で一度アクセスすれば、間違えた問題のデータが同期されるようになります。
