from django import forms
from board.models import Question, Answer, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content', 'top_fixed'] # QuestionForm에서 사용할 Question 모델의 속성
        # Question 모델과 연결된 폼으로, 속성으로 Question 모델의 subject, content를 사용합니다.
        labels = {
            'subject' : '제목 ',
            'content' : '내용 ',
            'top_fixed' : '상단고정 ',  # 공지사항 상단고정하기 추가
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }