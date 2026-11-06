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


def bt_dang18_p3_b2_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp để tạo ra bộ số nguyên đẹp cho bài toán
                while True:
                    u1 = randint(1, 6) * random.choice([-1, 1])
                    u2 = randint(1, 6) * random.choice([-1, 1])
                    u3 = randint(1, 3) * random.choice([-1, 1])
                    a0 = randint(-4, 4)
                    b0 = randint(-4, 4)
                    S = random.choice([10, 20, 50, 100])

                    # Tọa độ điểm H(a,b,c) - hình chiếu của O lên d
                    a = a0 * u3 * S
                    b = b0 * u3 * S
                    c = -(u1 * a0 + u2 * b0) * S

                    t_val = random.choice([20, 30, 40, 50, 100])
                    M_x = a - t_val * u1
                    M_y = b - t_val * u2
                    M_z = c - t_val * u3

                    k_val = random.choice([10, 20, 30, 40, 50])
                    if k_val == t_val:
                        continue

                    N_x = M_x + k_val * u1
                    N_y = M_y + k_val * u2
                    N_z = M_z + k_val * u3

                    if M_x == N_x and M_y == N_y and M_z == N_z:
                        continue
                    if a == 0 and b == 0 and c == 0:
                        continue
                    break

                vec_MN_x = N_x - M_x
                vec_MN_y = N_y - M_y
                vec_MN_z = N_z - M_z

                gcd_val = math.gcd(math.gcd(abs(vec_MN_x), abs(vec_MN_y)), abs(vec_MN_z))
                v_x = vec_MN_x // gcd_val
                v_y = vec_MN_y // gcd_val
                v_z = vec_MN_z // gcd_val

                # Đảm bảo hệ số hoành độ v_x của vecto chỉ phương ưu tiên mang dấu dương
                if v_x < 0 or (v_x == 0 and v_y < 0) or (v_x == 0 and v_y == 0 and v_z < 0):
                    v_x = -v_x
                    v_y = -v_y
                    v_z = -v_z

                t_prime = -(v_x * M_x + v_y * M_y + v_z * M_z) // (v_x**2 + v_y**2 + v_z**2)
                H_x = M_x + v_x * t_prime
                H_y = M_y + v_y * t_prime
                H_z = M_z + v_z * t_prime

                kq = H_x + H_y + H_z

                # Các đáp án trắc nghiệm
                da = kq
                s = [kq + 100, kq - 100, kq + 200, kq - 200, kq + 50, kq - 50, kq + 150, kq - 150]
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Các hàm hỗ trợ định dạng hiển thị chuỗi
                def fmt_t(c):
                    if c == 1: return "+ t"
                    if c == -1: return "- t"
                    if c > 0: return "+ %st" % c
                    return "- %st" % abs(c)

                str_x = "%s %s" % (M_x, fmt_t(v_x))
                str_y = "%s %s" % (M_y, fmt_t(v_y))
                str_z = "%s %s" % (M_z, fmt_t(v_z))

                def fmt_plane(a_p, b_p, c_p):
                    res = ""
                    for val, var in [(a_p, 'x'), (b_p, 'y'), (c_p, 'z')]:
                        if val == 0: continue
                        sign = "+" if val > 0 else "-"
                        abs_val = abs(val)
                        val_str = "" if abs_val == 1 else str(abs_val)
                        if res == "":
                            res += "%s%s%s" % ("-" if val < 0 else "", val_str, var)
                        else:
                            res += " %s %s%s" % (sign, val_str, var)
                    return res + " = 0"

                plane_eq = fmt_plane(v_x, v_y, v_z)

                sign_y = "+" if v_y > 0 else "-"
                sign_z = "+" if v_z > 0 else "-"

                sum_sq = v_x**2 + v_y**2 + v_z**2
                sum_prod = v_x * M_x + v_y * M_y + v_z * M_z

                str_eq_t = "%st" % sum_sq
                if sum_prod > 0:
                    str_eq_t += " + %s" % sum_prod
                elif sum_prod < 0:
                    str_eq_t += " - %s" % abs(sum_prod)

                str_Hy = "(%s)" % H_y if H_y < 0 else "%s" % H_y
                str_Hz = "(%s)" % H_z if H_z < 0 else "%s" % H_z
                hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\tikzset {_8rlwn2ubm/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-272 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_mvqaskakr}{150bp}{rgb(0bp)=(1,1,1);
            			rgb(37.5bp)=(1,1,1);
            			rgb(62.5bp)=(0.57,0.95,0.97);
            			rgb(100bp)=(0.57,0.95,0.97)}
            		\tikzset{every picture/.style={line width=0.75pt}} 
            		\draw  [draw opacity=0][shading=_mvqaskakr,_8rlwn2ubm] (42.33,17.6) -- (545,17.6) -- (545,239.62) -- (42.33,239.62) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (42.33,239.62) -- (545,239.62) -- (545,254.64) -- (42.33,254.64) -- cycle ;
            		\draw  [draw opacity=0] (120.67,194.07) -- (113.69,209.95) -- (110.81,208.68) -- (117.78,192.8) -- cycle ; \draw   (120.67,194.07) -- (117.78,192.8)(119.5,196.72) -- (116.62,195.45)(118.34,199.37) -- (115.45,198.1)(117.17,202.02) -- (114.29,200.75)(116.01,204.67) -- (113.13,203.4)(114.85,207.32) -- (111.96,206.05) ; \draw   (120.67,194.07) -- (113.69,209.95)(118.02,192.9) -- (111.04,208.78) ; \draw    ;
            		\draw  [fill={rgb, 255:red, 120; green, 128; blue, 138 }  ,fill opacity=1 ] (99.16,187.65) .. controls (99.97,187.07) and (100.78,186.62) .. (101.57,186.27) .. controls (108.42,202.51) and (116.34,200.96) .. (121.63,192.91) .. controls (122.37,193.36) and (123.12,193.8) .. (123.86,194.21) .. controls (116.34,203.47) and (109,205.79) .. (99.16,187.65) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (118.11,242.2) -- (118.11,250.4) -- (88.44,246.78) -- (88.2,239.06) -- cycle ;
            		\draw  [fill={rgb, 255:red, 162; green, 166; blue, 171 }  ,fill opacity=1 ] (139.58,236.41) -- (140.55,243.4) -- (118.11,250.4) -- (118.11,242.2) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 161; blue, 171 }  ,fill opacity=1 ] (139.58,236.41) -- (118.11,242.2) -- (88.2,239.06) -- (90.13,231.58) -- (107.98,228.69) -- (131.86,229.65) -- cycle ;
            		\draw    (88.44,243.89) -- (117.82,247.07) ;
            		\draw    (117.82,247.07) -- (140.31,240.99) ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (107.98,240.99) -- (107.98,243.89) -- (98.09,242.92) -- (98.09,240.27) -- cycle ;
            		\draw  [fill={rgb, 255:red, 153; green, 159; blue, 166 }  ,fill opacity=1 ] (133.07,238.34) -- (133.07,240.99) -- (125.35,242.92) -- (125.11,240.27) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (134.03,234.72) -- (116.9,239.3) -- (115.46,224.35) -- (124.87,222.9) -- cycle ;
            		\draw  [fill={rgb, 255:red, 140; green, 145; blue, 150 }  ,fill opacity=1 ] (124.87,222.9) -- (115.46,224.35) -- (115.7,221.69) -- (124.87,220.24) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (116.9,239.3) -- (94.71,237.13) -- (103.15,224.1) -- (115.46,224.35) -- cycle ;
            		\draw  [fill={rgb, 255:red, 132; green, 137; blue, 143 }  ,fill opacity=1 ] (115.46,224.35) -- (103.15,224.1) -- (103.15,221.69) -- (115.46,221.69) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (94.71,237.13) -- (94.71,232.31) -- (100.98,222.66) -- (103.15,224.1) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (103.15,224.1) -- (100.98,222.66) -- (101.22,220) -- (103.15,221.69) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (134.03,234.72) -- (116.9,239.3) -- (116.66,236.41) -- (132.34,232.31) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (116.9,239.3) -- (94.71,237.13) -- (96.4,234.48) -- (116.66,236.41) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (94.71,237.13) -- (94.71,232.31) -- (96.64,230.38) -- (96.4,234.48) -- cycle ;
            		\draw  [fill={rgb, 255:red, 128; green, 133; blue, 138 }  ,fill opacity=1 ] (129.21,233.27) -- (129.69,235.93) -- (122.21,237.86) -- (121.97,235.2) -- cycle ;
            		\draw  [fill={rgb, 255:red, 126; green, 132; blue, 140 }  ,fill opacity=1 ] (111.48,235.8) -- (111.48,238.7) -- (101.59,237.73) -- (101.59,235.08) -- cycle ;
            		\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (135.48,219.52) -- (98.33,222.17) -- (89.4,217.59) -- (120.04,214.94) -- cycle ;
            		\draw    (84.82,226.76) -- (93.87,219.88) ;
            		\draw    (87.23,228.21) -- (96.28,221.33) ;
            		\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (87.23,228.21) -- (83.52,229.05) -- (80.62,227.72) -- (84.48,226.83) -- cycle ;
            		\draw    (93.5,236.17) -- (87.23,228.21) ;
            		\draw    (90.27,237.73) -- (83.52,229.05) ;
            		\draw    (92.68,224.1) -- (90.25,222.54) ;
            		\draw    (90.99,225.55) -- (88.32,223.98) ;
            		\draw    (89.19,227) -- (86.39,225.43) ;
            		\draw    (94.73,222.54) -- (92.3,220.97) ;
            		\draw    (88.46,229.65) -- (84.94,230.62) ;
            		\draw    (89.43,231.1) -- (85.9,232.07) ;
            		\draw    (90.42,232.43) -- (86.89,233.39) ;
            		\draw    (91.72,233.75) -- (88.2,234.72) ;
            		\draw    (92.92,235.2) -- (89.4,236.17) ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (105.08,218.7) -- (101.22,216.87) -- (101.22,208.33) -- (105.08,208.57) -- cycle ;
            		\draw  [fill={rgb, 255:red, 128; green, 133; blue, 138 }  ,fill opacity=1 ] (111.84,218.46) -- (105.08,218.7) -- (105.08,208.57) -- (111.84,208.33) -- cycle ;
            		\draw  [fill={rgb, 255:red, 128; green, 133; blue, 138 }  ,fill opacity=1 ] (123.42,217.74) -- (111.84,218.46) -- (111.84,208.33) -- (123.68,208.18) -- cycle ;
            		\draw    (89.4,212.91) -- (89.4,217.59) ;
            		\draw    (98.33,217.49) -- (98.33,222.17) ;
            		\draw    (135.48,214.84) -- (135.48,219.52) ;
            		\draw    (100.74,212.19) -- (89.4,212.91) ;
            		\draw    (89.4,212.91) -- (98.33,217.49) ;
            		\draw    (98.33,217.49) -- (135.48,214.84) ;
            		\draw    (123.42,211.46) -- (135.48,214.84) ;
            		\draw    (92.3,212.67) -- (92.06,217.25) ;
            		\draw    (95.07,212.55) -- (94.83,217.13) ;
            		\draw    (98.57,212.03) -- (98.33,216.61) ;
            		\draw    (92.14,214.28) -- (91.9,218.86) ;
            		\draw    (95.51,216.05) -- (95.27,220.63) ;
            		\draw    (101.71,217.35) -- (101.46,221.93) ;
            		\draw    (105.32,217.17) -- (105.08,221.76) ;
            		\draw    (108.7,217.01) -- (108.46,221.6) ;
            		\draw    (111.76,217.01) -- (111.52,221.6) ;
            		\draw    (115.14,216.37) -- (114.89,220.95) ;
            		\draw    (118.83,216.37) -- (118.59,220.95) ;
            		\draw    (122.37,215.89) -- (122.13,220.47) ;
            		\draw    (125.59,215.66) -- (125.35,220.24) ;
            		\draw    (128.81,215.24) -- (128.56,219.83) ;
            		\draw    (132.34,215.24) -- (132.1,219.83) ;
            		\draw    (125.75,212.35) -- (125.51,216.93) ;
            		\draw    (128,212.64) -- (127.76,217.23) ;
            		\draw    (130.9,213.79) -- (130.66,218.38) ;
            		\draw   (102.61,213.17) .. controls (102.61,212.1) and (102.93,211.24) .. (103.33,211.24) .. controls (103.73,211.24) and (104.05,212.1) .. (104.05,213.17) .. controls (104.05,214.23) and (103.73,215.1) .. (103.33,215.1) .. controls (102.93,215.1) and (102.61,214.23) .. (102.61,213.17) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (105.08,208.57) -- (101.22,208.33) -- (88.74,187.65) -- (92.79,187.65) -- cycle ;
            		\draw  [fill={rgb, 255:red, 109; green, 118; blue, 128 }  ,fill opacity=1 ] (109.77,208.49) -- (105.08,208.57) -- (92.79,187.65) -- (94.53,186.87) -- cycle ;
            		\draw  [fill={rgb, 255:red, 108; green, 114; blue, 121 }  ,fill opacity=1 ] (123.68,208.18) -- (119.81,208.3) -- (126.95,187.26) -- (130.23,187.26) -- cycle ;
            		\draw  [fill={rgb, 255:red, 109; green, 118; blue, 128 }  ,fill opacity=1 ] (119.81,208.3) -- (115.12,208.37) -- (124.63,187.07) -- (126.95,187.26) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (92.6,187.89) -- (88.74,187.65) -- (89.89,186.49) -- (94.53,186.87) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (98.19,188.8) .. controls (99.01,188.23) and (99.81,187.77) .. (100.6,187.43) .. controls (107.46,203.67) and (115.37,202.12) .. (120.67,194.07) .. controls (121.41,194.52) and (122.15,194.96) .. (122.9,195.37) .. controls (115.37,204.63) and (108.04,206.95) .. (98.19,188.8) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (124.88,189.11) .. controls (118.74,194.36) and (109.04,195.16) .. (100.8,190.46) .. controls (97.51,188.58) and (94.86,186.05) .. (92.95,183.17) -- (96.25,181.43) .. controls (97.83,183.71) and (99.99,185.72) .. (102.65,187.23) .. controls (109.4,191.09) and (117.28,190.57) .. (122.27,186.46) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (97.81,183.21) -- (95.68,188.23) -- (90.86,182.82) -- (93.18,177.8) -- cycle ;
            		\draw [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ]   (82.07,158.24) .. controls (90.95,176.53) and (97.51,189.12) .. (135.14,190.33) ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (73.12,142.31) .. controls (77.08,135.26) and (98.97,140.04) .. (122.02,152.98) .. controls (145.07,165.92) and (160.54,182.13) .. (156.58,189.18) .. controls (152.62,196.23) and (130.73,191.45) .. (107.68,178.5) .. controls (84.64,165.56) and (69.16,149.35) .. (73.12,142.31) -- cycle ;
            		\draw    (72.42,144.49) .. controls (70.73,185.26) and (135.14,206.01) .. (153.24,192.02) ;
            		\draw    (72.42,144.49) .. controls (76.28,176.34) and (132.73,202.63) .. (153.24,192.02) ;
            		\draw    (93.46,169.15) -- (91.72,173.92) ;
            		\draw    (91.72,173.92) -- (94.85,182.85) ;
            		\draw    (104.5,176.82) -- (102.33,181.89) ;
            		\draw    (102.33,181.89) -- (102.65,187.23) ;
            		\draw    (84.53,162.15) -- (83.76,166.93) ;
            		\draw    (83.76,166.93) -- (86.41,176.82) ;
            		\draw    (78.02,156.6) -- (77.48,158.97) ;
            		\draw    (77.48,158.97) -- (78.21,166.45) ;
            		\draw    (114.88,182.37) -- (112.22,186.47) ;
            		\draw    (112.22,186.47) -- (107.64,189.12) ;
            		\draw    (126.95,187.26) -- (123.8,191.29) ;
            		\draw    (123.8,191.29) -- (116.81,192.98) ;
            		\draw    (139.01,191.36) -- (136.83,193.95) ;
            		\draw    (136.83,193.95) -- (129.11,195.88) ;
            		\draw    (146.25,192.57) -- (143.83,194.91) ;
            		\draw    (83.76,166.93) -- (78.21,166.45) ;
            		\draw    (91.72,173.92) -- (86.41,176.82) ;
            		\draw    (102.33,181.89) -- (94.85,182.85) ;
            		\draw    (112.22,186.47) -- (102.65,187.23) ;
            		\draw    (112.22,186.47) -- (116.81,192.98) ;
            		\draw    (123.8,191.29) -- (129.11,195.88) ;
            		\draw    (136.83,193.95) -- (139.49,196.12) ;
            		\draw    (143.83,194.91) -- (139.49,196.12) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (104.5,176.82) .. controls (107.88,172.72) and (119.46,159.45) .. (123.56,154.14) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (105.71,177.54) .. controls (109.81,174.17) and (125.49,163.55) .. (130.32,158.24) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (107.68,178.5) .. controls (115.12,175.61) and (130.32,168.13) .. (137.07,163.07) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (109.33,178.99) .. controls (118.74,178.03) and (135.14,172.72) .. (143.1,167.41) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (112.47,180.44) .. controls (117.05,180.92) and (140.93,178.03) .. (148.65,173.2) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (114.88,182.37) .. controls (119.46,182.85) and (141.9,181.64) .. (153.24,178.75) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (118.26,183.82) .. controls (122.84,184.3) and (144.79,185.5) .. (156.85,185.99) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (118.26,183.82) .. controls (124.29,187.43) and (141.9,190.33) .. (153.96,190.81) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (103.3,175.61) .. controls (105.47,170.79) and (112.32,156.27) .. (115.6,150.04) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (102.09,174.41) .. controls (102.57,169.82) and (104.12,152.17) .. (107.4,145.94) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (100.16,174.17) .. controls (99.44,171.03) and (96.54,151.01) .. (98.47,142.8) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (98.47,172.96) .. controls (96.54,170.06) and (89.55,148.83) .. (91.48,140.63) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (95.34,170.79) .. controls (93.41,167.89) and (82.55,152.45) .. (82.79,139.18) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (91.48,167.89) .. controls (89.55,165) and (76.28,155.35) .. (74.59,141.6) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (95.34,170.79) .. controls (92.68,163.07) and (118.5,175.37) .. (112.47,180.44) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (87.13,163.79) .. controls (85.2,146.42) and (141.17,176.58) .. (123.56,185.99) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (78.45,154.87) .. controls (78.07,144.36) and (102.56,150.19) .. (118.74,160.66) .. controls (134.91,171.12) and (153.96,187.19) .. (133.7,189.12) ;
            		\draw  [fill={rgb, 255:red, 119; green, 125; blue, 132 }  ,fill opacity=1 ] (108.83,172.92) -- (106.44,177.32) .. controls (106.29,177.58) and (105.48,177.41) .. (104.61,176.94) .. controls (103.74,176.47) and (103.16,175.87) .. (103.3,175.61) -- (105.69,171.21) .. controls (105.83,170.95) and (106.65,171.12) .. (107.51,171.59) .. controls (108.38,172.06) and (108.97,172.66) .. (108.83,172.92) .. controls (108.68,173.18) and (107.87,173.01) .. (107,172.54) .. controls (106.14,172.06) and (105.55,171.47) .. (105.69,171.21) ;
            		\draw  [fill={rgb, 255:red, 119; green, 125; blue, 132 }  ,fill opacity=1 ] (111.95,165.63) -- (108.08,172.76) .. controls (108,172.91) and (107.51,172.81) .. (107,172.54) .. controls (106.49,172.26) and (106.14,171.91) .. (106.22,171.75) -- (110.1,164.62) .. controls (110.18,164.47) and (110.66,164.57) .. (111.18,164.85) .. controls (111.69,165.13) and (112.04,165.48) .. (111.95,165.63) .. controls (111.87,165.79) and (111.39,165.68) .. (110.87,165.41) .. controls (110.36,165.13) and (110.01,164.78) .. (110.1,164.62) ;
            		\draw  [fill={rgb, 255:red, 167; green, 172; blue, 177 }  ,fill opacity=1 ] (117.82,144.81) .. controls (117.82,142.15) and (119.97,140.01) .. (122.62,140.01) .. controls (125.27,140.01) and (127.42,142.15) .. (127.42,144.81) .. controls (127.42,147.46) and (125.27,149.61) .. (122.62,149.61) .. controls (119.97,149.61) and (117.82,147.46) .. (117.82,144.81) -- cycle ;
            		\draw  [fill={rgb, 255:red, 131; green, 136; blue, 142 }  ,fill opacity=1 ] (120.19,144.11) -- (118.74,147.24) -- (84.53,162.15) -- (83.76,160.99) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (125.25,145.8) -- (123.8,148.69) -- (133.7,189.12) -- (135.14,190.33) -- cycle ;
            		\draw  [fill={rgb, 255:red, 113; green, 117; blue, 123 }  ,fill opacity=1 ] (127.42,146.52) -- (125.98,148.21) -- (141.66,179.71) -- (143.1,180.92) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 209; blue, 220 }  ,fill opacity=1 ] (117.77,143.38) -- (116.81,145.8) -- (91.77,150.33) -- (90.99,149.17) -- cycle ;
            		\draw  [draw opacity=0] (91.02,193.59) -- (100.17,208.32) -- (97.49,209.99) -- (88.34,195.25) -- cycle ; \draw   (91.02,193.59) -- (88.34,195.25)(92.54,196.05) -- (89.87,197.71)(94.07,198.51) -- (91.4,200.17)(95.6,200.97) -- (92.92,202.63)(97.13,203.43) -- (94.45,205.09)(98.65,205.89) -- (95.98,207.55) ; \draw   (91.02,193.59) -- (100.17,208.32)(88.56,195.12) -- (97.71,209.85) ; \draw    ;
            		\draw  [draw opacity=0] (89.89,186.49) -- (88.01,193) -- (84.96,192.11) -- (86.85,185.61) -- cycle ; \draw   (89.89,186.49) -- (86.85,185.61)(89.09,189.27) -- (86.04,188.39)(88.28,192.05) -- (85.24,191.17) ; \draw   (89.89,186.49) -- (88.01,193)(87.11,185.68) -- (85.23,192.19) ; \draw    ;
            		\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (91.03,193.43) -- (88.56,195.12) -- (85.2,193.08) -- (88.28,192.05) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.23 ] (124.87,222.9) -- (128.18,227.64) -- (115.84,230.33) -- (115.46,224.35) -- cycle ;
            		\draw   (119.92,229.17) .. controls (119.74,228.17) and (120.73,227.14) .. (122.14,226.88) .. controls (123.56,226.62) and (124.85,227.22) .. (125.04,228.23) .. controls (125.22,229.23) and (124.23,230.26) .. (122.81,230.52) .. controls (121.4,230.78) and (120.1,230.17) .. (119.92,229.17) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.24 ] (115.46,224.35) -- (115.84,230.33) -- (110.54,233.95) -- (100.16,228.88) -- (102.33,225.5) -- (109.57,228.64) -- (109.31,224.22) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.23 ] (102.33,225.5) -- (100.16,228.88) -- (96.64,230.38) -- (100.16,224.3) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.23 ] (94.98,192.2) -- (102.46,204.74) -- (98.12,204.02) -- (91.84,191.96) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.23 ] (120.19,189.32) -- (123.8,191.29) -- (115.6,193.18) -- (109.57,193.42) -- (100.8,190.46) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.23 ] (122.36,194.14) -- (121.15,197.52) -- (115.6,202.83) -- (109.33,201.62) -- (103.54,196.65) -- (112.47,199.93) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.33 ] (74.59,141.6) .. controls (80.14,136.72) and (93.17,140.58) .. (98.47,142.8) .. controls (98.71,154.09) and (97.27,164.23) .. (104.61,176.94) .. controls (87.13,165.19) and (64.94,146.42) .. (74.59,141.6) -- cycle ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.12 ][line width=2.25]    (91.77,150.33) .. controls (103.06,161.57) and (119.46,173.64) .. (141.66,179.71) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.12 ][line width=2.25]    (114.88,182.37) .. controls (125.49,184.25) and (135.63,182.08) .. (141.66,179.71) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.12 ][line width=2.25]    (133.7,189.12) .. controls (143.59,185.46) and (140.21,182.8) .. (142.38,180.2) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (42.33,254.64) -- (545,254.64) -- (545,259.6) -- (42.33,259.6) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (122.12,56.25) .. controls (125.92,56.25) and (129,59.33) .. (129,63.12) .. controls (129,66.92) and (125.92,70) .. (122.12,70) -- (88.88,70) .. controls (85.08,70) and (82,66.92) .. (82,63.12) .. controls (82,59.33) and (85.08,56.25) .. (88.88,56.25) .. controls (88.88,52.24) and (92.12,49) .. (96.13,49) .. controls (97.47,49) and (98.73,49.36) .. (99.81,50) .. controls (101.8,47.11) and (105.13,45.22) .. (108.89,45.22) .. controls (114.98,45.22) and (119.92,50.16) .. (119.92,56.25) -- (122.12,56.25) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (227.12,153.25) .. controls (230.92,153.25) and (234,156.33) .. (234,160.12) .. controls (234,163.92) and (230.92,167) .. (227.12,167) -- (193.88,167) .. controls (190.08,167) and (187,163.92) .. (187,160.12) .. controls (187,156.33) and (190.08,153.25) .. (193.88,153.25) .. controls (193.88,149.24) and (197.12,146) .. (201.13,146) .. controls (202.47,146) and (203.73,146.36) .. (204.81,147) .. controls (206.8,144.11) and (210.13,142.22) .. (213.89,142.22) .. controls (219.98,142.22) and (224.92,147.16) .. (224.92,153.25) -- (227.12,153.25) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (315.88,169.76) .. controls (318.71,169.76) and (321,172.05) .. (321,174.88) .. controls (321,177.71) and (318.71,180) .. (315.88,180) -- (291.12,180) .. controls (288.29,180) and (286,177.71) .. (286,174.88) .. controls (286,172.05) and (288.29,169.76) .. (291.12,169.76) .. controls (291.12,166.78) and (293.54,164.36) .. (296.52,164.36) .. controls (297.52,164.36) and (298.46,164.63) .. (299.26,165.1) .. controls (300.74,162.96) and (303.22,161.55) .. (306.03,161.55) .. controls (310.56,161.55) and (314.24,165.23) .. (314.24,169.76) -- (315.88,169.76) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (456.12,150.25) .. controls (459.92,150.25) and (463,153.33) .. (463,157.12) .. controls (463,160.92) and (459.92,164) .. (456.12,164) -- (422.88,164) .. controls (419.08,164) and (416,160.92) .. (416,157.12) .. controls (416,153.33) and (419.08,150.25) .. (422.88,150.25) .. controls (422.88,146.24) and (426.12,143) .. (430.13,143) .. controls (431.47,143) and (432.73,143.36) .. (433.81,144) .. controls (435.8,141.11) and (439.13,139.22) .. (442.89,139.22) .. controls (448.98,139.22) and (453.92,144.16) .. (453.92,150.25) -- (456.12,150.25) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (190.78,61.57) .. controls (195.87,61.57) and (200,65.69) .. (200,70.78) .. controls (200,75.87) and (195.87,80) .. (190.78,80) -- (146.22,80) .. controls (141.13,80) and (137,75.87) .. (137,70.78) .. controls (137,65.69) and (141.13,61.57) .. (146.22,61.57) .. controls (146.22,56.2) and (150.57,51.84) .. (155.94,51.84) .. controls (157.74,51.84) and (159.43,52.33) .. (160.87,53.19) .. controls (163.54,49.32) and (168,46.79) .. (173.05,46.79) .. controls (181.21,46.79) and (187.83,53.41) .. (187.83,61.57) -- (190.78,61.57) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (527.1,80.2) .. controls (531.46,80.2) and (535,83.74) .. (535,88.1) .. controls (535,92.46) and (531.46,96) .. (527.1,96) -- (488.9,96) .. controls (484.54,96) and (481,92.46) .. (481,88.1) .. controls (481,83.74) and (484.54,80.2) .. (488.9,80.2) .. controls (488.9,75.6) and (492.63,71.87) .. (497.23,71.87) .. controls (498.78,71.87) and (500.22,72.29) .. (501.46,73.02) .. controls (503.75,69.71) and (507.57,67.53) .. (511.9,67.53) .. controls (518.9,67.53) and (524.57,73.2) .. (524.57,80.2) -- (527.1,80.2) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (214,117.6) -- (338,85.6) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (271,107.6) -- (345,87.6) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (258,101.6) -- (337.69,80.29) ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (451.52,71.66) -- (448.42,73.3) -- (435.96,76.41) -- (434.53,75.86) -- (434.9,74.4) -- (447.69,71.11) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (406.03,78.27) .. controls (416.99,72.79) and (437.6,69.83) .. (443.96,75.31) .. controls (436.32,85.18) and (410.41,84.61) .. (405.88,82.94) .. controls (404.73,81.03) and (404.65,79.44) .. (406.03,78.27) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (443.96,75.31) .. controls (435.96,83.17) and (423.9,84.81) .. (406.04,83.21) .. controls (403.43,80.24) and (407.09,77.14) .. (405.99,72.94) .. controls (415.74,71.69) and (422.99,71.15) .. (427.92,72.57) .. controls (424.99,80.98) and (436.69,78.42) .. (443.96,75.31) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (452.36,52.65) -- (454.67,52.65) -- (454.67,60.33) -- (452.36,60.33) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (477.47,46.26) -- (493.84,45.89) -- (474,49.18) -- cycle ;
            		\draw  [fill={rgb, 255:red, 98; green, 110; blue, 111 }  ,fill opacity=1 ] (373.39,81.16) -- (369.3,88.47) -- (359.62,88.28) -- (359.98,82.62) -- cycle ;
            		\draw  [fill={rgb, 255:red, 54; green, 59; blue, 60 }  ,fill opacity=1 ] (349.57,71.47) .. controls (347.01,75.49) and (349.28,79.77) .. (351.47,83.97) .. controls (343.9,86.09) and (337.51,76.96) .. (349.57,71.47) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (377.78,56.13) .. controls (390.93,52.11) and (394.95,49.91) .. (417.06,40.6) .. controls (425.65,40.41) and (438.99,40.05) .. (454.52,37.12) .. controls (460.47,38.43) and (477.91,42.42) .. (481.56,47.17) .. controls (476.63,53.2) and (449.95,59.41) .. (429.67,62.16) .. controls (424.74,61.97) and (420.72,60.22) .. (416.88,60.15) .. controls (412.13,60.15) and (410.67,60.51) .. (402.63,59.96) .. controls (391.12,62.16) and (391.12,63.43) .. (377.6,68.37) .. controls (357.68,70.74) and (352.2,64.71) .. (377.78,56.13) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (351.87,70.27) .. controls (377.23,72.79) and (383.63,63.65) .. (402.63,59.96) .. controls (406.28,60.4) and (411.22,60.58) .. (416.49,59.78) .. controls (421.96,61.1) and (429.02,61.88) .. (432.78,62.78) .. controls (428.76,64.24) and (430.12,67.2) .. (426.93,72.1) .. controls (422.47,75.09) and (409.68,78.93) .. (385.82,80.68) .. controls (370.56,81.6) and (367.36,84.52) .. (351.47,83.97) .. controls (346.9,80.32) and (345.99,73.74) .. (351.87,70.27) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (321.8,78.14) -- (353.59,74.43) -- (356.22,76.17) -- (345.69,77.48) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (319.75,63.43) -- (387.02,59.84) -- (380.78,62.7) -- (326.51,64.17) -- cycle ;
            		\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (387.02,59.84) -- (443.45,48.09) ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (380.78,62.7) -- (357.83,71.47) -- (314.63,65.63) -- (320.66,63.43) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (327.35,60.51) -- (323.77,62.7) -- (311.89,66.54) -- (310.47,65.99) -- (310.83,64.53) -- (323.51,60.51) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (367.18,53.2) -- (377.78,56.13) -- (363.89,61.24) -- (349.28,61.79) -- (349.09,59.23) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (351.47,31.28) -- (367.18,53.2) -- (350.04,58.87) -- (342.88,34.38) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (350.55,29.27) -- (351.47,31.28) -- (341.97,34.57) -- (341.24,32.92) -- cycle ;
            		\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (349.82,74.76) -- (357.83,71.47) ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (341.42,64.35) -- (340.51,67.82) -- (329.54,70.56) -- (330.09,66.91) -- cycle ;
            		\draw  [fill={rgb, 255:red, 147; green, 152; blue, 152 }  ,fill opacity=1 ] (417.06,40.6) .. controls (426.38,30.98) and (443.01,24.77) .. (454.52,37.12) .. controls (438.99,40.12) and (433.14,39.75) .. (417.06,40.6) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (416.49,59.78) .. controls (424.05,60.47) and (422.41,61.02) .. (432.28,62.48) .. controls (426.43,67.78) and (432.64,74) .. (418.75,71.62) .. controls (414.8,69.98) and (410.35,64.49) .. (416.49,59.78) -- cycle ;
            		\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (395.61,64.68) -- (415.46,59.82) ;
            		\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (402.56,62.85) -- (402.63,59.96) ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.54 ] (417.36,61.02) .. controls (424.92,61.72) and (420.83,61.57) .. (430.69,63.03) .. controls (424.85,68.33) and (431.97,72.35) .. (419.73,70.71) .. controls (415.35,69.06) and (411.69,63.4) .. (417.36,61.02) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (351.47,31.28) -- (353.08,33.51) -- (343.57,36.98) -- (342.88,34.38) -- cycle ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (351.87,34.13) -- (363.86,54.52) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (346.15,35.83) -- (354.54,57.44) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 76; green, 86; blue, 87 }  ,fill opacity=1 ] (354.46,52.75) .. controls (354.36,52.41) and (354.55,52.05) .. (354.89,51.95) -- (359.77,50.5) .. controls (360.11,50.4) and (360.47,50.59) .. (360.57,50.93) -- (361.12,52.79) .. controls (361.22,53.13) and (361.03,53.49) .. (360.69,53.59) -- (355.81,55.04) .. controls (355.47,55.14) and (355.11,54.95) .. (355.01,54.61) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (350.58,42.83) -- (354.83,41.01) -- (355.87,43.44) -- (351.62,45.26) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (350.73,43.13) -- (354.93,41.33) -- (355.05,41.59) -- (350.85,43.4) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (351,43.71) -- (355.17,41.93) -- (355.27,42.17) -- (351.11,43.95) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (351.19,44.23) -- (355.43,42.41) -- (355.55,42.68) -- (351.31,44.5) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (351.41,44.76) -- (355.63,42.95) -- (355.74,43.21) -- (351.52,45.02) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 24; green, 81; blue, 149 }  ,fill opacity=1 ] (353.43,41.61) -- (354.83,41.01) -- (355.43,42.41) -- (354.03,43.01) -- cycle ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (363.86,54.52) -- (362.65,61.28) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (361.66,58.72) -- (357.72,60) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.53 ] (367.18,53.2) -- (377.78,56.13) -- (365.03,53.97) -- cycle ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (404.57,46.08) -- (401.75,51.78) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (401.75,51.78) -- (388.41,55.98) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (388.41,55.98) -- (385.31,60) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (400.83,53.97) .. controls (400.89,53.79) and (401.07,53.63) .. (401.25,53.61) -- (402.18,53.5) .. controls (402.35,53.48) and (402.45,53.61) .. (402.39,53.79) -- (401.83,55.58) .. controls (401.78,55.76) and (401.59,55.92) .. (401.42,55.94) -- (400.48,56.05) .. controls (400.31,56.07) and (400.21,55.94) .. (400.27,55.76) -- cycle ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (422.22,40.45) -- (420.75,43.56) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.41 ]   (420.75,43.56) -- (447.61,40.63) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.48 ]   (429.23,42.6) .. controls (429.52,46.11) and (427.7,48.67) .. (425.87,51.59) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (418.08,45.57) -- (420.78,45.14) -- (420.22,46.66) -- (418.3,48.5) -- (417.51,47.14) -- cycle ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.48 ]   (454.52,37.12) .. controls (441.77,40.27) and (442.31,56.89) .. (452.18,58.17) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.61 ] (447.08,45.72) .. controls (447.23,45.25) and (447.69,44.79) .. (448.1,44.7) -- (450.77,44.07) .. controls (451.18,43.98) and (451.4,44.28) .. (451.25,44.75) -- (451.25,44.75) .. controls (451.1,45.22) and (450.65,45.68) .. (450.23,45.78) -- (447.56,46.4) .. controls (447.15,46.5) and (446.94,46.19) .. (447.08,45.72) -- cycle ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (460.4,38.62) .. controls (452.91,38.62) and (447.61,52.14) .. (457.85,56.71) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.51 ] (448.53,40.59) .. controls (457.66,39.86) and (468.63,42.09) .. (479.3,47.17) .. controls (463.19,41.68) and (448.25,40.45) .. (446.2,43.74) .. controls (448.53,40.45) and (447.52,42.87) .. (448.53,40.59) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.27 ] (387.02,59.84) .. controls (400.25,56.89) and (430.58,50.68) .. (443.45,48.09) .. controls (435.6,50.78) and (424.26,53.75) .. (423.53,55.03) .. controls (424.81,57.59) and (455.63,55.34) .. (481.56,47.17) .. controls (476.45,52.87) and (451.6,58.9) .. (431.32,62.01) .. controls (425.29,61.83) and (423.09,59.63) .. (415.46,59.82) .. controls (407.36,61.86) and (394.15,66.58) .. (391.52,71.47) .. controls (383.37,68.4) and (364.11,71.86) .. (357.83,71.47) .. controls (349.59,71.58) and (340.94,67.67) .. (329.54,70.56) .. controls (327.53,70.29) and (330.93,68.42) .. (329.25,67.67) .. controls (326.52,66.46) and (318.87,66.25) .. (316.1,65.85) .. controls (316.72,64.85) and (318.19,63.99) .. (320.66,63.43) .. controls (321.47,62.97) and (378.07,62.92) .. (379.86,63.39) .. controls (382.84,61.89) and (385.78,60.43) .. (387.02,59.84) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (371.6,64.29) -- (379.28,72.84) -- (359.54,76.57) -- (358.23,68.04) -- cycle ;
            		\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (353.59,74.43) .. controls (364.55,68.95) and (385.16,65.99) .. (391.52,71.47) .. controls (383.88,81.34) and (357.97,80.77) .. (353.44,79.11) .. controls (352.3,77.19) and (352.21,75.6) .. (353.59,74.43) -- cycle ;
            		\draw    (415.67,62.16) -- (429.93,63.98) ;
            		\draw    (417.03,62.34) .. controls (419.15,64.9) and (419.88,67.64) .. (420.97,70.56) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.32 ] (347.89,77.5) .. controls (351.92,77.23) and (351.1,76.18) .. (353.59,74.43) .. controls (354.37,73.88) and (357.33,73) .. (358.48,72.39) .. controls (359.73,70.98) and (356.83,68.96) .. (358.23,68.04) .. controls (365.06,66.54) and (368.72,64.9) .. (371.6,64.29) .. controls (372.37,65.39) and (372.53,67.16) .. (371.27,69.28) .. controls (370.29,70.94) and (369.84,71.13) .. (369.08,73.3) .. controls (367.06,79.12) and (378.4,75.68) .. (391.52,71.47) .. controls (396.19,72.18) and (410.97,68.26) .. (414.2,68.65) .. controls (415.31,68.78) and (417.76,73.78) .. (428.1,71.47) .. controls (419.15,76.96) and (403.8,79.88) .. (382.6,80.79) .. controls (361.59,84.08) and (364.33,83.9) .. (351.47,83.97) .. controls (348.98,81.71) and (349.17,80.98) .. (347.89,77.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (396.36,66.89) -- (403,65.54) -- (402.92,67.33) -- (396.28,68.68) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (397.87,67.47) .. controls (397.92,66.44) and (398.75,65.45) .. (399.72,65.25) .. controls (400.7,65.05) and (401.45,65.73) .. (401.41,66.75) .. controls (401.36,67.78) and (400.53,68.77) .. (399.55,68.97) .. controls (398.58,69.17) and (397.82,68.5) .. (397.87,67.47) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ,even odd rule] (399.15,67.21) .. controls (399.16,66.93) and (399.39,66.65) .. (399.66,66.59) .. controls (399.93,66.54) and (400.14,66.73) .. (400.13,67.01) .. controls (400.12,67.3) and (399.89,67.57) .. (399.62,67.63) .. controls (399.34,67.68) and (399.14,67.5) .. (399.15,67.21)(398.41,67.36) .. controls (398.45,66.65) and (399.02,65.96) .. (399.7,65.82) .. controls (400.38,65.68) and (400.9,66.15) .. (400.87,66.86) .. controls (400.83,67.57) and (400.26,68.26) .. (399.58,68.4) .. controls (398.9,68.54) and (398.38,68.07) .. (398.41,67.36) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.61 ] (406.7,65.09) .. controls (406.85,64.62) and (407.31,64.16) .. (407.72,64.06) -- (410.39,63.44) .. controls (410.8,63.35) and (411.02,63.65) .. (410.87,64.12) -- (410.87,64.12) .. controls (410.72,64.59) and (410.27,65.05) .. (409.85,65.15) -- (407.18,65.77) .. controls (406.77,65.86) and (406.56,65.56) .. (406.7,65.09) -- cycle ;
            		\draw    (425.25,34.02) .. controls (424.44,35.3) and (423.53,37.85) .. (424.26,40.05) ;
            		\draw    (426.45,33.83) .. controls (425.65,35.11) and (424.81,37.85) .. (425.54,40.05) ;
            		\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (442.17,34.2) -- (453.75,36.58) -- (451.67,37.85) -- (438.88,39.32) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (431.97,34.28) .. controls (431.97,33.07) and (432.95,32.09) .. (434.16,32.09) .. controls (435.37,32.09) and (436.36,33.07) .. (436.36,34.28) .. controls (436.36,35.49) and (435.37,36.48) .. (434.16,36.48) .. controls (432.95,36.48) and (431.97,35.49) .. (431.97,34.28) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (431.41,38.1) .. controls (431.34,37.17) and (432.04,36.36) .. (432.97,36.3) -- (435.72,36.11) .. controls (436.65,36.04) and (437.46,36.74) .. (437.52,37.67) -- (437.64,39.35) .. controls (437.64,39.35) and (437.64,39.35) .. (437.64,39.35) -- (431.52,39.78) .. controls (431.52,39.78) and (431.52,39.78) .. (431.52,39.78) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (427.74,40.16) -- (428.86,35.99) -- (431.6,35.79) -- (433.31,39.75) -- cycle ;
            		\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1.5]    (426.45,33.83) .. controls (431.17,31.68) and (431.7,35.66) .. (432.97,36.3) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.51 ] (435.99,31.13) .. controls (440.93,31.13) and (448.05,31.86) .. (452.8,36.79) .. controls (444.21,30.76) and (431.1,29.85) .. (429.05,33.14) .. controls (432.89,31.5) and (435.63,33.87) .. (435.99,31.13) -- cycle ;
            	\end{tikzpicture}
            \end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Xét trong không gian $Oxyz$, đài kiểm soát không lưu sân bay đặt ở gốc toạ độ $O(0;0;0)$, đơn vị trên mỗi trục là ki-lô-mét. Một máy bay chuyển động theo đường thẳng, bay qua hai vị trí $M(%s; %s; %s)$ và $N(%s; %s; %s)$. %s Khi máy bay ở gần đài kiểm soát không lưu nhất, toạ độ của máy bay là $(a; b; c)$. Giá trị của biểu thức $P = a+b+c$ bằng bao nhiêu?'''
                                 % (M_x, M_y, M_z, N_x, N_y, N_z, hinhve))

                # Các đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = ('$%s$' % das1)
                da_s2 = ('$%s$' % das2)
                da_s3 = ('$%s$' % das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $\\overrightarrow{MN} = (%s; %s; %s)$. Chọn vectơ chỉ phương của đường thẳng $d$ (quỹ đạo của máy bay) là $\\overrightarrow{u} = (%s; %s; %s)$. \\\\
                           Phương trình tham số của đường thẳng $d$: $\\begin{cases} x = %s \\\\ y = %s \\\\ z = %s \\end{cases}$. \\\\
                           Vị trí máy bay gần đài kiểm soát nhất chính là hình chiếu vuông góc $H(a;b;c)$ của $O$ lên $d$. \\\\
                           Gọi $(P)$ là mặt phẳng đi qua $O(0;0;0)$ và vuông góc với $d$. Khi đó $(P)$ nhận $\\overrightarrow{u} = (%s; %s; %s)$ làm vectơ pháp tuyến. \\\\
                           Phương trình mặt phẳng $(P)$ là: $%s$. \\\\
                           Vì $H = d \\cap (P)$ nên toạ độ của $H$ ứng với giá trị $t$ thoả mãn: \\\\
                           $%s(%s) %s %s(%s) %s %s(%s) = 0$ \\\\
                           $\\Leftrightarrow %s = 0 \\Leftrightarrow t = %s$. \\\\
                           Suy ra toạ độ $H(%s; %s; %s)$. \\\\
                           Vậy $P = a + b + c = %s + %s + %s = %s$.'''
                           % (vec_MN_x, vec_MN_y, vec_MN_z, v_x, v_y, v_z,
                              str_x, str_y, str_z,
                              v_x, v_y, v_z,
                              plane_eq,
                              v_x, str_x, sign_y, abs(v_y), str_y, sign_z, abs(v_z), str_z,
                              str_eq_t, t_prime,
                              H_x, H_y, H_z,
                              H_x, str_Hy, str_Hz, kq
                              ))
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content 

