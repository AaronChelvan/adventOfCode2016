#!/usr/bin/python

inputText = []
inputText.append("LURLLLLLDUULRDDDRLRDDDUDDUULLRLULRURLRRDULUUURDUURLRDRRURUURUDDRDLRRLDDDDLLDURLDUUUDRDDDLULLDDLRLRRRLDLDDDDDLUUUDLUULRDUDLDRRRUDUDDRULURULDRUDLDUUUDLUDURUURRUUDRLDURRULURRURUUDDLRLDDDDRDRLDDLURLRDDLUDRLLRURRURRRURURRLLRLDRDLULLUDLUDRURDLRDUUDDUUDRLUDDLRLUDLLURDRUDDLRURDULLLUDDURULDRLUDLUDLULRRUUDDLDRLLUULDDURLURRRRUUDRUDLLDRUDLRRDUDUUURRULLDLDDRLUURLDUDDRLDRLDULDDURDLUUDRRLDRLLLRRRDLLLLURDLLLUDRUULUULLRLRDLULRLURLURRRDRLLDLDRLLRLULRDDDLUDDLLLRRLLLUURLDRULLDURDLULUDLRLDLUDURLLLURUUUDRRRULRDURLLURRLDLRLDLDRRUUDRDDDDDRDUUDULUL")
inputText.append("RRURLURRULLUDUULUUURURULLDLRLRRULRUDUDDLLLRRRRLRUDUUUUDULUDRULDDUDLURLRRLLDLURLRDLDUULRDLLLDLLULLURLLURURULUDLDUDLUULDDLDRLRRUURRRLLRRLRULRRLDLDLRDULDLLDRRULRDRDUDUUUDUUDDRUUUDDLRDULLULDULUUUDDUULRLDLRLUUUUURDLULDLUUUULLLLRRRLDLLDLUDDULRULLRDURDRDRRRDDDLRDDULDLURLDLUDRRLDDDLULLRULDRULRURDURRUDUUULDRLRRUDDLULDLUULULRDRDULLLDULULDUDLDRLLLRLRURUDLUDDDURDUDDDULDRLUDRDRDRLRDDDDRLDRULLURUDRLLUDRLDDDLRLRDLDDUULRUDRLUULRULRLDLRLLULLUDULRLDRURDD")
inputText.append("UUUUUURRDLLRUDUDURLRDDDURRRRULRLRUURLLLUULRUDLLRUUDURURUDRDLDLDRDUDUDRLUUDUUUDDURRRDRUDDUURDLRDRLDRRULULLLUDRDLLUULURULRULDRDRRLURULLDURUURDDRDLLDDDDULDULUULLRULRLDURLDDLULRLRRRLLURRLDLLULLDULRULLDLRULDDLUDDDLDDURUUUURDLLRURDURDUUDRULDUULLUUULLULLURLRDRLLRULLLLRRRRULDRULLUURLDRLRRDLDDRLRDURDRRDDDRRUDRLUULLLULRDDLDRRLRUDLRRLDULULRRDDURULLRULDUDRLRUUUULURLRLRDDDUUDDULLULLDDUDRLRDDRDRLDUURLRUULUULDUDDURDDLLLURUULLRDLRRDRDDDUDDRDLRRDDUURDUULUDDDDUUDDLULLDRDDLULLUDLDDURRULDUDRRUURRDLRLLDDRRLUUUDDUUDUDDDDDDDLULURRUULURLLUURUDUDDULURDDLRDDRRULLLDRRDLURURLRRRDDLDUUDR")
inputText.append("URLLRULULULULDUULDLLRDUDDRRLRLLLULUDDUDLLLRURLLLLURRLRRDLULRUDDRLRRLLRDLRRULDLULRRRRUUDDRURLRUUDLRRULDDDLRULDURLDURLRLDDULURDDDDULDRLLUDRULRDDLUUUDUDUDDRRUDUURUURLUUULRLULUURURRLRUUULDDLURULRRRRDULUDLDRLLUURRRLLURDLDLLDUDRDRLLUDLDDLRLDLRUDUULDRRLLULDRRULLULURRLDLUUDLUDDRLURDDUDRDUDDDULLDRUDLRDLRDURUULRRDRUUULRUURDURLDUDRDLLRUULUULRDDUDLRDUUUUULDDDDDRRULRURLLRLLUUDLUDDUULDRULDLDUURUDUDLRULULUULLLLRLULUDDDRRLLDRUUDRLDDDRDDURRDDDULURDLDLUDDUULUUURDULDLLULRRUURDDUDRUULDLRLURUDLRDLLLDRLDUURUDUDRLLLDDDULLUDUUULLUUUDLRRRURRRRRDUULLUURRDUU")
inputText.append("UDULUUDLDURRUDDUDRDDRRUULRRULULURRDDRUULDRLDUDDRRRRDLRURLLLRLRRLLLULDURRDLLDUDDULDLURLURUURLLLDUURRUUDLLLUDRUDLDDRLRRDLRLDDDULLRUURUUUDRRDLLLRRULDRURLRDLLUDRLLULRDLDDLLRRUDURULRLRLDRUDDLUUDRLDDRUDULLLURLRDLRUUDRRUUDUDRDDRDRDDLRULULURLRULDRURLURLRDRDUUDUDUULDDRLUUURULRDUDRUDRULUDDULLRDDRRUULRLDDLUUUUDUDLLLDULRRLRDDDLULRDUDRLDLURRUUDULUDRURUDDLUUUDDRLRLRLURDLDDRLRURRLLLRDRLRUUDRRRLUDLDLDDDLDULDRLURDURULURUDDDUDUULRLLDRLDDDDRULRDRLUUURD")

code = []

for line in inputText:
	currentNumber = 5
	for move in line:
		if move == "U":
			if not(currentNumber == 1 or currentNumber == 2 or currentNumber == 3):
				currentNumber -= 3
		elif move == "D":
			if not(currentNumber == 7 or currentNumber == 8 or currentNumber == 9):
				currentNumber += 3
		elif move == "L":
			if not(currentNumber == 1 or currentNumber == 4 or currentNumber == 7):
				currentNumber -= 1
		elif move == "R":
			if not(currentNumber == 3 or currentNumber == 6 or currentNumber == 9):
				currentNumber += 1
	code.append(currentNumber)

print("The code is " + str(code))
