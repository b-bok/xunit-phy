### TODOLIST
* 테스트 메서드 호출하기
* 먼저 setUp 호출하기
* 나중에 tearDown 호출하기
* 테스트 메서드가 실패하더라도 tearDown 호출하기
* 테스트 여러개 실행하기
* 수집한 결과를 호출하기


### 테스트 작성의 공통된 패턴
1. 준비(arrage) : 객체 생성
2. 행동(act) : 어떤 자극 주기
3. 확인(assert) : 결과를 검 



### 테스트 사이의 커플링은 확실하게 지저분한 결과를 야기한다.

새로운 객체를 얼마나 자주 생성해야하는가?

성능 : 테스트가 빨리 실행되기를 원한다. 이때, 객체 하나만 생성해서 모든 테스트가 이 객체를 사용한다면!

격리 : 하나의 테스트의 성공이나 실패가 다른 테스트에 영향을 주지 않기를 원한다. 