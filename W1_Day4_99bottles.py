bottles = 99
text1 = " bottles of beer on the wall"
text2 = " bottles of beer."
text3 = "Take one down and pass it around, "
text4 = " bottle of beer on the wall"
text5 = " bottle of beer."
text6 = " no more bottles of beer on the wall."
text7 = "Go to the store and buy some more"
while bottles > 2:
	print(str(bottles) + text1 + ',' + str(bottles) + text2) 
	print(text3 + str(bottles - 1) + text1 + '.')
	bottles = bottles - 1 
if bottles == 2:
	print(str(bottles) + text1 + ','+ str(bottles) + text2) 
	print(text3 + str(bottles - 1) + text4 + '.')
	bottles = bottles - 1 
if bottles == 1:
	print(str(bottles) + text4 + ', ' + str(bottles) + text5)
	print(text3 + text6)
	bottles = bottles - 1 	
if bottles == 0:
	print("No more " + text1 + ', '+ " no more" + text2)
	print(text7 + ', ' + str(99) + text1 + '.')
