from django.views.generic import TemplateView

from .models import PersonalInfo, Project, Skill


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = PersonalInfo.objects.first()
        context['languages'] = Skill.objects.filter(category='language')
        context['frameworks'] = Skill.objects.filter(category='framework')
        context['tools'] = Skill.objects.filter(category='tool')
        context['projects'] = Project.objects.all()
        return context
