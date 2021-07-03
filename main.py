import random as r
import time as t

class BlueMarble:
    road1 = '0000jb00000000f00001'
    road2 = '00000000j00000b00001'
    road3 = '000b000000000j000001'
    road4 = '00000f0000000000b001'

    board = road1 + road2 + road3 + road4

    def dice(self, player):
        amount = 0
        while True:
            input('{} 주사위 던지기\n'.format(player.name))
            for i in range(0, 5):
                print(r.sample(['.', '!', '@', '#', '$', '%'], 1)[0], end='')
                t.sleep(0.2)

            dice1 = r.randint(1, 6)
            dice2 = r.randint(1, 6)

            print('\n첫번째 주사위: {}'.format(dice1))
            print('두번째 주사위: {}'.format(dice2))
            amount += dice1 + dice2

            if not self.isSame(dice1, dice2):
                break
        print('합계: {}'.format(amount))

        return amount

    def isSame(self, d1, d2):
        if d1 == d2:
            return True
        return False

class Player:
    name = ""
    position = 0
    board = BlueMarble.board
    turnCount = 0

    def move(self, moveNum):
        self.position += moveNum
        if self.position > len(self.board):
            self.turnCount += 1
            self.position -= len(self.board)
        print('{} {}로 이동! \n'.format(self.name,self.position))
        while self.blockDetect():
            continue
        print('현재 {}의 위치는 {}번 블록 입니다'.format(self.name, self.position))

    def blockDetect(self):
        block = self.board[self.position]
        if block == 'j':
            self.position = 0
            print('앗! J칸에 와버렸어요! 다시 원점으로 돌아갑니다.')
            return True
        elif block == 'b':
            self.position -= 3
            print('오 이런, B칸에 왔어요! 3칸 뒤로 가야됩니다.')
            return True
        elif block == 'f':
            self.position += 2
            print('와! F칸에 왔네요! 2칸 앞으로 가겠습니다.')
            return True
        return False


if __name__ == '__main__':
    game = BlueMarble()
    peopleNum = int(input('플레이어 수: '))
    players = []
    for i in range(0, peopleNum):
        player = Player()
        player.name = "PLAYER{}".format(r.randint(1, 1000))
        players.append(player)

    while True:
        for i in players:
            result = game.dice(i)
            i.move(result)
