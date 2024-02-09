import cv2
import numpy as np



def add_glow_to_image(frame,glow_intensity:float,glow_radius:int):
    """Returns a Frame with glow added to it
    
    Arguments:
        frame: a Opencv frame which you want to add a glow to
        glow_intensity: The intensity of the glow. Can be a float value
        glow_radius: radius of the glow. Must be a Integer
    """

    img_blurred = cv2.GaussianBlur(frame, (glow_radius, glow_radius), 1)
    img_blended = cv2.addWeighted(frame, 1, img_blurred, glow_intensity, 0)

    return img_blended

def canny_edge_detection(frame,lower_threshold:float,upper_threshold:float,kernel_size:tuple=(3,5),sigmaX:float=0.5):
    """Gets all the edges of a frame using the cv2.Canny function
    
    Arguments:
        frame: a Opencv frame
        lower_threshold: The lower threshold of the edge detection, can be a float.
        upper_threshold: The upper threshold of the edge detection, can be a float.
        kernel_size: the size of the gaussian blur kernel, Values must be odd numbers. Must be a Tuple with 2 values.
        sigmaX: sigmaX value for the gaussian blur, must be a float.

    """
    gray_scale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(src=gray_scale_frame,ksize=kernel_size,sigmaX=sigmaX)
    
    detected_edges = cv2.Canny(blurred_frame,lower_threshold,upper_threshold)

    return detected_edges

def replace_colors(frame,old_color:list,new_color:list):
    """Replace a solid color with another
    
    Arguments:
        frame: a Opencv frame
        old_color: The color to replace, Must be a List with BGR values of a color
        new_color: the new color to replace the old color with, Must be a List with BGR values of a color
    """

    frame[np.where((frame==old_color).all(axis=2))] = new_color

    return frame



