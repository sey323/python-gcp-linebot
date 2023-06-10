from os import environ
from dotenv import load_dotenv

load_dotenv(verbose=True)

# フロントエンドのURL
FRONTEND_URL = environ.get(
    "FRONTEND_URL", "https://myna-safety-388707.web.app/"
)


# LINEBotの認証情報
LINE_CHANNEL_ACCESS_TOKEN = environ.get("LINE_CHANNEL_ACCESS_TOKEN", "")
LINE_CHANNEL_SECRET = environ.get("LINE_CHANNEL_SECRET", "")

# OpenAIのAPIキー
OPENAI_API_KEY = environ.get("OPENAI_API_KEY", "")

# マイナポータルAPIの接続情報
MYNA_API_URL = environ.get("MYNA_API_URL", "")
MYNA_API_TOKEN = environ.get("MYNA_API_TOKEN", "")

# FireStoreの認証キー
CRED_PATH = environ.get("CRED_PATH", "app/key/credential.json")
GOOGLE_CLOUD_STORAGE_BUCKET_NAME = environ.get(
    "GOOGLE_CLOUD_STORAGE_BUCKET_NAME", "myna-safety"
)


# 画像パス
LINEBOT_ENTRY_FORM_REQEST_THUMBNAIL_URL = environ.get(
    "CRED_PATH",
    "https://ff9454ac3b3a15e562d4f6ff7baa8e061a2c919b93e05269ca4bce8-apidata.googleusercontent.com/download/storage/v1/b/myna-safety/o/system%2Fquestions.png?jk=ARTXCFFbKQ3y53lE4Oo6wBXqnQ6YS0T8Zia4pmTcpROnZpIDKSoVV5XxCGnJezhpTtQq8Q2DG9HJuMqymbAjf4KVwloMqLYCXmn1892UweDS1fm3POc09P1qGILVgP7-O228KFzIPI73sC9k_emjqx4Ex74u3UcUqifXRgCzxgfsMmPUMmZ1NaK361rUj5ebKqUpGhfPGmtffyR0eTt4dWegLgCWj_MeNJZDODIryBvHvz2b2Qk5T2LBe3OVliu37gJThuABKiMqZ3Rhc_e3tkR2fxR59be3ittn6TB0Dnj93L7yXfMJ19Uga89z87T-DG97lhKvQBimUBK1L6uzRf0JWfafvwLx6dVlcLGn-tQI4uA4Uwgx4siq4_OV3Q5yKj07XsraLgfdSrGQWTSrCssHZe-NEHtAd62om4kbUD6LE84l-f9I3sA1A8fsgEY3ihnJm5WtXt5E8uhKTMwN8SjcOrrPiGvcO7TFLG52Ij0asojkCerGkFNm6CQDyUfFg7LTEarUDZ5VDjhORXonPQS4azxCCkB4sYGVExGwipGuV2-K3hCQP8bGIZueANaj6gMuxZjTWRE9mZQ8x4gNvayqlUSi-tMbKDEaNbr4tMTxKmHEq-TeK_y25Xe4uGgoMGyP8qEPOXWABSV7MP2XhIoUxEwuDutk9mcVornhTH8Ol8jC73Uup5lwQumj31MeocktQxs_MR6Oj2_tmVZqu5Y4kfEBA5TGhoOPy4iobKL38ietc0JBCTwlIo2dIq1eqaJTO4520vVQ7wa0bXLSlJH4LQdyBaJ0qGW7AwmZG4Wg4vWUpV2F8NR-z3t4t-zSzrEHxpGJpFYxic8P4DUfudxzGU0kXfVbiG6z4Cw-yXBPQE7hqvnFuhU8mNVWz7KfoKYtzMsFQjVTcYBXsSjCPRUiLiRzpgsPi86wkcaxbWMd4QT_Gf_-TaRnIIoKYhuBsch5161JUaxaU-6TAgTd06-MNQm9wtI9VKOtOhPOyjBkShX4CroyegxqoMQx3EUvcT19PqttBoazzxPDprfQKpuYNNL31lATU_jdvZQLKvnqZTpoNy2UdThnNHeoTfszZhXX4f2xTu7efSc5mhH51WLQwobzP3u5JPahmPl008cfMbkDmQ_YIdT5HtVyltryW4LmLdndWDvMu--c4NIHZqZaiGCFFmKq8KDIsRogKWnkz6-1v-Vvh02ghm9mWk4gBqY-Qzc&isca=1",
)
