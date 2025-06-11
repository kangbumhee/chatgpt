class BlockStacker:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.board = [['.' for _ in range(width)] for _ in range(height)]
        self.score = 0

    def drop_block(self, column):
        column -= 1
        if column < 0 or column >= self.width:
            return False
        for row in reversed(range(self.height)):
            if self.board[row][column] == '.':
                self.board[row][column] = '#'
                self.score += 1
                return True
        return False

    def display(self):
        for row in self.board:
            print(''.join(row))
        print('-' * self.width)
        print(f'Score: {self.score}')

    def is_full(self):
        return all(self.board[0][c] == '#' for c in range(self.width))

def main():
    import os
    game = BlockStacker()
    while True:
        os.system('clear')
        game.display()
        if game.is_full():
            print('Board is full! Game over.')
            break
        choice = input(f'Choose column 1-{game.width} or q to quit: ')
        if choice.lower() == 'q':
            print('Thanks for playing!')
            break
        try:
            col = int(choice)
        except ValueError:
            continue
        if not game.drop_block(col):
            print('Column full! Game over.')
            break

if __name__ == '__main__':
    main()
