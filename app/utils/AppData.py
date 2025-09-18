from app.models import Project, Category, Experience, Skill, User


class AppData:
    def __init__(self):
        self._categories = None
        self._experiences = None
        self._skills = None
        self._projects = None
        self._users = None

    @property
    def categories(self):
        if self._categories is None:
            self._categories = Category.objects.prefetch_related("category").all()
        return self._categories

    @property
    def experiences(self):
        if self._experiences is None:
            self._experiences = Experience.objects.all().order_by("user")
        return self._experiences

    @property
    def skills(self):
        if self._skills is None:
            self._skills = Skill.objects.all().order_by("name")
        return self._skills

    @property
    def projects(self):
        if self._projects is None:
            self._projects = Project.objects.all().order_by("user")
        return self._projects

    @property
    def users(self):
        if self._users is None:
            self._users = User.objects.first()
        return self._users

    # ==== MÉTODO DE ESTADÍSTICAS PARA DASHBOARD====
    def counts(self):
        return {
            "num_categories": self.categories.count(),
            "num_experiences": self.experiences.count(),
            "num_skills": self.skills.count(),
            "num_projects": self.projects.count(),
        }
