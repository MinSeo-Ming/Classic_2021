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
    cloth_list = Clothing.objects.filter(month =mon) # 월별로 옷 필터링 하는 중 추후 기온으로 필터링 할예정
    
    return render(request,'clothes/test_main.html',{'cloth_list':cloth_list})

def getMypage(request):
    mon = int(datetime.now().month)
    if request.user=='default' or request.user =='admin':
        pass
    # 난 x모달을 띄우고 싶음-> html을 따로 만든다.. bootstrap -> 데코레이터 로그인 유무 하는것처럼 파이보 처럼 하는 방법이 하나 있음 success/fail -> 추후 방식으로.... 
    # best : template안에 띄우는거 brower/localstorage에서 세션 정보 저장 가능 key value로 저장하고  -> js에서 처리 
    # 세션 스토리지  이걸로 저장 하고 : 로컬 스토리지로 저장하기... 
    # view rendering해서 전송하는거라 성공 에러로 렌더링을 다르게.. 데이터에 따라 프론트에서 하면 되지만... 여기선 페이지 렌더링이라..
    else:
        user = Clothing.objects.filter(author=request.user)
        if user =='':
            pass
        #그럴일은 없겠지만 혹시나 해서 넣어둠
        clothes = Clothing.objects.filter(author = request.user,month = mon)
        if clothes ==[] :
            pass
        #x모달 띄우기        

    