# django_usang
이 프로젝트는 Django REST 프레임워크를 사용하여 작성된 API입니다.<br>
유상증자 중 주주배정증자 원시 공문 데이터를 조회할 수 있습니다.
<br><br><br>

## 기술 스택
- django-chartjs                      2.3.0<br>
- django-cors-headers                 4.0.0<br>
- djangorestframework                 3.14.0<br>
- djangorestframework-simplejwt       5.3.0<br>
<br><br><br>

## 사용 방법
### 1. Token Key 발급
- URL: http://172.25.0.21:8001/api/v1/token/
- Method: POST
- Request Body:
```
{
  "username": "test",
  "password": "test123~"
}
```
- Response: Success 200 OK
- Response Body:
```
{
    "refresh": refresh_access_key,
    "access": jwt_access_key
}
```
- Response: Failed 401 Unauthorized (잘못된 사용자)
- Response Body:
```
{
    "error": "Invalid credentials"
}
```
<br><br>
### 2. 유상증자 검색 API
접근하기 위해 발급받은 JWT 토큰이 필요합니다.
- URL: http://172.25.0.21:8001/api/v1/search/
- Method: POST
- Headers:
```
Authorization: "Bearer <JWT_TOKEN>" 
```
- Request Body:
```
### 조회할 공시날짜
{
  "pub_ann_dt": "2023-09-14"
}
```
- Response: Success 200 OK
- Response Body:
```
### 해당 날짜에 공시가 있을때
{
    "data": [
        {
            "cst_cnt": "6173763",
            "pst_cnt": "-",
            "cst_iss_val": "36574",
            "pst_iss_val": "-",
            "pre_cst_val": "-",
            "pre_pst_val": "-",
            "pre_cst_val_dt": "-",
            "pre_pst_val_dt": "-",
            "all_bs_dt": "2023- 09- 13",
            "new_asn_cnt": "0.047",
            "emp_bgn_dt": "-",
            "emp_end_dt": "-",
            "sh_bgn_dt": "2023- 09- 13",
            "sh_end_dt": "2023- 09- 13",
            "pym_dt": "2023- 09- 13",
            "prc_pln": "미발행 처리",
            "lst_pln_dt": "-",
            "chf_agn": "-",
            "nst_gv_yn": "N",
            "fip_cm": "-",
            "nst_rm": "신주인수권증서 미발행9) 기타사항① 청약증거금은 납입일에 주금 납입금으로 대체하며 청약일로부터 납입일까지의 이자는 없습니다.② 1주 미만의 단수주는 절사하여 배정하지 않습니다.③ 상기의 기재사항은 관계기관과의 협의 및 진행과정에서 변경될 수 있습니다.④ 기타 본건 신주발행과 관련한 부수적인 사항은 대표집행임원에게 위임합니다.",
            "nst_sch_dt": "-",
            "notes": "1) 2023년 9월 13일 이사회에서 결의된 신주발행에 관한 공시입니다.2) 신주의 종류와 수  기명식 보통주 6,173,763주3) 주당 액면가액  500원4) 신주의 발행예정가액  36,574원(모집가액 36,574원은 2023년 9월 13일에 당사 이사회를 통하여 결정하였습니다. 당사는 주권비상장법인으로서 당사의 금번 유상증자의 모집가액은 주권상장법인의 시가 발행을 통한 유상증자 모집가액 산출 방식인 증권의 발행 및 공시 등에 관한 규정 제5장 제518조(유상증자의 발행가액)을 적용받지 않습니다.)5) 신주의 배당기산일은 당사 정관 제11조(동등배당)에 의거하여 기재를 생략합니다.6) 청약 취급처  당사 본점 (경기도 성남시 분당구 판교로227번길 23(삼평동))7) 납입처  하나은행 삼성역지점8) 신주인수권에 관한 사항  신주인수권증서 미발행9) 기타사항① 청약증거금은 납입일에 주금 납입금으로 대체하며 청약일로부터 납입일까지의 이자는 없습니다.② 1주 미만의 단수주는 절사하여 배정하지 않습니다.③ 상기의 기재사항은 관계기관과의 협의 및 진행과정에서 변경될 수 있습니다.④ 기타 본건 신주발행과 관련한 부수적인 사항은 대표집행임원에게 위임합니다.",
            "recei_dt": "2023-08-22"
        },
        {
            "cst_cnt": "6173763",
            "pst_cnt": "-",
            "cst_iss_val": "36574",
            "pst_iss_val": "-",
            "pre_cst_val": "-",
            "pre_pst_val": "-",
            "pre_cst_val_dt": "-",
            "pre_pst_val_dt": "-",
            "all_bs_dt": "2023- 09- 13",
            "new_asn_cnt": "0.047",
            "emp_bgn_dt": "-",
            "emp_end_dt": "-",
            "sh_bgn_dt": "2023- 09- 13",
            "sh_end_dt": "2023- 09- 13",
            "pym_dt": "2023- 09- 13",
            "prc_pln": "미발행 처리",
            "lst_pln_dt": "-",
            "chf_agn": "-",
            "nst_gv_yn": "N",
            "fip_cm": "-",
            "nst_rm": "신주인수권증서 미발행9) 기타사항① 청약증거금은 납입일에 주금 납입금으로 대체하며 청약일로부터 납입일까지의 이자는 없습니다.② 1주 미만의 단수주는 절사하여 배정하지 않습니다.③ 상기의 기재사항은 관계기관과의 협의 및 진행과정에서 변경될 수 있습니다.④ 기타 본건 신주발행과 관련한 부수적인 사항은 대표집행임원에게 위임합니다.",
            "nst_sch_dt": "-",
            "notes": "1) 2023년 9월 13일 이사회에서 결의된 신주발행에 관한 공시입니다.2) 신주의 종류와 수  기명식 보통주 6,173,763주3) 주당 액면가액  500원4) 신주의 발행예정가액  36,574원(모집가액 36,574원은 2023년 9월 13일에 당사 이사회를 통하여 결정하였습니다. 당사는 주권비상장법인으로서 당사의 금번 유상증자의 모집가액은 주권상장법인의 시가 발행을 통한 유상증자 모집가액 산출 방식인 증권의 발행 및 공시 등에 관한 규정 제5장 제518조(유상증자의 발행가액)을 적용받지 않습니다.)5) 신주의 배당기산일은 당사 정관 제11조(동등배당)에 의거하여 기재를 생략합니다.6) 청약 취급처  당사 본점 (경기도 성남시 분당구 판교로227번길 23(삼평동))7) 납입처  하나은행 삼성역지점8) 신주인수권에 관한 사항  신주인수권증서 미발행9) 기타사항① 청약증거금은 납입일에 주금 납입금으로 대체하며 청약일로부터 납입일까지의 이자는 없습니다.② 1주 미만의 단수주는 절사하여 배정하지 않습니다.③ 상기의 기재사항은 관계기관과의 협의 및 진행과정에서 변경될 수 있습니다.④ 기타 본건 신주발행과 관련한 부수적인 사항은 대표집행임원에게 위임합니다.",
            "recei_dt": "2018-01-09"
        }
    ]
}

### 해당 날짜에 공시가 없을때
{
    "message": "No data retrieved"
}
```
- Response: Failed 401 Unauthorized (잘못된 토큰키)
- Response Body:
```
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}
```
<br><br>
### 3. 남은 만료횟수 조회
해당 JWT 토큰키의 만료횟수를 조회합니다
- URL: http://172.25.0.21:8001/api/v1/count/
- Method: GET
- Headers:
```
Authorization: "Bearer <JWT_TOKEN>"
```

- Response: Success 200 OK
- Response Body:
```
{
    "message": "Number of requests left is 2"
}
```
- Response: Failed 401 Unauthorized (잘못된 토큰키)
- Response Body:
```
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}
```
