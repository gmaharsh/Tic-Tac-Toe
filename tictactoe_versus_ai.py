board = [' ' for x in range(10)]

def insertLetter(letter, pos):
	board[pos] = letter

def freespace(pos):
	return board[pos] == ' '

def printBoard(board):
	print('   |   | ')
	print(' '+ board[1] + ' | '  + board[2] + ' | ' + board[3])
	print('   |   | ')
	print('----------')
	print('   |   | ')
	print(' '+ board[4] + ' | '  + board[5] + ' | ' + board[6])
	print('   |   | ')
	print('----------')
	print('   |   | ')
	print(' '+ board[7] + ' | '  + board[8] + ' | ' + board[9])
	print('   |   | ')

def winner(board, letter):
	return((board[7] == letter and board[8] == letter  and board[9] == letter) or
	(board[4] == letter and board[5] == letter  and board[6] == letter) or
	(board[1] == letter and board[2] == letter  and board[3] == letter) or
	(board[1] == letter and board[5] == letter  and board[9] == letter) or
	(board[3] == letter and board[5] == letter  and board[7] == letter) or
	(board[1] == letter and board[4] == letter  and board[7] == letter) or
	(board[2] == letter and board[5] == letter  and board[8] == letter) or
	(board[3] == letter and board[6] == letter  and board[9] == letter))

def playerMove():
	run = True
	while run:
		move = input("Please select a position to place your X from (1-9):")

		try:
			move  = int(move)
			if move >0 and move <10:
				if freespace(move):
					run = False
					insertLetter('X', move)
				else:
					print("Sorry, this place is occupied")
			else:
				print("Please try number within the range")
		except:
			print("Please enter a number")



def compMove():
	pass

def selectRandom(board):
	pass

def isBoardFull(board):
	if board.count(' ') > 1:
		return True
	else:
		return False

def main():
	print("Let's Play Tic Tac Toe")
	printBoard()

	while  not(isBoardFull(board)):
		if not(isWinner(board, 'O')):
			playerMove()
			printBoard()
		else:
			print('Sorry, Computer Won this time')


		if not(isWinner(board, 'X')):
			playerMove()
			printBoard()
		else:
			print('Yeah, You Won this time')


	if isBoardFull(board):
		print("Tie Game")