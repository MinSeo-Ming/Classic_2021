from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Clothes_Main_type(models.Model):
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.type

class Color(models.Model):
    color = models.CharField(max_length=20)
    def __str__(self):
        return self.color

# 분리를 시켜서 좀더 구체화를 해야함


class Length(models.Model):
    length = models.CharField(max_length=10)
    def __str__(self):
        return self.length


class Clothing(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    type = models.ForeignKey(Clothes_Main_type,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    
    alias = models.CharField(max_length=10) # 별명 혹은 이름
    create_date = models.DateTimeField()
    month = models.IntegerField() #계절 입력
    
    length = models.ForeignKey(Length,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="clothing/images") #DB에는 파일명만 저장 , 실질적인 이미지 데이터는 media의clothing/images에 저장

    def __str__(self):
        return self.alias
##어떤 모델링이 좋을지 감이 안잡히네...
#온도로 필터링을 하려면 옷 정보에 온도를 넣는게 좋은데.....
#굉장히 고민이 되네... 어떤걸로 나누지.... 범용적인걸 생가가혐 그냥 이 모델링에서 진행하는게 가장 좋은거고...
# 그냥 돌아가는 걸 생각하면 기준 데이터랑 분리를 해야하고....

# 일단 1. 시나리오 : 범용적이게 데이터를 넣어둔다.
# 나중을 위해 자세히 설명을 하면 기준 데이터 (로그인을 하지 않아도  보여줄 애들을 넣을때 디비에 배열로 아,아아아ㅏㅏㅏㅏㅏㅏ -> 기온부분에 최고 기온 최저 기온을 따로 분리 하자! 좋아좋아 )
#
# 왜냐면 날씨 객체를 다르게 넣어둬서............ 흠으으으음... 생각을 했는데 안보이게 하는건 어렵겠지...?? 가능할것도 같은데 admin 아 근데 
# 좀더 생각을 해보자


# 개선된 시나리오:
# 그냥 현재 모델링 상태에서 진행을 하되,
# 계절은 내가 2가지로 넣어두자 (봄 가을인경우 아님 같은 이름 다른 이미지를 넣어서 계절을 분리)
#  결론은 일단 날씨랑옷 모델링은 그대로 두되, 쿼리 질문을 어찌 짤지 좀 생각을 해보자 필터링이 많이 필용 할거 같다아아아아아

# --------------------

# 결론
# 모델리은 옷에서 session 계절 부분을 고유로 가져가게함
# 검색과관련된 필터링은 다른 파일에서 weather 과 clothing의 조인문으로 해결할 예정 -> 이걸 알아봐야한다. 08.02 
# 고로 default 데이터를 넣을떄 좀 10~25도 사이 옷들은 내가 2가지 버전 봄 버전 가을 버전으로 넣어줘야함 -> 스크립트로 만들고 싶다.

# 대신 날씨 모델링은 수정이 필요함 최고 기온 최저 기온해서 나중에 온도 &오늘 날짜 month를 받아 왔을때 
# 1차로는 계절로 필터링...? 흠...날씨 모델링을 찢어야 하나
#날씨 모델링을 일단..... 찢자 그게 중요할거 같다.

# 1. 계절로 찢고 (봄 여름 가을 겨울 ,달)
# 2. 미세 먼지로 찢고 
# 3. 달별로... 일단은 찢어보자 (최저 기온, 최고 기온 ,달)

#그럼 지금 생각하는 꼬이는 것들이 해결될거 같음...!! 일단 모델링 수정

#필터링이 들어갈건
#시나리오
# 오늘 현재 시각& 위치를 기반으로 날씨를 가져온다
# 온도 날짜(달)로 필터링을 한다. 
#       -> 만약 달과 최저 최고 기온이 매치가 되면 계절에 따라 
#           설정한......? 이것도 살짝 분류가 필요 하겠네.. 암튼 옷을 가져오고
#       -> 만약 맞지 않으면 +- 위아래 계절로 들어가서 온도를 필터링해서 거기에 맞는 옷을 가져온다.



# 장고 모델 쿡북 -> 사이트 에서 참조하기 다대 다 관계 쿼리문으로 