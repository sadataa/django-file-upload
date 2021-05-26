from django.apps import AppConfig


class DocumentsConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'documents'

    def ready(self):
        import documents.signals
