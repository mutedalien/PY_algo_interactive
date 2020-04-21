# Крестики-нолики, где х побеждает с первой попытки

row = [''] * 3
board = [row] * 3
print(board)
board[0][0] = 'x'
print(board)
board = [[''] * 3 for _ in range(3)]
print(board)
board[0][0] = 'x'
print(board)
