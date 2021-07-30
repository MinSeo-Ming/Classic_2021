from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q, Count


def index(request):
# board 목록 출력
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 정렬하기 (수정중) (최신순으로 모두 반영될때가 있어 꼭 필요한 기능으로 판단되었을 경우 develop 하는 방향으로 가는게 어떨까요?)
    so = request.GET.get('so', 'recent') # 정렬 기준
    if so == 'recommend':  # 추천순
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':  # 인기순
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:                  # 최신순
        question_list = Question.objects.order_by('-create_date')

    # 조회(검색)
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) |  # 답변 글쓴이 검색
            Q(answer__content__icontains=kw) # 답변 내용 검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page':page, 'kw':kw, 'so':so}
    return render(request, 'board/question_list.html', context)


def detail(request, question_id):
# board 내용 출력
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)
