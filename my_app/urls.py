from django.urls import path, include
from .views import indexView, postFriend, checkNickName

app_name = 'my_app'

urlpatterns = [
    path('', indexView),
    path('post/ajax/friend', postFriend, name='post_friend'),
    path('get/ajax/validate/nickname', checkNickName, name = "validate_nickname"),
]
