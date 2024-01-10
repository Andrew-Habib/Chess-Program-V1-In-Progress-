from tkinter import Tk, Frame, Label, font
from DrewChessClassV1 import ChessBoard

surfaceWindow = Tk()
surfaceWindow.title("Andrew Habib - Experimental Chess Program")
windowHeight, windowWidth = surfaceWindow.winfo_screenheight(), surfaceWindow.winfo_screenwidth()
xPosWindowLocation = surfaceWindow.winfo_screenwidth() // 2 - windowWidth // 2
yPosWindowLocation = surfaceWindow.winfo_screenheight() // 2 - windowHeight // 2
surfaceWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, 
    xPosWindowLocation, yPosWindowLocation))
surfaceWindow.state("zoomed")
surfaceWindow.configure(background='#0D0D0D')
surfaceWindow.resizable(False, False)
original_width, original_height = windowWidth, windowHeight

titleFont = font.Font(family="Cooper Black", size=40)

mainFrame = Frame(surfaceWindow, height=windowHeight, width=windowWidth, background="#0D0D0D")
mainFrame.pack()

lblProgramTitle = Label(mainFrame, text="Chess Engine", anchor='n', 
    background='#0D0D0D', font=titleFont, foreground='White')
lblProgramTitle.grid(row=0, column=0, ipady=10)

frameBoard = Frame(mainFrame)
frameBoard.grid(row=1, column=0)

chessBoard = ChessBoard(8, 8, windowHeight // 10, "#C6C6E0", "#1D0022", "yellow", "yellow")
chessBoard.setImageWhitePawn(file="images/Actual Photos/pawn_white.png")
chessBoard.setImageBlackPawn(file="images/Actual Photos/pawn_black.png")
chessBoard.setImageWhiteBishop(file="images/Actual Photos/bishop_white.png")
chessBoard.setImageBlackBishop(file="images/Actual Photos/bishop_black.png")
chessBoard.setImageWhiteKnight(file="images/Actual Photos/knight_white.png")
chessBoard.setImageBlackKnight(file="images/Actual Photos/knight_black.png")
chessBoard.setImageWhiteRook(file="images/Actual Photos/rook_white.png")
chessBoard.setImageBlackRook(file="images/Actual Photos/rook_black.png")
chessBoard.setImageWhiteQueen(file="images/Actual Photos/queen_white.png")
chessBoard.setImageBlackQueen(file="images/Actual Photos/queen_black.png")
chessBoard.setImageWhiteKing(file="images/Actual Photos/king_white.png")
chessBoard.setImageBlackKing(file="images/Actual Photos/king_black.png")
chessBoard.setImageBlankSquare(file="images/Actual Photos/blank.png")

chessBoard.initializeBoard(frameBoard)

surfaceWindow.mainloop()