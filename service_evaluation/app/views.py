from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Evaluation
from app.forms import EvaluationForm, EvaluationWithServiceForm

@login_required
def evaluation(request):
    is_complete = False
    if request.method == 'POST':
        form = EvaluationWithServiceForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.user = request.user
            evaluation.save()
            is_complete = True
    else: 
        form = EvaluationWithServiceForm()

    if is_complete:
        return render(request, 'complete.html', {'user': request.user, 'service': evaluation.service} )
    else:
        return render(request, 'eval.html', {'form': form })
 


@login_required
def evaluation_with_service(request, service):
    is_complete = False
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.user = request.user
            evaluation.service = service
            evaluation.save()
            is_complete = True
    else: 
        # prev_eval = Evaluation.objects.filter(user=request.user, service=service)
        # if prev_eval.exists():
        #     is_complete = True
        # else:
        form = EvaluationForm()

    if is_complete:
        return render(request, 'complete.html', {'user': request.user, 'service': service} )
    else:
        return render(request, 'eval.html', {'form': form, 'service': service })

def index(request):
    return render(request, 'index.html')