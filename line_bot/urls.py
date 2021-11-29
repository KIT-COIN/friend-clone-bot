from django.contrib import admin
from django.urls import include, path  # 追加部分

urlpatterns = [
    path('line_bot_ai/', include('line_bot_ai.urls')),  # 追加部分
    path('admin/', admin.site.urls),
]
