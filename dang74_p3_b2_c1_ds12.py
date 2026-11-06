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


def bt_dang74_p3_b2_c1_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        x = symbols('x')

        # Danh sách các bộ số đảm bảo x0 nguyên, là ước của M và nằm trong [1, M]
        bo_so = [
            (3600, 50, Rational(5, 1000), "0,005"),     # x0 = 100
            (4800, 60, Rational(15, 10000), "0,0015"),  # x0 = 200
            (4000, 40, Rational(1, 1000), "0,001"),     # x0 = 200
            (5400, 90, Rational(1, 1000), "0,001"),     # x0 = 300
            (4500, 45, Rational(5, 10000), "0,0005"),  # x0 = 300
            (2400, 24, Rational(6, 10000), "0,0006"),  # x0 = 200
            (3600, 81, Rational(9, 10000), "0,0009"),  # x0 = 300
            (4800, 48, Rational(3, 10000), "0,0003")   # x0 = 400
        ]

        # Lọc bộ số hợp lệ
        bo_hop_le = []
        for M_val, A_val, B_val, B_str in bo_so:
            val_sq = A_val / B_val
            x0_calc = int(round(math.sqrt(float(val_sq))))
            if x0_calc * x0_calc == val_sq and M_val % x0_calc == 0 and 1 <= x0_calc <= M_val:
                bo_hop_le.append((M_val, A_val, B_val, B_str, x0_calc))

        M_val, A_val, B_val, B_str, x0_val = random.choice(bo_hop_le)

        # Tính các hệ số hàm tổng chi phí: C(x) = (M/x) * (A + B*x^2) = (M*A)/x + (M*B)*x
        c1 = M_val * A_val
        c2 = M_val * B_val
        c2_float = float(c2)
        if c2_float.is_integer():
            c2_str = str(int(c2_float))
        else:
            c2_str = str(c2_float).replace('.', ',')

        # Giá trị chi phí nhỏ nhất tại x0
        c_min = int(c1 / x0_val + c2_float * x0_val)

        # Giá trị tại biên x = 1 và x = M để hoàn thiện dữ liệu
        c_tai_1 = int(c1 + c2_float)
        c_tai_M = int(c1 / M_val + c2_float * M_val)

        kq_str = str(x0_val)

        # Nội dung câu hỏi
        noidungcauhoi = ('''\\immini{Một hợp tác xã cần vận chuyển %s kg sầu riêng trong một mùa vụ. Hợp tác xã chia thành nhiều chuyến, mỗi chuyến chở $x$ kg ($1 \\le x \\le %s, x \\in \\mathbb{N}^*$) giả sử $x$ là ước của %s để khối lượng hàng được chia đều cho các chuyến. Chi phí cho mỗi chuyến gồm: \\\\
    - Phí xe cố định là %s nghìn đồng/chuyến. \\\\
    - Phí bảo quản lạnh được tính $%s x^2$ (nghìn đồng/chuyến). \\\\
    Hỏi mỗi chuyến nên chở bao nhiêu kg để tổng chi phí vận chuyển là nhỏ nhất?}
                         {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.1 ] (216.83,200.92) .. controls (216.83,187.64) and (245.83,176.88) .. (281.61,176.88) .. controls (317.39,176.88) and (346.4,187.64) .. (346.4,200.92) .. controls (346.4,214.2) and (317.39,224.96) .. (281.61,224.96) .. controls (245.83,224.96) and (216.83,214.2) .. (216.83,200.92) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.1 ] (125.11,218) .. controls (125.11,206.95) and (153.8,198) .. (189.2,198) .. controls (224.6,198) and (253.3,206.95) .. (253.3,218) .. controls (253.3,229.05) and (224.6,238) .. (189.2,238) .. controls (153.8,238) and (125.11,229.05) .. (125.11,218) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.4 ][fill={rgb, 255:red, 143; green, 107; blue, 76 }  ,fill opacity=1 ] (189.4,46.6) .. controls (193.4,39.5) and (197.4,44) .. (201.4,44) .. controls (203.4,66.5) and (206.4,66) .. (215.4,75) .. controls (235.4,105) and (221.4,102) .. (201.4,72) .. controls (193.4,60) and (195.4,58.5) .. (189.4,46.6) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 234; green, 202; blue, 151 }  ,fill opacity=1 ] (189.4,45.28) .. controls (189.4,43.77) and (192.2,42.55) .. (195.65,42.55) .. controls (199.1,42.55) and (201.9,43.77) .. (201.9,45.28) .. controls (201.9,46.78) and (199.1,48) .. (195.65,48) .. controls (192.2,48) and (189.4,46.78) .. (189.4,45.28) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 153; green, 191; blue, 33 }  ,fill opacity=1 ] (237.8,62.5) -- (244.8,56) -- (248.8,64.5) -- (256.8,61.5) -- (259.8,72.5) -- (268.8,69) -- (272.8,76.5) -- (278.8,74.5) -- (282.3,82) -- (290.3,82) -- (288.8,91.5) -- (298.3,91.5) -- (299.3,100.5) -- (306.8,100) -- (304.8,106.5) -- (313.3,106.5) -- (310.8,116.5) -- (319.3,119.5) -- (315.8,127.5) -- (323.8,132.5) -- (319.3,142) -- (327.3,143) -- (322.3,153.5) -- (328.8,161) -- (319.3,166.5) -- (324.3,176.5) -- (313.3,180.5) -- (315.8,191) -- (304.8,189) -- (306.6,209.67) -- (293.3,203.5) -- (291.3,214.5) -- (281.3,208) -- (278.8,218) -- (271.8,211.5) -- (268.8,217) -- (263.3,212.5) -- (260.8,218.5) -- (255.3,212) -- (253.3,218) -- (247.9,208.5) -- (242.9,216) -- (240.9,208) -- (234.4,212.5) -- (232.9,202.5) -- (225.4,208.5) -- (226.4,194.5) -- (218.9,200) -- (220.4,188.5) -- (210.9,193.5) -- (212.4,183) -- (204.4,186.5) -- (206.9,176.5) -- (197.4,176.5) -- (199.9,167) -- (191.4,167) -- (196.9,156.5) -- (187.4,154) -- (193.4,145) -- (186.4,144) -- (187.4,138) -- (181.9,133) -- (186.9,126.5) -- (182.9,122.5) -- (187.9,116.5) -- (181.4,110.5) -- (190.9,103) -- (184.9,95.5) -- (192.9,89) -- (188.9,82.5) -- (198.4,78) -- (194.4,70.5) -- (203.4,69.5) -- (204.4,60) -- (212.9,62) -- (216.9,55.1) -- (226.3,62.5) -- (232.3,53.5) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.15 ] (237.8,62.5) -- (244.8,56) -- (248.8,64.5) -- (256.8,61.5) -- (259.8,72.5) -- (268.8,69) -- (272.8,76.5) -- (278.8,74.5) -- (282.3,82) -- (290.3,82) -- (288.8,91.5) -- (298.3,91.5) -- (299.3,100.5) -- (306.8,100) -- (304.8,106.5) -- (313.3,106.5) -- (310.8,116.5) -- (319.3,119.5) -- (315.8,127.5) -- (323.8,132.5) -- (319.3,142) -- (327.3,143) -- (322.3,153.5) -- (328.8,161) -- (319.3,166.5) -- (324.3,176.5) -- (313.3,180.5) -- (315.8,191) -- (304.8,189) -- (304.8,189) -- (301.8,182) -- (310.8,176.5) -- (302.3,171) -- (307.8,161.5) -- (297.8,156.5) -- (303.3,148) -- (291.8,146) -- (296.8,135) -- (285.3,135.5) -- (287.3,124.5) -- (273.8,124) -- (277.8,114) -- (264.8,114) -- (267.8,105) -- (253.8,104) -- (255.8,94.5) -- (242.8,95) -- (243.8,84.5) -- (232.3,87.5) -- (232.8,78.5) -- (222.8,80) -- (221.8,73) -- (209.3,72.5) -- (204.4,60) -- (212.9,62) -- (216.9,55.1) -- (226.3,62.5) -- (232.3,53.5) -- cycle ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (232.6,62.1) -- (236.8,71) ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (230.73,66.67) -- (232.6,62.1) ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (253.27,67.43) -- (257.47,76.33) ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (251.4,72) -- (253.27,67.43) ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (283,87.33) -- (275.33,86.67) ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (280.33,93.33) -- (283,87.33) ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (299,106) -- (291.33,105.33) ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (296.67,112) -- (299,106) ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (317.33,133.67) -- (308,130.67) ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (317.33,133.67) -- (311.67,136) ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (322,159.67) -- (314.67,154.33) ;
                         	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.62 ]   (315.33,160.33) -- (322,159.67) ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 144; green, 205; blue, 14 }  ,fill opacity=1 ] (197.88,105.78) -- (190.83,111) -- (197.04,116.49) -- (192.69,123.36) -- (201.22,128.43) -- (196.22,136.14) -- (201.59,141.42) -- (198.54,146.63) -- (204.02,151.44) -- (202.18,158.93) -- (210.48,159.47) -- (208.31,168.37) -- (215.62,171.15) -- (213.48,178.07) -- (219.38,177.53) -- (217.43,185.49) -- (226.38,185.2) -- (226.95,193.77) -- (234.45,192.14) -- (236.81,200.65) -- (245.8,198.39) -- (244.8,206.08) -- (254.74,203.56) -- (259.54,211.18) -- (266.32,203.41) -- (273.55,210.15) -- (279.42,200.67) -- (289.27,208.67) -- (292.27,199.2) -- (286.27,198.67) -- (283.32,190.21) -- (276.65,197.51) -- (273.99,188.42) -- (264.77,191.62) -- (262.87,181.23) -- (254.49,184.64) -- (255.45,173.46) -- (245.09,175.89) -- (248.15,165.22) -- (238.47,164.84) -- (241.15,152.1) -- (231.85,153.79) -- (234.83,141.62) -- (226.61,142.58) -- (228.98,129.27) -- (220.56,129.2) -- (223.96,117.13) -- (214.94,115.91) -- (220.09,105.76) -- (212.43,104.38) -- (215.98,95.33) -- (210.35,92.96) -- (212.79,81.15) -- (203.45,74) -- (203.17,82.37) -- (196.47,84.7) -- (200.52,95.02) -- (191.6,98.79) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (245.43,65.27) -- (248.27,78) -- (245.22,67.34) -- (240.6,73.18) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (267.24,80.51) -- (265.64,90.06) -- (266.43,81.81) -- (260.82,83.93) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (290.49,99.6) -- (279.31,105.96) -- (288.5,100.14) -- (281.81,98.69) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (307.76,126.03) -- (295.77,124.79) -- (306.03,125.2) -- (302.45,119.13) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (312.86,149.34) -- (303.16,142.59) -- (311.58,147.93) -- (309.81,142.05) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (227.76,85.33) -- (230.6,97.67) -- (227.55,87.34) -- (222.93,93) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (240.39,98.67) -- (243.6,109) -- (240.15,100.35) -- (234.93,105.09) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (260.39,118.67) -- (263.6,129) -- (260.15,120.35) -- (254.93,125.09) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (278.06,133) -- (281.27,143.33) -- (277.82,134.68) -- (272.6,139.42) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (242.56,115) -- (239.6,125.33) -- (242.78,116.68) -- (247.6,121.42) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (289.91,153.38) -- (282.85,161.58) -- (288.36,154.07) -- (281.57,152.16) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (300.17,175.59) -- (290.09,179.52) -- (298.47,175.47) -- (293.37,170.6) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (282.05,176.44) -- (277.52,182.91) -- (280.92,176.88) -- (275.44,174.4) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (268.71,164.44) -- (264.18,170.91) -- (267.59,164.88) -- (262.1,162.4) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (263.05,144.78) -- (258.52,151.25) -- (261.92,145.21) -- (256.44,142.73) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (253.38,134.11) -- (248.85,140.58) -- (252.26,134.55) -- (246.77,132.06) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (200.93,101.46) -- (207.03,96.43) -- (202.13,101.34) -- (206.75,105.2) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (201.93,118.79) -- (208.03,113.77) -- (203.13,118.67) -- (207.75,122.53) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (210.27,134.79) -- (216.36,129.77) -- (211.46,134.67) -- (216.09,138.53) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (212.13,153.01) -- (216.29,146.29) -- (213.23,152.51) -- (218.85,154.68) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (224.13,159.68) -- (228.29,152.96) -- (225.23,159.18) -- (230.85,161.34) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (220.13,170.01) -- (224.29,163.29) -- (221.23,169.51) -- (226.85,171.68) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (235.06,176.45) -- (234.85,168.55) -- (235.7,175.43) -- (241.59,174.16) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (229.06,184.11) -- (228.85,176.22) -- (229.7,183.09) -- (235.59,181.82) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (243.06,189.45) -- (242.85,181.55) -- (243.7,188.43) -- (249.59,187.16) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (255.06,196.45) -- (254.85,188.55) -- (255.7,195.43) -- (261.59,194.16) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (203.72,171.45) -- (203.51,163.55) -- (204.37,170.43) -- (210.26,169.16) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (190.39,136.11) -- (190.18,128.22) -- (191.04,135.09) -- (196.92,133.82) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (188.11,124.39) -- (187.9,116.5) -- (188.76,123.38) -- (194.64,122.1) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (252.72,166.78) -- (252.51,158.88) -- (253.37,165.76) -- (259.26,164.49) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (269.39,183.78) -- (269.18,175.88) -- (270.04,182.76) -- (275.92,181.49) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (294.71,193.57) -- (289.19,187.92) -- (294.49,192.38) -- (297.95,187.45) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (302.25,200.55) -- (294.63,198.48) -- (301.46,199.64) -- (301.94,193.64) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (245.06,156.45) -- (244.85,148.55) -- (245.7,155.43) -- (251.59,154.16) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (239.06,143.11) -- (238.85,135.22) -- (239.7,142.09) -- (245.59,140.82) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (228.72,125.11) -- (228.51,117.22) -- (229.37,124.09) -- (235.26,122.82) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (224.72,109.11) -- (224.51,101.22) -- (225.37,108.09) -- (231.26,106.82) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (255.74,84.7) -- (257.09,95.86) -- (255.13,86.34) -- (248.44,89.96) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (273.55,98.99) -- (268.09,108.83) -- (272.09,99.97) -- (264.55,98.97) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (290.12,112.84) -- (282.03,120.66) -- (288.44,113.35) -- (281.52,110.19) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 101; green, 123; blue, 77 }  ,fill opacity=1 ] (277.23,152.24) -- (268.16,158.89) -- (275.5,152.51) -- (269.06,148.46) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 122; green, 147; blue, 45 }  ,fill opacity=1 ] (122.56,154.44) -- (157.36,154.8) -- (239.76,163.6) -- (269.76,161.6) -- (290.16,158.4) -- (280.96,165.6) -- (286.96,172.8) -- (277.76,177.6) -- (281.36,184) -- (272.16,186.8) -- (272.96,194) -- (264.56,195.6) -- (262.96,202) -- (256.16,203.2) -- (253.36,211.2) -- (242.16,210.8) -- (242.96,218) -- (234.96,216) -- (232.16,222.4) -- (224.56,217.6) -- (218.56,225.6) -- (210.16,222.8) -- (208.96,230.4) -- (202.96,222) -- (198.96,230.4) -- (192.56,222.8) -- (186.96,231.6) -- (180.56,224) -- (172.16,229.2) -- (166.96,220.4) -- (160.56,227.6) -- (154.56,220.4) -- (146.96,220) -- (144.96,209.6) -- (136.56,209.2) -- (138.16,201.2) -- (127.76,195.6) -- (130.96,186.8) -- (121.36,179.6) -- (125.76,169.6) -- (119.76,162.8) -- (128.56,156.8) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 225; green, 242; blue, 142 }  ,fill opacity=1 ] (125.45,156.51) -- (158.9,156.84) -- (238.11,164.95) -- (266.95,163.1) -- (286.56,160.15) -- (277.72,166.79) -- (283.48,173.42) -- (274.64,177.84) -- (278.1,183.74) -- (269.26,186.32) -- (270.03,192.96) -- (261.95,194.43) -- (260.41,200.33) -- (253.88,201.43) -- (251.19,208.8) -- (240.42,208.43) -- (241.19,215.07) -- (233.5,213.23) -- (230.81,219.12) -- (223.5,214.7) -- (217.73,222.07) -- (209.66,219.49) -- (208.51,226.49) -- (202.74,218.75) -- (198.89,226.49) -- (192.74,219.49) -- (187.36,227.6) -- (181.21,220.6) -- (173.13,225.39) -- (168.13,217.28) -- (161.98,223.91) -- (156.21,217.28) -- (148.91,216.91) -- (146.98,207.33) -- (138.91,206.96) -- (140.45,199.59) -- (130.45,194.43) -- (133.53,186.32) -- (124.3,179.69) -- (128.53,170.47) -- (122.76,164.21) -- (131.22,158.68) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 252; green, 248; blue, 201 }  ,fill opacity=1 ] (128.73,154.4) -- (160.67,154.73) -- (236.3,162.76) -- (263.84,160.93) -- (282.56,158.01) -- (274.12,164.58) -- (279.62,171.15) -- (271.18,175.53) -- (274.48,181.37) -- (266.04,183.92) -- (266.77,190.49) -- (259.06,191.95) -- (257.59,197.79) -- (251.35,198.89) -- (248.78,206.19) -- (238.5,205.82) -- (239.24,212.39) -- (231.9,210.57) -- (229.33,216.41) -- (222.35,212.03) -- (216.84,219.33) -- (209.13,216.77) -- (208.03,223.71) -- (202.52,216.04) -- (198.85,223.71) -- (192.98,216.77) -- (187.84,224.8) -- (181.96,217.87) -- (174.25,222.61) -- (169.48,214.58) -- (163.61,221.15) -- (158.1,214.58) -- (151.13,214.22) -- (149.29,204.73) -- (141.58,204.36) -- (143.05,197.06) -- (133.5,191.95) -- (136.44,183.92) -- (127.63,177.36) -- (131.67,168.23) -- (126.16,162.03) -- (134.24,156.55) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 220; blue, 28 }  ,fill opacity=1 ] (185.16,158.22) .. controls (185.69,166.67) and (198.36,191.02) .. (183.16,203.82) .. controls (157.56,216.22) and (135.16,160.62) .. (139.96,154.62) .. controls (160.36,153.02) and (170.36,155.42) .. (185.16,158.22) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 220; blue, 28 }  ,fill opacity=1 ] (234.56,161.6) .. controls (235.09,170.05) and (231.76,214) .. (191.36,203.6) .. controls (184.96,197.2) and (201.36,195.2) .. (187.76,158) .. controls (208.16,156.4) and (219.76,158.8) .. (234.56,161.6) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 220; blue, 28 }  ,fill opacity=1 ] (273.36,160.4) .. controls (273.89,168.85) and (247.36,211.2) .. (221.36,204) .. controls (214.96,197.6) and (237.36,200.8) .. (236.82,162.83) .. controls (251.76,161.6) and (258.56,159.2) .. (273.36,160.4) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (269.76,161.6) .. controls (270.29,170.05) and (228.16,197.6) .. (210.56,192.8) .. controls (169.36,196.8) and (145.36,160) .. (150.16,154) .. controls (170.56,152.4) and (254.96,158.8) .. (269.76,161.6) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (180.96,161.42) .. controls (181.06,163.81) and (173.28,171.6) .. (170.03,170.24) .. controls (162.43,171.37) and (158,160.97) .. (158.89,159.27) .. controls (162.65,158.82) and (178.23,160.63) .. (180.96,161.42) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (225.76,163.99) .. controls (225.89,165.69) and (215.31,171.26) .. (210.89,170.29) .. controls (200.55,171.1) and (194.52,163.66) .. (195.73,162.45) .. controls (200.85,162.13) and (222.04,163.42) .. (225.76,163.99) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (257.81,163.72) .. controls (258.13,164.99) and (252.85,170.34) .. (250.18,170.08) .. controls (244.36,171.81) and (239.84,166.85) .. (240.36,165.81) .. controls (243.26,165.01) and (255.6,163.69) .. (257.81,163.72) -- cycle ;
                         \\end{tikzpicture}}'''
                         %(str(M_val), str(M_val), str(M_val), str(A_val), str(B_str)))

        # Nội dung lời giải theo hướng xét hàm số và bảng biến thiên
        loigiai = ('''Số chuyến xe cần vận chuyển là $\\dfrac{%s}{x}$ (chuyến). \\\\
    Chi phí cho mỗi chuyến xe là $f(x) = %s + %s x^2$ (nghìn đồng). \\\\
    Tổng chi phí vận chuyển cho %s kg sầu riêng là: \\\\
    $C(x) = \\dfrac{%s}{x} \\cdot \\left(%s + %s x^2\\right) = \\dfrac{%s}{x} + %s x$ (nghìn đồng), với $x \\in [1; %s]$. \\\\
    Xét hàm số $C(x) = \\dfrac{%s}{x} + %s x$ liên tục trên $[1; %s]$. \\\\
    Đạo hàm: $C'(x) = -\\dfrac{%s}{x^2} + %s$. \\\\
    Cho $C'(x) = 0 \\Leftrightarrow -\\dfrac{%s}{x^2} + %s = 0 \\Leftrightarrow x^2 = %s \\Leftrightarrow x = %s$ (do $x \\in [1; %s]$). \\\\
    Bảng biến thiên của hàm số $C(x)$ trên đoạn $[1; %s]$: \\\\
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (0,0) rectangle (9,3);
    \\draw[line width=1pt] (0,2) -- (9,2);
    \\draw[line width=1pt] (0,1.2) -- (9,1.2);
    \\draw[line width=1pt] (1.5,0) -- (1.5,3);
    \\node at (0.75,2.5) {$x$};
    \\node at (0.75,1.6) {$C'(x)$};
    \\node at (0.75,0.6) {$C(x)$};
    \\node at (2,2.5) {$1$};
    \\node at (5.25,2.5) {$%s$};
    \\node at (8.5,2.5) {$%s$};
    \\node at (5.25,1.6) {$0$};
    \\node at (3.6,1.6) {$-$};
    \\node at (6.9,1.6) {$+$};
    \\node at (2,0.9) {$%s$};
    \\node at (5.25,0.2) {$%s$};
    \\node at (8.5,0.9) {$%s$};
    \\draw[->, line width=1pt] (2.4,0.8) -- (4.8,0.25);
    \\draw[->, line width=1pt] (5.7,0.25) -- (8.1,0.8);
    \\end{tikzpicture}
    \\end{center}
    Căn cứ bảng biến thiên, hàm số $C(x)$ đạt giá trị nhỏ nhất tại $x = %s$. \\\\
    Mặt khác, $x = %s$ là số tự nhiên và là ước của %s (vì $%s : %s = %s$ chuyến). \\\\
    Vậy mỗi chuyến nên chở $%s$ kg để tổng chi phí vận chuyển là nhỏ nhất.'''
                   %(str(M_val),
                     str(A_val), str(B_str),
                     str(M_val),
                     str(M_val), str(A_val), str(B_str), str(c1), str(c2_str), str(M_val),
                     str(c1), str(c2_str), str(M_val),
                     str(c1), str(c2_str),
                     str(c1), str(c2_str), str(x0_val**2), str(x0_val), str(M_val),
                     str(M_val),
                     str(x0_val), str(M_val),
                     str(c_tai_1), str(c_min), str(c_tai_M),
                     str(x0_val),
                     str(x0_val), str(M_val), str(M_val), str(x0_val), str(M_val // x0_val),
                     str(x0_val)
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage} \n\n')
    return content

