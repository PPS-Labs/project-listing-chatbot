from django.db import models


class Component(models.Model):
    """A robotics component like a sensor, actuator, or microcontroller."""
    CATEGORY_CHOICES = [
        ('microcontroller', 'Microcontroller'),
        ('sensor', 'Sensor'),
        ('actuator', 'Actuator'),
        ('module', 'Module'),
        ('display', 'Display'),
        ('power', 'Power'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    keywords = models.TextField(
        help_text="Comma-separated keywords for matching (e.g., 'arduino, uno, atmega328')"
    )

    def __str__(self):
        return self.name

    def get_keywords_list(self):
        return [kw.strip().lower() for kw in self.keywords.split(',') if kw.strip()]


class Project(models.Model):
    """A robotics project idea."""
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=15, choices=DIFFICULTY_CHOICES)
    components = models.ManyToManyField(Component, through='ProjectComponent')
    instructions = models.TextField(blank=True, help_text="Brief build instructions or tips")

    def __str__(self):
        return self.title


class ProjectComponent(models.Model):
    """Links a project with a required component and its quantity."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('project', 'component')

    def __str__(self):
        return f"{self.project.title} - {self.component.name} x{self.quantity}"


class ChatSession(models.Model):
    """Stores a chat conversation session."""
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.id} - {self.created_at}"


class ChatMessage(models.Model):
    """Individual chat message within a session."""
    ROLE_CHOICES = [
        ('user', 'User'),
        ('bot', 'Bot'),
    ]

    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=4, choices=ROLE_CHOICES)
    content = models.TextField()
    matched_components = models.ManyToManyField(Component, blank=True)
    suggested_projects = models.ManyToManyField(Project, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"[{self.role}] {self.content[:50]}..."
