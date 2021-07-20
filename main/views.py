from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from .models import TrainingList
from django.shortcuts import redirect, reverse
from django.conf import settings

from .models import UserInfo
from django.http import JsonResponse
import requests
from json.decoder import JSONDecodeError

from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework import status

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SigninView(TemplateView):
    template_name = 'signin.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class HomeView(ListView):
    template_name = 'home.html'
    model = TrainingList

class TestView(TemplateView):
    template_name = 'test.html'




def kakao_login(request):
    rest_api_key = getattr(settings, 'KAKAO_REST_API_KEY')
    KAKAO_CALLBACK_URI = 'http://127.0.0.1:8000/kakao/callback/'
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code"
    )

def kakao_callback(request):
    rest_api_key = getattr(settings, 'KAKAO_REST_API_KEY')
    code = request.GET.get("code")
    redirect_uri = 'http://127.0.0.1:8000/kakao/callback/'
    """
    Access Token Request
    """
    token_req = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={redirect_uri}&code={code}")
    token_req_json = token_req.json()
    print(token_req_json)
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get("access_token")
    """
    Email Request
    """
    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"})
    profile_json = profile_request.json()
    id = profile_json.get('id')
    kakao_account = profile_json.get('kakao_account')
    nickname = kakao_account.get('profile').get('nickname')

    """
    kakao_account에서 이메일 외에
    카카오톡 프로필 이미지, 배경 이미지 url 가져올 수 있음
    print(kakao_account) 참고
    """
    # print(kakao_account)
    """
    Signup or Signin Request
    """
    try:
        user = UserInfo.objects.get(id=id)
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            "http://127.0.0.1:8000/kakao/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        # return JsonResponse(accept_json)
        return redirect("http://127.0.0.1:8000/home")

    except UserInfo.DoesNotExist:
        # 기존에 가입된 유저가 없으면 새로 가입
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            "http://127.0.0.1:8000/kakao/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
        # user의 pk, email, first name, last name과 Access Token, Refresh token 가져옴
        accept_json = accept.json()
        accept_json.pop('user', None)
        # return JsonResponse(accept_json)
        return redirect("http://127.0.0.1:8000/home")
        
class KakaoLogin(SocialLoginView):
    KAKAO_CALLBACK_URI = 'http://127.0.0.1:8000/kakao/callba'
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = KAKAO_CALLBACK_URI