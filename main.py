# Dataset - https://github.com/codebrainz/color-names/blob/master/output/colors.csv

import cv2
import pandas as pd
import params as p

img_path = "G:\My Drive\wannatry\M2_SIIA\MCSI\Project\Color_Detection\\Basketball.png"
img = cv2.imread(img_path)


# declaring global variables (are used later on)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


# function to get x,y coordinates of mouse double click
def draw_function(event, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = p.X_POS_SAMPLING
        y_pos = p.Y_POS_SAMPLING
        b, g, r = img[x_pos, y_pos]
        b = int(b)
        g = int(g)
        r = int(r)

# Function to start the WebCam 
def start_WebCam(id : int = 0) :
    # start webcam
    cap = cv2.VideoCapture(id)
    cap.set(3, p.CAM_WIDTH)
    cap.set(4, p.CAM_HEIGHT)
    return cap 

def extract_color() :
    global b, g, r, x_pos, y_pos 
    x_pos = p.X_POS_SAMPLING
    y_pos = p.Y_POS_SAMPLING
    b, g, r = img[y_pos, x_pos]
    b = int(b)
    g = int(g)
    r = int(r)


cap = start_WebCam(0)

cv2.namedWindow('Webcam')
# cv2.setMouseCallback('Webcam', draw_function)

while cap.isOpened():

    # cv2.imshow("image", img)
    success, img = cap.read()
    cv2.imshow('Webcam', img)

    # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
    # cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

    # extracting color 
    extract_color()
    # Creating text string to display( Color name and RGB values )
    text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
    print(f"color is : {text}")
    # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
    # cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    # For very light colours we will display text in black colour
    # if r + g + b >= 600:
    #     cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    # clicked = False

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()