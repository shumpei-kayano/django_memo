from django.shortcuts import render, redirect
from .models import Memo
from .forms import MemoForm
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
    # POST送信でnew_memoにアクセスした時
    if request.method == "POST":
        # ユーザー入力情報を元にMemoFormインスタンスの生成
        form = MemoForm(request.POST)
        '''
        if form.is_valid():では、生成されたMemoインスタンスが正しい値を持っているかを検証している。
        Memoモデルは、タイトルが150文字より多かったりタイトルがblankではいけないなどの条件を指定しているが
        インスタンスがこの条件を満たしているかを判定している
        '''
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        '''
        MemoFormをインポートして、変数formに代入
        これで、new_memo.htmlでは、{{ form }}という記述でフォームが表示されるようになる。
        '''
        form = MemoForm
    return render(request, 'app/new_memo.html', {'form': form })