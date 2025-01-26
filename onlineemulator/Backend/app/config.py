import os

DB_URL = os.getenv("DB_URL","mongodb://dan:dan@localhost:27017/main_db?replicaSet=rs0")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME","dan-terraform-s3")  # S3 bucket name
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID","AKIAYXWBODBPDV3GGIU4")  # AWS access key
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY","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")  # AWS secret key

