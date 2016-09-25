import tingbot
from tingbot import *

bar_max = 300.0
bar_min = 20.0


# right button increases brightness by one
@right_button.press
def brightness_increase ():
    
    brightness = screen.brightness

    brightness += 1
    if brightness > 100:
        brightness = 100
        
    screen_update (compute_x (brightness), 200, brightness)

# midright button increases brightness by 25
@midright_button.press
def brightness_increase_25 ():
    
    brightness = screen.brightness

    if brightness < 25:
        brightness = 25
    elif brightness < 50:
        brightness = 50
    elif brightness < 75:
        brightness = 75
    else:
        brightness = 100
        
    screen_update (compute_x (brightness), 200, brightness)

# left button decreases brightness by one
@left_button.press
def brightness_decrease ():

    brightness = screen.brightness
    
    brightness -= 1
    if brightness < 0:
        brightness = 0

    screen_update (compute_x (brightness), 200, brightness)

# midleft button decreases brightness by 25
@midleft_button.press
def brightness_decrease_25 ():
    
    brightness = screen.brightness

    if brightness > 75:
        brightness = 75
    elif brightness > 50:
        brightness = 50
    elif brightness > 25:
        brightness = 25
    else:
        brightness = 0
        
    screen_update (compute_x (brightness), 200, brightness)


# called once to initialize brightness to 50
@once (seconds=0.25)
def on_stratup ():
    screen_update (160, 200, 50)
    screen.rectangle (xy=(160,200), size=(10,25), color='blue')


# update screen brightness, slider position and brightness text
def screen_update (x_slider, y_slider, brightness):

    screen.brightness = brightness

    screen.fill ('black')
    screen.text (str (brightness), align='center', color='white', font_size=50)
    screen.rectangle (xy=(160,200), size=(280,25), color='grey')
    screen.rectangle (xy=(x_slider,y_slider), size=(10,25), color='blue')
    
    global gbl_x_slider
    gbl_x_slider = x_slider
    
    global gbl_brightness
    gbl_brightness = brightness
    
# compute x location of slider based on brightness
def compute_x (brightness):
    x = ((brightness / 100.0) * (bar_max - bar_min)) + bar_min
    return int (x)
    
# compute brightness based on x position of slider
def compute_brightness (x):
    # 300 - 20 = 280
    percentage = (float(x - bar_min) / (bar_max - bar_min)) * 100
    return int(percentage)

# move slider and brightness based on touchscreen
@touch (xy=(160,200), size=(280,25))
def on_touch (xy, action):
    
    x = xy [0]
    y = xy [1]
    # on down event reposition indicator, but only within bounds of scrollbar
    if (action == "down"):
        screen_update (x, 200, compute_brightness (x))
    elif (action == "move"): # on move track indicator
        # make sure movement occurred inside of scrollbar
#        if (x > 20 and x < 300) and (y > 188 and y < 212):
        if (x >= 20 and x <= 300): # only concerned within x
            screen_update (x, 200, compute_brightness (x))


tingbot.run()
