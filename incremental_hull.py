import matplotlib.pyplot as plt
import random
import numpy as np

# global variables
GLOBAL_DELAY = 0.1
NUM_OF_POINTS = 18
VALUES_RANGE = 634.0 # values in range from 1 to n

def half_hull(x_sorted_points ,top_botton):
    stack = []
    # push the 1st 3 vertices
    stack.append(x_sorted_points[0])
    stack.append(x_sorted_points[1])
    
    lines = []
    first_line = draw_line(stack[0], stack[1], "blue" ,delay=GLOBAL_DELAY)
    lines.append(first_line)

    red_points = []
    for i in range(2, len(x_sorted_points)):
        
        new_line = draw_line(stack[len(stack)-1], x_sorted_points[i], "blue" ,delay=GLOBAL_DELAY)
        lines.append(new_line)
        
        while(orientation(stack[len(stack)-2], stack[len(stack)-1], x_sorted_points[i]) != top_botton):
            plt.scatter(stack[len(stack)-1][0], stack[len(stack)-1][1], s=10, c="red", zorder=0)

            red_points.append(stack[len(stack)-1])
            # stack will be popped --> delete two lines
            length = len(lines)
            # copy the top two lines --> plot them as red to represend the lines that will be deleted
            topl = lines[length-1]
            x1 = topl[0].get_xdata()
            y1 = topl[0].get_ydata()
            err1_line = plt.plot(x1, y1, c = "red", linestyle = "-", zorder=0)
            
            nextTopl = lines[length-2]
            x2 = nextTopl[0].get_xdata()
            y2 = nextTopl[0].get_ydata()
            err2_line = plt.plot(x2, y2, c = "red", linestyle = "-", zorder=0)
            
            l = lines.pop().pop(0)
            l.remove()
            l = lines.pop().pop(0)
            l.remove()
            
            plt.pause(GLOBAL_DELAY)
            l = err1_line.pop(0)
            l.remove()
            l = err2_line.pop(0)
            l.remove()
            # delete the algorithm/error lines
                
            a = stack.pop()
            
            new_line = draw_line(stack[len(stack)-1], x_sorted_points[i], "blue" ,delay=GLOBAL_DELAY)
            lines.append(new_line)
            if(len(stack) == 1):
                break
        #append the next point to the stack
        stack.append(x_sorted_points[i])
    for point in red_points:
        plt.scatter(point[0], point[1], s=10, c="black", zorder=0)
    plt.pause(GLOBAL_DELAY)
    return stack, lines

def draw_line(point1, point2, color = "black", line_style = "-", delay = GLOBAL_DELAY, delaybool = True):
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    line = plt.plot(x_values, y_values, c = color, linestyle = line_style, zorder=0)
    if(delaybool):
        plt.pause(delay)
    return line

# https://iq.opengenus.org/graham-scan-convex-hull/
# Orientation function from here
# https://algs4.cs.princeton.edu/91primitives/#:~:text=Given%20three%20points%20a%2C%20b,b%2D%3Ec%20are%20collinear.
# Given 3 colinnear points, find the turn (CCW or CW)
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]);
    if val == 0:
        return 0
    
    if val > 0:
        return 1 #cw
    else:
        return 2 #ccw
    
# Start of the algorithm
plt.axis('off')

angles = []
randomx = []
randomy = []
random_points = []
# generate random points
for i in range(NUM_OF_POINTS):   
    x = round(random.uniform(1.0, VALUES_RANGE), 2)
    y = round(random.uniform(1.0, VALUES_RANGE), 2)
    point = [x, y]
    random_points.append(point)
    randomx.append(x)
    randomy.append(y)

# HARD CODED CASE #
random_points = [[82.0, -383.0], [148.0, -127.0], [170.0, -142.0], [215.0, -334.0], [249.0, -278.0], 
                 [373.0, -132.0], [429.0, -210.0], [440.0, -445.0], [476.0, -43.0], [564.0, -86.0], 
                 [542.0, -345.0], [582.0, -491.0], [642.0, -209.0], [699.0, -311.0], [744.0, -413.0], 
                 [799.0, -245.0], [881.0, -162.0], [921.0, -389.0]]
randomx = []
randomy = []
for i in random_points:
    randomx.append(i[0])
    randomy.append(i[1])
NUM_OF_POINTS = 18
# HARD CODED CASE #

randomx = np.array(randomx)
randomy = np.array(randomy) # waste of memory fix later 
# plot the points
random_points = sorted(random_points, key=lambda x:x[0]) # sort bse on the angle column
plt.scatter(randomx, randomy, s=10, c="black", zorder=0)
plt.pause(2)


b_points, b_lines = half_hull(random_points, 2)
t_points, t_lines = half_hull(random_points, 1)
plt.pause(GLOBAL_DELAY)

length = len(b_lines)
for i in range(length):
    l = b_lines[i].pop(0)
    l.remove()
length = len(t_lines)
for i in range(length):
    l = t_lines[i].pop(0)
    l.remove() 

t_points.reverse()
b_points = b_points + t_points


for i in range(len(b_points)):
	draw_line(b_points[i], b_points[i-1], "black", "-", 0.1, delaybool=False)
 
plt.pause(GLOBAL_DELAY)
plt.show()