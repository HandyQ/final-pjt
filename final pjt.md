- 홈 화면
  - 영화 리스트 (개봉순)으로 보여주기 (카드식, 리스트식)
    - 영화 클릭하면 상세정보보기
      - 평점, 개봉, 줄거리, 출연진, ...
  - 네비게이션 바
    - 회원정보(로그인, 회원가입, ...)
    - 리뷰쓰기 & 보기
    - 영화 랭킹(관객수, 개봉순, 평점순, 리뷰순)



- 기능
  - 회원가입( 로그인, 정보수정, 팔로우 ...)
    - 아이디, 비밀번호, 이름, 좋아하는 영화 장르, 프로필사진
    - 소셜 로그인
  - 영화 리스트 보여주기
    - 검색하는 기능
    - 종류별(관객수, 개봉순, 평점순, 리뷰순) 으로 보여주기
    - 추천
    - 비슷한 영화 추천(같은 장르, 출연진)
  - 예매하기
  - 찜하기



- 어려운거
  - 종류별(관객수, 개봉순, 평점순, 리뷰순) 으로 보여주기
  - 검색하는 기능
  - 비슷한 영화 추천(같은 장르, 출연진)
  - CSS 꾸미기
  - 예매하기



- 추가할 만한 기능
  - 별로 평점 표시
  - 예고편, 사진들



# django

- app
  - accounts
  - movies
  - communities
- url
  - accounts
    - 로그인 - accounts/login		POST
    - 회원가입 - accounts/signin      POST
    - 회원탈퇴 - accounts/{user_id}      DELETE
    - 정보수정 - accounts/{user_id}    PUT
    - 프로필 - accounts/{user_id}     GET
  - movies
    - 영화 목록 - movies/				GET
    - 상세 정보 - movies/{movie_id}           GET
  - reviews
    - 목록 - reviews/          GET
    - 생성 - reviews/	POST
    - 상세정보 - reviews/{community_id}     GET
    - 삭제 - reviews/{community_id}    DELETE
    - 수정 - reviews/{community_id}   PUT



- tmdb api

```6b3db2093be8e14d01eccd56d390ec42```





## 일정	

- 19(수)
  - 회원가입, 로그인,(css) 영화 데이터베이스 저장
- 20(목) 
  - 영화 데이터 가져오기
  - 유저 관련된거 다 끝내기(로그인, 로그아웃, 회원가입, **정보수정**, 팔로우)
  - 홈 화면에 영화 리스트(개봉순) 보여주기
    - 페이지네이션
    - 카드식? 리스트식?
  - 리뷰 쓰고 읽기
    - 영화제목, 영화포스터, **리뷰, 댓글**...
- 21(금)
  - **종류별**(관객순, 평점순, ..) 보여주기
  - 검색기능
- 22(토)
  - CSS(BootStrap)
- 23(일)
  - Vue 가능하면
- 24(월)
- 25(화)
- 26(수)
- 27(목)