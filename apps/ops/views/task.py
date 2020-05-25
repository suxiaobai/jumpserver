# ~*~ coding: utf-8 ~*~
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic import TemplateView, DetailView
from common.mixins import DatetimeSearchMixin
from common.permissions import PermissionsMixin, IsOrgAdmin
from ..models import Task, TaskMeta

__all__ = [
    'TaskManagementListView',
    'TaskDetailInfoView',
    'TaskExecutionHistoryView',
    'TaskUpdateView'
]


class TaskManagementListView(PermissionsMixin, DatetimeSearchMixin, TemplateView):
    template_name = 'ops/task_management_list.html'
    permission_classes = [IsOrgAdmin]

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Ops'),
            'action': _('任务管理'),
            'date_from': self.date_from,
            'date_to': self.date_to,
            'task_type': TaskMeta.TASK_TYPE_CHOICE
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class TaskDetailInfoView(PermissionsMixin, DetailView):
    model = TaskMeta
    template_name = 'ops/task_detail_info.html'
    permission_classes = [IsOrgAdmin]

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Ops'),
            'action': _('Task detail'),
            'task_info': self.get_object().task_info
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class TaskExecutionHistoryView(PermissionsMixin, DetailView):
    model = TaskMeta
    template_name = 'ops/task_execution_history.html'
    permission_classes = [IsOrgAdmin]

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Ops'),
            'action': _('Task run history'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class TaskUpdateView(PermissionsMixin, View):
    permission_classes = [IsOrgAdmin]

    def get(self, request, **kwargs):
        task_meta = TaskMeta.objects.get(pk=kwargs.pop('pk'))
        task_type = task_meta.task_type
        if task_type == 'file_deploy':
            return redirect(reverse('ops:file-task-update', kwargs={'pk': str(task_meta.id)}))