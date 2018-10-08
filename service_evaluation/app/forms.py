from django import forms
from app.fields import ListTextWidget
from app.models import Evaluation

AVAILABLE_SERVICE = ['ระบบแจ้งซ่อม', 'ระบบฐานข้อมูลวิจัย']

class EvaluationForm(forms.ModelForm):
    performance_score = forms.ChoiceField(
        choices=Evaluation.EVAL_CHOICES,
        label=Evaluation.PERFORMANCE_LABEL,
        widget=forms.RadioSelect())

    ease_of_use_score = forms.ChoiceField(
        choices=Evaluation.EVAL_CHOICES,
        label=Evaluation.EASE_OF_USE_LABEL,
        widget=forms.RadioSelect())

    correctness_score = forms.ChoiceField(
        choices=Evaluation.EVAL_CHOICES,
        label=Evaluation.CORRECTNESS_LABEL,
        widget=forms.RadioSelect())

    comment = forms.CharField(label=Evaluation.COMMENT_LABEL, widget=forms.Textarea())
    class Meta:
        model = Evaluation
        fields = ( 
            'performance_score', 'ease_of_use_score', 
            'correctness_score', 'comment',)

class EvaluationWithServiceForm(forms.ModelForm):
    service = forms.CharField(
        label="ชื่อระบบที่จะประเมิน", 
        widget=ListTextWidget(data_list=AVAILABLE_SERVICE, name="service"))

    performance_score = forms.ChoiceField(
        choices=Evaluation.EVAL_CHOICES, 
        label=Evaluation.PERFORMANCE_LABEL, 
        widget=forms.RadioSelect())

    ease_of_use_score = forms.ChoiceField(
        choices=Evaluation.EVAL_CHOICES, 
        label=Evaluation.EASE_OF_USE_LABEL, 
        widget=forms.RadioSelect())

    correctness_score = forms.ChoiceField(
        choices=Evaluation.EVAL_CHOICES, 
        label=Evaluation.CORRECTNESS_LABEL, 
        widget=forms.RadioSelect())

    comment = forms.CharField(
        label=Evaluation.COMMENT_LABEL,
        widget=forms.Textarea())

    class Meta:
        model = Evaluation
        fields = ( 'service',
            'performance_score', 'ease_of_use_score', 
            'correctness_score', 'comment',)
