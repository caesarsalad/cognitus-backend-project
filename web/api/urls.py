from django.urls import include, path

from api.views import  DataViewCreate,TrainViewGet,PredictViewGet

urlpatterns = [
    path('add/', DataViewCreate.as_view(),
        name='data_create'),
    path('train/', TrainViewGet,
        name='call_train'),
    path('predict/', PredictViewGet,
        name='call_predict'),
]
