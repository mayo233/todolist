from django.shortcuts import render

def index(request):
    # テスト用
    records = Timer.objects.all()
    return render(request, 'record/index.html', {'records': records})

