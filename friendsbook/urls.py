from post.views import post_detail, post_feed, add_post
from profilepage.views import profile_detail
from useraccount.views import useraccount_edit
from business.views import business_listing
from django.conf import settings
from django.conf.urls.static import static

"""friendsbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post.views import handler_404, PostList
from useraccount.views import accountlist

handler404 = handler_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_feed, name='home'),
    path('post/<int:post_id>', post_detail, name='post'),
    path('add_post', add_post),
    path('profile/<int:profilepage_id>', profile_detail, name='profile page'),
    path('useraccount/<int:useraccount_id>/edit', useraccount_edit, name='edit user profile'),
    path('businesses', business_listing, name='business_listing'),
    path("postlist", PostList.as_view(), name="post_list"),
    path('accountlist', accountlist, name='account_listing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
