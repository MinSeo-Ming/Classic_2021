from django.core import paginator
from django.core.checks import messages
from django.shortcuts import get_object_or_404, redirect, render
from .form import *
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import datetime
from django.views import generic
from django.urls import reverse
import copy
from databaseCreations.database_create import createDB

from django.contrib.auth.models import User
from django.core.paginator import Paginator
# createDB()

# runserver한번 한다음엔 바로 주석처리 하기 ㅋㅋㅋㅋㅋㅋ

def clothing_upload (request):
    if request.method == 'POST':
        form = UploadingFileForm(request.POST,request.FILES)
        if form.is_valid():
            upload_clothes = form.save(commit=False)
            upload_clothes.create_date = timezone.now()
            upload_clothes.author = request.user
            
            upload_clothes.save()
            return redirect('clothes:myclothes')
    else:
        form = UploadingFileForm()#수정할거임
        return render(request, 'clothes/test_form.html', {'form':form})
        

def clothing_update (request,clothes_id):
    cl = get_object_or_404(Clothing,pk =clothes_id)
    if request.user != cl.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('clothes:myclothes')
    if request.method == 'POST':
        form = UploadingFileForm(request.POST,instance=cl)
        if form.is_valid():
            upload_clothes = form.save(commit=False)
            upload_clothes.create_date = timezone.now()
            
            upload_clothes.save()
            return redirect('clothes:myclothes')
    else:
        form = UploadingFileForm(instance=cl)#수정할거임
        context ={'clothing':cl,'form':form,}
        return render(request, 'clothes/test_form.html', context)


# def clothes_index(request):
#     lists = Clothing.objects.order_by('-create_date')
#     clothes_list=[]
#     default_list =[]
    
#     for com in lists:
#         if request.user == com.author:
#             clothes_list.append(com)

#         if str(com.author) == "default":
#             default_list.append(com)
    
#     if len(clothes_list)==0:
#         clothes_list = copy.deepcopy(default_list)
#     #if session == logout -> default 내용 뿌리기 ... 
#     # 흠... 메소드 분리가필요할거 같은데 일단 보류
#     #테스트가 필요함 로그인 해서 잘 뿌려지는지 확인! ->구현 확인
    
#     # paginator =Paginator(clothes_list,10)
#     # page_obj = paginator.get_page(page)
#     context = {'clothes_list':clothes_list}

#     return render(request,'clothes/test_list.html',context)

#삭제 수정이 필요함 아 만약 default이면 삭제 수정이 없게 해야함 => hidden으로 바꾸기


def clothes_detail(request,clothes_id):
    clothes = get_object_or_404(Clothing,pk = clothes_id)
    return render(request,'clothes/test_detail.html',{"clothes":clothes})


def filter(request):
    mon = int(datetime.now().month)
    products = Clothing.objects.filter(month =mon) # 월별로 옷 필터링 하는 중 추후 기온으로 필터링 할예정
    
    cloth_list = [[products, range(1,len(products))]]
    
    return render(request,'clothes/test_main.html',{'cloth_list':cloth_list})

def getMyclothes(request):
    user = get_object_or_404(User,username = request.user)
    clothes= Clothing.objects.filter(author = request.user)
    
    paginator = Paginator(clothes,8)
    page = request.GET.get('page',1)
    
    page_obj = paginator.get_page(page)
    context = {'clothes':page_obj,'user':user}

    return render(request,'clothes/test_myclothes.html',context)

def clothing_delete(request,clothes_id):
    
    clothes = get_object_or_404(Clothing, pk = clothes_id)
    if request.user != clothes.author:
        messages.error(request,"삭제 권한이 없습니다.")
        return redirect('clothes:clothes_detail',clothes_id=clothes_id)
    
    clothes.delete()
    
    return redirect('clothes:myclothes')
    
    #rendering 을 해야함... 
    # 응답을 포워드를 하던 redirect를 하던 응답을 어떤 형태로든... 부르는 url패턴...