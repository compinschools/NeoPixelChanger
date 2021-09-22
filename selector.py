import time
import board
import neopixel
import keyboard
num_pixels = 150
ORDER= neopixel.GRB
pixels = neopixel.NeoPixel(board.D18,150,brightness=0.2,auto_write=False, pixel_order=ORDER)


def wheel(pos):
	if pos < 0 or pos > 255:
		r = g = b= 0
	elif pos < 85:
		r = int(pos * 3)
		g = int(255 - pos * 3)
		b = 0
	elif pos < 170:
		pos -=85
		r = int(255 -pos * 3)
		g = 0
		b = int(pos * 3)
	else:
		pos -=170
		r = 0
		g = int(pos * 3)
		b = int(255 - pos * 3)
	return (r,g,b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r,g,b,0)

def rainbow_cycle(wait):
	global current
	for j in range(255):
		for i in  range (num_pixels):
			pixel_index = (i * 256 // num_pixels) + j
			pixels[i] = wheel(pixel_index & 255)
		if(current != "rainbow"):
			break
		pixels.show()
		time.sleep(wait)

def chase_cycle(wait):
	global currentR
	global currentG
	global currentB
	global current
	for i in range(num_pixels):
		pixels.fill((0,0,0));
		for j in range(10):
			try:
				pixels[i+j] = (int(currentR),int(currentG),int(currentB));
			except:
				break;
		if(current != "chase"):
			break;
		pixels.show()
		time.sleep(wait)

current = "test";
options = ["none","rainbow","chase","full"]
optionIndex = 0
currentR = "255"
newR = "000"
currentG = "255"
newG = "000"
currentB = "255"
newB = "000"
rgbIndex = 0

def workOutColor(character,index,color):
	if(index == 0):
		return character + "00"
	elif index == 1:
		return color[0] + character + "0"
	else:
		return color[0] + color[1] + character

def pushRGB(character,index):
	global currentR
	global currentG
	global currentB
	global newR
	global newG
	global newB
	if(index  >= 0 and index < 3):
		#red
		newR = workOutColor(character,index,newR)
		if(index == 2 and int(newR) <= 255):
			currentR = newR
	if(index >= 3 and index < 6):
		#green
		newG = workOutColor(character,index-3,newG)
		if(index == 5 and int(newG) <= 255):
			currentG = newG
	if(index >=6):
		#blue
		newB = workOutColor(character,index-6,newB)
		if(index == 8 and int(newB) <= 255):
			currentB = newB

def on_u():
	global current;
	global optionIndex;
	global options;
	optionIndex+=1;
	if(optionIndex >= len(options)):
		optionIndex = 0
	current = options[optionIndex];
	print(current)
def on_d():
	global current
	global optionIndex;
	global options;
	optionIndex-=1;
	if(optionIndex < 0):
		optionIndex = len(options) - 1;
	current = options[optionIndex]
	print(current)

def on_num(num):
	global current
	global rgbIndex
	global newR
	global newG
	global newB
	pushRGB(num,rgbIndex)
	rgbIndex+=1
	if(rgbIndex > 8):
		rgbIndex = 0
	print("R:" + newR + " G:" + newG + " B: " + newB);
	print(current)

def on_0():
	on_num("0");

def on_1():
	on_num("1");

def on_2():
	on_num("2");

def on_3():
	on_num("3");
def on_4():
	on_num("4");
def on_5():
	on_num("5");
def on_6():
	on_num("6");
def on_7():
	on_num("7");
def on_8():
	on_num("8");
def on_9():
	on_num("9");

def on_ud():
	global current
	current = "quit"

keyboard.add_hotkey('u',on_u);
keyboard.add_hotkey('d',on_d);
keyboard.add_hotkey('1',on_1);
keyboard.add_hotkey('0',on_0);
keyboard.add_hotkey('2',on_2);
keyboard.add_hotkey('3',on_3);
keyboard.add_hotkey('4',on_4);
keyboard.add_hotkey('5',on_5);
keyboard.add_hotkey('6',on_6);
keyboard.add_hotkey('7',on_7);
keyboard.add_hotkey('8',on_8);
keyboard.add_hotkey('9',on_9);
keyboard.add_hotkey('u+d',on_ud);

while current != "quit":
	#time.sleep(1);
	if (current == "rainbow"):
		rainbow_cycle(0.01)

	if (current == "none"):
		pixels.fill((0,0,0));
		pixels.show()
		current = ""

	if(current == "full"):
		pixels.fill((int(currentR),int(currentG),int(currentB)))
		pixels.show()

	if(current == "test"):
		for i in range(num_pixels):
			pixels.fill((0,0,0))
			pixels.show()
			pixels[i] = ((255,255,255))
			pixels.show()
		current = "none"
	if(current == "chase"):
		chase_cycle(0.1);
#pixels.fill((255,0,0))
	#pixels.show()
	#time.sleep(1)

	#pixels.fill((0,255,0))
	#pixels.show()
	#time.sleep(1)

	#pixels.fill((0,0,255))
	#pixels.show()
	#time.sleep(1)
