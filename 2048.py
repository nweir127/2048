#!/usr/bin/python
from Tkinter import *
import random
import os
import copy
sqsize=70

def copyboard():
	canvas.data.prevboard = copy.deepcopy(canvas.data.board)
	canvas.data.prevscore = copy.deepcopy(canvas.data.score)
def keyPressed(event):
	if event.char == 'u':
		canvas.data.board = copy.deepcopy(canvas.data.prevboard)
		canvas.data.score = copy.deepcopy(canvas.data.prevscore)
		redrawAll()
	if event.char == 'r':
		redrawAll()
		init()
	if event.keysym == 'Right':
		copyboard()
		truegrid=[[],[],[],[]]
		for row in range(0,4):
			for col in range(0,4):
				if canvas.data.board[row][col]==0:
					truegrid[row].append(False)
				else:
					truegrid[row].append(True)
		shiftRight()
		nexttruegrid=[[],[],[],[]]
		for row in range(0,4):
			for col in range(0,4):
				if canvas.data.board[row][col]==0:
					nexttruegrid[row].append(False)
				else:
					nexttruegrid[row].append(True)
		if truegrid!=nexttruegrid:
			setNewTile()						
		redrawAll()
	if event.keysym =='Down':
		copyboard()
		truegrid=[[],[],[],[]]
		for row in range(0,4):
			for col in range(0,4):
				if canvas.data.board[row][col]==0:
					truegrid[row].append(False)
				else:
					truegrid[row].append(True)
		shiftDown()
		nexttruegrid=[[],[],[],[]]
		for row in range(0,4):
			for col in range(0,4):
				if canvas.data.board[row][col]==0:
					nexttruegrid[row].append(False)
				else:
					nexttruegrid[row].append(True)
		if truegrid!=nexttruegrid:
			setNewTile()			
		redrawAll()
	if event.keysym=='Up':
		copyboard()
		truegrid=[[],[],[],[]]
		for row in range(0,4):
			for col in range(0,4):
				if canvas.data.board[row][col]==0:
					truegrid[row].append(False)
				else:
					truegrid[row].append(True)
		shiftUp()
		nexttruegrid=[[],[],[],[]]
		for row in range(0,4):
			for col in range(0,4):
				if canvas.data.board[row][col]==0:
					nexttruegrid[row].append(False)
				else:
					nexttruegrid[row].append(True)
		if truegrid!=nexttruegrid:
			setNewTile()			
		redrawAll()
	if event.keysym=='Left':
		copyboard()
		truegrid=[[],[],[],[]]
		for row in range(0,4):
			for col in range(0,4):
				if canvas.data.board[row][col]==0:
					truegrid[row].append(False)
				else:
					truegrid[row].append(True)
		shiftLeft()
		nexttruegrid=[[],[],[],[]]
		for row in range(0,4):
			for col in range(0,4):
				if canvas.data.board[row][col]==0:
					nexttruegrid[row].append(False)
				else:
					nexttruegrid[row].append(True)
		if truegrid!=nexttruegrid:
			setNewTile()			
		redrawAll()
	if event.char=='r':
		init()
		redrawAll()		
def run():
	root = Tk()
	global canvas
	canvas = Canvas(root, width = (5)*sqsize, height = (7.5)*sqsize)
	canvas.pack()
	root.resizable(width=0, height=0)
	class Struct: pass
	canvas.data = Struct()

	root.bind("<Key>",keyPressed)
	init()
	#redrawAll()
	root.mainloop()
def init():
	canvas.data.emptyColor="dim grey"
	canvas.data.score=0
	canvas.data.prevscore = 0 
	canvas.data.hiscoresize=0
	canvas.data.txt=open('score.txt',"rw+")
	canvas.data.best= int(canvas.data.txt.readline())
	if len("%i" %(canvas.data.best) ) <5:
		canvas.data.hiscoresize=22
	else:
		canvas.data.hiscoresize=18
	canvas.data.scoresize=22
	canvas.data.prevboard = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	canvas.data.board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	canvas.data.numbers=[2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]
	canvas.data.colors={0:'grey', 2:'white smoke',4:'bisque2',8:'sandy brown',16:'chocolate',32:'coral',64:'orange red',128:'LightGoldenrod1',256:'gold', 512:'yellow2',1024:'gold2',2048:'DarkGoldenRod1',4096:'SeaGreen1',8192:'SpringGreen3', 16384:'SpringGreen4'}
	canvas.data.fontsize={2:32,4:32,8:32,16:32,32:32,64:32,128:28,256:28,512:28,1024:22,2048:22,4096:22,8192:22,16384:16}
	setNewTile()
	drawGame()
def redrawAll():
	canvas.delete(ALL)
	drawGame()

