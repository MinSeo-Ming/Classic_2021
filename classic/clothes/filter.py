from .models import Clothing
from weather.models import *
from django_filters import FilterSet

class ClothesFilter(FilterSet):
    class Meta:
        model = Clothing
        fields =[]


# 첫번째 전제 조건... 현재 월 & 현재 온도를 갖고 온다.
# 온도 객체서 찾는다
#   month의 min max select mon from month where pre_temp>min and pre_temp<max_temp
# if select 결과 == null -> select max_temp from month where month='8' ifpre temp > maxtemp 
#  그럼 여름옷 추천
#                       else 가장 낮은 온도 이면 1월...? 인가 이걸 추천
# 
# 아 아ㅏㅏ 검색 할때 하루의 평균 온도로 검색 하기
# 
# select session from weather where month =="mon"
#               => Weather.object.filter(month =="")
# select * from clothing where session == 'session'; 
#               => Clothing.object.filter(session='계절')
# 이렇게 돌ㅇ가야 하나?? 잠시만 데이터 넣고 생각해보자


# excel로 데이터를 만들어서 데이터를 읽어서 넣어서 자동생성하게