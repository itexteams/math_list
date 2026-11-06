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


def bt_dang34_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':


                a_val = 0.001302
                b_val = 0.09029
                c_val = random.choice([50, 60, 70, 80, 83, 90, 100])

                # Tính t tại gia tốc min
                t_min = b_val / (3 * a_val)

                # Tính v tại t_min
                v_min = a_val * (t_min**3) - b_val * (t_min**2) + c_val

                # Làm tròn đến hàng phần mười
                kq_num = round(v_min, 1)

                # Định dạng các số ra chuỗi theo yêu cầu có dấu phẩy
                a_str = "0,001302"
                b_str = "0,09029"
                c_str = str(c_val)
                kq_str = str(kq_num).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_str),
                      ]
                da = random.choice(du)

                s = ['$%s$'%(latex(round(kq_num + 1.2, 1)).replace('.', ',')),
                     '$%s$'%(latex(round(kq_num - 1.5, 1)).replace('.', ',')),
                     '$%s$'%(latex(round(kq_num + 2.5, 1)).replace('.', ',')),
                     '$%s$'%(latex(round(kq_num - 2.1, 1)).replace('.', ',')),
                     '$%s$'%(latex(round(kq_num + 3.4, 1)).replace('.', ',')),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (334.4,245.33) .. controls (342.51,245.33) and (349.37,249.53) .. (351.76,255.34) .. controls (353.91,254.63) and (356.27,254.24) .. (358.74,254.24) .. controls (368.83,254.24) and (377,260.74) .. (377,268.76) .. controls (377,276.78) and (368.83,283.28) .. (358.74,283.28) .. controls (351.89,283.28) and (345.92,280.27) .. (342.8,275.83) .. controls (342.2,285.54) and (332.11,293.27) .. (319.75,293.27) .. controls (307.01,293.27) and (296.68,285.05) .. (296.68,274.91) .. controls (296.68,265.64) and (305.33,257.97) .. (316.57,256.73) .. controls (318.37,250.21) and (325.67,245.33) .. (334.4,245.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 179; green, 171; blue, 171 }  ,fill opacity=1 ] (334.73,248.59) .. controls (341.74,248.59) and (347.67,252.21) .. (349.73,257.23) .. controls (351.59,256.62) and (353.63,256.28) .. (355.77,256.28) .. controls (364.48,256.28) and (371.55,261.9) .. (371.55,268.83) .. controls (371.55,275.76) and (364.48,281.38) .. (355.77,281.38) .. controls (349.85,281.38) and (344.69,278.78) .. (341.99,274.94) .. controls (341.47,283.34) and (332.75,290.01) .. (322.07,290.01) .. controls (311.06,290.01) and (302.13,282.91) .. (302.13,274.15) .. controls (302.13,266.13) and (309.61,259.51) .. (319.32,258.44) .. controls (320.87,252.81) and (327.18,248.59) .. (334.73,248.59) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 203; green, 198; blue, 198 }  ,fill opacity=1 ] (337.89,252.26) .. controls (344.29,252.26) and (349.72,255.58) .. (351.6,260.17) .. controls (353.3,259.61) and (355.17,259.3) .. (357.12,259.3) .. controls (365.09,259.3) and (371.55,264.43) .. (371.55,270.77) .. controls (371.55,277.11) and (365.09,282.24) .. (357.12,282.24) .. controls (351.71,282.24) and (346.99,279.87) .. (344.52,276.36) .. controls (344.05,284.03) and (336.08,290.14) .. (326.31,290.14) .. controls (316.24,290.14) and (308.08,283.64) .. (308.08,275.63) .. controls (308.08,268.3) and (314.92,262.24) .. (323.8,261.27) .. controls (325.21,256.12) and (330.99,252.26) .. (337.89,252.26) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (422.4,229.67) .. controls (430.51,229.67) and (437.37,234.94) .. (439.76,242.25) .. controls (441.91,241.36) and (444.27,240.86) .. (446.74,240.86) .. controls (456.83,240.86) and (465,249.04) .. (465,259.12) .. controls (465,269.2) and (456.83,277.37) .. (446.74,277.37) .. controls (439.89,277.37) and (433.92,273.6) .. (430.8,268.01) .. controls (430.2,280.22) and (420.11,289.93) .. (407.75,289.93) .. controls (395.01,289.93) and (384.68,279.6) .. (384.68,266.86) .. controls (384.68,255.19) and (393.33,245.55) .. (404.57,244) .. controls (406.37,235.8) and (413.67,229.67) .. (422.4,229.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 179; green, 171; blue, 171 }  ,fill opacity=1 ] (422.73,233.76) .. controls (429.74,233.76) and (435.67,238.32) .. (437.73,244.63) .. controls (439.59,243.86) and (441.63,243.43) .. (443.77,243.43) .. controls (452.48,243.43) and (459.55,250.5) .. (459.55,259.21) .. controls (459.55,267.92) and (452.48,274.99) .. (443.77,274.99) .. controls (437.85,274.99) and (432.69,271.72) .. (429.99,266.9) .. controls (429.47,277.45) and (420.75,285.84) .. (410.07,285.84) .. controls (399.06,285.84) and (390.13,276.91) .. (390.13,265.9) .. controls (390.13,255.82) and (397.61,247.49) .. (407.32,246.15) .. controls (408.87,239.06) and (415.18,233.76) .. (422.73,233.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 203; green, 198; blue, 198 }  ,fill opacity=1 ] (425.89,238.37) .. controls (432.29,238.37) and (437.72,242.54) .. (439.6,248.32) .. controls (441.3,247.61) and (443.17,247.22) .. (445.12,247.22) .. controls (453.09,247.22) and (459.55,253.68) .. (459.55,261.65) .. controls (459.55,269.61) and (453.09,276.07) .. (445.12,276.07) .. controls (439.71,276.07) and (434.99,273.09) .. (432.52,268.67) .. controls (432.05,278.32) and (424.08,286) .. (414.31,286) .. controls (404.24,286) and (396.08,277.83) .. (396.08,267.76) .. controls (396.08,258.55) and (402.92,250.93) .. (411.8,249.7) .. controls (413.21,243.22) and (418.99,238.37) .. (425.89,238.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (255.4,226.67) .. controls (263.51,226.67) and (270.37,231.94) .. (272.76,239.25) .. controls (274.91,238.36) and (277.27,237.86) .. (279.74,237.86) .. controls (289.83,237.86) and (298,246.04) .. (298,256.12) .. controls (298,266.2) and (289.83,274.37) .. (279.74,274.37) .. controls (272.89,274.37) and (266.92,270.6) .. (263.8,265.01) .. controls (263.2,277.22) and (253.11,286.93) .. (240.75,286.93) .. controls (228.01,286.93) and (217.68,276.6) .. (217.68,263.86) .. controls (217.68,252.19) and (226.33,242.55) .. (237.57,241) .. controls (239.37,232.8) and (246.67,226.67) .. (255.4,226.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 179; green, 171; blue, 171 }  ,fill opacity=1 ] (255.73,230.76) .. controls (262.74,230.76) and (268.67,235.32) .. (270.73,241.63) .. controls (272.59,240.86) and (274.63,240.43) .. (276.77,240.43) .. controls (285.48,240.43) and (292.55,247.5) .. (292.55,256.21) .. controls (292.55,264.92) and (285.48,271.99) .. (276.77,271.99) .. controls (270.85,271.99) and (265.69,268.72) .. (262.99,263.9) .. controls (262.47,274.45) and (253.75,282.84) .. (243.07,282.84) .. controls (232.06,282.84) and (223.13,273.91) .. (223.13,262.9) .. controls (223.13,252.82) and (230.61,244.49) .. (240.32,243.15) .. controls (241.87,236.06) and (248.18,230.76) .. (255.73,230.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 203; green, 198; blue, 198 }  ,fill opacity=1 ] (258.89,235.37) .. controls (265.29,235.37) and (270.72,239.54) .. (272.6,245.32) .. controls (274.3,244.61) and (276.17,244.22) .. (278.12,244.22) .. controls (286.09,244.22) and (292.55,250.68) .. (292.55,258.65) .. controls (292.55,266.61) and (286.09,273.07) .. (278.12,273.07) .. controls (272.71,273.07) and (267.99,270.09) .. (265.52,265.67) .. controls (265.05,275.32) and (257.08,283) .. (247.31,283) .. controls (237.24,283) and (229.08,274.83) .. (229.08,264.76) .. controls (229.08,255.55) and (235.92,247.93) .. (244.8,246.7) .. controls (246.21,240.22) and (251.99,235.37) .. (258.89,235.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (385.06,235.64) .. controls (364.99,223.4) and (379.71,236.46) .. (365.66,234.01) .. controls (364.32,278.9) and (353.61,240.54) .. (333.54,277.27) .. controls (332.87,285.43) and (409.81,278.08) .. (455.98,280.53) .. controls (468.02,200.55) and (387.07,285.43) .. (385.06,235.64) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (380.38,235.64) .. controls (360.3,223.4) and (383.62,235.99) .. (369.57,233.54) .. controls (368.23,278.43) and (359.64,242.99) .. (338.23,278.08) .. controls (337.83,282.94) and (360.21,281.49) .. (391.93,280.7) .. controls (413.53,280.16) and (432.59,280.36) .. (451.3,281.35) .. controls (464.68,212.79) and (382.38,285.43) .. (380.38,235.64) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (380.38,235.64) .. controls (360.3,223.4) and (377.03,248.7) .. (372.35,236.46) .. controls (371.01,281.35) and (365.66,242.17) .. (344.25,277.27) .. controls (343.85,282.12) and (360.21,281.49) .. (391.93,280.7) .. controls (413.53,280.16) and (428.58,280.36) .. (447.28,281.35) .. controls (457.32,226.66) and (382.38,285.43) .. (380.38,235.64) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (297.87,237.31) .. controls (317.87,225.07) and (303.2,238.13) .. (317.2,235.68) .. controls (318.53,280.57) and (329.2,242.21) .. (349.2,278.94) .. controls (349.87,287.1) and (273.2,279.75) .. (227.2,282.2) .. controls (215.2,202.21) and (295.87,287.1) .. (297.87,237.31) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (302.53,237.31) .. controls (322.53,225.07) and (299.3,237.66) .. (313.3,235.21) .. controls (314.63,280.1) and (323.2,244.66) .. (344.53,279.75) .. controls (344.93,284.61) and (322.62,283.16) .. (291.02,282.36) .. controls (269.5,281.82) and (250.5,282.02) .. (231.87,283.02) .. controls (218.53,214.46) and (300.53,287.1) .. (302.53,237.31) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (302.53,237.31) .. controls (322.53,225.07) and (305.87,250.37) .. (310.53,238.13) .. controls (311.87,283.02) and (317.2,243.84) .. (338.53,278.94) .. controls (338.93,283.79) and (322.62,283.16) .. (291.02,282.36) .. controls (269.5,281.82) and (254.5,282.02) .. (235.87,283.02) .. controls (225.87,228.33) and (300.53,287.1) .. (302.53,237.31) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (365.74,191.84) -- (364.19,201.47) -- (340.53,201.47) -- (338.98,191.84) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (341.73,201.47) -- (362.99,201.47) -- (362.99,209.21) -- (341.73,209.21) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (343.28,209.21) -- (361.44,209.21) -- (361.44,213.86) -- (343.28,213.86) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (341.73,201.47) -- (362.99,201.47) -- (362.99,204.57) -- (341.73,204.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (343.28,209.21) -- (361.44,209.21) -- (361.44,212.31) -- (343.28,212.31) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (344.48,214.03) -- (360.24,214.03) -- (360.24,216.59) -- (344.48,216.59) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (343.85,191.23) -- (342.3,200.86) -- (318.63,200.86) -- (317.09,191.23) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (319.84,200.86) -- (341.09,200.86) -- (341.09,208.6) -- (319.84,208.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (321.38,208.6) -- (339.55,208.6) -- (339.55,213.25) -- (321.38,213.25) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (319.84,200.86) -- (341.09,200.86) -- (341.09,203.96) -- (319.84,203.96) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (321.38,208.6) -- (339.55,208.6) -- (339.55,211.7) -- (321.38,211.7) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (322.59,213.42) -- (338.34,213.42) -- (338.34,216.59) -- (322.59,216.59) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 138; blue, 35 }  ,fill opacity=1 ] (341.63,16.62) .. controls (348.88,21.68) and (356.78,34.5) .. (363.07,49.68) .. controls (361.79,90.43) and (362.7,136.95) .. (362.24,151.09) .. controls (344,169.34) and (337.61,168.88) .. (322.56,169.79) .. controls (320.73,148.81) and (321.19,86.78) .. (320.64,51) .. controls (326.72,33.85) and (334.63,20.12) .. (341.63,16.62) -- cycle ;
            	\draw [line width=1.5]    (323.47,79.02) -- (359.96,79.02) ;
            	\draw [line width=0.75]    (323.47,91.34) -- (359.96,91.34) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.11 ] (342.08,16.17) .. controls (337.16,27.02) and (328.03,38.88) .. (326.66,52.57) .. controls (325.39,93.31) and (328.03,149.27) .. (327.58,163.41) .. controls (309.33,181.65) and (338.07,168.43) .. (323.02,169.34) .. controls (321.19,148.36) and (321.65,86.32) .. (321.09,50.55) .. controls (327.17,33.4) and (335.09,19.66) .. (342.08,16.17) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.32 ] (340.71,17.08) .. controls (347.97,22.14) and (357.68,33.86) .. (362.15,50.13) .. controls (360.87,90.88) and (361.79,137.41) .. (361.33,151.55) .. controls (343.09,169.79) and (370.45,145.62) .. (355.4,146.53) .. controls (353.58,125.55) and (356.41,94.73) .. (355.86,58.95) .. controls (357.68,44.36) and (349.02,32.5) .. (340.71,17.08) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (298.79,92.34) -- (316.81,92.34) -- (316.81,209.02) -- (298.79,209.02) -- cycle ;
            	\draw    (298.79,100.92) -- (317.09,100.92) ;
            	\draw    (298.79,114.15) -- (317.09,114.15) ;
            	\draw    (299.25,129.2) -- (317.09,129.2) ;
            	\draw    (299.48,142.88) -- (317.09,142.88) ;
            	\draw    (299.25,157.94) -- (317.09,157.94) ;
            	\draw   (308.1,64.06) .. controls (318.64,79.48) and (317.72,83.13) .. (317.72,92.48) .. controls (307.23,91.79) and (303.81,92.48) .. (298.11,92.02) .. controls (297.65,83.81) and (296.51,77.43) .. (308.1,64.06) -- cycle ;
            	\draw    (297.88,86.78) -- (301.3,86.78) ;
            	\draw    (313.85,87.01) -- (317.72,87.01) ;
            	\draw    (301.3,86.78) .. controls (301.3,76.06) and (312.93,76.06) .. (313.85,87.01) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (305.41,86.53) .. controls (305.41,85.63) and (306.13,84.91) .. (307.03,84.91) .. controls (307.92,84.91) and (308.65,85.63) .. (308.65,86.53) .. controls (308.65,87.42) and (307.92,88.15) .. (307.03,88.15) .. controls (306.13,88.15) and (305.41,87.42) .. (305.41,86.53) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (306.09,81.05) .. controls (306.09,80.41) and (306.61,79.89) .. (307.26,79.89) .. controls (307.9,79.89) and (308.42,80.41) .. (308.42,81.05) .. controls (308.42,81.7) and (307.9,82.22) .. (307.26,82.22) .. controls (306.61,82.22) and (306.09,81.7) .. (306.09,81.05) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (297.2,217.69) -- (300.21,207.65) -- (314.71,207.65) -- (317.72,217.69) -- cycle ;
            	\draw    (299.71,210.39) -- (315.44,210.39) ;
            	\draw    (299.02,212.67) -- (316.36,212.67) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (297.2,217.69) -- (317.72,217.69) -- (317.72,232.06) -- (297.2,232.06) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (297.2,225.22) -- (317.72,225.22) -- (317.72,228.18) -- (297.2,228.18) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (294.19,235.71) -- (297.33,232.06) -- (317.55,232.06) -- (320.69,235.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (308.1,64.06) .. controls (317.72,76.51) and (317.5,82.67) .. (317.72,92.48) .. controls (316.58,118.71) and (317.5,182.11) .. (316.81,209.02) .. controls (314.17,209.04) and (312.1,208.51) .. (310.52,207.51) .. controls (309.74,203.32) and (312.02,121.44) .. (310.88,91.79) .. controls (310.2,80.85) and (312.25,84.5) .. (308.1,64.06) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.34 ] (312.25,217.92) -- (310.52,207.51) -- (314.71,207.65) -- (317.72,217.69) -- (317.55,232.06) -- (320.69,235.71) -- (312.25,235.71) -- (312.02,232.06) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (300.39,224.81) -- (302.58,224.81) -- (302.58,228.18) -- (300.39,228.18) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (366,90.76) -- (384.02,90.76) -- (384.02,207.44) -- (366,207.44) -- cycle ;
            	\draw    (366,99.34) -- (384.29,99.34) ;
            	\draw    (366,112.56) -- (384.29,112.56) ;
            	\draw    (366.45,127.62) -- (384.29,127.62) ;
            	\draw    (366.68,141.3) -- (384.29,141.3) ;
            	\draw    (366.45,156.35) -- (384.29,156.35) ;
            	\draw   (375.3,62.48) .. controls (385.84,77.9) and (384.93,81.55) .. (384.93,90.9) .. controls (374.44,90.21) and (371.02,90.9) .. (365.31,90.44) .. controls (364.86,82.23) and (363.72,75.85) .. (375.3,62.48) -- cycle ;
            	\draw    (365.09,85.2) -- (368.51,85.2) ;
            	\draw    (381.05,85.42) -- (384.93,85.42) ;
            	\draw    (368.51,85.2) .. controls (368.51,74.48) and (380.14,74.48) .. (381.05,85.42) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (372.61,84.95) .. controls (372.61,84.05) and (373.34,83.33) .. (374.23,83.33) .. controls (375.13,83.33) and (375.85,84.05) .. (375.85,84.95) .. controls (375.85,85.84) and (375.13,86.56) .. (374.23,86.56) .. controls (373.34,86.56) and (372.61,85.84) .. (372.61,84.95) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (373.3,79.47) .. controls (373.3,78.83) and (373.82,78.31) .. (374.46,78.31) .. controls (375.1,78.31) and (375.62,78.83) .. (375.62,79.47) .. controls (375.62,80.11) and (375.1,80.63) .. (374.46,80.63) .. controls (373.82,80.63) and (373.3,80.11) .. (373.3,79.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (364.4,216.11) -- (367.41,206.07) -- (381.92,206.07) -- (384.93,216.11) -- cycle ;
            	\draw    (366.91,208.81) -- (382.65,208.81) ;
            	\draw    (366.23,211.09) -- (383.56,211.09) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (364.4,216.11) -- (384.93,216.11) -- (384.93,230.48) -- (364.4,230.48) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (364.4,223.63) -- (384.93,223.63) -- (384.93,226.6) -- (364.4,226.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (361.39,234.13) -- (364.54,230.48) -- (384.75,230.48) -- (387.89,234.13) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.34 ] (375.3,62.48) .. controls (369.65,73.11) and (368.96,78.35) .. (368.74,90.21) .. controls (369.88,156.35) and (368.96,180.99) .. (370.1,205.39) .. controls (367.14,205.39) and (366.68,206.07) .. (366.91,208.81) .. controls (365.54,197.18) and (366.08,97.85) .. (365.22,90.43) .. controls (364.03,80.16) and (367.52,71.96) .. (375.3,62.48) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (375.3,62.48) .. controls (384.93,74.93) and (384.7,81.09) .. (384.93,90.9) .. controls (383.79,117.13) and (384.7,180.53) .. (384.02,207.44) .. controls (381.37,207.46) and (379.31,206.93) .. (377.72,205.93) .. controls (376.95,201.74) and (379.23,119.86) .. (378.09,90.21) .. controls (377.4,79.27) and (379.45,82.92) .. (375.3,62.48) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.34 ] (364.4,216.11) -- (367.41,206.07) -- (370.1,206.53) -- (368.96,215.65) -- (369.19,230.25) -- (368.05,234.35) -- (361.39,234.13) -- (364.54,230.48) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.34 ] (379.45,216.34) -- (377.72,205.93) -- (381.92,206.07) -- (384.93,216.11) -- (384.75,230.48) -- (387.89,234.13) -- (379.45,234.13) -- (379.23,230.48) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (367.6,223.22) -- (369.78,223.22) -- (369.78,226.6) -- (367.6,226.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (340.26,72.33) .. controls (355.34,79.02) and (355.64,100.01) .. (355.64,112.47) .. controls (358.69,130.72) and (360.21,131.02) .. (365.98,145.01) .. controls (369.53,150.33) and (393.35,169.95) .. (399.13,177.85) .. controls (399.74,182.11) and (400.65,186.37) .. (400.35,190.32) .. controls (386.4,192.33) and (363.13,199.9) .. (340.14,198.84) .. controls (315.82,197.71) and (291.48,192.15) .. (280.84,190.32) .. controls (280.84,185.15) and (280.84,179.98) .. (280.53,176.03) .. controls (287.53,165.39) and (310.64,153.53) .. (316.42,144.1) .. controls (320.07,135.28) and (322.01,127.07) .. (325.84,113.69) .. controls (325.93,93.14) and (330.81,77.06) .. (340.26,72.33) -- cycle ;
            	\draw    (325.84,113.69) -- (325.84,183.63) ;
            	\draw    (355.64,114.6) -- (355.64,183.33) ;
            	\draw    (340.9,110.41) -- (340.9,195.49) ;
            	\draw    (328.28,112.17) .. controls (329.43,103.71) and (331.01,93.62) .. (334.66,90.27) .. controls (338.92,87.84) and (341.66,87.54) .. (347.13,89.67) .. controls (352.3,93.92) and (352.38,103.26) .. (353.52,112.17) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (337.82,94.08) .. controls (337.82,92.98) and (339.16,92.1) .. (340.8,92.1) .. controls (342.45,92.1) and (343.78,92.98) .. (343.78,94.08) .. controls (343.78,95.17) and (342.45,96.05) .. (340.8,96.05) .. controls (339.16,96.05) and (337.82,95.17) .. (337.82,94.08) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (344.21,96.2) .. controls (344.21,95.11) and (345.54,94.23) .. (347.19,94.23) .. controls (348.84,94.23) and (350.17,95.11) .. (350.17,96.2) .. controls (350.17,97.3) and (348.84,98.18) .. (347.19,98.18) .. controls (345.54,98.18) and (344.21,97.3) .. (344.21,96.2) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (331.74,95.9) .. controls (331.74,94.81) and (333.08,93.92) .. (334.72,93.92) .. controls (336.37,93.92) and (337.7,94.81) .. (337.7,95.9) .. controls (337.7,96.99) and (336.37,97.88) .. (334.72,97.88) .. controls (333.08,97.88) and (331.74,96.99) .. (331.74,95.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (340.26,72.33) .. controls (342.88,73.58) and (345.28,75.71) .. (348.95,79.33) .. controls (344.66,83.02) and (344.7,82.67) .. (340.5,79.78) .. controls (335.57,82.37) and (335.57,84.5) .. (332.84,79.63) .. controls (334.88,74.67) and (338.31,76.29) .. (340.26,72.33) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (338.43,80.24) .. controls (338.43,78.98) and (339.36,77.96) .. (340.5,77.96) .. controls (341.64,77.96) and (342.57,78.98) .. (342.57,80.24) .. controls (342.57,81.5) and (341.64,82.52) .. (340.5,82.52) .. controls (339.36,82.52) and (338.43,81.5) .. (338.43,80.24) -- cycle ;
            	\draw    (281.45,185.76) -- (399.43,185.46) ;
            	\draw    (286.01,191.23) -- (287.22,185.76) ;
            	\draw    (293.61,192.75) -- (294.83,186.37) ;
            	\draw    (300.6,193.97) -- (302.43,185.46) ;
            	\draw    (308.21,195.49) -- (310.33,185.76) ;
            	\draw    (315.81,196.1) -- (318.24,185.76) ;
            	\draw    (395.48,190.93) -- (393.35,185.46) ;
            	\draw    (389.7,192.45) -- (386.66,185.76) ;
            	\draw    (383.32,193.97) -- (379.67,185.46) ;
            	\draw    (376.32,195.49) -- (372.98,185.46) ;
            	\draw    (369.94,196.71) -- (365.98,185.76) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (325.84,113.69) .. controls (322.8,129.81) and (321.59,138.02) .. (319.15,145.92) .. controls (313.38,151.7) and (286.31,172.68) .. (284.18,176.03) .. controls (284.79,177.25) and (282.97,186.06) .. (283.88,190.63) .. controls (281.45,190.63) and (283.88,190.32) .. (280.84,190.32) .. controls (281.14,186.98) and (280.53,182.11) .. (280.53,176.03) .. controls (283.88,169.95) and (306.99,154.74) .. (316.42,144.1) .. controls (320.07,134.06) and (320.98,129.2) .. (325.84,113.69) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (355.34,117.03) .. controls (358.46,133.15) and (361.36,139.84) .. (363.85,147.75) .. controls (369.79,153.52) and (395.93,176.03) .. (398.12,179.37) .. controls (397.5,180.59) and (399.15,186.67) .. (398.22,191.23) .. controls (401.04,187.89) and (399.44,187.58) .. (401.87,190.63) .. controls (401.55,187.28) and (400.65,184.24) .. (400.65,178.16) .. controls (397.22,172.08) and (375.66,155.65) .. (365.98,145.01) .. controls (362.24,134.98) and (360.34,132.54) .. (355.34,117.03) -- cycle ;
            	\draw [line width=3]    (280.84,190.32) .. controls (291.36,192.12) and (316.43,199.8) .. (341.35,200.05) .. controls (366.28,200.3) and (392.5,191.57) .. (400.65,188.8) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (338.68,185.76) -- (325.84,183.63) -- (317.27,202.48) -- (337.95,206.44) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (355.64,183.33) -- (343.24,185.76) -- (344.76,206.74) -- (365.13,202.48) -- cycle ;
            	\draw [line width=3]    (319.03,199.44) .. controls (322.25,200.36) and (328.64,201.88) .. (338.37,202.18) ;
            	\draw [line width=3]    (344.15,202.18) .. controls (347.37,203.09) and (356.62,200.66) .. (363.92,199.14) ;
            	\draw [line width=1.5]    (318.18,202.48) .. controls (320.73,193.06) and (321.04,189.41) .. (326.76,183.63) ;
            	\draw [line width=1.5]    (365.13,202.48) .. controls (362.7,193.67) and (359.05,187.89) .. (355.64,183.33) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (340.8,195.49) -- (343.24,185.76) -- (344.76,200.66) -- (338.37,202.18) -- (338.68,185.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (367.69,179.37) -- (378.51,179.37) -- (378.51,182.72) -- (367.69,182.72) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (364.22,179.37) -- (367.69,179.37) -- (367.69,182.72) -- (364.22,182.72) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (369.69,181.2) -- (374.68,181.38) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (303.1,176.94) -- (316.6,176.94) -- (316.6,182.11) -- (303.1,182.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 230; green, 53; blue, 210 }  ,fill opacity=1 ] (316.6,176.94) -- (316.6,182.11) -- (303.1,182.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (307.8,176.64) -- (308.6,178.83) -- (311.47,178.76) -- (309.1,180.04) -- (310.07,182.19) -- (307.8,180.79) -- (305.53,182.19) -- (306.5,180.04) -- (304.13,178.76) -- (307,178.83) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.23 ] (340.26,72.33) .. controls (348.82,76.94) and (356.01,87.84) .. (355.64,112.47) .. controls (357.82,121.49) and (364.52,147.14) .. (375.17,156.57) .. controls (370,166.3) and (363.92,166.91) .. (369.94,196.71) .. controls (367.63,194.5) and (360.78,206.25) .. (357.83,199.14) .. controls (356.92,197.67) and (356.01,191.54) .. (351.45,184.85) .. controls (350.97,182.56) and (347.35,187.12) .. (346.89,184.54) .. controls (344.76,165.39) and (344.45,140.15) .. (344.45,129.81) .. controls (349.93,105.17) and (348.1,88.45) .. (340.26,72.33) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (338.43,216.59) -- (336.15,225.26) -- (324.87,225.26) -- (322.59,216.59) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (360.33,216.59) -- (358.05,225.26) -- (346.76,225.26) -- (344.48,216.59) -- cycle ;
            	\draw    (328.28,112.17) .. controls (341.21,110.04) and (340.84,109.68) .. (353.52,112.17) ;
            	\draw    (327.91,138.08) .. controls (340.84,135.95) and (340.48,135.58) .. (353.15,138.08) ;
            	\draw    (327.58,163.41) .. controls (340.51,161.28) and (340.14,160.92) .. (352.82,163.41) ;
            	\draw    (353.52,112.17) -- (353.52,183.33) ;
            	\draw    (328.28,112.17) -- (328.28,183.63) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (270.55,243.2) .. controls (276.96,243.2) and (282.4,247.38) .. (284.29,253.16) .. controls (286,252.46) and (287.87,252.07) .. (289.83,252.07) .. controls (297.81,252.07) and (304.29,258.54) .. (304.29,266.53) .. controls (304.29,274.51) and (297.81,280.99) .. (289.83,280.99) .. controls (284.4,280.99) and (279.67,277.99) .. (277.2,273.57) .. controls (276.72,283.24) and (268.73,290.93) .. (258.94,290.93) .. controls (248.85,290.93) and (240.67,282.75) .. (240.67,272.66) .. controls (240.67,263.42) and (247.52,255.78) .. (256.42,254.55) .. controls (257.84,248.06) and (263.63,243.2) .. (270.55,243.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (270.81,246.44) .. controls (276.36,246.44) and (281.06,250.05) .. (282.69,255.05) .. controls (284.16,254.44) and (285.78,254.1) .. (287.47,254.1) .. controls (294.37,254.1) and (299.97,259.7) .. (299.97,266.6) .. controls (299.97,273.5) and (294.37,279.1) .. (287.47,279.1) .. controls (282.78,279.1) and (278.69,276.51) .. (276.56,272.69) .. controls (276.14,281.04) and (269.24,287.69) .. (260.78,287.69) .. controls (252.06,287.69) and (244.99,280.62) .. (244.99,271.9) .. controls (244.99,263.91) and (250.91,257.31) .. (258.6,256.25) .. controls (259.83,250.64) and (264.83,246.44) .. (270.81,246.44) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (273.31,250.1) .. controls (278.38,250.1) and (282.68,253.4) .. (284.17,257.97) .. controls (285.52,257.41) and (286.99,257.1) .. (288.54,257.1) .. controls (294.85,257.1) and (299.97,262.22) .. (299.97,268.53) .. controls (299.97,274.84) and (294.85,279.95) .. (288.54,279.95) .. controls (284.25,279.95) and (280.51,277.59) .. (278.56,274.1) .. controls (278.19,281.74) and (271.87,287.82) .. (264.14,287.82) .. controls (256.16,287.82) and (249.7,281.35) .. (249.7,273.37) .. controls (249.7,266.07) and (255.11,260.04) .. (262.15,259.07) .. controls (263.27,253.94) and (267.84,250.1) .. (273.31,250.1) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (416.59,244.2) .. controls (409.88,244.2) and (404.19,248.38) .. (402.21,254.16) .. controls (400.42,253.46) and (398.47,253.07) .. (396.42,253.07) .. controls (388.06,253.07) and (381.29,259.54) .. (381.29,267.53) .. controls (381.29,275.51) and (388.06,281.99) .. (396.42,281.99) .. controls (402.1,281.99) and (407.05,278.99) .. (409.64,274.57) .. controls (410.13,284.24) and (418.5,291.93) .. (428.74,291.93) .. controls (439.3,291.93) and (447.87,283.75) .. (447.87,273.66) .. controls (447.87,264.42) and (440.69,256.78) .. (431.38,255.55) .. controls (429.89,249.06) and (423.84,244.2) .. (416.59,244.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (416.32,247.44) .. controls (410.52,247.44) and (405.6,251.05) .. (403.89,256.05) .. controls (402.34,255.44) and (400.65,255.1) .. (398.88,255.1) .. controls (391.66,255.1) and (385.8,260.7) .. (385.8,267.6) .. controls (385.8,274.5) and (391.66,280.1) .. (398.88,280.1) .. controls (403.79,280.1) and (408.07,277.51) .. (410.31,273.69) .. controls (410.74,282.04) and (417.96,288.69) .. (426.82,288.69) .. controls (435.95,288.69) and (443.35,281.62) .. (443.35,272.9) .. controls (443.35,264.91) and (437.15,258.31) .. (429.1,257.25) .. controls (427.81,251.64) and (422.58,247.44) .. (416.32,247.44) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (413.71,251.1) .. controls (408.4,251.1) and (403.9,254.4) .. (402.34,258.97) .. controls (400.93,258.41) and (399.38,258.1) .. (397.76,258.1) .. controls (391.16,258.1) and (385.8,263.22) .. (385.8,269.53) .. controls (385.8,275.84) and (391.16,280.95) .. (397.76,280.95) .. controls (402.25,280.95) and (406.16,278.59) .. (408.21,275.1) .. controls (408.6,282.74) and (415.21,288.82) .. (423.3,288.82) .. controls (431.65,288.82) and (438.42,282.35) .. (438.42,274.37) .. controls (438.42,267.07) and (432.75,261.04) .. (425.39,260.07) .. controls (424.21,254.94) and (419.43,251.1) .. (413.71,251.1) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (346.94,259.98) .. controls (351.89,261.37) and (355.2,265.72) .. (355.42,270.51) .. controls (356.89,270.34) and (358.41,270.45) .. (359.92,270.88) .. controls (366.08,272.61) and (369.69,278.91) .. (367.99,284.96) .. controls (366.29,291) and (359.92,294.5) .. (353.76,292.77) .. controls (349.58,291.6) and (346.57,288.31) .. (345.6,284.42) .. controls (343.18,291.64) and (335.38,295.73) .. (327.83,293.61) .. controls (320.05,291.42) and (315.48,283.46) .. (317.63,275.81) .. controls (319.6,268.82) and (326.51,264.52) .. (333.64,265.52) .. controls (336.11,260.91) and (341.61,258.48) .. (346.94,259.98) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (346.46,262.49) .. controls (350.73,263.69) and (353.59,267.45) .. (353.78,271.59) .. controls (355.05,271.44) and (356.36,271.54) .. (357.67,271.91) .. controls (362.99,273.4) and (366.11,278.85) .. (364.65,284.08) .. controls (363.18,289.3) and (357.67,292.33) .. (352.35,290.83) .. controls (348.73,289.81) and (346.13,286.97) .. (345.3,283.61) .. controls (343.2,289.85) and (336.46,293.39) .. (329.94,291.56) .. controls (323.22,289.67) and (319.27,282.78) .. (321.12,276.17) .. controls (322.82,270.13) and (328.8,266.41) .. (334.95,267.28) .. controls (337.1,263.29) and (341.84,261.2) .. (346.46,262.49) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (347.6,265.8) .. controls (351.51,266.9) and (354.12,270.33) .. (354.3,274.12) .. controls (355.46,273.99) and (356.66,274.07) .. (357.86,274.41) .. controls (362.72,275.78) and (365.58,280.76) .. (364.23,285.54) .. controls (362.89,290.32) and (357.86,293.08) .. (352.99,291.71) .. controls (349.69,290.78) and (347.31,288.18) .. (346.55,285.11) .. controls (344.63,290.82) and (338.47,294.05) .. (332.5,292.38) .. controls (326.35,290.65) and (322.75,284.35) .. (324.44,278.31) .. controls (326,272.78) and (331.46,269.39) .. (337.09,270.18) .. controls (339.05,266.54) and (343.39,264.62) .. (347.6,265.8) -- cycle ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Vận tốc của một tàu con thoi từ lúc cất cánh tại thời điểm $t=0$ (s) cho đến thời điểm $t=126$ (s) được cho bởi công thức $v(t) = %st^3 - %st^2 + %s$ (vận tốc được tính bằng đơn vị ft/s). Hỏi tại thời điểm tàu con thoi đạt gia tốc nhỏ nhất thì vận tốc tàu con thoi gần bằng bao nhiêu ft/s? (Kết quả làm tròn đến hàng phần mười).}{%s}'''
                                 %(a_str, b_str, c_str, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gia tốc của tàu con thoi là $a(t) = v'(t) = 3 \\cdot %s t^2 - 2 \\cdot %s t = 0,003906t^2 - 0,18058t$.\\\\
                             Đây là một hàm số bậc hai biến $t$, có đồ thị là một parabol bề lõm hướng lên trên, nên nó đạt giá trị nhỏ nhất tại đỉnh.\\\\
                             Hoành độ đỉnh là $t = \\frac{0,18058}{2 \\cdot 0,003906} \\approx 23,115$ (s) (thuộc đoạn $[0; 126]$).\\\\
                             Tại thời điểm $t \\approx 23,115$ (s), tàu con thoi đạt gia tốc nhỏ nhất.\\\\
                             Vận tốc của tàu con thoi tại thời điểm đó là:\\\\
                             $v(23,115) = %s \\cdot (23,115)^3 - %s \\cdot (23,115)^2 + %s \\approx %s$ (ft/s).'''
                             %(a_str, b_str, 
                               a_str, b_str, c_str, kq_str))
            dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content  

