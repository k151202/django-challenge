from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "This command superuser"

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username="ebadmin")
        if not admin:
            User.objects.create_superuser("admin", "k151202@naver.com", "admin")
            self.stdout.write(self.style.SUCCESS(f"Superuser Created"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser Exists"))
