from django.views.generic.base import TemplateView
from typing import Any, Dict


# (수정중) 이렇게 구성해도 되고, 수정하셔도 좋습니다. (urls에는 주석처리해두었습니다.)
class HomeView(TemplateView) :
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['app_list'] = [''] # 앱들 추가하면 홈화면으로 구성해줌
        return context # context에서 위의 리스트를 저장해서 홈페이지에서 보여줌
