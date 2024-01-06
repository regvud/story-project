from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Change the following values as per your requirements
        app = SocialApp.objects.create(
            provider="google",
            name="Google",
            client_id="431854145639-imlb1bu2ufuktskff2uhjq9l3b4g2d4a.apps.googleusercontent.com",
            secret="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",
        )

        # Associate the social app with the default site
        site = Site.objects.get_current()
        app.sites.add(site)
        app.save()

        self.stdout.write(self.style.SUCCESS("Social App added successfully!"))
