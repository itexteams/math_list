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


def bt_dang15_p3_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các khoảng cách (a < b)
                a = random.randint(2, 6)      # AM
                b = random.randint(a + 2, 12) # BN
                c = random.randint(10, 25)    # MN

                # Tính AB^2 = MN^2 + (BN - AM)^2
                KB = b - a
                AB_sq = c**2 + KB**2
                AB_val = sp.sqrt(AB_sq)
                AB_tex = sp.latex(AB_val)

                # Tính T_min = A'B = sqrt(MN^2 + (AM + BN)^2)
                HB = a + b
                T_sq = c**2 + HB**2
                T_val = math.sqrt(T_sq)

                # Làm tròn đến hàng phần chục theo yêu cầu đề
                kq_dec = Decimal(float(T_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các đáp án sai (nhiễu) dựa trên sai lầm thường gặp
                s = [
                    '$%s$' % (str(Decimal(float(T_val + 1.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$' % (str(Decimal(float(T_val - 1.5)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$' % (str(Decimal(float(math.sqrt(c**2 + KB**2))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')), # Quên cộng AM mà lại trừ
                    '$%s$' % (str(Decimal(float(math.sqrt((c+2)**2 + HB**2))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$' % (str(Decimal(float(T_val + 0.5)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$' % (str(Decimal(float(T_val - 0.4)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Thành phố Hải Đông dự định xây dựng một trạm nước sạch để cung cấp cho hai khu dân cư $A$ và $B$. Trạm nước sạch đặt tại vị trí $C$ trên bờ sông. Biết $AB = %s \\text{ km}$, khoảng cách từ $A$ và $B$ đến bờ sông lần lượt là $AM = %s \\text{ km}, BN = %s \\text{ km}$ (hình vẽ). Gọi $T$ là tổng độ dài đường ống từ trạm nước đến $A$ và $B$. 
                                 \\begin{center}
                                 	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 137; green, 195; blue, 235 }  ,fill opacity=1 ] (82.5,172.4) -- (425,172.4) -- (425,216.4) -- (82.5,216.4) -- cycle ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (82.5,169.4) -- (425,169.4) -- (425,172.8) -- (82.5,172.8) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (83,177.4) .. controls (84.67,175.73) and (86.33,175.73) .. (88,177.4) .. controls (89.67,179.07) and (91.33,179.07) .. (93,177.4) .. controls (94.67,175.73) and (96.33,175.73) .. (98,177.4) .. controls (99.67,179.07) and (101.33,179.07) .. (103,177.4) .. controls (104.67,175.73) and (106.33,175.73) .. (108,177.4) .. controls (109.67,179.07) and (111.33,179.07) .. (113,177.4) .. controls (114.67,175.73) and (116.33,175.73) .. (118,177.4) .. controls (119.67,179.07) and (121.33,179.07) .. (123,177.4) .. controls (124.67,175.73) and (126.33,175.73) .. (128,177.4) .. controls (129.67,179.07) and (131.33,179.07) .. (133,177.4) .. controls (134.67,175.73) and (136.33,175.73) .. (138,177.4) .. controls (139.67,179.07) and (141.33,179.07) .. (143,177.4) .. controls (144.67,175.73) and (146.33,175.73) .. (148,177.4) .. controls (149.67,179.07) and (151.33,179.07) .. (153,177.4) .. controls (154.67,175.73) and (156.33,175.73) .. (158,177.4) .. controls (159.67,179.07) and (161.33,179.07) .. (163,177.4) .. controls (164.67,175.73) and (166.33,175.73) .. (168,177.4) .. controls (169.67,179.07) and (171.33,179.07) .. (173,177.4) .. controls (174.67,175.73) and (176.33,175.73) .. (178,177.4) .. controls (179.67,179.07) and (181.33,179.07) .. (183,177.4) .. controls (184.67,175.73) and (186.33,175.73) .. (188,177.4) .. controls (189.67,179.07) and (191.33,179.07) .. (193,177.4) .. controls (194.67,175.73) and (196.33,175.73) .. (198,177.4) .. controls (199.67,179.07) and (201.33,179.07) .. (203,177.4) .. controls (204.67,175.73) and (206.33,175.73) .. (208,177.4) .. controls (209.67,179.07) and (211.33,179.07) .. (213,177.4) .. controls (214.67,175.73) and (216.33,175.73) .. (218,177.4) .. controls (219.67,179.07) and (221.33,179.07) .. (223,177.4) .. controls (224.67,175.73) and (226.33,175.73) .. (228,177.4) .. controls (229.67,179.07) and (231.33,179.07) .. (233,177.4) .. controls (234.67,175.73) and (236.33,175.73) .. (238,177.4) .. controls (239.67,179.07) and (241.33,179.07) .. (243,177.4) .. controls (244.67,175.73) and (246.33,175.73) .. (248,177.4) .. controls (249.67,179.07) and (251.33,179.07) .. (253,177.4) .. controls (254.67,175.73) and (256.33,175.73) .. (258,177.4) .. controls (259.67,179.07) and (261.33,179.07) .. (263,177.4) .. controls (264.67,175.73) and (266.33,175.73) .. (268,177.4) .. controls (269.67,179.07) and (271.33,179.07) .. (273,177.4) .. controls (274.67,175.73) and (276.33,175.73) .. (278,177.4) .. controls (279.67,179.07) and (281.33,179.07) .. (283,177.4) .. controls (284.67,175.73) and (286.33,175.73) .. (288,177.4) .. controls (289.67,179.07) and (291.33,179.07) .. (293,177.4) .. controls (294.67,175.73) and (296.33,175.73) .. (298,177.4) .. controls (299.67,179.07) and (301.33,179.07) .. (303,177.4) .. controls (304.67,175.73) and (306.33,175.73) .. (308,177.4) .. controls (309.67,179.07) and (311.33,179.07) .. (313,177.4) .. controls (314.67,175.73) and (316.33,175.73) .. (318,177.4) .. controls (319.67,179.07) and (321.33,179.07) .. (323,177.4) .. controls (324.67,175.73) and (326.33,175.73) .. (328,177.4) .. controls (329.67,179.07) and (331.33,179.07) .. (333,177.4) .. controls (334.67,175.73) and (336.33,175.73) .. (338,177.4) .. controls (339.67,179.07) and (341.33,179.07) .. (343,177.4) .. controls (344.67,175.73) and (346.33,175.73) .. (348,177.4) .. controls (349.67,179.07) and (351.33,179.07) .. (353,177.4) .. controls (354.67,175.73) and (356.33,175.73) .. (358,177.4) .. controls (359.67,179.07) and (361.33,179.07) .. (363,177.4) .. controls (364.67,175.73) and (366.33,175.73) .. (368,177.4) .. controls (369.67,179.07) and (371.33,179.07) .. (373,177.4) .. controls (374.67,175.73) and (376.33,175.73) .. (378,177.4) .. controls (379.67,179.07) and (381.33,179.07) .. (383,177.4) .. controls (384.67,175.73) and (386.33,175.73) .. (388,177.4) .. controls (389.67,179.07) and (391.33,179.07) .. (393,177.4) .. controls (394.67,175.73) and (396.33,175.73) .. (398,177.4) .. controls (399.67,179.07) and (401.33,179.07) .. (403,177.4) .. controls (404.67,175.73) and (406.33,175.73) .. (408,177.4) .. controls (409.67,179.07) and (411.33,179.07) .. (413,177.4) .. controls (414.67,175.73) and (416.33,175.73) .. (418,177.4) .. controls (419.67,179.07) and (421.33,179.07) .. (423,177.4) -- (425.5,177.4) -- (425.5,177.4) ;
                                 		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (84,182.4) .. controls (85.67,180.74) and (87.33,180.74) .. (89,182.41) .. controls (90.67,184.08) and (92.33,184.08) .. (94,182.41) .. controls (95.67,180.75) and (97.33,180.75) .. (99,182.42) .. controls (100.67,184.09) and (102.33,184.09) .. (104,182.43) .. controls (105.67,180.77) and (107.33,180.77) .. (109,182.44) .. controls (110.67,184.11) and (112.33,184.11) .. (114,182.44) .. controls (115.67,180.78) and (117.33,180.78) .. (119,182.45) .. controls (120.67,184.12) and (122.33,184.12) .. (124,182.46) .. controls (125.67,180.8) and (127.33,180.8) .. (129,182.47) .. controls (130.67,184.14) and (132.33,184.14) .. (134,182.47) .. controls (135.67,180.81) and (137.33,180.81) .. (139,182.48) .. controls (140.67,184.15) and (142.33,184.15) .. (144,182.49) .. controls (145.67,180.83) and (147.33,180.83) .. (149,182.5) .. controls (150.67,184.17) and (152.33,184.17) .. (154,182.5) .. controls (155.67,180.84) and (157.33,180.84) .. (159,182.51) .. controls (160.67,184.18) and (162.33,184.18) .. (164,182.52) .. controls (165.67,180.85) and (167.33,180.85) .. (169,182.52) .. controls (170.67,184.19) and (172.33,184.19) .. (174,182.53) .. controls (175.67,180.87) and (177.33,180.87) .. (179,182.54) .. controls (180.67,184.21) and (182.33,184.21) .. (184,182.55) .. controls (185.67,180.88) and (187.33,180.88) .. (189,182.55) .. controls (190.67,184.22) and (192.33,184.22) .. (194,182.56) .. controls (195.67,180.9) and (197.33,180.9) .. (199,182.57) .. controls (200.67,184.24) and (202.33,184.24) .. (204,182.58) .. controls (205.67,180.91) and (207.33,180.91) .. (209,182.58) .. controls (210.67,184.25) and (212.33,184.25) .. (214,182.59) .. controls (215.67,180.93) and (217.33,180.93) .. (219,182.6) .. controls (220.67,184.27) and (222.33,184.27) .. (224,182.61) .. controls (225.67,180.94) and (227.33,180.94) .. (229,182.61) .. controls (230.67,184.28) and (232.33,184.28) .. (234,182.62) .. controls (235.67,180.96) and (237.33,180.96) .. (239,182.63) .. controls (240.67,184.3) and (242.33,184.3) .. (244,182.63) .. controls (245.67,180.97) and (247.33,180.97) .. (249,182.64) .. controls (250.67,184.31) and (252.33,184.31) .. (254,182.65) .. controls (255.67,180.99) and (257.33,180.99) .. (259,182.66) .. controls (260.67,184.33) and (262.33,184.33) .. (264,182.66) .. controls (265.67,181) and (267.33,181) .. (269,182.67) .. controls (270.67,184.34) and (272.33,184.34) .. (274,182.68) .. controls (275.67,181.02) and (277.33,181.02) .. (279,182.69) .. controls (280.67,184.36) and (282.33,184.36) .. (284,182.69) .. controls (285.67,181.03) and (287.33,181.03) .. (289,182.7) .. controls (290.67,184.37) and (292.33,184.37) .. (294,182.71) .. controls (295.67,181.05) and (297.33,181.05) .. (299,182.72) .. controls (300.67,184.39) and (302.33,184.39) .. (304,182.72) .. controls (305.67,181.06) and (307.33,181.06) .. (309,182.73) .. controls (310.67,184.4) and (312.33,184.4) .. (314,182.74) .. controls (315.67,181.07) and (317.33,181.07) .. (319,182.74) .. controls (320.67,184.41) and (322.33,184.41) .. (324,182.75) .. controls (325.67,181.09) and (327.33,181.09) .. (329,182.76) .. controls (330.67,184.43) and (332.33,184.43) .. (334,182.77) .. controls (335.67,181.1) and (337.33,181.1) .. (339,182.77) .. controls (340.67,184.44) and (342.33,184.44) .. (344,182.78) .. controls (345.67,181.12) and (347.33,181.12) .. (349,182.79) .. controls (350.67,184.46) and (352.33,184.46) .. (354,182.8) .. controls (355.67,181.13) and (357.33,181.13) .. (359,182.8) .. controls (360.67,184.47) and (362.33,184.47) .. (364,182.81) .. controls (365.67,181.15) and (367.33,181.15) .. (369,182.82) .. controls (370.67,184.49) and (372.33,184.49) .. (374,182.83) .. controls (375.67,181.16) and (377.33,181.16) .. (379,182.83) .. controls (380.67,184.5) and (382.33,184.5) .. (384,182.84) .. controls (385.67,181.18) and (387.33,181.18) .. (389,182.85) .. controls (390.67,184.52) and (392.33,184.52) .. (394,182.85) .. controls (395.67,181.19) and (397.33,181.19) .. (399,182.86) .. controls (400.67,184.53) and (402.33,184.53) .. (404,182.87) .. controls (405.67,181.21) and (407.33,181.21) .. (409,182.88) .. controls (410.67,184.55) and (412.33,184.55) .. (414,182.88) .. controls (415.67,181.22) and (417.33,181.22) .. (419,182.89) .. controls (420.67,184.56) and (422.33,184.56) .. (424,182.9) -- (425,182.9) -- (425,182.9) ;
                                 		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (84.5,187.73) .. controls (86.17,186.06) and (87.83,186.06) .. (89.5,187.73) .. controls (91.17,189.4) and (92.83,189.4) .. (94.5,187.73) .. controls (96.17,186.06) and (97.83,186.06) .. (99.5,187.73) .. controls (101.17,189.4) and (102.83,189.4) .. (104.5,187.73) .. controls (106.17,186.06) and (107.83,186.06) .. (109.5,187.73) .. controls (111.17,189.4) and (112.83,189.4) .. (114.5,187.73) .. controls (116.17,186.06) and (117.83,186.06) .. (119.5,187.73) .. controls (121.17,189.4) and (122.83,189.4) .. (124.5,187.73) .. controls (126.17,186.06) and (127.83,186.06) .. (129.5,187.73) .. controls (131.17,189.4) and (132.83,189.4) .. (134.5,187.73) .. controls (136.17,186.06) and (137.83,186.06) .. (139.5,187.73) .. controls (141.17,189.4) and (142.83,189.4) .. (144.5,187.73) .. controls (146.17,186.06) and (147.83,186.06) .. (149.5,187.73) .. controls (151.17,189.4) and (152.83,189.4) .. (154.5,187.73) .. controls (156.17,186.06) and (157.83,186.06) .. (159.5,187.73) .. controls (161.17,189.4) and (162.83,189.4) .. (164.5,187.73) .. controls (166.17,186.06) and (167.83,186.06) .. (169.5,187.73) .. controls (171.17,189.4) and (172.83,189.4) .. (174.5,187.73) .. controls (176.17,186.06) and (177.83,186.06) .. (179.5,187.73) .. controls (181.17,189.4) and (182.83,189.4) .. (184.5,187.73) .. controls (186.17,186.06) and (187.83,186.06) .. (189.5,187.73) .. controls (191.17,189.4) and (192.83,189.4) .. (194.5,187.73) .. controls (196.17,186.06) and (197.83,186.06) .. (199.5,187.73) .. controls (201.17,189.4) and (202.83,189.4) .. (204.5,187.73) .. controls (206.17,186.06) and (207.83,186.06) .. (209.5,187.73) .. controls (211.17,189.4) and (212.83,189.4) .. (214.5,187.73) .. controls (216.17,186.06) and (217.83,186.06) .. (219.5,187.73) .. controls (221.17,189.4) and (222.83,189.4) .. (224.5,187.73) .. controls (226.17,186.06) and (227.83,186.06) .. (229.5,187.73) .. controls (231.17,189.4) and (232.83,189.4) .. (234.5,187.73) .. controls (236.17,186.06) and (237.83,186.06) .. (239.5,187.73) .. controls (241.17,189.4) and (242.83,189.4) .. (244.5,187.73) .. controls (246.17,186.06) and (247.83,186.06) .. (249.5,187.73) .. controls (251.17,189.4) and (252.83,189.4) .. (254.5,187.73) .. controls (256.17,186.06) and (257.83,186.06) .. (259.5,187.73) .. controls (261.17,189.4) and (262.83,189.4) .. (264.5,187.73) .. controls (266.17,186.06) and (267.83,186.06) .. (269.5,187.73) .. controls (271.17,189.4) and (272.83,189.4) .. (274.5,187.73) .. controls (276.17,186.06) and (277.83,186.06) .. (279.5,187.73) .. controls (281.17,189.4) and (282.83,189.4) .. (284.5,187.73) .. controls (286.17,186.06) and (287.83,186.06) .. (289.5,187.73) .. controls (291.17,189.4) and (292.83,189.4) .. (294.5,187.73) .. controls (296.17,186.06) and (297.83,186.06) .. (299.5,187.73) .. controls (301.17,189.4) and (302.83,189.4) .. (304.5,187.73) .. controls (306.17,186.06) and (307.83,186.06) .. (309.5,187.73) .. controls (311.17,189.4) and (312.83,189.4) .. (314.5,187.73) .. controls (316.17,186.06) and (317.83,186.06) .. (319.5,187.73) .. controls (321.17,189.4) and (322.83,189.4) .. (324.5,187.73) .. controls (326.17,186.06) and (327.83,186.06) .. (329.5,187.73) .. controls (331.17,189.4) and (332.83,189.4) .. (334.5,187.73) .. controls (336.17,186.06) and (337.83,186.06) .. (339.5,187.73) .. controls (341.17,189.4) and (342.83,189.4) .. (344.5,187.73) .. controls (346.17,186.06) and (347.83,186.06) .. (349.5,187.73) .. controls (351.17,189.4) and (352.83,189.4) .. (354.5,187.73) .. controls (356.17,186.06) and (357.83,186.06) .. (359.5,187.73) .. controls (361.17,189.4) and (362.83,189.4) .. (364.5,187.73) .. controls (366.17,186.06) and (367.83,186.06) .. (369.5,187.73) .. controls (371.17,189.4) and (372.83,189.4) .. (374.5,187.73) .. controls (376.17,186.06) and (377.83,186.06) .. (379.5,187.73) .. controls (381.17,189.4) and (382.83,189.4) .. (384.5,187.73) .. controls (386.17,186.06) and (387.83,186.06) .. (389.5,187.73) .. controls (391.17,189.4) and (392.83,189.4) .. (394.5,187.73) .. controls (396.17,186.06) and (397.83,186.06) .. (399.5,187.73) .. controls (401.17,189.4) and (402.83,189.4) .. (404.5,187.73) .. controls (406.17,186.06) and (407.83,186.06) .. (409.5,187.73) .. controls (411.17,189.4) and (412.83,189.4) .. (414.5,187.73) .. controls (416.17,186.06) and (417.83,186.06) .. (419.5,187.73) .. controls (421.17,189.4) and (422.83,189.4) .. (424.5,187.73) -- (427,187.73) -- (427,187.73) ;
                                 		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (82,201.9) .. controls (83.67,200.23) and (85.33,200.23) .. (87,201.9) .. controls (88.67,203.57) and (90.33,203.57) .. (92,201.9) .. controls (93.67,200.23) and (95.33,200.23) .. (97,201.9) .. controls (98.67,203.57) and (100.33,203.57) .. (102,201.9) .. controls (103.67,200.23) and (105.33,200.23) .. (107,201.9) .. controls (108.67,203.57) and (110.33,203.57) .. (112,201.9) .. controls (113.67,200.23) and (115.33,200.23) .. (117,201.9) .. controls (118.67,203.57) and (120.33,203.57) .. (122,201.9) .. controls (123.67,200.23) and (125.33,200.23) .. (127,201.9) .. controls (128.67,203.57) and (130.33,203.57) .. (132,201.9) .. controls (133.67,200.23) and (135.33,200.23) .. (137,201.9) .. controls (138.67,203.57) and (140.33,203.57) .. (142,201.9) .. controls (143.67,200.23) and (145.33,200.23) .. (147,201.9) .. controls (148.67,203.57) and (150.33,203.57) .. (152,201.9) .. controls (153.67,200.23) and (155.33,200.23) .. (157,201.9) .. controls (158.67,203.57) and (160.33,203.57) .. (162,201.9) .. controls (163.67,200.23) and (165.33,200.23) .. (167,201.9) .. controls (168.67,203.57) and (170.33,203.57) .. (172,201.9) .. controls (173.67,200.23) and (175.33,200.23) .. (177,201.9) .. controls (178.67,203.57) and (180.33,203.57) .. (182,201.9) .. controls (183.67,200.23) and (185.33,200.23) .. (187,201.9) .. controls (188.67,203.57) and (190.33,203.57) .. (192,201.9) .. controls (193.67,200.23) and (195.33,200.23) .. (197,201.9) .. controls (198.67,203.57) and (200.33,203.57) .. (202,201.9) .. controls (203.67,200.23) and (205.33,200.23) .. (207,201.9) .. controls (208.67,203.57) and (210.33,203.57) .. (212,201.9) .. controls (213.67,200.23) and (215.33,200.23) .. (217,201.9) .. controls (218.67,203.57) and (220.33,203.57) .. (222,201.9) .. controls (223.67,200.23) and (225.33,200.23) .. (227,201.9) .. controls (228.67,203.57) and (230.33,203.57) .. (232,201.9) .. controls (233.67,200.23) and (235.33,200.23) .. (237,201.9) .. controls (238.67,203.57) and (240.33,203.57) .. (242,201.9) .. controls (243.67,200.23) and (245.33,200.23) .. (247,201.9) .. controls (248.67,203.57) and (250.33,203.57) .. (252,201.9) .. controls (253.67,200.23) and (255.33,200.23) .. (257,201.9) .. controls (258.67,203.57) and (260.33,203.57) .. (262,201.9) .. controls (263.67,200.23) and (265.33,200.23) .. (267,201.9) .. controls (268.67,203.57) and (270.33,203.57) .. (272,201.9) .. controls (273.67,200.23) and (275.33,200.23) .. (277,201.9) .. controls (278.67,203.57) and (280.33,203.57) .. (282,201.9) .. controls (283.67,200.23) and (285.33,200.23) .. (287,201.9) .. controls (288.67,203.57) and (290.33,203.57) .. (292,201.9) .. controls (293.67,200.23) and (295.33,200.23) .. (297,201.9) .. controls (298.67,203.57) and (300.33,203.57) .. (302,201.9) .. controls (303.67,200.23) and (305.33,200.23) .. (307,201.9) .. controls (308.67,203.57) and (310.33,203.57) .. (312,201.9) .. controls (313.67,200.23) and (315.33,200.23) .. (317,201.9) .. controls (318.67,203.57) and (320.33,203.57) .. (322,201.9) .. controls (323.67,200.23) and (325.33,200.23) .. (327,201.9) .. controls (328.67,203.57) and (330.33,203.57) .. (332,201.9) .. controls (333.67,200.23) and (335.33,200.23) .. (337,201.9) .. controls (338.67,203.57) and (340.33,203.57) .. (342,201.9) .. controls (343.67,200.23) and (345.33,200.23) .. (347,201.9) .. controls (348.67,203.57) and (350.33,203.57) .. (352,201.9) .. controls (353.67,200.23) and (355.33,200.23) .. (357,201.9) .. controls (358.67,203.57) and (360.33,203.57) .. (362,201.9) .. controls (363.67,200.23) and (365.33,200.23) .. (367,201.9) .. controls (368.67,203.57) and (370.33,203.57) .. (372,201.9) .. controls (373.67,200.23) and (375.33,200.23) .. (377,201.9) .. controls (378.67,203.57) and (380.33,203.57) .. (382,201.9) .. controls (383.67,200.23) and (385.33,200.23) .. (387,201.9) .. controls (388.67,203.57) and (390.33,203.57) .. (392,201.9) .. controls (393.67,200.23) and (395.33,200.23) .. (397,201.9) .. controls (398.67,203.57) and (400.33,203.57) .. (402,201.9) .. controls (403.67,200.23) and (405.33,200.23) .. (407,201.9) .. controls (408.67,203.57) and (410.33,203.57) .. (412,201.9) .. controls (413.67,200.23) and (415.33,200.23) .. (417,201.9) .. controls (418.67,203.57) and (420.33,203.57) .. (422,201.9) -- (424.5,201.9) -- (424.5,201.9) ;
                                 		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (82.5,208.4) .. controls (84.17,206.74) and (85.83,206.74) .. (87.5,208.41) .. controls (89.17,210.08) and (90.83,210.08) .. (92.5,208.41) .. controls (94.17,206.75) and (95.83,206.75) .. (97.5,208.42) .. controls (99.17,210.09) and (100.83,210.09) .. (102.5,208.43) .. controls (104.17,206.77) and (105.83,206.77) .. (107.5,208.44) .. controls (109.17,210.11) and (110.83,210.11) .. (112.5,208.44) .. controls (114.17,206.78) and (115.83,206.78) .. (117.5,208.45) .. controls (119.17,210.12) and (120.83,210.12) .. (122.5,208.46) .. controls (124.17,206.8) and (125.83,206.8) .. (127.5,208.47) .. controls (129.17,210.14) and (130.83,210.14) .. (132.5,208.47) .. controls (134.17,206.81) and (135.83,206.81) .. (137.5,208.48) .. controls (139.17,210.15) and (140.83,210.15) .. (142.5,208.49) .. controls (144.17,206.83) and (145.83,206.83) .. (147.5,208.5) .. controls (149.17,210.17) and (150.83,210.17) .. (152.5,208.5) .. controls (154.17,206.84) and (155.83,206.84) .. (157.5,208.51) .. controls (159.17,210.18) and (160.83,210.18) .. (162.5,208.52) .. controls (164.17,206.85) and (165.83,206.85) .. (167.5,208.52) .. controls (169.17,210.19) and (170.83,210.19) .. (172.5,208.53) .. controls (174.17,206.87) and (175.83,206.87) .. (177.5,208.54) .. controls (179.17,210.21) and (180.83,210.21) .. (182.5,208.55) .. controls (184.17,206.88) and (185.83,206.88) .. (187.5,208.55) .. controls (189.17,210.22) and (190.83,210.22) .. (192.5,208.56) .. controls (194.17,206.9) and (195.83,206.9) .. (197.5,208.57) .. controls (199.17,210.24) and (200.83,210.24) .. (202.5,208.58) .. controls (204.17,206.91) and (205.83,206.91) .. (207.5,208.58) .. controls (209.17,210.25) and (210.83,210.25) .. (212.5,208.59) .. controls (214.17,206.93) and (215.83,206.93) .. (217.5,208.6) .. controls (219.17,210.27) and (220.83,210.27) .. (222.5,208.61) .. controls (224.17,206.94) and (225.83,206.94) .. (227.5,208.61) .. controls (229.17,210.28) and (230.83,210.28) .. (232.5,208.62) .. controls (234.17,206.96) and (235.83,206.96) .. (237.5,208.63) .. controls (239.17,210.3) and (240.83,210.3) .. (242.5,208.63) .. controls (244.17,206.97) and (245.83,206.97) .. (247.5,208.64) .. controls (249.17,210.31) and (250.83,210.31) .. (252.5,208.65) .. controls (254.17,206.99) and (255.83,206.99) .. (257.5,208.66) .. controls (259.17,210.33) and (260.83,210.33) .. (262.5,208.66) .. controls (264.17,207) and (265.83,207) .. (267.5,208.67) .. controls (269.17,210.34) and (270.83,210.34) .. (272.5,208.68) .. controls (274.17,207.02) and (275.83,207.02) .. (277.5,208.69) .. controls (279.17,210.36) and (280.83,210.36) .. (282.5,208.69) .. controls (284.17,207.03) and (285.83,207.03) .. (287.5,208.7) .. controls (289.17,210.37) and (290.83,210.37) .. (292.5,208.71) .. controls (294.17,207.05) and (295.83,207.05) .. (297.5,208.72) .. controls (299.17,210.39) and (300.83,210.39) .. (302.5,208.72) .. controls (304.17,207.06) and (305.83,207.06) .. (307.5,208.73) .. controls (309.17,210.4) and (310.83,210.4) .. (312.5,208.74) .. controls (314.17,207.07) and (315.83,207.07) .. (317.5,208.74) .. controls (319.17,210.41) and (320.83,210.41) .. (322.5,208.75) .. controls (324.17,207.09) and (325.83,207.09) .. (327.5,208.76) .. controls (329.17,210.43) and (330.83,210.43) .. (332.5,208.77) .. controls (334.17,207.1) and (335.83,207.1) .. (337.5,208.77) .. controls (339.17,210.44) and (340.83,210.44) .. (342.5,208.78) .. controls (344.17,207.12) and (345.83,207.12) .. (347.5,208.79) .. controls (349.17,210.46) and (350.83,210.46) .. (352.5,208.8) .. controls (354.17,207.13) and (355.83,207.13) .. (357.5,208.8) .. controls (359.17,210.47) and (360.83,210.47) .. (362.5,208.81) .. controls (364.17,207.15) and (365.83,207.15) .. (367.5,208.82) .. controls (369.17,210.49) and (370.83,210.49) .. (372.5,208.83) .. controls (374.17,207.16) and (375.83,207.16) .. (377.5,208.83) .. controls (379.17,210.5) and (380.83,210.5) .. (382.5,208.84) .. controls (384.17,207.18) and (385.83,207.18) .. (387.5,208.85) .. controls (389.17,210.52) and (390.83,210.52) .. (392.5,208.85) .. controls (394.17,207.19) and (395.83,207.19) .. (397.5,208.86) .. controls (399.17,210.53) and (400.83,210.53) .. (402.5,208.87) .. controls (404.17,207.21) and (405.83,207.21) .. (407.5,208.88) .. controls (409.17,210.55) and (410.83,210.55) .. (412.5,208.88) .. controls (414.17,207.22) and (415.83,207.22) .. (417.5,208.89) .. controls (419.17,210.56) and (420.83,210.56) .. (422.5,208.9) -- (423.5,208.9) -- (423.5,208.9) ;
                                 		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (82.5,194.4) .. controls (84.17,192.73) and (85.83,192.73) .. (87.5,194.4) .. controls (89.17,196.07) and (90.83,196.07) .. (92.5,194.4) .. controls (94.17,192.73) and (95.83,192.73) .. (97.5,194.4) .. controls (99.17,196.07) and (100.83,196.07) .. (102.5,194.4) .. controls (104.17,192.73) and (105.83,192.73) .. (107.5,194.4) .. controls (109.17,196.07) and (110.83,196.07) .. (112.5,194.4) .. controls (114.17,192.73) and (115.83,192.73) .. (117.5,194.4) .. controls (119.17,196.07) and (120.83,196.07) .. (122.5,194.4) .. controls (124.17,192.73) and (125.83,192.73) .. (127.5,194.4) .. controls (129.17,196.07) and (130.83,196.07) .. (132.5,194.4) .. controls (134.17,192.73) and (135.83,192.73) .. (137.5,194.4) .. controls (139.17,196.07) and (140.83,196.07) .. (142.5,194.4) .. controls (144.17,192.73) and (145.83,192.73) .. (147.5,194.4) .. controls (149.17,196.07) and (150.83,196.07) .. (152.5,194.4) .. controls (154.17,192.73) and (155.83,192.73) .. (157.5,194.4) .. controls (159.17,196.07) and (160.83,196.07) .. (162.5,194.4) .. controls (164.17,192.73) and (165.83,192.73) .. (167.5,194.4) .. controls (169.17,196.07) and (170.83,196.07) .. (172.5,194.4) .. controls (174.17,192.73) and (175.83,192.73) .. (177.5,194.4) .. controls (179.17,196.07) and (180.83,196.07) .. (182.5,194.4) .. controls (184.17,192.73) and (185.83,192.73) .. (187.5,194.4) .. controls (189.17,196.07) and (190.83,196.07) .. (192.5,194.4) .. controls (194.17,192.73) and (195.83,192.73) .. (197.5,194.4) .. controls (199.17,196.07) and (200.83,196.07) .. (202.5,194.4) .. controls (204.17,192.73) and (205.83,192.73) .. (207.5,194.4) .. controls (209.17,196.07) and (210.83,196.07) .. (212.5,194.4) .. controls (214.17,192.73) and (215.83,192.73) .. (217.5,194.4) .. controls (219.17,196.07) and (220.83,196.07) .. (222.5,194.4) .. controls (224.17,192.73) and (225.83,192.73) .. (227.5,194.4) .. controls (229.17,196.07) and (230.83,196.07) .. (232.5,194.4) .. controls (234.17,192.73) and (235.83,192.73) .. (237.5,194.4) .. controls (239.17,196.07) and (240.83,196.07) .. (242.5,194.4) .. controls (244.17,192.73) and (245.83,192.73) .. (247.5,194.4) .. controls (249.17,196.07) and (250.83,196.07) .. (252.5,194.4) .. controls (254.17,192.73) and (255.83,192.73) .. (257.5,194.4) .. controls (259.17,196.07) and (260.83,196.07) .. (262.5,194.4) .. controls (264.17,192.73) and (265.83,192.73) .. (267.5,194.4) .. controls (269.17,196.07) and (270.83,196.07) .. (272.5,194.4) .. controls (274.17,192.73) and (275.83,192.73) .. (277.5,194.4) .. controls (279.17,196.07) and (280.83,196.07) .. (282.5,194.4) .. controls (284.17,192.73) and (285.83,192.73) .. (287.5,194.4) .. controls (289.17,196.07) and (290.83,196.07) .. (292.5,194.4) .. controls (294.17,192.73) and (295.83,192.73) .. (297.5,194.4) .. controls (299.17,196.07) and (300.83,196.07) .. (302.5,194.4) .. controls (304.17,192.73) and (305.83,192.73) .. (307.5,194.4) .. controls (309.17,196.07) and (310.83,196.07) .. (312.5,194.4) .. controls (314.17,192.73) and (315.83,192.73) .. (317.5,194.4) .. controls (319.17,196.07) and (320.83,196.07) .. (322.5,194.4) .. controls (324.17,192.73) and (325.83,192.73) .. (327.5,194.4) .. controls (329.17,196.07) and (330.83,196.07) .. (332.5,194.4) .. controls (334.17,192.73) and (335.83,192.73) .. (337.5,194.4) .. controls (339.17,196.07) and (340.83,196.07) .. (342.5,194.4) .. controls (344.17,192.73) and (345.83,192.73) .. (347.5,194.4) .. controls (349.17,196.07) and (350.83,196.07) .. (352.5,194.4) .. controls (354.17,192.73) and (355.83,192.73) .. (357.5,194.4) .. controls (359.17,196.07) and (360.83,196.07) .. (362.5,194.4) .. controls (364.17,192.73) and (365.83,192.73) .. (367.5,194.4) .. controls (369.17,196.07) and (370.83,196.07) .. (372.5,194.4) .. controls (374.17,192.73) and (375.83,192.73) .. (377.5,194.4) .. controls (379.17,196.07) and (380.83,196.07) .. (382.5,194.4) .. controls (384.17,192.73) and (385.83,192.73) .. (387.5,194.4) .. controls (389.17,196.07) and (390.83,196.07) .. (392.5,194.4) .. controls (394.17,192.73) and (395.83,192.73) .. (397.5,194.4) .. controls (399.17,196.07) and (400.83,196.07) .. (402.5,194.4) .. controls (404.17,192.73) and (405.83,192.73) .. (407.5,194.4) .. controls (409.17,196.07) and (410.83,196.07) .. (412.5,194.4) .. controls (414.17,192.73) and (415.83,192.73) .. (417.5,194.4) .. controls (419.17,196.07) and (420.83,196.07) .. (422.5,194.4) -- (425,194.4) -- (425,194.4) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (82.5,216.4) -- (425,216.4) -- (425,220.8) -- (82.5,220.8) -- cycle ;
                                 		\\draw [line width=1]    (137.5,102.4) -- (137,169.4) ;
                                 		\\draw [line width=1]    (369,62.9) -- (368.5,169.4) ;
                                 		\\draw [line width=1]    (137.5,102.4) -- (304,169.9) ;
                                 		\\draw [line width=1]    (369,62.9) -- (304,169.9) ;
                                 		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (134.97,102.4) .. controls (134.97,101.01) and (136.11,99.87) .. (137.5,99.87) .. controls (138.89,99.87) and (140.03,101.01) .. (140.03,102.4) .. controls (140.03,103.79) and (138.89,104.92) .. (137.5,104.92) .. controls (136.11,104.92) and (134.97,103.79) .. (134.97,102.4) -- cycle ;
                                 		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (366.35,62.9) .. controls (366.35,61.44) and (367.54,60.25) .. (369,60.25) .. controls (370.46,60.25) and (371.65,61.44) .. (371.65,62.9) .. controls (371.65,64.36) and (370.46,65.55) .. (369,65.55) .. controls (367.54,65.55) and (366.35,64.36) .. (366.35,62.9) -- cycle ;
                                 		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (301.72,167.62) -- (306.28,167.62) -- (306.28,172.17) -- (301.72,172.17) -- cycle ;
                                 		\\draw (126.8,76) node [anchor=north west][inner sep=0.75pt]    {$A$};
                                 		\\draw (361.8,36) node [anchor=north west][inner sep=0.75pt]    {$B$};
                                 		\\draw (291.3,142.5) node [anchor=north west][inner sep=0.75pt]    {$C$};
                                 		\\draw (114.8,149) node [anchor=north west][inner sep=0.75pt]    {$M$};
                                 		\\draw (368.3,148.5) node [anchor=north west][inner sep=0.75pt]    {$N$};
                                 	\\end{tikzpicture}
                                 \\end{center}
                                 Giá trị nhỏ nhất của $T$ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục).'''
                                 % (AB_tex, a, b))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                		\\draw [line width=1]    (115.33,174.34) -- (463.2,176.9) ;
                		\\draw [line width=1]    (178.16,123.49) -- (178,233.11) ;
                		\\draw  [line width=1]  (178.16,116.55) -- (399.55,116.55) -- (399.55,234.77) -- (178.16,234.77) -- cycle ;
                		\\draw [line width=1]    (399.55,116.55) -- (399.55,46.28) ;
                		\\draw [line width=1]    (399.55,46.28) -- (178.16,234.77) ;
                		\\draw [line width=1]    (399.55,46.28) -- (178.16,116.55) ;
                		\\draw (151.39,111) node [anchor=north west][inner sep=0.75pt]    {$A$};
                		\\draw (150.21,179) node [anchor=north west][inner sep=0.75pt]    {$M$};
                		\\draw (152.81,237.32) node [anchor=north west][inner sep=0.75pt]    {$A'$};
                		\\draw (399.15,29) node [anchor=north west][inner sep=0.75pt]    {$B$};
                		\\draw (232.28,152.18) node [anchor=north west][inner sep=0.75pt]    {$C$};
                		\\draw (404.23,106.71) node [anchor=north west][inner sep=0.75pt]    {$K$};
                		\\draw (403.64,150.11) node [anchor=north west][inner sep=0.75pt]    {$N$};
                		\\draw (401.83,237.41) node [anchor=north west][inner sep=0.75pt]    {$H$};
                	\\end{tikzpicture}
                \\end{center} Kẻ $AK \\perp BN$; $A'H \\perp BN$. \\\\
                            Gọi $A'$ đối xứng với $A$ qua $MN$. Ta có $T = CA + CB = CA' + CB \\ge A'B$ (không đổi). \\\\
                            Đẳng thức xảy ra khi $C$ là giao điểm của $MN$ và $A'B$ (tức $C \\equiv MN \\cap A'B$). \\\\
                            Ta có $KB = BN - AM = %s - %s = %s \\text{ km}$. \\\\
                            Độ dài đoạn $MN$ là: $MN = AK = \\sqrt{AB^2 - KB^2} = \\sqrt{(%s)^2 - %s^2} = \\sqrt{%s - %s} = %s \\text{ km}$. \\\\
                            Xét tam giác vuông $A'HB$, ta có $A'H = MN = %s \\text{ km}$, $HB = HN + NB = A'M + BN = %s + %s = %s \\text{ km}$. \\\\
                            Vậy giá trị nhỏ nhất là $A'B = \\sqrt{A'H^2 + HB^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s} \\approx %s \\text{ km}$.'''
                           % (b, a, KB,
                              AB_tex, KB, AB_sq, KB**2, c,
                              c, a, b, HB,
                              c, HB, T_sq, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

