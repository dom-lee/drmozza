# 닥터 자르트(Dr.Jart+) Clone Project

## 프로젝트 소개
- React, Django를 이용한 [Dr.Jart+](https://us.drjart.com) 홈페이지 클론 프로젝트
- 첫 협업 프로젝트로서, 다양한 카테고리를 활용할 수 있는 커머스 사이트 중 닥터자르트를 선정했습니다.
- 짧은 프로젝트 기간, 개발에 집중하기 위하여 디자인 및 기능의 기획 부분만 클론했습니다.
- 개발은 초기 세팅부터 전부 직접 구현하였습니다.

## 데모영상
(이미지 클릭시 유튜브 링크로 이동)

[![](https://img.youtube.com/vi/lqHxD3Zq770/0.jpg)](https://www.youtube.com/watch?v=lqHxD3Zq770)

## 프로젝트 참여자
- front-end: [황소미](https://github.com/somangoi), [박정훈](https://github.com/Junghoon-P), [이종민](https://github.com/sui3422)
- back-end: [이동명](https://github.com/dom-lee), [김한준](https://github.com/hanjkim10), [안희수](https://github.com/heesu-ahn)
 
## API 문서
- https://documenter.getpostman.com/view/12180757/Tzm3nciR

## 프로젝트 기간
- 2021.7.5 - 2021.7.16

## 기술스택
- Front-End : JavaScript, React.js, sass
- Back-End : Python, Django, MySQL, Bcrypt, PyJWT

## 팀원별 역할
### 공통
- 프로젝트 초기 세팅
- Database 모델링 및 ERD 작성

### 이동명
* 장바구니 엔드포인트
  - 카트 제품 추가 및 수량 변경
  - 요청 수량 및 재고 비교
* 주문 엔드포인트
  - 카트에 있는 제품 주문
  - 주문 이력 관리
* 쿠폰 엔드포인트
  - 쿠폰 코드 유효성 검토
* 메인페이지 엔드포인트
  - 메인페이지 Banner data 제공
  - 네비게이션바 data 제공
* 백엔드 서버 배포
  - AWS(EC2, RDS) 연동

### 김한준
* 회원가입 & 로그인
  - 이메일, 비밀번호 정규식 검사
  - 비밀번호 BCRYPT 암호화
  - JWT ACCESS TOKEN 전송
* 유저인증
  - JWT ACCESS TOKEN 유효성 검토
  - decorator로 활용
* 제품 상세페이지 엔드포인트
  - 특정 상품 상세 data
  - 상품에 따 추천/비교 상품 data

### 안희수
* 카테고리 페이지 엔드포인트
  - 카테고리별 제품 data
  - 가격/판매량/평점에 따라 Sort된 제품 List 제공


## Reference
- 이 프로젝트는 [닥터 자르트](https://us.drjart.com) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
