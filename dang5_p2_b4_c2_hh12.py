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


def bt_dang5_p2_b4_c2_hh12(self):
            # Khai báo biến
            # ----------------- PHẦN RANDOM TẠO BIẾN SỐ TỌA ĐỘ TỰ ĐỘNG -----------------
            # Bộ các số gốc (a, b, c, R) thỏa mãn a^2 + b^2 + c^2 = R^2 (Bộ 3 Pythagoras không gian)
            base_tuples = [
                (280, 40, 100, 300),   # Bộ gốc của đề bài
                (20, 30, 60, 70),      # Tỉ lệ từ (2,3,6,7)
                (10, 40, 80, 90),      # Tỉ lệ từ (1,4,8,9)
                (40, 40, 70, 90),      # Tỉ lệ từ (4,4,7,9)
                (20, 60, 90, 110),     # Tỉ lệ từ (2,6,9,11)
                (30, 40, 120, 130),    # Tỉ lệ từ (3,4,12,13)
                (20, 100, 110, 150),   # Tỉ lệ từ (2,10,11,15)
                (80, 90, 120, 170),    # Tỉ lệ từ (8,9,12,17)
                (120, 160, 210, 290)   # Tỉ lệ từ (12,16,21,29)
            ]

            # 1. Chọn ngẫu nhiên một bộ thông số gốc và nhân hệ số scale
            a_base, b_base, c_base, R_base = random.choice(base_tuples)
            k_scale = random.choice([1, 2])
            a, b, c, R_val = a_base * k_scale, b_base * k_scale, c_base * k_scale, R_base * k_scale

            # Trộn dấu và đảo vị trí x, y để đa dạng hóa các góc phần tư
            if random.choice([True, False]):
                a, b = b, a
            a = a * random.choice([1, -1])
            b = b * random.choice([1, -1])

            # 2. Tạo 2 điểm giao cắt (B1 và B2) chắn chắn nằm trên mặt cầu
            x1, y1, z1 = a, b, c
            # Các phép biến đổi giữ nguyên x^2 + y^2
            transform = random.choice([(-b, a), (b, -a), (-a, -b)])
            x2, y2, z2 = transform[0], transform[1], c

            # 3. Tính Vector chỉ phương đảm bảo t luôn nguyên
            dx = x2 - x1
            dy = y2 - y1
            g = math.gcd(abs(dx), abs(dy))

            # Tìm ước số chung để chọn làm khoảng thời gian delta_t bay trong vòm
            divisors = [i for i in range(2, min(g + 1, 30)) if g % i == 0]
            if not divisors:
                divisors = [1]
            delta_t = random.choice(divisors)

            u_x_val = dx // delta_t
            u_y_val = dy // delta_t
            u_z_val = 0

            # 4. Xác định thời điểm chạm vòm (t1) và dịch ngược ra điểm phóng A
            t1 = random.randint(3, 12)
            t2 = t1 + delta_t

            x_A_val = x1 - u_x_val * t1
            y_A_val = y1 - u_y_val * t1
            z_A_val = c
            R_sq = R_val**2

            # Tính toán câu b (Thông hiểu)
            OA_sq = x_A_val**2 + y_A_val**2 + z_A_val**2
            OA_val = math.sqrt(OA_sq)
            OA_approx_str = str(round(OA_val, 1)).replace('.', ',')

            # Xác định tọa độ B1, B2 thực tế theo t1, t2
            B1_x, B1_y, B1_z = x_A_val + u_x_val * t1, y_A_val + u_y_val * t1, z_A_val + u_z_val * t1
            B2_x, B2_y, B2_z = x_A_val + u_x_val * t2, y_A_val + u_y_val * t2, z_A_val + u_z_val * t2

            def format_eq(a_val, b_val):
                return f"{a_val}{b_val}t" if b_val < 0 else f"{a_val}+{b_val}t"
            eq_x = format_eq(x_A_val, u_x_val)
            eq_y = format_eq(y_A_val, u_y_val)

            # Tính toán câu d (Vận dụng cao) - Khoảng cách
            cross_x = y_A_val * u_z_val - z_A_val * u_y_val
            cross_y = z_A_val * u_x_val - x_A_val * u_z_val
            cross_z = x_A_val * u_y_val - y_A_val * u_x_val

            cross_mag_sq = cross_x**2 + cross_y**2 + cross_z**2
            u_mag_sq = u_x_val**2 + u_y_val**2 + u_z_val**2

            d_val = math.sqrt(cross_mag_sq / u_mag_sq)
            d_approx_str = str(round(d_val, 1)).replace('.', ',')
            d_fake_approx_str = str(round(d_val + random.randint(5, 15), 1)).replace('.', ',')

            cross_mag_sympy = sp.sqrt(cross_mag_sq)
            u_mag_sympy = sp.sqrt(u_mag_sq)
            d_sympy = sp.simplify(cross_mag_sympy / u_mag_sympy)


            hinhve=r'''\begin{center}
                \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.4,xscale=0.4]
                    \draw    (32.13,786.87) -- (26.63,772.5) ;
                    \draw    (88.13,787.37) -- (67.13,758.87) ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (56.63,715.5) -- (102.39,660.28) -- (106.57,663.75) -- (60.81,718.96) -- cycle ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (102.39,660.28) -- (109.55,651.8) -- (116.19,647.73) -- (113.28,654.95) -- (106.11,663.43) -- cycle ;
                    \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (50.31,718.24) -- (56.51,710.36) -- (65.87,709.21) -- (66.97,718.58) -- (60.77,726.47) -- cycle ;
                    \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (54.85,721.67) -- (67.28,705.87) -- (68.59,706.9) -- (56.17,722.7) -- cycle ;
                    \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (49.54,726.49) -- (53.91,720.93) -- (57.53,723.77) -- (53.15,729.33) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (26.67,787.37) -- (96.67,787.37) -- (96.67,790.37) -- (26.67,790.37) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (24,773.48) -- (71.96,756.02) -- (72.63,757.87) -- (24.67,775.33) -- cycle ;
                    \draw    (42.13,798.37) -- (36.63,784) ;
                    \draw    (98.13,798.87) -- (77.13,770.37) ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (25.31,783.47) -- (92.69,758.93) -- (94.55,764.03) -- (27.16,788.57) -- cycle ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (92.69,758.93) -- (103.16,755.23) -- (110.95,755.07) -- (104.78,759.83) -- (94.32,763.53) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (36.67,798.87) -- (106.67,798.87) -- (106.67,801.87) -- (36.67,801.87) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (34,786.98) -- (81.96,769.52) -- (82.63,771.37) -- (34.67,788.83) -- cycle ;
                    \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (18.47,782.64) -- (27.8,778.97) -- (36.46,782.72) -- (32.67,791.36) -- (23.34,795.03) -- cycle ;
                    \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (20.66,787.9) -- (39.36,780.54) -- (39.97,782.09) -- (21.27,789.45) -- cycle ;
                    \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (13.64,789.38) -- (20.22,786.78) -- (21.91,791.06) -- (15.32,793.65) -- cycle ;
                    \draw    (71.13,814.37) -- (65.63,800) ;
                    \draw    (127.13,814.87) -- (106.13,786.37) ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (54.31,799.47) -- (121.69,774.93) -- (123.55,780.03) -- (56.16,804.57) -- cycle ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (121.69,774.93) -- (132.16,771.23) -- (139.95,771.07) -- (133.78,775.83) -- (123.32,779.53) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (65.67,814.87) -- (135.67,814.87) -- (135.67,817.87) -- (65.67,817.87) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (63,802.98) -- (110.96,785.52) -- (111.63,787.37) -- (63.67,804.83) -- cycle ;
                    \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (47.47,798.64) -- (56.8,794.97) -- (65.46,798.72) -- (61.67,807.36) -- (52.34,811.03) -- cycle ;
                    \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (49.66,803.9) -- (68.36,796.54) -- (68.97,798.09) -- (50.27,805.45) -- cycle ;
                    \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (42.64,805.38) -- (49.22,802.78) -- (50.91,807.06) -- (44.32,809.65) -- cycle ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (68.36,796.54) -- (106.3,782.23) ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (39.36,780.54) -- (77.3,766.23) ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (67.28,705.87) -- (94.3,673.07) ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (1.13,818) -- (1005.47,818) -- (1005.47,829) -- (1.13,829) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (392.23,820.16) -- (393.3,816.6) -- (399.54,816.6) -- (400.61,820.16) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (394.36,791.07) -- (398.11,791.07) -- (398.11,816.56) -- (394.36,816.56) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (393.62,774.81) -- (399.17,774.81) -- (399.17,800.29) -- (393.62,800.29) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (330.72,819.69) -- (331.79,816.12) -- (338.03,816.12) -- (339.1,819.69) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (332.86,790.59) -- (336.61,790.59) -- (336.61,816.08) -- (332.86,816.08) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (332.11,775.04) -- (337.66,775.04) -- (337.66,800.53) -- (332.11,800.53) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (304.23,820.4) -- (305.3,816.83) -- (311.53,816.83) -- (312.6,820.4) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (306.36,791.3) -- (310.11,791.3) -- (310.11,816.79) -- (306.36,816.79) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (305.62,775.04) -- (311.17,775.04) -- (311.17,800.53) -- (305.62,800.53) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (217.64,819.22) -- (218.71,815.65) -- (224.95,815.65) -- (226.02,819.22) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (219.78,790.83) -- (223.53,790.83) -- (223.53,816.32) -- (219.78,816.32) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (224.35,756.42) -- (226.91,756.42) -- (226.91,769.77) -- (224.35,769.77) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (238.22,758.49) -- (242.24,761.25) -- (224.3,787.3) -- (220.29,784.54) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (218.95,756.42) -- (224.24,756.42) -- (224.24,800.06) -- (218.95,800.06) -- cycle ;
                    \draw    (226.91,756.42) .. controls (239.81,746.11) and (231.14,757.61) .. (235.39,763.09) ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (419.2,778.85) -- (346.16,778.16) -- (346.54,738.05) -- (383.14,729.13) -- (419.58,738.73) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (386.69,772.39) -- (436.47,772.39) -- (436.47,782.79) -- (386.69,782.79) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (344.21,729.13) -- (383.14,729.13) -- (383.14,773.56) -- (344.21,773.56) -- cycle ; 
                    \draw  [draw opacity=0] (434.16,747.81) -- (434.62,780.02) -- (408.33,777.01) -- (407.87,744.79) -- cycle ; \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ] (434.16,747.81) -- (407.87,744.79)(434.28,756.33) -- (407.99,753.31)(434.41,764.84) -- (408.11,761.82)(434.53,773.36) -- (408.24,770.34) ; \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ] (434.16,747.81) -- (434.62,780.02)(425.63,746.83) -- (426.09,779.05)(417.1,745.85) -- (417.56,778.07)(408.57,744.87) -- (409.03,777.09) ; \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]  ;
                    \draw  [draw opacity=0] (408.56,744.33) -- (409.02,776.55) -- (391.96,776.55) -- (391.5,744.33) -- cycle ; \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ] (408.56,744.33) -- (391.5,744.33)(408.68,752.85) -- (391.62,752.85)(408.8,761.36) -- (391.74,761.36)(408.93,769.88) -- (391.87,769.88) ; \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ] (408.56,744.33) -- (409.02,776.55)(400.04,744.33) -- (400.5,776.55)(391.53,744.33) -- (391.99,776.55) ; \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]  ; 
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (342.08,772.39) -- (386.69,772.39) -- (386.69,782.79) -- (342.08,782.79) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (338.17,767.71) -- (325.73,772.49) -- (283.19,763.6) -- (273.71,754.23) -- cycle ;
                    \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (307.49,733.67) -- (315.11,736.18) -- (310.54,750.04) -- (302.92,747.53) -- cycle ;
                    \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (282.65,727.99) -- (290.67,730.64) -- (286.1,744.5) -- (278.09,741.85) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (272.31,737.69) -- (341.43,752.73) -- (338.17,767.71) -- (269.05,752.66) -- cycle ;
                    \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (271.04,715.33) -- (330.01,734.76) -- (326.39,745.76) -- (267.41,726.33) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (345.17,676.12) -- (328.01,745.04) -- (282.64,724.82) -- (299.79,655.9) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (299.44,655.6) -- (282.64,724.82) -- (267.41,726.33) -- (284.22,657.12) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (256.91,737.69) -- (272.31,737.69) -- (272.31,752.74) -- (256.91,752.74) -- cycle ;
                    \draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (299.79,655.9) -- (297.47,756.44) ;
                    \draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (345.17,676.12) -- (341.43,752.73) ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (289.24,772.07) -- (289.41,764.18) .. controls (289.5,759.81) and (293.11,756.35) .. (297.47,756.44) .. controls (301.83,756.53) and (305.29,760.14) .. (305.2,764.51) -- (305.03,772.4) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (316.92,772.78) -- (317.09,764.88) .. controls (317.18,760.52) and (320.79,757.06) .. (325.15,757.15) .. controls (329.51,757.24) and (332.97,760.85) .. (332.88,765.22) -- (332.71,773.11) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (252.65,758.09) -- (283.19,758.09) -- (283.19,772.07) -- (252.65,772.07) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (335.82,734.05) -- (341.43,734.05) -- (341.43,752.73) -- (335.82,752.73) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (256.91,752.74) -- (272.31,752.74) -- (272.31,758.24) -- (256.91,758.24) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (231.26,772.18) -- (386.69,772.18) -- (386.69,782.93) -- (231.26,782.93) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (237.19,768.86) -- (242.24,761.25) -- (244.35,762.65) -- (239.31,770.26) -- cycle ;
                    \draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (255.75,760.72) -- (260.1,760.72) -- (260.1,765.06) -- (255.75,765.06) -- cycle ;
                    \draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (263.57,760.74) -- (267.92,760.74) -- (267.92,765.08) -- (263.57,765.08) -- cycle ;
                    \draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (271.36,760.72) -- (275.71,760.72) -- (275.71,765.06) -- (271.36,765.06) -- cycle ;
                    \draw  [draw opacity=0] (245.36,668.65) .. controls (246,657.5) and (255.22,648.66) .. (266.52,648.61) -- (266.61,669.9) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (245.36,668.65) .. controls (246,657.5) and (255.22,648.66) .. (266.52,648.61) ;  
                    \draw  [draw opacity=0] (231.18,665.9) .. controls (232.17,648.84) and (246.28,635.29) .. (263.58,635.22) -- (263.73,667.81) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (231.18,665.9) .. controls (232.17,648.84) and (246.28,635.29) .. (263.58,635.22) ;  
                    \draw  [draw opacity=0] (216.66,665.04) .. controls (218.09,640.36) and (238.5,620.78) .. (263.51,620.67) -- (263.73,667.81) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (216.66,665.04) .. controls (218.09,640.36) and (238.5,620.78) .. (263.51,620.67) ;  
                    \draw  [draw opacity=0] (203.02,664.24) .. controls (204.87,632.41) and (231.19,607.15) .. (263.45,607.01) -- (263.73,667.81) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (203.02,664.24) .. controls (204.87,632.41) and (231.19,607.15) .. (263.45,607.01) ;  
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (379.27,733.03) -- (379.27,769.24) ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (346.96,751.35) -- (365.43,751.35) -- (365.43,761.9) -- (346.96,761.9) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (536.68,802.97) -- (540.38,802.97) -- (540.38,815.38) -- (536.68,815.38) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (533.05,815.33) -- (544.48,815.33) -- (544.48,817.9) -- (533.05,817.9) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (656.34,802.97) -- (660.04,802.97) -- (660.04,815.38) -- (656.34,815.38) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (652.71,815.33) -- (664.15,815.33) -- (664.15,817.9) -- (652.71,817.9) -- cycle ;
                    \draw  [draw opacity=0] (604.52,799.36) -- (624.87,799.36) -- (624.87,820.87) -- (604.52,820.87) -- cycle ; \draw   (604.52,799.36) -- (604.52,820.87)(614.21,799.36) -- (614.21,820.87)(623.9,799.36) -- (623.9,820.87) ; \draw   (604.52,799.36) -- (624.87,799.36)(604.52,809.05) -- (624.87,809.05)(604.52,818.74) -- (624.87,818.74) ; \draw    ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (530.2,738.02) -- (666.53,738.02) -- (666.53,796.93) -- (530.2,796.93) -- cycle ; 
                    \draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (525.07,796.16) -- (671.86,796.16) -- (671.86,808.76) -- (525.07,808.76) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (537.18,732.86) -- (572.54,732.86) -- (572.54,738.02) -- (537.18,738.02) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (624.87,732.86) -- (660.23,732.86) -- (660.23,738.02) -- (624.87,738.02) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (530.85,728.78) -- (667.18,728.78) -- (667.18,732.98) -- (530.85,732.98) -- cycle ;
                    \draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (666.99,745.19) -- (677.66,745.19) -- (677.66,780.45) -- (666.99,780.45) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (595.96,621.98) -- (596.92,621.98) -- (596.92,738.67) -- (595.96,738.67) -- cycle ;
                    \draw    (595.63,662.67) .. controls (617.25,624.14) and (576.58,636.51) .. (595.96,621.98) ;
                    \draw    (596.27,712.41) .. controls (617.9,673.88) and (576.25,677.21) .. (595.63,662.67) ;
                    \draw    (596.92,738.67) .. controls (618.55,700.14) and (576.89,726.95) .. (596.27,712.41) ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (533.8,742.13) -- (533.8,791.63) ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (616,748.85) -- (643.47,748.85) -- (643.47,756.67) -- (616,756.67) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (793.74,794.14) -- (802.77,794.14) -- (802.77,813.01) -- (793.74,813.01) -- cycle ; 
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (790.98,812.93) -- (805.53,812.93) -- (805.53,817.67) -- (790.98,817.67) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (970.25,795.44) -- (979.28,795.44) -- (979.28,814.31) -- (970.25,814.31) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (967.49,814.23) -- (982.04,814.23) -- (982.04,818.96) -- (967.49,818.96) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (786.5,791) -- (985.16,791) -- (985.16,797.29) -- (786.5,797.29) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (782.33,785.82) -- (989.47,785.82) -- (989.47,791.43) -- (782.33,791.43) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (819.82,724.35) -- (829.74,724.35) -- (829.74,785.82) -- (819.82,785.82) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (785.35,758.82) -- (823.7,758.82) -- (823.7,785.82) -- (785.35,785.82) -- cycle ;
                    \draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (794.83,777.78) -- (815.95,777.78) -- (815.95,782.81) -- (794.83,782.81) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (805.49,738.42) -- (819.39,738.42) -- (819.39,758.68) -- (805.49,758.68) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (805.49,705.67) -- (806.78,705.67) -- (806.78,739.28) -- (805.49,739.28) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (795.15,727.22) -- (819.71,727.22) -- (819.71,728.94) -- (795.15,728.94) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (795.15,713) -- (796.87,713) -- (796.87,727.22) -- (795.15,727.22) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (800.69,716.18) -- (800.75,718.17) -- (791.95,718.42) -- (791.89,716.43) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (829.74,755.93) -- (888.66,755.93) -- (888.66,778.93) -- (829.74,778.93) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (856.88,759.54) -- (861.94,759.54) -- (861.94,781.95) -- (856.88,781.95) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (855.14,756.24) -- (858.76,759.81) -- (833.5,785.39) -- (829.88,781.82) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (858.76,759.81) -- (862.15,756.02) -- (888.95,779.99) -- (885.56,783.78) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (829.74,778.93) -- (935.2,778.93) -- (935.2,785.82) -- (829.74,785.82) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (889.09,759.11) -- (931.32,759.11) -- (931.32,778.93) -- (889.09,778.93) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (977.81,732.89) -- (978.98,785.74) -- (969.98,785.65) -- (972.19,732.84) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (877.27,618.38) -- (955.95,721.44) -- (919.66,749.15) -- (840.98,646.09) -- cycle ;
                    \draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (898.18,614.2) -- (976.86,717.26) -- (955.95,721.44) -- (877.27,618.38) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (978.76,716.72) -- (941.53,745.06) -- (918.32,749.71) -- (955.55,721.37) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (953.29,718.02) -- (976.22,713.79) -- (979.28,716.82) -- (956.35,721.05) -- cycle ;
                    \draw    (869.27,625.52) -- (944.95,724.58) ;
                    \draw    (858.55,633.12) -- (934.23,732.18) ;
                    \draw    (848.23,641.19) -- (923.9,740.25) ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (868.41,625.44) -- (944.09,724.5) ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (858.94,634.74) -- (934.62,733.8) ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (847.71,642) -- (923.39,741.06) ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (916.58,747.33) -- (953.65,718.48) -- (955.95,721.44) -- (918.88,750.29) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (845.64,653.01) -- (882.45,624.37) -- (885.8,628.67) -- (848.99,657.31) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (860.11,673.07) -- (896.91,644.43) -- (900.26,648.73) -- (863.46,677.37) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (878.39,695.93) -- (915.19,667.29) -- (918.54,671.59) -- (881.74,700.23) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (897.28,721.8) -- (934.08,693.15) -- (937.43,697.46) -- (900.62,726.1) -- cycle ;
                    \draw    (885.95,627.78) -- (848.67,656.81) ;
                    \draw    (900.35,647.87) -- (863.07,676.9) ;
                    \draw    (918.63,670.74) -- (881.35,699.76) ;
                    \draw    (937.98,696.21) -- (900.71,725.24) ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (882.08,624.83) -- (905.01,620.6) -- (908.58,624.47) -- (885.65,628.7) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (896.91,644.43) -- (919.84,640.2) -- (923.42,644.07) -- (900.49,648.3) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (914.97,667.72) -- (937.89,663.49) -- (941.47,667.36) -- (918.54,671.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (933.85,693.58) -- (956.78,689.36) -- (960.36,693.23) -- (937.43,697.46) -- cycle ;
                    \draw    (884.9,629.46) -- (907.82,625.23) ;
                    \draw    (899.79,649.12) -- (922.72,644.89) ;
                    \draw    (918.03,672.41) -- (940.96,668.18) ;
                    \draw    (936.91,698.27) -- (959.84,694.04) ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (935.2,785.82) -- (935.38,760.98) .. controls (935.49,747.26) and (943.01,736.19) .. (952.2,736.26) .. controls (961.38,736.33) and (968.74,747.51) .. (968.64,761.23) -- (968.45,786.07) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (941.63,760.4) -- (936.46,818.4) -- (964.04,818.4) -- (958.87,760.4) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (939.19,813.83) -- (961.03,813.83) -- (961.03,815.99) -- (939.19,815.99) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (941.78,807.8) -- (958.44,807.8) -- (958.44,809.96) -- (941.78,809.96) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (943.07,802.2) -- (957.15,802.2) -- (957.15,804.35) -- (943.07,804.35) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (955.12,764.34) -- (957.86,797.52) -- (941.48,797.36) -- (944.88,764.24) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (838.12,753.86) -- (891.01,711.7) -- (895.63,717.5) -- (842.75,759.66) -- cycle ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (891.11,714.55) -- (847.13,750) ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (829.3,752.64) -- (934.77,752.64) -- (934.77,758.68) -- (829.3,758.68) -- cycle ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (975.88,735.26) -- (976.74,774.91) ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (831.95,754.22) -- (905.21,753.79) ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (825.05,797.89) -- (832.81,797.89) -- (832.81,808.2) -- (825.05,808.2) -- cycle ;
                    \draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (886.24,797.89) -- (894,797.89) -- (894,808.2) -- (886.24,808.2) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (816.43,801.31) -- (902.62,801.31) -- (902.62,808.2) -- (816.43,808.2) -- cycle ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (893.14,764.25) -- (904.34,764.25) -- (904.34,767.7) -- (893.14,767.7) -- cycle ;
                    \draw  [draw opacity=0][dash pattern={on 4.5pt off 4.5pt}] (352.42,373.5) .. controls (391,363.67) and (432.39,358.33) .. (475.47,358.33) .. controls (618.61,358.33) and (743.18,417.27) .. (807.34,504.18) -- (475.47,638.33) -- cycle ; \draw  [dash pattern={on 4.5pt off 4.5pt}] (352.42,373.5) .. controls (391,363.67) and (432.39,358.33) .. (475.47,358.33) .. controls (618.61,358.33) and (743.18,417.27) .. (807.34,504.18) ;  
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (218.26,416.64) -- (313.01,383.38) -- (315.53,390.56) -- (220.77,423.81) -- cycle ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (313.01,383.38) -- (327.72,378.38) -- (338.63,378.27) -- (329.92,384.84) -- (315.21,389.85) -- cycle ;
                    \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (208.7,415.37) -- (221.82,410.38) -- (233.89,415.76) -- (228.44,427.8) -- (215.32,432.79) -- cycle ;
                    \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (211.68,422.76) -- (237.99,412.76) -- (238.82,414.95) -- (212.51,424.95) -- cycle ;
                    \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (201.82,424.71) -- (211.09,421.19) -- (213.37,427.21) -- (204.11,430.73) -- cycle ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (237.99,412.76) -- (294.08,392.89) ;
                    \draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (468.92,301) -- (490.35,338.91) -- (538.26,344.99) -- (503.59,374.5) -- (511.78,416.17) -- (468.92,396.5) -- (426.06,416.17) -- (434.24,374.5) -- (399.57,344.99) -- (447.49,338.91) -- cycle ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (468.92,316.33) -- (483.3,345.12) -- (515.47,349.73) -- (492.19,372.13) -- (497.69,403.77) -- (468.92,388.83) -- (440.14,403.77) -- (445.64,372.13) -- (422.36,349.73) -- (454.53,345.12) -- cycle ;
                    \draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (427.82,316.41) -- (468.02,333.18) -- (509.57,308.56) -- (500.32,353.14) -- (532.37,381.01) -- (486.46,391.79) -- (464.71,433.64) -- (445.59,395.72) -- (400.1,393.72) -- (434.19,359.5) -- cycle ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (437.24,328.52) -- (466.27,342.4) -- (494.49,326.29) -- (489.87,358.27) -- (513.64,379.86) -- (481.76,385.74) -- (468.22,415.2) -- (453.13,386.85) -- (421,383.46) -- (443.56,360.07) -- cycle ;
                    \draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (31.18,859.94) .. controls (31.18,847.6) and (41.18,837.6) .. (53.52,837.6) .. controls (65.86,837.6) and (75.87,847.6) .. (75.87,859.94) .. controls (75.87,872.29) and (65.86,882.29) .. (53.52,882.29) .. controls (41.18,882.29) and (31.18,872.29) .. (31.18,859.94) -- cycle ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (35.27,859.94) .. controls (35.27,849.86) and (43.44,841.69) .. (53.52,841.69) .. controls (63.6,841.69) and (71.78,849.86) .. (71.78,859.94) .. controls (71.78,870.03) and (63.6,878.2) .. (53.52,878.2) .. controls (43.44,878.2) and (35.27,870.03) .. (35.27,859.94) -- cycle ;
                    \draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (298.38,859.52) .. controls (298.38,847.18) and (308.38,837.18) .. (320.72,837.18) .. controls (333.06,837.18) and (343.07,847.18) .. (343.07,859.52) .. controls (343.07,871.86) and (333.06,881.87) .. (320.72,881.87) .. controls (308.38,881.87) and (298.38,871.86) .. (298.38,859.52) -- cycle ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (302.47,859.52) .. controls (302.47,849.44) and (310.64,841.27) .. (320.72,841.27) .. controls (330.8,841.27) and (338.98,849.44) .. (338.98,859.52) .. controls (338.98,869.6) and (330.8,877.78) .. (320.72,877.78) .. controls (310.64,877.78) and (302.47,869.6) .. (302.47,859.52) -- cycle ;
                    \draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (571.98,861.12) .. controls (571.98,848.78) and (581.98,838.78) .. (594.32,838.78) .. controls (606.66,838.78) and (616.67,848.78) .. (616.67,861.12) .. controls (616.67,873.46) and (606.66,883.47) .. (594.32,883.47) .. controls (581.98,883.47) and (571.98,873.46) .. (571.98,861.12) -- cycle ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (576.07,861.12) .. controls (576.07,851.04) and (584.24,842.87) .. (594.32,842.87) .. controls (604.4,842.87) and (612.58,851.04) .. (612.58,861.12) .. controls (612.58,871.2) and (604.4,879.38) .. (594.32,879.38) .. controls (584.24,879.38) and (576.07,871.2) .. (576.07,861.12) -- cycle ;
                    \draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (862.38,861.12) .. controls (862.38,848.78) and (872.38,838.78) .. (884.72,838.78) .. controls (897.06,838.78) and (907.07,848.78) .. (907.07,861.12) .. controls (907.07,873.46) and (897.06,883.47) .. (884.72,883.47) .. controls (872.38,883.47) and (862.38,873.46) .. (862.38,861.12) -- cycle ;
                    \draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (866.47,861.12) .. controls (866.47,851.04) and (874.64,842.87) .. (884.72,842.87) .. controls (894.8,842.87) and (902.98,851.04) .. (902.98,861.12) .. controls (902.98,871.2) and (894.8,879.38) .. (884.72,879.38) .. controls (874.64,879.38) and (866.47,871.2) .. (866.47,861.12) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (860.01,578.14) -- (852.61,584.52) -- (842.53,572.53) -- (843.9,566.58) -- (849.93,566.15) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (843.31,561.46) -- (836.59,553.31) -- (829.89,549.7) -- (832.14,556.97) -- (838.85,565.13) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (880.81,599.05) -- (856.53,581.53) -- (869.04,608.73) -- (865.73,592.71) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (843.31,561.46) -- (874.27,599.09) -- (869.82,602.76) -- (838.85,565.13) -- cycle ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ]   (867.66,592.79) -- (845.73,566.23) ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (610.24,363.78) -- (607.48,378.35) -- (584.18,373.61) -- (580.19,365.24) -- (586.95,359.05) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (574.66,359.73) -- (558.98,356.37) -- (547.61,358.41) -- (557.15,364.93) -- (572.82,368.29) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (654.7,368.98) -- (609.31,371.09) -- (649.86,391.61) -- (630.8,375.69) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (574.66,359.73) -- (646.97,375.22) -- (645.14,383.78) -- (572.82,368.29) -- cycle ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ]   (633.17,373.96) -- (582.04,363.1) ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (760.14,444.51) -- (754.28,452.33) -- (741.87,442.77) -- (741.94,436.65) -- (747.74,434.95) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (740.27,431.79) -- (731.97,425.25) -- (724.65,423.16) -- (728.4,429.78) -- (736.7,436.32) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (784.94,460.49) -- (757.47,448.57) -- (775.5,472.47) -- (768.85,457.53) -- cycle ;
                    \draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (740.27,431.79) -- (778.55,461.94) -- (774.98,466.47) -- (736.7,436.32) -- cycle ;
                    \draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ]   (770.75,457.19) -- (743.65,435.92) ;
                    \draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1.5]  (328.84,569.56) .. controls (331.75,506.11) and (391.92,455.44) .. (465.73,455.44) .. controls (541.4,455.44) and (602.73,508.68) .. (602.73,574.37) .. controls (602.73,574.7) and (602.73,575.04) .. (602.73,575.37) -- (465.73,574.37) -- cycle ; \draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ][dash pattern={on 5.63pt off 4.5pt}][line width=1.5]  (328.84,569.56) .. controls (331.75,506.11) and (391.92,455.44) .. (465.73,455.44) .. controls (541.4,455.44) and (602.73,508.68) .. (602.73,574.37) .. controls (602.73,574.7) and (602.73,575.04) .. (602.73,575.37) ;  
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (405.16,533.75) -- (419.02,533.75) -- (419.02,573.59) -- (405.16,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (419.02,511.31) -- (433.19,511.31) -- (433.19,573.59) -- (419.02,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (433.19,549.1) -- (454.45,549.1) -- (454.45,573.59) -- (433.19,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (454.45,530.2) -- (459.17,530.2) -- (459.17,573.59) -- (454.45,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (456.81,556.19) -- (481.61,556.19) -- (481.61,573.59) -- (456.81,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (481.61,538.47) -- (500.51,538.47) -- (500.51,573.59) -- (481.61,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (368.77,550.28) -- (405.16,550.28) -- (405.16,573.59) -- (368.77,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (500.51,524.3) -- (511.14,524.3) -- (511.14,573.59) -- (500.51,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (511.14,552.64) -- (548.62,552.64) -- (548.62,573.59) -- (511.14,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (548.62,561.78) -- (575.47,561.78) -- (575.47,573.59) -- (548.62,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (354.91,556.2) -- (368.77,556.2) -- (368.77,573.59) -- (354.91,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (383.58,507.76) -- (385.95,507.76) -- (385.95,549.97) -- (383.58,549.97) -- cycle ; 
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (466.26,513.67) -- (468.62,513.67) -- (468.62,555.87) -- (466.26,555.87) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (519.41,521.94) -- (522.95,521.94) -- (522.95,552.33) -- (519.41,552.33) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (386.96,561.93) -- (441.55,561.93) -- (441.55,573.59) -- (386.96,573.59) -- cycle ;
                    \draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (518.57,572.98) -- (519.3,554.96) .. controls (519.7,545.01) and (528.09,537.27) .. (538.05,537.67) .. controls (548,538.07) and (555.74,546.46) .. (555.34,556.41) -- (554.61,574.43) -- cycle ;
                    \draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (316.96,571.13) -- (615.47,571.13) -- (615.47,584.13) -- (316.96,584.13) -- cycle ;
                    \draw (42,844) node [anchor=north west][inner sep=0.75pt]    {$\textcolor[rgb]{0.97,0.91,0.11}{1}$};
                    \draw (308,844) node [anchor=north west][inner sep=0.75pt]    {$\textcolor[rgb]{0.97,0.91,0.11}{2}$};
                    \draw (581,844) node [anchor=north west][inner sep=0.75pt]    {$\textcolor[rgb]{0.97,0.91,0.11}{3}$};
                    \draw (870,844) node [anchor=north west][inner sep=0.75pt]   {$\textcolor[rgb]{0.97,0.91,0.11}{4}$};
                    \draw (454.53,352) node [anchor=north west][inner sep=0.75pt]  {$\textcolor[rgb]{0.97,0.91,0.11}{5}$};
                \end{tikzpicture}
            \end{center}'''

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('Hệ thống phòng không “vòm sắt” là một trong những hệ thống đánh chặn tên lửa từ xa rất nổi tiếng của Isarel. '
                             'Để “vòm sắt” hoạt động được chính xác, người ta trang bị một Radar có khả năng phát hiện tên lửa với bán kính $%s$ km. '
                             'Trong không gian với hệ trục tọa độ $Oxyz$ (đơn vị: km), một hệ thống “vòm sắt” đang ở vị trí gốc tọa độ $O\\left(0;0;0\\right)$ '
                             'và một quả tên lửa của đối phương được phóng lên từ vị trí $A\\left(%s;%s;%s\\right)$ bay theo một quỹ đạo là đường thẳng '
                             'có vectơ chỉ phương là $\\vec{u}=\\left(%s;%s;%s\\right)$.' % (R_val, x_A_val, y_A_val, z_A_val, u_x_val, u_y_val, u_z_val)) + hinhve

            # --- Ý a) NHẬN BIẾT ---
            nb_da_1_d = '\\True Phương trình mặt cầu thể hiện vùng phủ sóng của Radar là: $x^2+y^2+z^2=%s$' % (R_sq)
            nb_da_1_s = 'Phương trình mặt cầu thể hiện vùng phủ sóng của Radar là: $x^2+y^2+z^2=%s$' % (R_val)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = ('Radar có bán kính quét là $R=%s$ km và tâm $O\\left(0;0;0\\right)$.\\\\\n'
                            'Phương trình mặt cầu biểu diễn vùng phủ sóng là: $x^2+y^2+z^2=%s^2$.' % (R_val, R_val))

            # --- Ý b) THÔNG HIỂU ---
            th_da_1_d = '\\True Radar không phát hiện được quả tên lửa ngay tại vị trí nó vừa được phóng lên'
            th_da_1_s = 'Radar phát hiện được quả tên lửa ngay tại vị trí nó vừa được phóng lên'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = ('Khoảng cách từ vị trí phóng $A\\left(%s;%s;%s\\right)$ đến radar $O$ là:\\\\\n'
                            '$OA = \\sqrt{%s^2 + \\left(%s\\right)^2 + %s^2} \\approx %s$ km.\\\\\n'
                            'Vì $OA > R$ nên radar không thể phát hiện tên lửa ngay tại vị trí phóng.' 
                            % (x_A_val, y_A_val, z_A_val, x_A_val, y_A_val, z_A_val, OA_approx_str))

            # --- Ý c) VẬN DỤNG ---
            vd_da_1_d = '\\True Giả sử hệ thống “vòm sắt” gặp trục trặc không thể bắn hạ tên lửa, khi đó vị trí cuối cùng của quả tên lửa xuất hiện trên màn hình radar có tọa độ là $B\\left(%s;%s;%s\\right)$' % (B2_x, B2_y, B2_z)
            vd_da_1_s = 'Giả sử hệ thống “vòm sắt” gặp trục trặc không thể bắn hạ tên lửa, khi đó vị trí cuối cùng của quả tên lửa xuất hiện trên màn hình radar có tọa độ là $B\\left(%s;%s;%s\\right)$' % (B1_x, B1_y, B1_z)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = ('Phương trình đường bay tên lửa: $\\begin{cases} x = %s \\\\ y = %s \\\\ z = %s \\end{cases}$\\\\\n'
                            'Điểm $B$ là giao điểm của đường bay và mặt cầu radar: \\\\ $\\left(%s\\right)^2 + \\left(%s\\right)^2 + %s^2 = %s^2$\\\\\n'
                            'Giải phương trình ta được $t = %s$ hoặc $t = %s$. \\\\\n'
                            'Tại $t = %s \\Rightarrow B\\left(%s;%s;%s\\right)$ và tại $t = %s \\Rightarrow B\\left(%s;%s;%s\\right)$. \\\\\n'
                            'Vị trí cuối cùng của tên lửa là $B\\left(%s;%s;%s\\right)$.' 
                            % (eq_x, eq_y, z_A_val, eq_x, eq_y, z_A_val, R_val, t1, t2, t1, B1_x, B1_y, B1_z, t2, B2_x, B2_y, B2_z, B2_x, B2_y, B2_z))

            # --- Ý d) VẬN DỤNG CAO ---
            vdc_da_1_d = rf'\True Trong suốt quá trình bay, khoảng cách gần nhất từ hệ thống “vòm sắt” đến quả tên lửa bằng ${d_approx_str}$ (Kết quả làm tròn đến hàng phần chục)'
            vdc_da_1_s = rf'Trong suốt quá trình bay, khoảng cách gần nhất từ hệ thống “vòm sắt” đến quả tên lửa bằng ${d_fake_approx_str}$ (Kết quả làm tròn đến hàng phần chục)'

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Chia nhỏ các công thức toán, không để xuống dòng \\ bên trong dấu $
            loigiai_vdc_1 = (
                rf"Khoảng cách gần nhất từ $O$ đến đường thẳng quỹ đạo là: $d(O,\Delta) = \frac{{\left| \left[ \overrightarrow{{OA}}, \vec{{u}} \right] \right|}}{{\left| \vec{{u}} \right|}}.$" + "\n\n"
                rf"Ta có: $\overrightarrow{{OA}} = ({x_A_val}; {y_A_val}; {z_A_val})$, $\vec{{u}} = ({u_x_val}; {u_y_val}; {u_z_val})$." + "\n\n"
                rf"$\left[ \overrightarrow{{OA}}, \vec{{u}} \right] = ({cross_x}; {cross_y}; {cross_z})$" + "\n\n"
                rf"$\Rightarrow \left| \left[ \overrightarrow{{OA}}, \vec{{u}} \right] \right| = \sqrt{{({cross_x})^2 + ({cross_y})^2 + {cross_z}^2}} = {latex(cross_mag_sympy)}$." + "\n\n"
                rf"Khi đó: $\left| \vec{{u}} \right| = \sqrt{{({u_x_val})^2 + {u_y_val}^2}} = {latex(u_mag_sympy)}$." + "\n\n"
                rf"Suy ra $d = \frac{{{latex(cross_mag_sympy)}}}{{{latex(u_mag_sympy)}}} = {latex(d_sympy)} \approx {d_approx_str}$."
            )                
            # --- HÀM ĐẾM ĐÁP ÁN ĐÚNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # --- VÒNG LẶP ĐẢM BẢO SỐ CÂU ĐÚNG TỪ 1 ĐẾN 3 ---
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán vào list để xáo trộn
            list_nb_1 = [nb_sel]
            list_th_1 = [th_sel]
            list_vd_1 = [vd_sel]
            list_vdc_1 = [vdc_sel]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # --- XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

