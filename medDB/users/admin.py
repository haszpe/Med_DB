from django.contrib import admin
from .models import Laboratory
from .models import Employees
from .models import Project
from .models import Results
from .models import Experiments
from .models import KeyWords
from .models import Protocols
from .models import Patients


admin.site.register(Laboratory)
admin.site.register(Employees)
admin.site.register(Project)
admin.site.register(Results)
admin.site.register(Experiments)
admin.site.register(KeyWords)
admin.site.register(Protocols)
admin.site.register(Patients)
