from django.shortcuts import render
from .models import Memo
from django.shortcuts import get_object_or_404

# トップページの表示
def index(request):
    memos = Memo.objects.all().order_by('-updated_datetime')
    return render(request, 'app/index.html', {'memos':memos})

# メモ詳細ページ
def detail(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    return render(request, 'app/detail.html', {'memo':memo})

# メモ新規ページ
def new_memo(request):
    return render(request, 'app/new_memo.html')