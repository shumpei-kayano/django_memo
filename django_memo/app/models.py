from django.db import models

# Create your models here.
class Memo(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    # モデルインスタンスが初めて作成されたときにフィールドが現在の日時で自動的に設定
    created_datetime = models.DateTimeField(auto_now_add=True)
    # モデルインスタンスが保存されるたびにフィールドが現在の日時で自動的に更新
    updated_datetime = models.DateTimeField(auto_now=True)