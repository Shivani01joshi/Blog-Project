from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.timezone import now

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    print(f"User {user.username} logged in at {now()}")
    ip=request.META.get("REMOTE_ADDR")
    print("client IP",ip)
    request.session['ip']=ip