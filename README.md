# play_ground
for playing with codes

## tic-tac-to AI with RL

### using q_table
~~라이브러리 없이 만들어보자!~~

dependency
- numpy

board.py
- 틱택토 관련 클래스 구현
- bitmask를 이용해 틱택토 보드를 정수로 치환

train.py
- Q-table을 이용해 Agent를 학습시킨 후 .npy파일로 저장

test.py
- train.py에서 학습한 데이터를 불러와 게임을 진행