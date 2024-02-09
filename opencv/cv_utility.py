import cv2


def add_glow_to_image(frame,glow_intensity:float,glow_radius:int):
    """Returns a Frame with glow
    
    Arguments:
        frame: a Opencv frame which you want to add a glow to
        glow_intensity: The intensity of the glow. Can be a float value
        glow_radius: radius of the glow. Must be a Integer
    """

    img_blurred = cv2.GaussianBlur(frame, (glow_radius, glow_radius), 1)
    img_blended = cv2.addWeighted(frame, 1, img_blurred, glow_intensity, 0)

    return img_blended

    
