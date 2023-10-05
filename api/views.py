from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.core.cache import cache
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import UsangData
from .serializers import UsangDataSerializer
from django.http import HttpResponse, FileResponse
import zipfile
from django.conf import settings
from rest_framework import status
import os

class TokenObtainView(APIView):
    # POST 요청을 처리하는 뷰입니다.
    # 클라이언트가 제공한 사용자 인증 정보(username과 password)를 검증하여 유효한 경우, 새로운 JWT 토큰(refresh token과 access token)을 생성하고 반환합니다.
    # 유효하지 않은 인증 정보인 경우, 에러 응답을 반환합니다.
    # POST 메서드로 api/v1/token/ 엔드포인트에 요청을 보냅니다.
    # Body 탭에서 x-www-form-urlencoded 형식으로 username과 password 파라미터를 전달합니다.

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user using Django's built-in authenticate() function
        user = authenticate(username=username, password=password)

        if user is not None:
            # 사용자 인증 로직 수행

            token_key = f'token:{username}'  # 고유한 저장소(캐시 등)에 저장하기 위한 key
            # cache.set(token_key, settings.YOUR_REQUEST_LIMIT, timeout=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds())
            cache.set(token_key, settings.YOUR_REQUEST_LIMIT, timeout=None)

            refresh = RefreshToken.for_user(user)
            
            # jwt access token 생성
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=201)
        else:
            return Response({'error': 'Invalid credentials'}, 
                            status=401)

class SearchView(APIView):
    # POST 요청에 대해서만 허용되는 뷰입니다.
    # 해당 뷰에 접근하려면 클라이언트가 유효한 JWT 액세스 토큰(access token)을 제공해야 합니다.
    # 액세스 토큰이 유효한 경우, data에 대한 응답을 반환합니다.
    # 액세스 토큰이 유효하지 않거나 제공되지 않은 경우, 인증 오류 응답이 반환됩니다.
    # POST 메서드로 /search/ 엔드포인트에 요청을 보냅니다.
    # Headers 탭에서 Authorization 필드를 추가하고 값으로 "Bearer <access_token>" 형식으로 액세스 토큰(access token) 값을 전달합니다.
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token_key = f'token:{request.user.username}'
        request_count = cache.get(token_key)

        if request_count is not None:
            request_count -= 1
            cache.set(token_key, request_count)

        if request_count == 0:
            cache.delete(token_key)
            return Response({'error': 'Token expired'}, status=401)
        
        # DB에서 데이터 검색
        data = request.data.get('pub_ann_dt')
        queryset = UsangData.objects.filter(pub_ann_dt=data)
        # 검색 결과를 직렬화하여 JSON 응답 생성
        serialized_data = UsangDataSerializer(queryset, many=True).data
        if len(serialized_data) != 0:
            return Response({'data': serialized_data}, status=200)
        else:
            return Response({'message': "No data retrieved"}, status=200)


class DownloadView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        token_key = f'token:{request.user.username}'
        request_count = cache.get(token_key)

        if request_count is not None:
            request_count -= 1
            cache.set(token_key, request_count)

        if request_count == 0:
            cache.delete(token_key)
            return Response({'error': 'Token expired'}, status=401)
        
        folder_path = "/home/manager/usang/pdf"
        data = request.data.get('pub_ann_dt')
        
        zip_file_path = os.path.join(folder_path, data+".zip")  # 다운로드할 파일의 경로
    
        try:
            if os.path.exists(zip_file_path):
                with open(zip_file_path, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='application/octet-stream')
                    response['Content-Disposition'] = 'attachment; filename="%s"'%(data+".zip")
                    return response
            else:
                return HttpResponse("File not found.", status=404)
        
        except FileNotFoundError:
            return HttpResponse("Folder not found.", status=404)


class RequestCountView(APIView):
    # 이 뷰는 인증된 사용자에게만 허용되며, 해당 사용자의 request_count 값을 반환합니다.
    # 해당 뷰에 접근하려면 클라이언트가 유효한 JWT 액세스 토큰(access token)을 제공해야 합니다.
    # 요청마다 토큰 키(token:<username>)에서 request_count 값을 조회하고, 값이 존재하지 않으면 오류 응답(404 Not Found)을 반환합니다. 
    # 그렇지 않은 경우에는 { 'request_count': <count> } 형식의 응답을 반환합니다.
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token_key = f'token:{request.user.username}'
        request_count = cache.get(token_key)

        return Response({'message': "Number of requests left is %s"%request_count})