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


def bt_dang8_p2_b4_c2_hh12(self):
            # Khai báo biến
            # --- HÀM HỖ TRỢ ĐỊNH DẠNG ---
            def fmt_sq(var, val):
                if val == 0: return f"{var}^2"
                if val > 0: return f"\\left({var}-{val}\\right)^2"
                return f"\\left({var}+{abs(val)}\\right)^2"

            def format_line_param(start, dir, var='t'):
                if dir == 0: return str(start)
                if start == 0:
                    if dir == 1: return var
                    if dir == -1: return f"-{var}"
                    return f"{dir}{var}"
                if dir == 1: return f"{start}+{var}"
                if dir == -1: return f"{start}-{var}"
                if dir > 0: return f"{start}+{dir}{var}"
                return f"{start}-{abs(dir)}{var}"

            def clx(s): 
                return str(s).replace('(', '\\left(').replace(')', '\\right)')

            # --- VÒNG LẶP RANDOM ĐỂ ĐẢM BẢO SỐ LIỆU HỢP LÝ ---
            while True:
                # 1. Random tâm mặt cầu I
                xI = random.randint(-3, 3)
                yI = random.randint(-3, 3)
                zI = random.randint(-3, 3)

                # 2. Random đường thẳng d (đi qua M, VTCP u)
                xM = random.randint(-3, 3)
                yM = random.randint(-3, 3)
                zM = random.randint(-3, 3)
                if (xI, yI, zI) == (xM, yM, zM): continue

                u1 = random.randint(-3, 3)
                u2 = random.randint(-3, 3)
                u3 = random.randint(-3, 3)
                if u1 == 0 and u2 == 0 and u3 == 0: continue

                IM = Matrix([xM - xI, yM - yI, zM - zI])
                u = Matrix([u1, u2, u3])

                cross_prod = IM.cross(u)
                cross_sq = cross_prod.dot(cross_prod)
                u_sq = u.dot(u)

                if cross_sq == 0: continue

                # Khoảng cách bình phương từ I đến d
                h_sq = Rational(cross_sq, u_sq)

                # 3. Random bán kính R^2
                R_sq = random.randint(1, 10)
                # Đường thẳng phải nằm ngoài mặt cầu
                if R_sq >= h_sq: continue

                # 4. Tính toán cho ý c (cos AIB)
                # cos(AIB) = 2 * (R/h)^2 - 1 = 2 * (R^2 / h^2) - 1
                cos_AIB_val = 2 * Rational(R_sq, h_sq) - 1
                a_val = cos_AIB_val.p
                b_val = cos_AIB_val.q
                if b_val <= 0:
                    a_val = -a_val
                    b_val = -b_val

                if b_val == 1: continue # Tránh trường hợp mẫu số = 1 quá đơn giản
                a2_b2 = a_val**2 + b_val**2

                # 5. Tính toán cho ý d (thời gian con kiến)
                v_kien = random.randint(2, 5)
                try:
                    theta_val = acos(cos_AIB_val).evalf()
                    R_sym = sqrt(R_sq)
                    R_cm_sym = 10 * R_sym
                    time_val = (R_cm_sym * theta_val) / v_kien
                    time_rounded = round(time_val)
                    if time_rounded <= 0: continue
                    break
                except:
                    continue

            # --- KHAI BÁO CÁC CHUỖI HIỂN THỊ ---
            sphere_str = f"{fmt_sq('x', xI)}+{fmt_sq('y', yI)}+{fmt_sq('z', zI)}={R_sq}"
            line_x = format_line_param(xM, u1)
            line_y = format_line_param(yM, u2)
            line_z = format_line_param(zM, u3)

            h_sym = sqrt(h_sq)
            h_latex = clx(latex(h_sym))
            R_latex = clx(latex(R_sym))

            # Tọa độ I sai để làm đáp án nhiễu
            xI_w, yI_w, zI_w = -xI, -yI, -zI
            if (xI_w, yI_w, zI_w) == (xI, yI, zI):
                xI_w += 1
            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.6,xscale=0.6]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.5 ] (205.94,275.66) -- (390.84,243.41) -- (311.42,240.93) -- (148,266.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (282.5,90.44) -- (407.84,222.57) -- (328.42,220.1) -- (203.07,87.96) -- cycle ;
            	\draw  [fill={rgb, 255:red, 225; green, 144; blue, 9 }  ,fill opacity=1 ] (265.5,111.27) -- (390.84,243.41) -- (311.42,240.93) -- (186.07,108.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.45 ] (150.88,262.32) .. controls (150.88,254.95) and (175.53,248.97) .. (205.94,248.97) .. controls (236.35,248.97) and (261,254.95) .. (261,262.32) .. controls (261,269.69) and (236.35,275.66) .. (205.94,275.66) .. controls (175.53,275.66) and (150.88,269.69) .. (150.88,262.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.45 ] (168.88,260.05) .. controls (168.88,253.94) and (185.47,248.97) .. (205.94,248.97) .. controls (226.41,248.97) and (243,253.94) .. (243,260.05) .. controls (243,266.17) and (226.41,271.13) .. (205.94,271.13) .. controls (185.47,271.13) and (168.88,266.17) .. (168.88,260.05) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 187; blue, 90 }  ,fill opacity=1 ] (203.07,87.96) -- (282.5,90.44) -- (265.5,111.27) -- (186.07,108.8) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (282.5,90.44) -- (407.84,222.57) -- (390.84,243.41) -- (265.5,111.27) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.3 ] (245,151.6) -- (390.84,243.41) -- (311.42,240.93) -- (242,165.6) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.11 ][fill={rgb, 255:red, 225; green, 222; blue, 222 }  ,fill opacity=1 ] (139.3,202.65) .. controls (139.3,166.61) and (168.51,137.4) .. (204.55,137.4) .. controls (240.59,137.4) and (269.8,166.61) .. (269.8,202.65) .. controls (269.8,238.69) and (240.59,267.9) .. (204.55,267.9) .. controls (168.51,267.9) and (139.3,238.69) .. (139.3,202.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.37 ] (142.8,195.65) .. controls (142.8,164.03) and (168.43,138.4) .. (200.05,138.4) .. controls (231.67,138.4) and (257.3,164.03) .. (257.3,195.65) .. controls (257.3,227.27) and (231.67,252.9) .. (200.05,252.9) .. controls (168.43,252.9) and (142.8,227.27) .. (142.8,195.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.37 ] (153.3,180.4) .. controls (153.3,157.2) and (172.1,138.4) .. (195.3,138.4) .. controls (218.5,138.4) and (237.3,157.2) .. (237.3,180.4) .. controls (237.3,203.6) and (218.5,222.4) .. (195.3,222.4) .. controls (172.1,222.4) and (153.3,203.6) .. (153.3,180.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (203.1,170.9) -- (231.1,189.4) -- (220.6,219.9) -- (186.1,220.4) -- (177.6,188.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (184.6,140.4) .. controls (188.6,137.9) and (205.45,133.65) .. (224.95,140.65) .. controls (226.9,144.15) and (226.05,142.15) .. (227.53,146.89) .. controls (205.7,149.65) and (226.7,146.9) .. (204.55,149.65) .. controls (196.05,147.9) and (195.05,147.9) .. (182.05,146.65) .. controls (184.05,140.9) and (182.55,146.4) .. (184.6,140.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (153.95,160.9) .. controls (161.2,161.15) and (153.7,160.65) .. (161.2,160.9) .. controls (155.7,182.4) and (161.2,160.65) .. (155.45,182.9) .. controls (144.2,205.15) and (154.95,183.4) .. (144.45,205.4) .. controls (144.45,204.9) and (139.2,201.65) .. (139.2,200.9) .. controls (139.95,185.15) and (141.45,178.65) .. (153.95,160.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (151.2,228.9) .. controls (162.95,235.4) and (161.45,235.4) .. (173.95,240.4) .. controls (182.45,250.4) and (184.95,253.4) .. (190.45,258.4) .. controls (186.7,261.9) and (187.7,260.9) .. (183.45,264.4) .. controls (170.2,260.9) and (154.45,247.9) .. (148.7,236.65) .. controls (150.2,232.4) and (149.2,234.4) .. (151.2,228.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (236.9,239.15) .. controls (254.25,231.9) and (246.7,234.65) .. (259.35,228.4) .. controls (261.35,235.9) and (261.4,234.4) .. (261.15,235.4) .. controls (254.5,251.9) and (235.5,261.65) .. (227.9,263.65) .. controls (221.9,259.65) and (225.1,261.15) .. (220.1,257.9) .. controls (234.1,242.15) and (229.9,248.15) .. (236.9,239.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (247.85,159.4) .. controls (254.85,160.65) and (247.85,159.4) .. (254.9,160.35) .. controls (268.1,179.65) and (267.6,186.15) .. (269.85,199.15) .. controls (264.35,203.65) and (268.35,200.65) .. (264.1,203.15) .. controls (258.85,193.65) and (262.35,200.15) .. (252.35,181.9) .. controls (250.6,171.9) and (249.6,168.15) .. (247.85,159.4) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (204.55,149.65) -- (203.1,170.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (227.53,146.89) -- (247.85,159.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (182.05,146.65) -- (161.2,160.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (252.35,181.9) -- (231.1,189.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (155.45,182.9) -- (177.6,188.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (143.95,204.15) -- (151.2,228.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (186.1,220.4) -- (173.95,240.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (236.9,239.15) -- (220.6,219.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.15 ]   (259.35,228.4) -- (264.1,203.15) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.12 ]   (190.45,258.4) -- (220.1,257.9) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.79 ] (204.55,149.65) -- (203.1,170.9) -- (178.95,188.9) -- (155.45,182.9) -- (178.2,187.15) -- (200.95,170.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (204.55,149.65) -- (206.2,169.9) -- (221.7,183.15) -- (203.1,170.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (249.95,171.9) -- (252.35,181.9) -- (231.1,189.4) -- (249.7,180.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (203.35,220.15) -- (187.2,222.9) -- (177.95,234.15) -- (186.1,220.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (145.95,212.15) -- (143.2,205.9) -- (140.95,202.9) -- (144.45,205.4) -- cycle ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.71 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ]   (182.05,145.65) -- (159.7,161.15) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.77 ] (203.45,171.9) -- (193.95,181.4) -- (190.7,183.9) -- (180.45,189.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.77 ] (159.2,162.9) -- (154.7,180.15) -- (154.45,175.65) -- (157.2,164.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.77 ] (195.7,144.9) -- (198.7,146.9) -- (184.7,145.65) -- (188.7,144.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (265.2,181.15) -- (268.7,196.9) -- (265.95,198.65) -- (263.45,183.65) -- (256.95,166.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.28 ] (257.7,235.9) -- (259.2,236.9) -- (252.7,246.4) -- (241.45,256.15) -- (227.9,263.65) -- (222.7,257.9) -- (237.45,251.9) -- (246.7,245.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.28 ] (187.7,258.4) -- (182.95,262.9) -- (169.95,256.65) -- (158.95,248.15) -- (150.45,238.4) -- (151.2,234.2) -- (161.45,243.4) -- (171.7,250.4) -- cycle ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.71 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ]   (150.5,230.9) -- (144.45,205.4) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.71 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ]   (236.38,240.53) -- (220.6,219.9) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.71 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ]   (237.9,239.15) -- (220.6,219.9) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.71 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ]   (227.53,146.89) -- (250,159.65) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.08 ] (144.8,187.6) .. controls (144.8,163.3) and (170.99,143.6) .. (203.3,143.6) .. controls (235.61,143.6) and (261.8,163.3) .. (261.8,187.6) .. controls (261.8,211.9) and (235.61,231.6) .. (203.3,231.6) .. controls (170.99,231.6) and (144.8,211.9) .. (144.8,187.6) -- cycle ;
            \end{tikzpicture}'''
            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Trong không gian với hệ trục tọa độ $Oxyz$ với đơn vị trên mỗi trục là dm, mặt ngoài của một quả bóng được mô hình hóa bởi phương trình mặt cầu $%s$. Quả bóng nằm yên trên sàn nhà. Người ta nhìn thấy một tấm ván ngã xuống đè lên quả bóng, phần giao của tấm ván và sàn nhà là đường thẳng $d:\begin{cases} x = %s \\ y = %s \\ z = %s \end{cases}$. Gọi $A, B$ lần lượt là hai tiếp điểm của tấm ván, sàn nhà với quả bóng và $I$ là tâm quả bóng.}{%s}''' 
                             % (sphere_str, line_x, line_y, line_z, hinhve))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Quả bóng có tâm $I\\left(%s; %s; %s\\right)$ và bán kính $R=%s$' % (xI, yI, zI, R_latex)
            nb_da_1_s = 'Quả bóng có tâm $I\\left(%s; %s; %s\\right)$ và bán kính $R=%s$' % (xI_w, yI_w, zI_w, R_latex)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Từ phương trình mặt cầu $%s$, ta xác định được tâm $I\\left(%s; %s; %s\\right)$ và bán kính $R=\\sqrt{%s}=%s$.''' 
                            % (sphere_str, xI, yI, zI, R_sq, R_latex))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            h_wrong = clx(latex(h_sym + 1))
            # Các đáp án
            th_da_1_d = '\\True Khoảng cách từ tâm quả bóng đến đường thẳng $d$ bằng $%s$' % h_latex 
            th_da_1_s = 'Khoảng cách từ tâm quả bóng đến đường thẳng $d$ bằng $%s$' % h_wrong
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Đường thẳng $d$ đi qua điểm $M\\left(%s; %s; %s\\right)$ và có một vectơ chỉ phương là $\\vec{u}=\\left(%s; %s; %s\\right)$. \\\\
            Ta có $\\vec{IM}=\\left(%s; %s; %s\\right)$ suy ra $\\left[\\vec{IM}, \\vec{u}\\right] = \\left(%s; %s; %s\\right)$. \\\\
            Khoảng cách từ tâm $I$ đến đường thẳng $d$ là $d\\left(I, d\\right) = \\frac{\\left|\\left[\\vec{IM}, \\vec{u}\\right]\\right|}{\\left|\\vec{u}\\right|} = \\frac{\\sqrt{%s}}{\\sqrt{%s}} = %s$.'''       
                       % (xM, yM, zM, u1, u2, u3, xM-xI, yM-yI, zM-zI, cross_prod[0], cross_prod[1], cross_prod[2], cross_sq, u_sq, h_latex))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            a2_b2_wrong = a2_b2 + random.choice([-2, 2, 4])
            # Các đáp án
            vd_da_1_d = '\\True Nếu $\\cos \\widehat{AIB} = \\frac{a}{b}$ (với $\\frac{a}{b}$ phân số tối giản và $a, b \\in \\mathbb{Z}$) thì giá trị biểu thức $a^2+b^2=%s$' % a2_b2  
            vd_da_1_s = 'Nếu $\\cos \\widehat{AIB} = \\frac{a}{b}$ (với $\\frac{a}{b}$ phân số tối giản và $a, b \\in \\mathbb{Z}$) thì giá trị biểu thức $a^2+b^2=%s$' % a2_b2_wrong
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Gọi $H$ là hình chiếu vuông góc của $I$ lên đường thẳng $d$. Khi đó $IH = d\\left(I, d\\right) = %s$. \\\\
            Mặt phẳng đi qua $I$ và vuông góc với $d$ cắt các mặt phẳng tiếp diện tại các giao tuyến chứa $A, B$. Góc $\\widehat{AIB}$ nhận $IH$ làm phân giác. \\\\
            Xét tam giác $IHA$ vuông tại $A$ có $\\cos \\widehat{AIH} = \\frac{IA}{IH} = \\frac{%s}{%s}$. \\\\
            Do đó $\\cos \\widehat{AIB} = \\cos \\left(2\\widehat{AIH}\\right) = 2\\cos^2 \\widehat{AIH} - 1 = 2\\left(\\frac{%s}{%s}\\right)^2 - 1 = %s$. \\\\
            Suy ra $a=%s, b=%s \\Rightarrow a^2+b^2=%s$.'''  
                       % (h_latex, R_latex, h_latex, R_latex, h_latex, clx(latex(cos_AIB_val)), a_val, b_val, a2_b2))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            time_wrong = time_rounded + random.choice([-3, -2, 2, 3])
            # Các đáp án
            vdc_da_1_d = '\\True Một con kiến bò từ vị trí $A$ đến vị trí $B$ trên quả bóng với tốc độ $%s$ (cm/s) thì thời gian ngắn nhất cho chuyến đi này là $%s$ giây (Kết quả làm tròn đến hàng đơn vị)' % (v_kien, time_rounded)
            vdc_da_1_s = 'Một con kiến bò từ vị trí $A$ đến vị trí $B$ trên quả bóng với tốc độ $%s$ (cm/s) thì thời gian ngắn nhất cho chuyến đi này là $%s$ giây (Kết quả làm tròn đến hàng đơn vị)' % (v_kien, time_wrong)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            theta_str = f"{theta_val:.3f}".replace('.', ',')
            time_float_str = f"{time_val.evalf():.2f}".replace('.', ',')

            loigiai_vdc_1 = ('''Bán kính quả bóng là $R = %s \\text{ dm} = 10%s \\text{ cm}$. \\\\
            Quãng đường ngắn nhất kiến bò trên mặt quả bóng là độ dài cung nhỏ $AB$, kí hiệu là $l = R_{cm} \\cdot \\widehat{AIB}$. \\\\
            Ta có $\\cos \\widehat{AIB} = %s \\Rightarrow \\widehat{AIB} \\approx %s$ (rad). \\\\
            Thời gian ngắn nhất để con kiến di chuyển là $t = \\frac{l}{v} = \\frac{10%s \\cdot %s}{%s} \\approx %s$ giây. \\\\
            Làm tròn đến hàng đơn vị ta được %s giây.'''
                       % (R_latex, R_latex, clx(latex(cos_AIB_val)), theta_str, R_latex, theta_str, v_kien, time_float_str, time_rounded))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

