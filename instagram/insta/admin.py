from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

#admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(Friend)
admin.site.register(otp_generate)
admin.site.register(FriendRequest)

'''
  current_site = get_current_site(request)

  from_mail =EMAIL_HOST_USER
  mail_subject = 'Activate your blog account.'
  message = render_to_string('insta/activation.html',{
       'user': user,
       'domain': current_site.domain,
       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
       'token': account_activation_token.make_token(user),
    })
    # to_email = form.cleaned_data.get('email')
  to_email = user.email
  # print(to_email)
  # email = EmailMessage(
  #  mail_subject, message,from_mail, to=[to_email]
  #   )
  #email.send()
  send_mail(mail_subject, message, from_mail, to_email, fail_silently=False)
  messages.success(request, 'Confirm your email to complete registering with ONLINE-AUCTION.')
  return Response('Please confirm your email address to complete the registration')
 
        #current_site = get_current_site(data.request)
        current_site=EMAIL_HOST_USER
        mail_subject = 'Activate your blog account.'
        message =render_to_string('insta/activation.html',{
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        #to_email = form.cleaned_data.get('email')
        to_email=user.email
        print(to_email)
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return Response('Please confirm your email address to complete the registration')

# current_site = get_current_site(data.request)
current_site = EMAIL_HOST_USER
mail_subject = 'Activate your blog account.'
message = render_to_string('insta/activation.html', {
    'user': user,
    'domain': current_site.domain,
    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    'token': account_activation_token.make_token(user),
})
# to_email = form.cleaned_data.get('email')
to_email = user.email
print(to_email)
email = EmailMessage(
    mail_subject, message, to=[to_email]
)
email.send()
return Response('Please confirm your email address to complete the registration')
'''
