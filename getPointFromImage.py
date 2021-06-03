# -*- coding:utf-8 -*-
"""
根据像素值,利用鼠标获取图片中的像素点坐标,然后用matplotlib将点画出
@author: Weijie Shen
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("./1111111")

img_sum = np.sum(img,axis=2)
# img_sum = img
pointers = dict()

upper = []
lower = []

def get_Real_Data_Coordinates(upper_xy,lower_xy,xy):
    """
    获得每个点在坐标系中的坐标
    "左上角:",(upper[0][0],upper[0][1])
    "右上角:",(upper[1][0],upper[1][1])
    "左下角:",(lower[0][0],lower[0][1])
    "右下角:",(lower[1][0],lower[1][1])
    :param upper_xy:
    :param lower_xy:
    :return:
    """
    upper_left = (min(upper[0][0],lower[0][0]),min(upper[0][1],lower[1][1]))
    upper_right = (min(upper[1][0],lower[1][0]),min(upper[1][1],upper[0][1]))
    lower_left = (min(lower[0][0],upper[0][0]),min(lower[0][1],lower[1][1]))
    lower_right = (min(lower[1][0],upper[1][0]),min(lower[1][1],lower[0][1]))
    return (0+abs(xy[0]-lower_left[0]),0+abs(xy[1]-lower_left[1]))

def on_EVENT_LBUTTONDOWN(event, x, y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        if param == "ul":
            print("call ul")
            upper.append((x,y))
            cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 0), thickness=1)
            cv2.imshow("image", img)
        elif param == "ur":
            print("call ur")
            upper.append((x,y))
            cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 0), thickness=1)
            cv2.imshow("image", img)
        elif param == "ll":
            print("call ll")
            lower.append((x,y))
            cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 0), thickness=1)
            cv2.imshow("image", img)
        elif param == "lr":
            print("call lr")
            lower.append((x,y))
            cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 0), thickness=1)
            cv2.imshow("image", img)
        else:
            if img_sum[x,y] in pointers:
                xy_md = get_Real_Data_Coordinates(upper,lower,(x,y))
                pointers[img_sum[x,y]].append((xy_md[0],xy_md[1],img[x,y][0],img[x,y][1],img[x,y][2]))
            else:
                xy_md = get_Real_Data_Coordinates(upper, lower, (x, y))
                pointers.setdefault(img_sum[x,y],[]).append((xy_md[0],xy_md[1],img[x,y][0],img[x,y][1],img[x,y][2]))
            cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 0), thickness=1)
            cv2.imshow("image", img)


def draw(pointers):
    pointers_list_x = []
    pointers_list_y = []
    for pointer_k in pointers:
        # pointers是字典
        # pointer_k是key
        point_list_x = []
        point_list_y = []
        for pointer in pointers[pointer_k]:
            point_list_x.append(pointer[0])
            point_list_y.append(pointer[1])
        pointers_list_x.append(point_list_x)
        pointers_list_y.append(point_list_y)

    colors = ['red','blue','pink','yellow','darkblue','lightgreen','green','gray']
    for i in range(len(pointers_list_x)):
        plt.scatter(pointers_list_x[i], pointers_list_y[i], s=100, c=colors[i], alpha=0.65)

    plt.show()



cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN,"ul")
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN,"ur")
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN,"ll")
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN,"lr")
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)
cv2.waitKey(0)
draw(pointers)