


Board=["-- ","-- ","-- ",
"-- ","-- ","-- ",
"-- ","-- ","--"]


""" ------------GLOBALVARIABLES--------------"""


game_going=True

Winner=None

currently_player=" X "

#Display Board

def screen():
	
	print(Board[0]+"|"+Board[1]+"|"+Board[2]+   "  1|2|3       "                )
	
	print(Board[3]+"|"+Board[4]+"|"+Board[5]+   "  4|5|6        "               )

	print(Board[6]+"|"+Board[7]+"|"+Board[8]+  "   7|8|9         "              )


#For 

def handling(player):
	
	
	print(player+"'S Turn:")

	Turn=input("Which Place =====>>>>>  \n")
				
	Turn=int(Turn)-1
		
	Board[Turn]=player
	screen()


#tweaking Progress

def Check_progress():
	
	check_win()
	
	check_tie()
	

#Decidence

def check_win():
	global Winner
	
	rows=rows_win()
	
	columns=columns_win()
	
	diagonal=diagonal_win()
	
	######################
	if rows:
		
		Winner=rows_win()
				
	elif columns:	
	
		Winner=columns_win()	
		
	elif diagonal:
	
		Winner=diagonal_win()		
					
	else:
		
		Winner=None
	################
	
"""---------------------"""	
def rows_win():
		
		global game_going
		
		row1= Board[0]==Board[1]==Board[2] ==" X "
		
		row2= Board[3]==Board[4]==Board[5]==" X "
		
		row3= Board[6]==Board[7]==Board[8]==" X "
			
		if row1 or row2 or row3:
			
			game_going=False
			
		if row1:
				
				
			return Board[0]
			
		if row2:
			
			
			return Board[3]
			
		if row3:
			
			
			return Board[6]
		

		
		
def columns_win():
	
	global game_going
		
	columns1=Board[0]==Board[3]==Board[6]==" X "
		
	columns2=Board[1]==Board[4]==Board[7]==" X "
		
	columns3=Board[2]==Board[5]==Board[8]==" X "
			
	if columns1 or columns2 or columns3:
			
			game_going=False
			
	if columns1:
				
			return Board[0:3]
			
	if columns2:
			
			return Board[3]
			
	if columns3:
		
			
			return Board[6]
	
"""------------------------------------------"""	
	
def diagonal_win():
	
	
	global game_going
		
	diagonal1= Board[0]==Board[4]==Board[8] ==" X "
	
	diagonal2= Board[6]==Board[4]==Board[2]==" X "
			
	if diagonal1 or diagonal2 :
			
			
			game_going=False
			
				
	if diagonal1:
			
				
			return Board[0]
			
	if diagonal2:
			
			
			
			return Board[6]
				
	

"""-----------------------"""





"""-----------------------"""

def check_tie():
	global game_going	
	if "--"not in Board:
		
		game_going=False

	
	
	
def flip_player():
	
	global currently_player
	
	if currently_player==" X ":
			
		currently_player=" O "
		
		
	elif currently_player==" O ":
	
		currently_player=" X "
		
		

	
	
	
"""--------------------------"""		

def Game_logic():
	
	global Winner

	global game_going
	
	while game_going:
			
			handling(currently_player)
			Check_progress()
			flip_player()
			
			
			if Winner==" X " or Winner==" O ":
					
					print("Game Over")
					
					print(Winner+"Won")
					
			if Winner==None:
					
					print("Tie")

screen()
Game_logic()
