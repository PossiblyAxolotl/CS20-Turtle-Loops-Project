# PossiblyAxolotl
# Input functions for my circular super hexagon clone
# -=-=-=-=-=-=-=-=-=-=-=-=-
# Started Oct 31, 2023
# Last updated Nov 10, 2023 

def get_mouse_pos(canvas, screen_size_x, screen_size_y):
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx() - screen_size_x/2
    mouse_y = -(canvas.winfo_pointery() - canvas.winfo_rooty() - screen_size_y/2)   
    
    return mouse_x, mouse_y
