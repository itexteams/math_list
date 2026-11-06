import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang3_p2_b2_c1_hh12(self):
            # Khai báo biến
            # Khởi tạo các giá trị ngẫu nhiên
            t_val = random.randint(30, 50)
            Dx = random.randint(100, 200)

            # Đảm bảo D_y là số nguyên để t_val là nghiệm nguyên của phương trình
            if (9 * t_val - Dx + 2) % 2 != 0:
                Dx += 1
            Dy = (9 * t_val - Dx + 2) // 2

            # Tính các thông số liên quan
            MD_x = Dx - 1
            MD_y_num = 2 * Dy - 1

            # Tọa độ điểm M khi khoảng cách là nhỏ nhất
            x0 = 1 + t_val
            y0_num = 1 + 4 * t_val
            z0 = 2 * t_val

            # Giá trị biểu thức đích 20(x_0+y_0+z_0)
            sum_num = 2 * x0 + y0_num + 2 * z0
            val_20 = 10 * sum_num
            val_20_false = val_20 + random.choice([-90, 90, -100, 100])
            MD_y_num_false = MD_y_num - random.choice([80, 100, 120])

            # Nội dung câu hỏi
            noidungcauhoi = ('''\\immini{Một chiếc trực thăng $H$ cất cánh từ một sân bay. Xét hệ trục tọa độ $Oxyz$ có gốc tọa độ $O$ là chân tháp điều khiển sân bay; trục $Ox$ là hướng đông, trục $Oy$ là hướng bắc và trục $Oz$ là trục thẳng đứng, đơn vị trên mỗi trục là kilômét. Trực thăng cất cánh từ điểm $G$ trên mặt đất. Vectơ $\\vec{u}$ chỉ vị trí của trực thăng tại thời điểm $t$ phút sau khi cất cánh ($t \\ge 0$) có tọa độ là $\\vec{u}=\\left(1+t; \\frac{1}{2}+2t; 2t\\right)$. Một hòn đảo ở vị trí $D(%s; %s; 0)$. Gọi $M$ là vị trí của máy bay $H$ tại thời điểm $t$ phút sau khi cất cánh.}
                             { \\scalebox{0.7}{  \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                             	\\tikzset {_hnnlap4jm/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-90 }  \\pgftransformscale{2 }  }}}
                             	\\pgfdeclarehorizontalshading{_ba86tk3cj}{150bp}{rgb(0bp)=(0.6,0.85,1);
                             		rgb(37.5bp)=(0.6,0.85,1);
                             		rgb(62.5bp)=(1,1,1);
                             		rgb(100bp)=(1,1,1)}
                             	\\tikzset{every picture/.style={line width=0.75pt}}  
                             	\\draw  [draw opacity=0][shading=_ba86tk3cj,_hnnlap4jm] (36.53,1.6) -- (429.2,1.6) -- (429.2,210.27) -- (36.53,210.27) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 176; green, 186; blue, 200 }  ,fill opacity=1 ] (261.87,144.93) -- (429.2,210.27) -- (179,284.6) -- (36.53,210.27) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (157.89,211.68) .. controls (154.59,197.32) and (176.91,185.3) .. (207.74,184.81) .. controls (238.58,184.33) and (266.24,195.57) .. (269.54,209.92) .. controls (272.84,224.27) and (250.52,236.3) .. (219.69,236.78) .. controls (188.85,237.27) and (161.19,226.03) .. (157.89,211.68) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 176; green, 186; blue, 200 }  ,fill opacity=1 ] (166.62,211.54) .. controls (164.16,200.81) and (183.02,191.79) .. (208.75,191.39) .. controls (234.48,190.98) and (257.34,199.35) .. (259.8,210.07) .. controls (262.26,220.8) and (243.4,229.82) .. (217.67,230.23) .. controls (191.94,230.63) and (169.09,222.26) .. (166.62,211.54) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (237.53,208.48) -- (246.27,212.85) -- (207.82,222.47) -- (199.08,218.53) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (215.24,198.43) -- (223.98,202.8) -- (185.53,212.42) -- (176.79,208.48) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (210.44,205.86) -- (223.11,212.85) -- (215.68,214.82) -- (202.57,207.61) -- cycle ;
                             	\\draw [line width=1]    (58,184.6) -- (238.48,281.7) ;
                             	\\draw [shift={(242,283.6)}, rotate = 208.28] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                             	\\draw [line width=1]    (105.87,209.27) -- (329.75,145.5) ;
                             	\\draw [shift={(333.6,144.4)}, rotate = 164.1] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                             	\\draw [line width=1]    (105.87,209.27) -- (105.87,45.93) ;
                             	\\draw [shift={(105.87,41.93)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                             	\\draw [line width=1]    (277.2,69.6) -- (214.67,212) ;
                             	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (365.87,209.6) -- (214.67,212) ;
                             	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (277.2,210.27) -- (277.2,69.6) ;
                             	\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (269.92,40.97) .. controls (269.92,40.03) and (271.63,39.27) .. (273.74,39.27) .. controls (275.85,39.27) and (277.56,40.03) .. (277.56,40.97) .. controls (277.56,41.91) and (275.85,42.67) .. (273.74,42.67) .. controls (271.63,42.67) and (269.92,41.91) .. (269.92,40.97) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (270.77,48.16) -- (271.2,44.93) -- (276.84,44.93) -- (277.28,48.16) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ][fill={rgb, 255:red, 228; green, 224; blue, 224 }  ,fill opacity=1 ] (213.27,51.61) -- (217.52,51.32) -- (223.46,61.23) -- (217.8,70.99) -- (213.42,70.57) -- (218.23,61.51) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.57 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (257.7,55.71) -- (259.11,65.76) -- (221.76,62.93) -- (218.23,61.51) -- (223.32,59.53) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (292.04,62.13) -- (299.29,72.39) -- (298.28,73.11) -- (291.03,62.85) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (283.4,61.39) -- (282.69,73.93) -- (281.45,73.86) -- (282.16,61.32) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (307.33,69.53) -- (308.72,70.26) -- (302.97,73.45) -- (270.74,74.91) -- (270.22,73.86) -- (302.72,72.18) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (288.69,64.18) -- (288.44,76.74) -- (287.2,76.72) -- (287.45,64.16) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (271.02,65.64) -- (265.52,76.94) -- (264.4,76.39) -- (269.9,65.1) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.58 ][fill={rgb, 255:red, 228; green, 224; blue, 224 }  ,fill opacity=1 ] (255.43,55.74) .. controls (255.63,54.01) and (256.73,52.62) .. (257.73,51.44) .. controls (263.58,47.24) and (274.46,46.02) .. (280.25,47.19) .. controls (282.44,48.15) and (285,49.13) .. (285.6,51.3) .. controls (288.28,56.67) and (254.84,60.72) .. (255.43,55.74) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (267.73,49.87) .. controls (267.87,49.13) and (268.58,48.45) .. (269.3,48.36) -- (274.32,47.77) .. controls (275.04,47.69) and (275.51,48.22) .. (275.37,48.97) -- (274.94,51.19) .. controls (274.79,51.94) and (274.09,52.61) .. (273.37,52.7) -- (268.34,53.29) .. controls (267.62,53.38) and (267.15,52.84) .. (267.3,52.09) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.45 ][fill={rgb, 255:red, 230; green, 226; blue, 226 }  ,fill opacity=1 ] (255.43,55.74) .. controls (266.64,51.01) and (282.2,50.59) .. (297.14,50.02) .. controls (299.6,51.58) and (301.58,51.72) .. (306.39,57.1) .. controls (308.23,57.8) and (314.69,59.25) .. (314.17,62.61) .. controls (314.17,70.11) and (264.94,72.66) .. (261.12,69.97) .. controls (258.43,67) and (254.05,62.61) .. (255.43,55.74) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (295.92,50.59) -- (299.18,50.73) -- (305.97,57.1) -- (301.87,58.09) -- (296.21,59.5) -- (291.82,51.72) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (291.11,52.29) -- (294.65,59.08) -- (288.85,59.93) -- (287.86,52.71) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (286.73,52.85) -- (287.58,59.79) -- (281.63,60.35) -- (281.07,53.28) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (279.65,53.56) -- (280.36,60.35) -- (275.13,60.78) -- (274.28,54.13) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (273,54.27) -- (273.57,59.08) -- (268.62,59.64) -- (268.05,55.12) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.48 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (255.18,57.24) .. controls (257.13,56.27) and (258.76,56.57) .. (262.54,55.68) .. controls (264.52,57.66) and (265.93,61.77) .. (267.91,62.47) .. controls (275.41,61.91) and (281.35,61.2) .. (297.76,60.21) .. controls (300.84,58.36) and (304.17,57.55) .. (307.39,57.44) .. controls (312.62,58.79) and (315.73,60.07) .. (313.89,63.46) .. controls (298.15,66.15) and (278.94,66.75) .. (266.27,67.4) .. controls (264.93,67.47) and (263.67,67.54) .. (262.49,67.61) .. controls (258.86,66.58) and (255.32,63.46) .. (255.18,57.24) -- cycle ;
                             	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.47 ]   (261.57,56.64) .. controls (262.96,60.21) and (265.22,62.05) .. (266.78,63.46) ;
                             	\\draw    (275.13,61.91) -- (276.12,67) ;
                             	\\draw    (276.4,61.91) -- (277.25,67) ;
                             	\\draw    (288.71,60.78) -- (289.7,65.87) ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (297.34,61.77) .. controls (298.75,60.35) and (303.85,61.91) .. (308.37,63.6) .. controls (307.81,67.42) and (302.71,68.7) .. (299.46,66.58) .. controls (296.91,63.6) and (296.77,62.76) .. (297.34,61.77) -- cycle ;
                             	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.4 ]   (260.98,68.42) -- (298.05,66.29) ;
                             	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (261.55,68.98) -- (298.61,66.86) ;
                             	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (258.65,58.42) .. controls (258.6,58.05) and (258.87,57.71) .. (259.24,57.67) -- (262.04,57.34) .. controls (262.41,57.29) and (262.75,57.56) .. (262.79,57.93) -- (262.92,59.04) .. controls (262.97,59.42) and (262.7,59.76) .. (262.33,59.8) -- (259.53,60.13) .. controls (259.16,60.17) and (258.82,59.91) .. (258.78,59.53) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (295.95,72.56) -- (297.54,73.3) -- (290.93,76.58) -- (253.95,78.19) -- (253.36,77.13) -- (290.65,75.29) -- cycle ;
                             	\\draw [color={rgb, 255:red, 100; green, 7; blue, 7 }  ,draw opacity=1 ]   (227.99,60.66) -- (255.01,58.4) ;
                             	\\draw [color={rgb, 255:red, 146; green, 21; blue, 21 }  ,draw opacity=1 ]   (241,61.94) -- (255.43,62.22) ;
                             	\\draw  [color={rgb, 255:red, 100; green, 12; blue, 12 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (215.96,52.88) -- (220.91,59.39) -- (224.03,55.71) -- (225.3,56.84) -- (221.9,60.95) -- (227,64.77) -- (224.88,66.46) -- (220.35,61.94) -- (216.25,68.16) -- (214.12,67.31) -- (219.92,60.95) -- (212.99,54.72) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (219.1,60.65) .. controls (219.1,59.56) and (219.98,58.68) .. (221.07,58.68) .. controls (222.16,58.68) and (223.04,59.56) .. (223.04,60.65) .. controls (223.04,61.73) and (222.16,62.61) .. (221.07,62.61) .. controls (219.98,62.61) and (219.1,61.73) .. (219.1,60.65) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (220.08,60.65) .. controls (220.08,60.1) and (220.52,59.66) .. (221.07,59.66) .. controls (221.62,59.66) and (222.06,60.1) .. (222.06,60.65) .. controls (222.06,61.2) and (221.62,61.64) .. (221.07,61.64) .. controls (220.52,61.64) and (220.08,61.2) .. (220.08,60.65) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (272.84,41.96) -- (274.59,41.96) -- (274.59,46.54) -- (272.84,46.54) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (308.37,32.93) -- (313.58,34.18) -- (275.52,42.38) -- (272.84,41.96) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (323.2,44.96) -- (319.55,46.77) -- (275.27,42.95) -- (273.71,41.96) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (272.84,41.96) -- (273.26,42.67) -- (238.74,48.89) -- (233.79,47.76) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (273.71,41.96) -- (272.33,42.78) -- (214.46,39.1) -- (218.57,37.4) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (278.86,39.87) -- (280.81,42.24) -- (279.12,43.8) -- (274.17,42.81) -- (270.63,44.08) -- (268.51,43.23) -- (268.08,40.4) -- (273.6,41.11) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (272.84,41.96) .. controls (272.84,41.45) and (273.28,41.04) .. (273.83,41.04) .. controls (274.37,41.04) and (274.82,41.45) .. (274.82,41.96) .. controls (274.82,42.47) and (274.37,42.88) .. (273.83,42.88) .. controls (273.28,42.88) and (272.84,42.47) .. (272.84,41.96) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ] (255.75,61.2) -- (256.76,65.02) -- (225.5,63.04) -- (223.46,61.23) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ] (262.92,59.04) -- (268.51,65.3) -- (260.3,66.01) -- (257.61,63.6) -- (256.2,60.35) -- cycle ;
                             	\\draw [color={rgb, 255:red, 220; green, 128; blue, 128 }  ,draw opacity=1 ]   (278.41,62.76) -- (295.67,61.48) ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.26 ] (289.5,52.48) -- (268.05,55.12) -- (280.36,60.35) -- (283.46,60.21) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.46 ] (298.18,50.59) -- (291.97,52.35) -- (301.2,57.38) -- (304.4,56.44) -- cycle ;
                             	\\draw (88.33,205) node [anchor=north west][inner sep=0.75pt]    {$O$};
                             	\\draw (211.33,271.33) node [anchor=north west][inner sep=0.75pt]    {$x$};
                             	\\draw (312.83,122) node [anchor=north west][inner sep=0.75pt]    {$y$};
                             	\\draw (90.67,35.67) node [anchor=north west][inner sep=0.75pt]    {$z$};
                             	\\draw (246.17,266) node [anchor=north west][inner sep=0.75pt]    {$D$};
                             	\\draw (332.5,139.17) node [anchor=north west][inner sep=0.75pt]    {$B$};
                             	\\draw (195.33,201) node [anchor=north west][inner sep=0.75pt]    {$G$};
                             	\\draw (278,77.33) node [anchor=north west][inner sep=0.75pt]    {$H$};
                             	\\draw (267.33,210.67) node [anchor=north west][inner sep=0.75pt]    {$F$};
                             \\end{tikzpicture} }
            }''' % (Dx, Dy))

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = '\\True Tọa độ điểm $M$ tại thời điểm $t$ phút sau khi máy bay $H$ cất cánh là $M\\left(1+t; \\frac{1}{2}+2t; 2t\\right)$'
            nb_da_1_s = 'Tọa độ điểm $M$ tại thời điểm $t$ phút sau khi máy bay $H$ cất cánh là $M\\left(1+t; \\frac{1}{2}-2t; 2t\\right)$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Gắn vào hệ trục tọa độ $Oxyz$, ta có $\\vec{u} = \\overrightarrow{OM} = \\left(1+t; \\frac{1}{2}+2t; 2t\\right)$. Khi đó vị trí máy bay $H$ ở thời điểm $t$ phút sau khi máy bay cất cánh là $M\\left(1+t; \\frac{1}{2}+2t; 2t\\right)$.''')
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Tọa độ điểm $G$ là $\\left(1; \\frac{1}{2}; 0\\right)$'
            th_da_1_s = 'Tọa độ điểm $G$ là $\\left(1; 1; 0\\right)$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Khi máy bay bắt đầu khởi hành, với $t=0 \\Rightarrow M \\equiv G\\left(1; \\frac{1}{2}; 0\\right)$.''')

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Tọa độ của vectơ $\\overrightarrow{MD}$ là $\\left(%s-t; \\frac{%s}{2}-2t; -2t\\right)$' % (MD_x, MD_y_num)
            vd_da_1_s = 'Tọa độ của vectơ $\\overrightarrow{MD}$ là $\\left(%s-t; \\frac{%s}{2}-2t; -2t\\right)$' % (MD_x, MD_y_num_false)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $M\\left(1+t; \\frac{1}{2}+2t; 2t\\right)$ và $D(%s; %s; 0)$. Suy ra $\\overrightarrow{MD} = \\left(%s - (1+t); %s - \\left(\\frac{1}{2}+2t\\right); 0 - 2t\\right) = \\left(%s-t; \\frac{%s}{2}-2t; -2t\\right)$.''' % (Dx, Dy, Dx, Dy, MD_x, MD_y_num))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Máy bay $H$ bay đến vị trí $M(x_0; y_0; z_0)$ thì khoảng cách từ máy bay đến $D$ là nhỏ nhất. Khi đó $20(x_0+y_0+z_0) = %s$' % (val_20)
            vdc_da_1_s = 'Máy bay $H$ bay đến vị trí $M(x_0; y_0; z_0)$ thì khoảng cách từ máy bay đến $D$ là nhỏ nhất. Khi đó $20(x_0+y_0+z_0) = %s$' % (val_20_false)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Máy bay chuyển động trên đường thẳng đi qua $G\\left(1; \\frac{1}{2}; 0\\right)$ và có vectơ chỉ phương $\\vec{v}=(1; 2; 2)$.\\\\
            Khoảng cách từ máy bay $H$ đến $D$ nhỏ nhất khi và chỉ khi $\\overrightarrow{MD} \\perp \\vec{v} \\Leftrightarrow \\overrightarrow{MD} \\cdot \\vec{v} = 0 \\Leftrightarrow 1(%s-t) + 2\\left(\\frac{%s}{2}-2t\\right) + 2(-2t) = 0 \\Leftrightarrow %s - t + %s - 4t - 4t = 0 \\Leftrightarrow 9t = %s \\Leftrightarrow t = %s$.\\\\
            Suy ra $M\\left(%s; \\frac{%s}{2}; %s\\right)$. Vậy $T = 20(x_0+y_0+z_0) = %s$.''' % (MD_x, MD_y_num, MD_x, MD_y_num, MD_x + MD_y_num, t_val, x0, y0_num, z0, val_20))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
               '{'+str(shuffled_answers_nb[0])+'}\n'
               '{'+str(shuffled_answers_th[0])+'}\n'
               '{'+str(shuffled_answers_vd[0])+'}\n'
               '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

