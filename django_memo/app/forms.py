from django.forms import ModelForm
from .models import Memo

# ModelFormを継承してMemoFormを作成
class MemoForm(ModelForm):
    class Meta:
        # model=MemoとすることでMemoモデルに対応したフォームを生成        
        model = Memo
        fields = ['title', 'text']