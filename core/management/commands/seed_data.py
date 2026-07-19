from django.core.management.base import BaseCommand

from core.models import PersonalInfo, Project, Skill


class Command(BaseCommand):
    help = 'Seed the database with portfolio content'

    def handle(self, *args, **kwargs):
        # Personal Info
        if not PersonalInfo.objects.exists():
            PersonalInfo.objects.create(
                name='Luu Bao Khanh Phuong',
                title='Student',
                bio='Passionate developer building web apps',
                email='luubaokhanhphuong@gmail.com',
            )
            self.stdout.write(self.style.SUCCESS('Personal info created'))

        # Skills - Languages
        languages = ['Python', 'JavaScript', 'HTML/CSS', 'SQL']
        for lang in languages:
            Skill.objects.get_or_create(
                name=lang, category='language',
                defaults={'proficiency': 70},
            )

        # Skills - Frameworks
        Skill.objects.get_or_create(
            name='Django', category='framework',
            defaults={'proficiency': 65},
        )

        # Skills - Tools
        tools = ['VS Code', 'OpenCode', 'Claude', 'Git']
        for tool in tools:
            Skill.objects.get_or_create(
                name=tool, category='tool',
                defaults={'proficiency': 75},
            )

        self.stdout.write(self.style.SUCCESS('Skills created'))

        # Projects
        if not Project.objects.exists():
            Project.objects.create(
                title='Portfolio Website',
                description='Personal portfolio built with Django showcasing my skills and projects',
                tech_stack='Django, SQLite, HTML/CSS',
            )
            Project.objects.create(
                title='ERLC Roleplay Server Bot',
                description='Discord bot for managing ERLC roleplay server',
                tech_stack='Node.js, Discord.js',
            )
            self.stdout.write(self.style.SUCCESS('Projects created'))

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
