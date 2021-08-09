from django.shortcuts import get_object_or_404, redirect, render
from .form import *
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import datetime
from django.views import generic
from django.urls import reverse
import copy
from databaseCreations.database_create import createDB
# createDB()
# runserver한번 한다음엔 바로 주석처리 하기 ㅋㅋㅋㅋㅋㅋ

# Create your views here.
def clothing_upload (request):
    if request.method == 'POST':
        form = UploadingFileForm(request.POST,request.FILES)
        if form.is_valid():
            upload_clothes = form.save(commit=False)
            upload_clothes.create_date = timezone.now()
            upload_clothes.author = request.user

            
            upload_clothes.save()
            return redirect(reverse('clothes:clothes_index'))
    else:
        form = UploadingFileForm()#수정할거임
        return render(request, 'clothes/test_form.html', {'form':form})
        

def clothes_index(request):
    '''
    이미지들 출력
    '''
    # page = request.GET.get('page',1)
    
    lists = Clothing.objects.order_by('-create_date')
    clothes_list=[]
    default_list =[] #로그인 하지 않은경우 default로 보여줄 값 그래서 user에 default가 존재해야함..? 아마
    #1~4 : 28도 이상
    #5~10: 27~23 도
    #11~
    for com in lists:
        if request.user == com.author:
            clothes_list.append(com)

        if str(com.author) == "default":
            default_list.append(com)
    
    if len(clothes_list)==0:
        clothes_list = copy.deepcopy(default_list)
    #if session == logout -> default 내용 뿌리기 ... 
    # 흠... 메소드 분리가필요할거 같은데 일단 보류
    #테스트가 필요함 로그인 해서 잘 뿌려지는지 확인! ->구현 확인
    
    # paginator =Paginator(clothes_list,10)
    # page_obj = paginator.get_page(page)
    context = {'clothes_list':clothes_list}

    return render(request,'clothes/test_list.html',context)

#삭제 수정이 필요함 아 만약 default이면 삭제 수정이 없게 해야함 => hidden으로 바꾸기


def clothes_detail(request,clothes_id):
    clothes = get_object_or_404(Clothing,pk = clothes_id)
    return render(request,'clothes/test_detail.html',{"clothes":clothes})

# class ClothesDetailView(generic.DetailView):
#     model = Clothing

def filter(request):
    mon = int(datetime.now().month)
    cloth_list = Clothing.objects.filter(month =mon)
    print(cloth_list)
    return render(request,'clothes/test_main.html',{'cloth_list':cloth_list})