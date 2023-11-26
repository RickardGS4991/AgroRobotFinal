import cv2

def sickDetect(pathPhoto):
    image = cv2.imread(pathPhoto)
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Rango de colores marrón en HSV
    lowerBrown = (10, 100, 20)
    upperBrown = (30, 255, 200)

    # Rango de colores café en HSV
    lowerCoffee = (0, 50, 20)
    upperCoffee = (20, 150, 200)

    maskBrown = cv2.inRange(hsvImage, lowerBrown, upperBrown)
    maskCoffee = cv2.inRange(hsvImage, lowerCoffee, upperCoffee)


    contoursBrown, _ = cv2.findContours(maskBrown, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contoursCoffee, _ = cv2.findContours(maskCoffee, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(image, contoursBrown, -1, (0, 255, 0), 2)  # Color verde para marrón
    cv2.drawContours(image, contoursCoffee, -1, (0, 0, 255), 2)  # Color rojo para café

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if len(contoursBrown) > 0 or len(contoursCoffee) > 0:
        health = True
    else:
        health = False

    return health
