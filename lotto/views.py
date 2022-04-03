from random import sample
from django.shortcuts import render


# Create your views here.
def lotto_input(request):
    if request.method == "GET":
        return render(request, "lotto.html")


lotto_num = list(range(1,46))

def lotto_result(request):
    if request.method == "POST":
        result = []
        num = request.POST.get("num", "")
        if num == "" or int(num) == 0:
            return render(request, "lotto_result.html", {"result":"공백 or 0을 제외한 자연수를 입력해주세요."})
        for i in range(int(num)):
            random_num = sample(lotto_num, 7)
            result.append(random_num)
        return render(request, "lotto_result.html", {"result":result, "num":num})
