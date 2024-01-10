from tkinter import Tk, Frame, Button
from PIL import Image, ImageTk

'''
Notes/Things to do:
-Eventually add board co-ordinate system (e4, etc.)
-Add Players and Scores
-Enpassant for pawns
-Pawn turns to Queen end of board
-Castle possible will be false
-Threatened squares king can't go on through invoke function
-Check if list chess square info is sufficient DONE
-Write getter / accessor methods DONE
'''

class ChessBoard:
    def __init__(self, rows=8, columns=8, size=100, light="White", dark="Black", 
        selectCol="lightgrey", genCol="yellow green"):
        self.__row = rows
        self.__column = columns
        self.__colorLight = light
        self.__colorDark = dark
        self.__pieceSquareSize = size
        self.__whiteTurn = True
        self.__capturable, self.__notCapturable = "Black", "White"
        self.__colorSelectPiece = selectCol
        self.__colorGeneratedMoves = genCol
        self.__whiteCastle = [True, True] # [White King Side Castle, White Queen Side Castle]
        self.__blackCastle = [True, True] # [Black King Side Castle, Black Queen Side Castle]
        
        self.__list2DButtonsChessBoard = [[None for column in range(self.__column)] 
        for row in range(self.__row)]
        self.__onEachSquare = [[None for column in range(self.__column)] 
        for row in range(self.__row)]
        self.__listChessSquareInfo = [[None for column in range(self.__column)]
        for row in range(self.__row)]
        self.__lightDarkSquare = [[None for column in range(self.__column)]
        for row in range(self.__row)]

        # Determine the color of each square on the board
        lightDarkSquareColor = "Light"
        currentSquareColor = self.__colorLight
        for row in range(len(self.__list2DButtonsChessBoard)):
            for column in range(len(self.__list2DButtonsChessBoard[row])):
                if column == 0:
                    pass
                elif lightDarkSquareColor == "Light":
                    lightDarkSquareColor = "Dark"
                    currentSquareColor = self.__colorDark
                elif lightDarkSquareColor == "Dark":
                    lightDarkSquareColor = "Light"
                    currentSquareColor = self.__colorLight
                self.__lightDarkSquare[row][column] = currentSquareColor

        # Variable for each loaded, resized and processed default piece image
        self.__imgWhitePawn = ImageTk.PhotoImage(Image.open("images/Sample Photos/PawnWSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgBlackPawn = ImageTk.PhotoImage(Image.open("images/Sample Photos/PawnBSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgWhiteBishop = ImageTk.PhotoImage(Image.open("images/Sample Photos/BishopWSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgBlackBishop = ImageTk.PhotoImage(Image.open("images/Sample Photos/BishopBSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgWhiteKnight = ImageTk.PhotoImage(Image.open("images/Sample Photos/KnightWSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgBlackKnight = ImageTk.PhotoImage(Image.open("images/Sample Photos/KnightBSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgWhiteRook = ImageTk.PhotoImage(Image.open("images/Sample Photos/RookWSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgBlackRook = ImageTk.PhotoImage(Image.open("images/Sample Photos/RookBSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgWhiteQueen = ImageTk.PhotoImage(Image.open("images/Sample Photos/QueenWSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgBlackQueen = ImageTk.PhotoImage(Image.open("images/Sample Photos/QueenBSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgWhiteKing = ImageTk.PhotoImage(Image.open("images/Sample Photos/KingWSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgBlackKing = ImageTk.PhotoImage(Image.open("images/Sample Photos/KingBSample.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
        self.__imgBlankSquare = ImageTk.PhotoImage(Image.open("images/Sample Photos/blank.png").resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))

        self.__rowPieceSelected, self.__colPieceSelected  = 0, 0 # Unselected
        self.__selectedPiece, self.__selectedPieceInfo = self.__imgBlankSquare, None 

    def initializeBoard(self, boardFrame):
        '''
        Rook, Knight, Bishop, Queen --> [Color, Piece, Value]
        King --> [Color, Piece, Alive or Dead (True or False)]
        Pawn --> [Color, Piece, Value, Two moves or not (True or False), 
        Able to Enpassent Left (True or False), Able to Enpassent Right (True or False)]
        '''
        # Rows: 7 - 1, 6 - 2, 5 - 3, 4 - 4, 3 - 5, 2 - 6, 1 - 7, 0 - 8
        # Columns: 0 - A, 1 - B, 2 - C, 3 - D, 4 - E, 5 - F, 6 - G, 7 - H
        # Determine where the chess pieces go
        # 100 pixels by 100 pixels
        # Set up starting position for the commencing of a chess game in a list
        for row in range(len(self.__onEachSquare)):
            for column in range(len(self.__onEachSquare[row])):
                if row == 0:
                    if column == 0 or column == 7:
                        self.__onEachSquare[row][column] = self.__imgBlackRook
                        self.__listChessSquareInfo[row][column] = ["Black", "Rook", 5]
                    elif column == 1 or column == 6:
                        self.__onEachSquare[row][column] = self.__imgBlackKnight
                        self.__listChessSquareInfo[row][column] = ["Black", "Knight", 3]
                    elif column == 2 or column == 5:
                        self.__onEachSquare[row][column] = self.__imgBlackBishop
                        self.__listChessSquareInfo[row][column] = ["Black", "Bishop", 3]
                    elif column == 3:
                        self.__onEachSquare[row][column] = self.__imgBlackQueen
                        self.__listChessSquareInfo[row][column] = ["Black", "Queen", 9]
                    elif column == 4:
                        self.__onEachSquare[row][column] = self.__imgBlackKing
                        self.__listChessSquareInfo[row][column] = ["Black", "King", True]
                    else:
                        self.__onEachSquare[row][column] = self.__imgBlankSquare
                        self.__listChessSquareInfo[row][column] = None
                elif row == 1:
                    self.__onEachSquare[row][column] = self.__imgBlackPawn
                    self.__listChessSquareInfo[row][column] = ["Black", "Pawn", 1, True, False, False]
                elif row == 6:
                    self.__onEachSquare[row][column] = self.__imgWhitePawn
                    self.__listChessSquareInfo[row][column] = ["White", "Pawn", 1, True, False, False]
                elif row == 7:
                    if column == 0 or column == 7:
                        self.__onEachSquare[row][column] = self.__imgWhiteRook
                        self.__listChessSquareInfo[row][column] = ["White", "Rook", 5]
                    elif column == 1 or column == 6:
                        self.__onEachSquare[row][column] = self.__imgWhiteKnight
                        self.__listChessSquareInfo[row][column] = ["White", "Knight", 3]
                    elif column == 2 or column == 5:
                        self.__onEachSquare[row][column] = self.__imgWhiteBishop
                        self.__listChessSquareInfo[row][column] = ["White", "Bishop", 3]
                    elif column == 3:
                        self.__onEachSquare[row][column] = self.__imgWhiteQueen
                        self.__listChessSquareInfo[row][column] = ["White", "Queen", 9]
                    elif column == 4:
                        self.__onEachSquare[row][column] = self.__imgWhiteKing
                        self.__listChessSquareInfo[row][column] = ["White", "King", True]
                    else:
                        self.__onEachSquare[row][column] = self.__imgBlankSquare
                        self.__listChessSquareInfo[row][column] = None
                else:
                    self.__onEachSquare[row][column] = self.__imgBlankSquare
                    self.__listChessSquareInfo[row][column] = None

        for row in range(len(self.__list2DButtonsChessBoard)):
            for column in range(len(self.__list2DButtonsChessBoard[row])):
                self.__list2DButtonsChessBoard[row][column] = Button(boardFrame,
                state="normal", relief="solid", background=self.__lightDarkSquare[row][column], 
                borderwidth=1, image=self.__onEachSquare[row][column],
                command=lambda row=row, col=column: self.generateLegalMoves(row, col))
                self.__list2DButtonsChessBoard[row][column].grid(row=row, column=column)     

    def generateLegalMoves(self, row, col):
        if self.__list2DButtonsChessBoard[row][col].cget("bg") != self.__colorGeneratedMoves:
            self.__rowPieceSelected, self.__colPieceSelected = row, col,
            self.__selectedPiece, self.__selectedPieceInfo = self.__onEachSquare[row][col], self.__listChessSquareInfo[row][col]
            for rowLoop in range(len(self.__list2DButtonsChessBoard)):
                for colLoop in range(len(self.__list2DButtonsChessBoard[rowLoop])):
                    self.__list2DButtonsChessBoard[rowLoop][colLoop].config(background=self.__lightDarkSquare[rowLoop][colLoop])
            self.__list2DButtonsChessBoard[row][col].config(background=self.__colorSelectPiece)
            # Check if there is a piece on the square
            if self.__listChessSquareInfo[row][col] != None:
                # White's Turn or Black's Turn (Only one must be true to disable one colour when the other is playing)
                if (self.__whiteTurn == True and self.__listChessSquareInfo[row][col][0] == "White") ^ (self.__whiteTurn == False and self.__listChessSquareInfo[row][col][0] == "Black"):
                    # Pawn
                    if self.__listChessSquareInfo[row][col][1] == "Pawn":
                        self.generatePawnMoves(row, col)        
                    # Bishop
                    if self.__listChessSquareInfo[row][col][1] == "Bishop":
                        self.generateBishopMoves(row, col)
                    # Knight
                    if self.__listChessSquareInfo[row][col][1] == "Knight":
                        self.generateKnightMoves(row, col)           
                    # Rook
                    if self.__listChessSquareInfo[row][col][1] == "Rook":
                        self.generateRookMoves(row, col)
                    # Queen
                    if self.__listChessSquareInfo[row][col][1] == "Queen":
                        self.generateQueenMoves(row, col)
                    # King    
                    if self.__listChessSquareInfo[row][col][1] == "King":
                        self.generateKingMoves(row, col)
        # Check if a generated move is detected
        elif self.__list2DButtonsChessBoard[row][col].cget("bg") == self.__colorGeneratedMoves:
            # print(row, col, self.__rowPieceSelected, self.__colPieceSelected)
            # Ensure nothing happens if the piece is reselected
            if row != self.__rowPieceSelected or col != self.__colPieceSelected:
                self.moveConfirmed(row, col)
            else:
                self.__rowPieceSelected, self.__colPieceSelected = row, col,
                self.__selectedPiece, self.__selectedPieceInfo = self.__onEachSquare[row][col], self.__listChessSquareInfo[row][col]
                for rowLoop in range(len(self.__list2DButtonsChessBoard)):
                    for colLoop in range(len(self.__list2DButtonsChessBoard[rowLoop])):
                        self.__list2DButtonsChessBoard[rowLoop][colLoop].config(background=self.__lightDarkSquare[rowLoop][colLoop])
                        
    def generatePawnMoves(self, row, col):
        # White pawn goes forward and black pawn goes backwards
        if self.__whiteTurn == True: f = 1
        else: f = -1
        # Check if black pieces diagonal to pawn for capture
        if col > 0 and self.__listChessSquareInfo[row - f][col - 1] != None:
            if self.__listChessSquareInfo[row - f][col - 1][0] == self.__capturable:
                self.__list2DButtonsChessBoard[row - f][col - 1].config(background=self.__colorGeneratedMoves)
        if col < 7 and self.__listChessSquareInfo[row - f][col + 1] != None:
            if self.__listChessSquareInfo[row - f][col + 1][0] == self.__capturable:
                self.__list2DButtonsChessBoard[row - f][col + 1].config(background=self.__colorGeneratedMoves)
        # No pieces 1 square ahead - Check front pawn obstruction first
        if self.__listChessSquareInfo[row - f][col] == None:
            self.__list2DButtonsChessBoard[row - f][col].config(background=self.__colorGeneratedMoves)
            # If first move for pawn (Potential 2 square move)bishop and the second square up is available
            if self.__listChessSquareInfo[row][col][3] == True and self.__listChessSquareInfo[row - 2*f][col] == None:
                # No pieces 2 square ahead
                self.__list2DButtonsChessBoard[row - 2*f][col].config(background=self.__colorGeneratedMoves)
        # Enpassente - Ability to enpassent activated on the opposing colour's turn
        if self.__listChessSquareInfo[row][col][4] == True: # Ability to Left side enpassent 
            self.__list2DButtonsChessBoard[row - f][col - 1].config(background=self.__colorGeneratedMoves)
        if self.__listChessSquareInfo[row][col][5] == True: # Ability to Right side enpassent
            self.__list2DButtonsChessBoard[row - f][col + 1].config(background=self.__colorGeneratedMoves)

    def generateBishopMoves(self, row, col):
        possibleMoves = []
        colCom, rowCom = col, row # colCom, rowCom is possible moves and col, row is the colCom of piece current location
        # Every Diagonal top left of the bishop
        while colCom > 0 and rowCom > 0:
            colCom = colCom - 1
            rowCom = rowCom - 1
            if self.__listChessSquareInfo[rowCom][colCom] == None: # Empty adjacent diagonal
                possibleMoves.append((rowCom, colCom))
            elif self.__listChessSquareInfo[rowCom][colCom][0] == self.__capturable: # Black piece in adjacent diagonal
                possibleMoves.append((rowCom, colCom))
                break
            else: break # White piece in adjacent diagonal
        colCom, rowCom = col, row
        # Every Diagonal Bottom left of the bishop
        while colCom > 0 and rowCom < 7:
            colCom = colCom - 1
            rowCom = rowCom + 1
            if self.__listChessSquareInfo[rowCom][colCom] == None: # Empty adjacent diagonal
                possibleMoves.append((rowCom, colCom))
            elif self.__listChessSquareInfo[rowCom][colCom][0] == self.__capturable: # Black piece in adjacent diagonal
                possibleMoves.append((rowCom, colCom))
                break
            else: break # White piece in adjacent diagonal
        colCom, rowCom = col, row
        # Every Diagonal Square Top Right of the Bishop
        while colCom < 7 and rowCom > 0:
            colCom = colCom + 1
            rowCom = rowCom - 1
            if self.__listChessSquareInfo[rowCom][colCom] == None: # Empty adjacent diagonal
                possibleMoves.append((rowCom, colCom))
            elif self.__listChessSquareInfo[rowCom][colCom][0] == self.__capturable: # Black piece in adjacent diagonal
                possibleMoves.append((rowCom, colCom)) 
                break
            else: break # White piece in adjacent diagonal
        colCom, rowCom = col, row
        # Every Diagonal Bottom Right of the bishop
        while colCom < 7 and rowCom < 7:
            colCom = colCom + 1
            rowCom = rowCom + 1
            if self.__listChessSquareInfo[rowCom][colCom] == None: # Empty adjacent diagonal
                possibleMoves.append((rowCom, colCom))
            elif self.__listChessSquareInfo[rowCom][colCom][0] == self.__capturable: # Black piece in adjacent diagonal
                possibleMoves.append((rowCom, colCom))
                break
            else: break # White piece in adjacent diagonal
        for moveCoord in possibleMoves:
            self.__list2DButtonsChessBoard[moveCoord[0]][moveCoord[1]].config(background=self.__colorGeneratedMoves)

    def generateKnightMoves(self, row, col):
        knightHopCombos = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
        for possible in knightHopCombos:
            if (row + possible[0]) >= 0 and (col + possible[1]) >= 0 and (row + possible[0]) <= 7 and (col + possible[1]) <= 7:
                if (self.__listChessSquareInfo[row + possible[0]][col + possible[1]] == None):
                    self.__list2DButtonsChessBoard[row + possible[0]][col + possible [1]].config(background=self.__colorGeneratedMoves)
                elif (self.__listChessSquareInfo[row + possible[0]][col + possible[1]][0] == self.__capturable):
                    self.__list2DButtonsChessBoard[row + possible[0]][col + possible [1]].config(background=self.__colorGeneratedMoves)

    def generateRookMoves(self, row, col):
        possibleMoves = []
        colCom, rowCom = col, row # colCom, rowCom is possible moves and col, row is the colCom of piece current location
        # Every Left Rook Move
        while colCom > 0:
            colCom = colCom - 1
            if self.__listChessSquareInfo[rowCom][colCom] == None: # Empty adjacent diagonal
                possibleMoves.append((rowCom, colCom))
            elif self.__listChessSquareInfo[rowCom][colCom][0] == self.__capturable: # Black piece in adjacent diagonal
                possibleMoves.append((rowCom, colCom))
                break
            else: break # White piece in adjacent diagonal
        colCom, rowCom = col, row
        # Every Right Rook Move
        while colCom < 7:
            colCom = colCom + 1
            if self.__listChessSquareInfo[rowCom][colCom] == None: # Empty adjacent diagonal
                possibleMoves.append((rowCom, colCom))
            elif self.__listChessSquareInfo[rowCom][colCom][0] == self.__capturable: # Black piece in adjacent diagonal
                possibleMoves.append((rowCom, colCom))
                break
            else: break # White piece in adjacent diagonal
        colCom, rowCom = col, row
        # Every Down Rook Move
        while rowCom > 0:
            rowCom = rowCom - 1
            if self.__listChessSquareInfo[rowCom][colCom] == None: # Empty adjacent diagonal
                possibleMoves.append((rowCom, colCom))
            elif self.__listChessSquareInfo[rowCom][colCom][0] == self.__capturable: # Black piece in adjacent diagonal
                possibleMoves.append((rowCom, colCom)) 
                break
            else: break # White piece in adjacent diagonal
        colCom, rowCom = col, row
        # Every Diagonal Bottom Right of the bishop
        while rowCom < 7:
            rowCom = rowCom + 1
            if self.__listChessSquareInfo[rowCom][colCom] == None: # Empty adjacent diagonal
                possibleMoves.append((rowCom, colCom))
            elif self.__listChessSquareInfo[rowCom][colCom][0] == self.__capturable: # Black piece in adjacent diagonal
                possibleMoves.append((rowCom, colCom))
                break
            else: break # White piece in adjacent diagonal
        for moveCoord in possibleMoves:
            self.__list2DButtonsChessBoard[moveCoord[0]][moveCoord[1]].config(background=self.__colorGeneratedMoves)

    def generateQueenMoves(self, row, col): # Queen moves are combination of Bishop and Rook moves
        self.generateBishopMoves(row, col)
        self.generateRookMoves(row, col)

    def generateKingMoves(self, row, col):
        # Left of King available
        if col > 0 and (self.__listChessSquareInfo[row][col - 1] == None or self.__listChessSquareInfo[row][col - 1][0] != self.__notCapturable):
            self.__list2DButtonsChessBoard[row][col - 1].config(background=self.__colorGeneratedMoves)
        # Right of King available
        if col < 7 and (self.__listChessSquareInfo[row][col + 1] == None or self.__listChessSquareInfo[row][col + 1][0] != self.__notCapturable):
            self.__list2DButtonsChessBoard[row][col + 1].config(background=self.__colorGeneratedMoves)
        # Top of King available
        if row > 0 and (self.__listChessSquareInfo[row - 1][col] == None or self.__listChessSquareInfo[row - 1][col][0] != self.__notCapturable):
            self.__list2DButtonsChessBoard[row - 1][col].config(background=self.__colorGeneratedMoves)
        # Bottom of King available
        if row < 7 and (self.__listChessSquareInfo[row + 1][col] == None or self.__listChessSquareInfo[row + 1][col][0] != self.__notCapturable):
            self.__list2DButtonsChessBoard[row + 1][col].config(background=self.__colorGeneratedMoves)
        # Top-left of King available
        if col > 0 and row > 0 and (self.__listChessSquareInfo[row - 1][col - 1] == None or self.__listChessSquareInfo[row - 1][col - 1][0] != self.__notCapturable):
            self.__list2DButtonsChessBoard[row - 1][col - 1].config(background=self.__colorGeneratedMoves)
        # Top-right of King available
        if col < 7 and row > 0 and (self.__listChessSquareInfo[row - 1][col + 1] == None or self.__listChessSquareInfo[row - 1][col + 1][0] != self.__notCapturable):
            self.__list2DButtonsChessBoard[row - 1][col + 1].config(background=self.__colorGeneratedMoves)
        # Bottom-left of King available
        if col > 0 and row < 7 and (self.__listChessSquareInfo[row + 1][col - 1] == None or self.__listChessSquareInfo[row + 1][col - 1][0] != self.__notCapturable):
            self.__list2DButtonsChessBoard[row + 1][col - 1].config(background=self.__colorGeneratedMoves)
        # Bottom-right of King available
        if col < 7 and row < 7 and (self.__listChessSquareInfo[row + 1][col + 1] == None or self.__listChessSquareInfo[row + 1][col + 1][0] != self.__notCapturable):
            self.__list2DButtonsChessBoard[row + 1][col + 1].config(background=self.__colorGeneratedMoves)
        # White Castling
        if self.__whiteTurn == True:
            # Castling King side
            if self.__whiteCastle[0] == True and self.__listChessSquareInfo[7][5] == None and self.__listChessSquareInfo[7][6] == None:
                self.__list2DButtonsChessBoard[7][5].config(background=self.__colorGeneratedMoves)
                self.__list2DButtonsChessBoard[7][6].config(background=self.__colorGeneratedMoves)
            # Castling Queen side
            if self.__whiteCastle[1] == True and self.__listChessSquareInfo[7][1] == None and self.__listChessSquareInfo[7][2] == None and self.__listChessSquareInfo[7][3] == None:
                self.__list2DButtonsChessBoard[7][2].config(background=self.__colorGeneratedMoves)
                self.__list2DButtonsChessBoard[7][3].config(background=self.__colorGeneratedMoves)
        # Black Castling
        elif self.__whiteTurn == False:
            # Castling King side
            if self.__blackCastle[0] == True and self.__listChessSquareInfo[0][5] == None and self.__listChessSquareInfo[0][6] == None:
                self.__list2DButtonsChessBoard[0][5].config(background=self.__colorGeneratedMoves)
                self.__list2DButtonsChessBoard[0][6].config(background=self.__colorGeneratedMoves)
            # Castling Queen side
            if self.__blackCastle[1] == True and self.__listChessSquareInfo[0][1] == None and self.__listChessSquareInfo[0][2] == None and self.__listChessSquareInfo[0][3] == None:
                self.__list2DButtonsChessBoard[0][2].config(background=self.__colorGeneratedMoves)
                self.__list2DButtonsChessBoard[0][3].config(background=self.__colorGeneratedMoves)

    # Evaluates if the King is in check or checkmate or stalemate. Otherwise it finds available squares not guarded by black pieces
    def determineKingStatus(self):
        pass

    # Confirming moves and updating board status and information - Includes captures and checks
    def moveConfirmed(self, Row, Col):
        # Determine if the King is currently castling left or right or not castling as the move is being confirmed
        castling = "None" # No castling
        if self.__colPieceSelected - Col == 2 and self.__selectedPieceInfo[1] == "King": # Left castling
            castling = "Left"
        if self.__colPieceSelected - Col == -2 and self.__selectedPieceInfo[1] == "King": # Right castling
            castling = "Right"                

        # Row, Col refer to new location of the pieces
        self.__onEachSquare[Row][Col] = self.__selectedPiece
        self.__listChessSquareInfo[Row][Col] = self.__selectedPieceInfo
        self.__onEachSquare[self.__rowPieceSelected][self.__colPieceSelected] = self.__imgBlankSquare
        self.__listChessSquareInfo[self.__rowPieceSelected][self.__colPieceSelected] = None
    
        # Adjustment piece features for white and black depending on turn
        if self.__listChessSquareInfo[Row][Col][1] == "Pawn": # Disable ability to move two squares after pawn moves at least once
            self.__listChessSquareInfo[Row][Col][3] = False
            if Row == 0: # Turn white pawn to white queen at opposing end of board
                self.__onEachSquare[Row][Col] = self.__imgWhiteQueen
                self.__listChessSquareInfo[Row][Col] = ["White", "Queen", 9]
            if Row == 7: # Turn black pawn to black queen at opposing end of board
                self.__onEachSquare[Row][Col] = self.__imgBlackQueen
                self.__listChessSquareInfo[Row][Col] = ["Black", "Queen", 9]
            # Enabling enpassent for opposing pieces when current colour moves up twice with a pawn
            if self.__rowPieceSelected - Row == 2: # If a white pawn moved up two squares
                if Col - 1 >= 0 and self.__listChessSquareInfo[Row][Col - 1] != None and self.__listChessSquareInfo[Row][Col - 1][:2] == ["Black", "Pawn"]: # Black pawn to the left
                    self.__listChessSquareInfo[Row][Col - 1][5] = True
                if Col + 1 <= 7 and self.__listChessSquareInfo[Row][Col + 1] != None and self.__listChessSquareInfo[Row][Col + 1][:2] == ["Black", "Pawn"]: # Black pawn to the right
                    self.__listChessSquareInfo[Row][Col + 1][4] = True
            if self.__rowPieceSelected - Row == -2: # If a black pawn moved up two squares
                if Col - 1 >= 0 and self.__listChessSquareInfo[Row][Col - 1] != None and self.__listChessSquareInfo[Row][Col - 1][:2] == ["White", "Pawn"]: # White pawn to the left
                    self.__listChessSquareInfo[Row][Col - 1][5] = True
                if Col + 1 <= 7 and self.__listChessSquareInfo[Row][Col + 1] != None and self.__listChessSquareInfo[Row][Col + 1][:2] == ["White", "Pawn"]: # White pawn to the right
                    self.__listChessSquareInfo[Row][Col + 1][4] = True
            # Executing Enpassent - The piece is already at its enpassent square but the piece behind must be deleted
            if self.__whiteTurn == True:
                self.__onEachSquare[Row + 1][Col] = self.__imgBlankSquare
                self.__listChessSquareInfo[Row + 1][Col] = None
            else:
                self.__onEachSquare[Row - 1][Col] = self.__imgBlankSquare
                self.__listChessSquareInfo[Row - 1][Col] = None
        # Disabling both castling sides for the colour that moves their king
        if self.__listChessSquareInfo[Row][Col][1] == "King" and self.__whiteTurn == True: # When King Moves both king and queen side castle disabled
            self.__whiteCastle[0] = False
            self.__whiteCastle[1] = False
        if self.__listChessSquareInfo[Row][Col][1] == "King" and self.__whiteTurn == False: # When King Moves both king and queen side castle disabled
            self.__blackCastle[0] = False
            self.__blackCastle[1] = False

        # Disabling castling for Rook moves
        if self.__listChessSquareInfo[7][0] == None or self.__listChessSquareInfo[7][0][1] != "Rook": # When left white rook moves queen side castle disabled - White
            self.__whiteCastle[1] = False
        if self.__listChessSquareInfo[7][7] == None or self.__listChessSquareInfo[7][7][1] != "Rook": # When right white rook moves king side castle disabled - White
            self.__whiteCastle[0] = False
        if self.__listChessSquareInfo[0][0] == None or self.__listChessSquareInfo[0][0][1] != "Rook": # When left white rook moves queen side castle disabled - Black
            self.__blackCastle[1] = False
        if self.__listChessSquareInfo[0][7] == None or self.__listChessSquareInfo[0][7][1] != "Rook": # When right white rook moves king side castle disabled - Black
            self.__blackCastle[0] = False

        # Handling Events when Castling
        if self.__whiteTurn == True:
            self.__rowPieceSelected = 7
        elif self.__whiteTurn == False:
            self.__rowPieceSelected = 0
        # Ensuring rooks also moved to correct location during castle from their original corner position
        if castling == "Left": # White Queen Side Castle
            self.__selectedPiece, self.__selectedPieceInfo = self.__onEachSquare[self.__rowPieceSelected][0], self.__listChessSquareInfo[self.__rowPieceSelected][0]
            self.__onEachSquare[self.__rowPieceSelected][3] = self.__selectedPiece
            self.__listChessSquareInfo[self.__rowPieceSelected][3] = self.__selectedPieceInfo
            self.__onEachSquare[self.__rowPieceSelected][0] = self.__imgBlankSquare
            self.__listChessSquareInfo[self.__rowPieceSelected][0] = None
        if castling == "Right": # White King Side Castle
            self.__selectedPiece, self.__selectedPieceInfo = self.__onEachSquare[self.__rowPieceSelected][7], self.__listChessSquareInfo[self.__rowPieceSelected][7]
            self.__onEachSquare[self.__rowPieceSelected][5] = self.__selectedPiece
            self.__listChessSquareInfo[self.__rowPieceSelected][5] = self.__selectedPieceInfo
            self.__onEachSquare[self.__rowPieceSelected][7] = self.__imgBlankSquare
            self.__listChessSquareInfo[self.__rowPieceSelected][7] = None
        
        # Re-initializing selection variables
        self.__rowPieceSelected, self.__colPieceSelected  = 0, 0 # Unselected
        self.__selectedPiece, self.__selectedPieceInfo = self.__imgBlankSquare, None 

        # Update appearance of the board after all changes have been made
        for row in range(len(self.__list2DButtonsChessBoard)):
            for column in range(len(self.__list2DButtonsChessBoard[row])):
                self.__list2DButtonsChessBoard[row][column].config(background=self.__lightDarkSquare[row][column], 
                    image=self.__onEachSquare[row][column])
                # Ensure that the current colour does not have any pawns that can enpassent after their turn is over
                if self.__whiteTurn == True: # No left or right side enpassent for white after turn over
                    if self.__listChessSquareInfo[row][column] != None and self.__listChessSquareInfo[row][column][:2] == ["White", "Pawn"]:
                        self.__listChessSquareInfo[row][column][4] = False 
                        self.__listChessSquareInfo[row][column][5] = False
                elif self.__whiteTurn == False: # No left or right side enpassent for black after turn over
                    if self.__listChessSquareInfo[row][column] != None and self.__listChessSquareInfo[row][column][:2] == ["Black", "Pawn"]:
                        self.__listChessSquareInfo[row][column][4] = False 
                        self.__listChessSquareInfo[row][column][5] = False
        
        # Switching turns to opposing colour after turn is complete
        if self.__whiteTurn == True:
            self.__whiteTurn = False
            self.__capturable, self.__notCapturable = "White", "Black"
        elif self.__whiteTurn == False:
            self.__whiteTurn = True
            self.__capturable, self.__notCapturable = "Black", "White"

    # Accessor and Mutator Functions
    def getRows(self):
        return self.__row
    
    def getColumns(self):
        return self.__column

    def getPieceSquareSize(self):
        return self.__pieceSquareSize

    def setTurn(self, white = True):
        self.__whiteTurn = white

    def isWhiteTurn(self):
        return self.__whiteTurn

    def getBoardButton(self, row, column):
        return self.__list2DButtonsChessBoard[row][column]

    def getImageOnSquare(self, row, column):
        return self.__onEachSquare[row][column]
    
    def getSquareInfo(self, row, column):
        return self.__listChessSquareInfo[row][column]

    def getLightSquaresColor(self):
        return self.__colorLight
    
    def getDarkSquaresColor(self):
        return self.__colorDark
    
    def setImageWhitePawn(self, file):
        self.__imgWhitePawn = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
    
    def getImageWhitePawn(self):
        return self.__imgWhitePawn
    
    def setImageBlackPawn(self, file):
        self.__imgBlackPawn = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
    
    def getImageBlackPawn(self):
        return self.__imgBlackPawn
    
    def setImageWhiteBishop(self, file):
        self.__imgWhiteBishop = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))

    def getImageWhiteBishop(self):
        return self.__imgWhiteBishop

    def setImageBlackBishop(self, file):
        self.__imgBlackBishop = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
    
    def getImageBlackBishop(self):
        return self.__imgBlackBishop
    
    def setImageWhiteKnight(self, file):
        self.__imgWhiteKnight = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
    
    def getImageWhiteKnight(self):
        return self.__imgWhiteKnight

    def setImageBlackKnight(self, file):
        self.__imgBlackKnight = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
    
    def getImageBlackKnight(self):
        return self.__imgBlackKnight

    def setImageWhiteRook(self, file):
        self.__imgWhiteRook = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))

    def getImageWhiteRook(self):
        return self.__imgWhiteRook
    
    def setImageBlackRook(self, file):
        self.__imgBlackRook = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))

    def getImageBlackRook(self):
        return self.__imgBlackRook

    def setImageWhiteQueen(self, file):
        self.__imgWhiteQueen = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
    
    def getImageWhiteQueen(self):
        return self.__imgWhiteQueen

    def setImageBlackQueen(self, file):
        self.__imgBlackQueen = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
    
    def getImageBlackQueen(self):
        return self.__imgBlackQueen

    def setImageWhiteKing(self, file):
        self.__imgWhiteKing = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
    
    def getImageWhiteKing(self):
        return self.__imgWhiteKing

    def setImageBlackKing(self, file):
        self.__imgBlackKing = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))
    
    def getImageBlackKing(self):
        return self.__imgBlackKing

    def setImageBlankSquare(self, file):
        self.__imgBlankSquare = ImageTk.PhotoImage(Image.open(file).resize(
            (self.__pieceSquareSize, self.__pieceSquareSize), Image.ANTIALIAS))

    def getImageBlankSquare(self):
        return self.__imgBlankSquare

class ChessPlayer:
    def __init__(self):
        pass

class ChessAI:
    def __init__(self):
        pass