def drawGame():
	if len(str(canvas.data.score))>4:
		canvas.data.scoresize= 16
	drawBoard()
	canvas.create_rectangle(.35*sqsize, .35*sqsize, 1.85*sqsize, 1.85*sqsize, fill=canvas.data.colors[2048], outline= 'white')
	canvas.create_text(sqsize*1.1, sqsize*1.1, text= "2048", fill= 'white', font= "ClearSans 36")
	canvas.create_rectangle(2.1*sqsize, .35*sqsize, 3.2*sqsize, 1.2*sqsize, fill='dim grey', outline='white')
	canvas.create_text(sqsize*2.65, sqsize*.6, text= "SCORE", fill= 'white', font= "ClearSans 16")
	canvas.create_text(sqsize*2.65, sqsize*.95, text= "%i" %(canvas.data.score), fill= 'white', font= "ClearSans %i" %canvas.data.scoresize)
	canvas.create_rectangle(3.45*sqsize, .35*sqsize, 4.55*sqsize, 1.2*sqsize, fill='dim grey', outline='white')
	canvas.create_text(sqsize*4, sqsize*.6, text= "BEST", fill= 'white', font= "ClearSans 16")
	canvas.create_text(sqsize*4, sqsize*.95, text= "%i" %(canvas.data.best), fill= 'white', font= "ClearSans %i" %(canvas.data.hiscoresize))
	if checkIfOver():
		canvas.create_rectangle(.35*sqsize, 2*sqsize, 4.65*sqsize, 2.8*sqsize, fill='red', outline= 'white')
		canvas.create_text(sqsize*2.5, sqsize*2.4, text= "GAME OVER", fill= 'white', font= "ClearSans 36")
		if canvas.data.score>canvas.data.best:
			os.remove('score.txt')
			file = open('score.txt','w')
			file.write("%i" %(canvas.data.score))
			file.close()
	

def drawBoard():
	for i in range(0,4):
		for j in range(0,4):
			drawSquare(canvas,i,j,canvas.data.colors[canvas.data.board[i][j]])
def drawSquare(canvas,row,col,color):
	if (canvas.data.board[row][col]==2) or (canvas.data.board[row][col]==4):
		textcolor='black'
	else:
		textcolor='white'
	canvas.create_rectangle((int(col)+.5)*sqsize,(int(row)+3)*sqsize,(int(col)+1.5)*sqsize, (int(row)+4)*sqsize,fill=color,outline="dim grey",width=9)

	canvas.create_rectangle((int(col)+.5)*sqsize+4.5,(int(row)+3)*sqsize+5.5,(int(col)+.5)*sqsize+4.5,(int(row)+3)*sqsize+5.5, fill="dim grey",outline= 'dim grey', width=18)
	canvas.create_oval((int(col)+.5)*sqsize+4.5,(int(row)+3)*sqsize+4.5,(int(col)+.5)*sqsize+21,(int(row)+3)*sqsize+21, fill=color,outline= color, width=0)
	canvas.create_rectangle((int(col)+.5)*sqsize+63,(int(row)+3)*sqsize+4.5,(int(col)+.5)*sqsize+66,(int(row)+3)*sqsize+4.5, fill="dim grey",outline= 'dim grey', width=18)
	canvas.create_oval((int(col)+.5)*sqsize+49,(int(row)+3)*sqsize+4.5,(int(col)+.5)*sqsize+65.5,(int(row)+3)*sqsize+21, fill=color,outline= color, width=0)
	
	canvas.create_rectangle((int(col)+.5)*sqsize+4.5,(int(row)+3)*sqsize+64.5,(int(col)+.5)*sqsize+4.5,(int(row)+3)*sqsize+64.5, fill="dim grey",outline= 'dim grey', width=18)
	canvas.create_oval((int(col)+.5)*sqsize+4.5,(int(row)+3)*sqsize+48.5,(int(col)+.5)*sqsize+21,(int(row)+3)*sqsize+66, fill=color,outline= color, width=0)
	canvas.create_rectangle((int(col)+.5)*sqsize+64,(int(row)+3)*sqsize+64.5,(int(col)+.5)*sqsize+66,(int(row)+3)*sqsize+65.5, fill="dim grey",outline= 'dim grey', width=18)
	canvas.create_oval((int(col)+.5)*sqsize+49,(int(row)+3)*sqsize+49.5,(int(col)+.5)*sqsize+65.5,(int(row)+3)*sqsize+66, fill=color,outline= color, width=0)

	if canvas.data.board[row][col] != 0:
		canvas.create_text((float(col)+1)*sqsize,(float(row)+3.5)*sqsize,text= "%i" %(canvas.data.board[row][col]), fill=textcolor,font="ClearSans %i bold" %canvas.data.fontsize[canvas.data.board[row][col]])
def setNewTile():
	row=random.randint(0,3)
	col=random.randint(0,3)
	numchoices=[2,2,2,2,2,2,2,2,2,4]
	num=random.randint(0,9)
	newnum=numchoices[num]
	if (canvas.data.board[row][col] == 0):
		canvas.data.board[row][col]= newnum
	else: setNewTile()
