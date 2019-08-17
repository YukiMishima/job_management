from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.views.generic import TemplateView
from django.shortcuts import render

from .models import Job
from .filters import JobFilter
from .forms import JobForm


# Create your views here.
# 検索一覧画面
class JobFilterView(LoginRequiredMixin, FilterView):
    model = Job
    filterset_class = JobFilter
    # デフォルトの並び順を新しい順とする
    queryset = Job.objects.all().order_by('-send_date')

    # クエリ未指定の時に全件検索を行うために以下のオプションを指定（django-filter2.0以降）
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 5

    # 検索条件をセッションに保存する or 呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)


# 詳細画面
class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job


# 登録画面
class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    success_url = reverse_lazy('index')


# 更新画面
class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    success_url = reverse_lazy('index')


# 削除画面
class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = reverse_lazy('index')

def OutcarView(request):
    return render(request, 'app/outcar.html')