def shiftRight():
	canvas.data.nocombosgrid=[[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
	for row in range (0,4):
		cols=[-2,-3,-4]
		for col in cols:
			if canvas.data.board[row][col]!=0:
				moveRight(row,col)
	return True
def moveRight(row,col,):

	sqcol=col
	while canvas.data.board[row][sqcol+1]==0:
		canvas.data.board[row][sqcol+1]=canvas.data.board[row][sqcol]
		canvas.data.board[row][sqcol]=0
		if sqcol<-1:
			sqcol+=1
		if sqcol==-1:
			break

	if sqcol!=-1:
		if canvas.data.board[row][sqcol+1]==canvas.data.board[row][sqcol]:
	 			if canvas.data.nocombosgrid[row][sqcol+1]==False:
	 			   	canvas.data.nocombosgrid[row][sqcol+1]=True
					canvas.data.board[row][sqcol+1]*=2
					canvas.data.score+=canvas.data.board[row][sqcol+1]
					canvas.data.board[row][sqcol]=0

def shiftDown():
	canvas.data.nocombosgrid=[[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
	for col in range (0,4):
		rows=[-2,-3,-4]
		for row in rows:
			if canvas.data.board[row][col]!=0:
				moveDown(row,col)
	return True
def moveDown(row,col):
	sqrow=row
	while canvas.data.board[sqrow+1][col]==0:
		canvas.data.board[sqrow+1][col]=canvas.data.board[sqrow][col]
		canvas.data.board[sqrow][col]=0
		if sqrow<-1:
			sqrow+=1
		if sqrow==-1:
			break
	if sqrow!=-1:
	 	if canvas.data.board[sqrow+1][col]==canvas.data.board[sqrow][col]:
	 		if canvas.data.nocombosgrid[sqrow+1][col]==False:
	 			canvas.data.nocombosgrid[sqrow+1][col]=True
				canvas.data.board[sqrow+1][col]*=2
				canvas.data.score+=canvas.data.board[sqrow+1][col]
				canvas.data.board[sqrow][col]=0
def shiftUp():
	canvas.data.nocombosgrid=[[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
	for col in range (0,4):
		rows=[1,2,3]
		for row in rows:
			if canvas.data.board[row][col]!=0:
				moveUp(row,col)
	return True
def moveUp(row,col):
	sqrow=row
	while canvas.data.board[sqrow-1][col]==0:

		canvas.data.board[sqrow-1][col]=canvas.data.board[sqrow][col]
		canvas.data.board[sqrow][col]=0
		if sqrow>0:
			sqrow-=1
		if sqrow==0:
			break
	if sqrow!=0:
	 	if canvas.data.board[sqrow-1][col]==canvas.data.board[sqrow][col]:
	 		if canvas.data.nocombosgrid[sqrow-1][col]==False:
	 			canvas.data.nocombosgrid[sqrow-1][col]=True
				canvas.data.board[sqrow-1][col]*=2
				canvas.data.score+=canvas.data.board[sqrow-1][col]
				canvas.data.board[sqrow][col]=0
def shiftLeft():
	canvas.data.nocombosgrid=[[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
	for row in range (0,4):
		cols=[-3,-2,-1]
		for col in cols:
			if canvas.data.board[row][col]!=0:
				moveLeft(row,col)
	return True
def moveLeft(row,col):
	sqcol=col
	while canvas.data.board[row][sqcol-1]==0:
		canvas.data.board[row][sqcol-1]=canvas.data.board[row][sqcol]
		canvas.data.board[row][sqcol]=0
		if sqcol>-4:
			sqcol-=1
		if sqcol==-4:
			break
	if sqcol!=-4:
	 	if canvas.data.board[row][sqcol-1]==canvas.data.board[row][sqcol]:
			if canvas.data.nocombosgrid[row][sqcol-1]==False:
	 			canvas.data.nocombosgrid[row][sqcol-1]=True
				canvas.data.board[row][sqcol-1]*=2
				canvas.data.score+=canvas.data.board[row][sqcol-1]
				canvas.data.board[row][sqcol]=0
def checkIfOver():
	gameIsFine=False
	for row in canvas.data.board:
		for num in row:
			if num ==0:
				gameIsFine=True
	if gameIsFine == True:
		return False
	rownum=0
	for row in canvas.data.board:
		colnum=0
		for col in row:
			if checkAround(rownum,colnum):
				return False
			colnum+=1
		rownum+=1
	return True
def checkAround(row,col):
	val=canvas.data.board[row][col]
	if row!=3:
		if canvas.data.board[row+1][col]==val:
			return True
	if row!=0:
		if canvas.data.board[row-1][col]==val:
			return True
	if col!=3:
		if canvas.data.board[row][col+1]==val:
			return True
	if col!=0:
		if canvas.data.board[row][col-1]==val:
			return True
	return False


run()