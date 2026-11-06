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


def bt_dang56_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các giá trị ngẫu nhiên
                # S = 40 cố định như hình để giữ logic bài toán thực tế về áp suất
                S = 40
                # Chọn a0, b0 sao cho khi chia S=40 ra số thập phân đẹp
                a0 = random.choice([4, 8, 12])
                b0 = random.choice([8, 12, 16, 20])
                h0_val = random.choice([0.4, 0.5, 0.6, 0.7])
                T = 2
                k = 2

                # Tính toán các hệ số
                a1 = Rational(a0, S) # Hệ số của t: 4/40 = 0,1
                b1 = Rational(b0, S) # Hệ số tự do: 12/40 = 0,3

                # Phương trình: h'(t) + 1/(t+2) * h(t) = a1*t + b1
                # Nhân tử tích phân: (t+2)
                # [(t+2)h(t)]' = (a1*t + b1)(t+2) = a1*t^2 + (2*a1 + b1)*t + 2*b1

                c_t2 = a1
                c_t1 = 2*a1 + b1
                c_t0 = 2*b1

                # Nguyên hàm: (a1/3)t^3 + (c_t1/2)t^2 + c_t0*t + C
                # Tại t=0: (0+2)*h(0) = C => C = 2 * h0
                C_val = Rational(int(h0_val*10), 10) * k

                # Tính h(2)
                # (2+2)*h(2) = (a1/3)*2^3 + (c_t1/2)*2^2 + c_t0*2 + C
                tu_so = (a1/3)*(T**3) + (c_t1/2)*(T**2) + c_t0*T + C_val
                h_2 = tu_so / (T + k)

                # Sự thay đổi mực nước
                delta_h = h_2 - Rational(int(h0_val*10), 10)

                # Làm tròn đến hàng phần trăm
                kq_float = float(delta_h)
                kq_rounded = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_rounded).replace('.', ',')

                # Tạo các phương án sai
                sai1 = float(kq_rounded) + random.choice([0.12, 0.15, 0.22])
                sai2 = float(kq_rounded) - random.choice([0.08, 0.11, 0.18])
                sai3 = float(kq_rounded) + random.choice([0.25, 0.31, 0.05])

                def fmt_num(num):
                    return str(Decimal(str(round(num, 2))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_a9815sq71/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-93 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_nd9msjuji}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            		rgb(37.5bp)=(0.61,0.61,0.61);
            		rgb(50bp)=(1,1,1);
            		rgb(62.5bp)=(0.61,0.61,0.61);
            		rgb(100bp)=(0.61,0.61,0.61)}
            	\tikzset {_ynl78vq5u/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-90 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_w8uukm956}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            		rgb(37.5bp)=(0.61,0.61,0.61);
            		rgb(50bp)=(1,1,1);
            		rgb(62.5bp)=(0.61,0.61,0.61);
            		rgb(100bp)=(0.61,0.61,0.61)}
            	\tikzset{every picture/.style={line width=0.75pt}} 
            	\draw  [draw opacity=0][fill={rgb, 255:red, 228; green, 228; blue, 198 }  ,fill opacity=1 ] (314.4,136.8) -- (255.6,180) -- (55.2,180) -- (127.2,134.8) -- cycle ;
            	\draw  [fill={rgb, 255:red, 196; green, 195; blue, 185 }  ,fill opacity=1 ] (288.8,131.2) -- (248.8,159.2) -- (105.2,156.8) -- (148.8,129.6) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 137; green, 244; blue, 236 }  ,fill opacity=0.66 ] (246.8,154) .. controls (247.47,126.4) and (247.13,129.07) .. (246.47,105.4) .. controls (259.8,103.73) and (251.8,99.4) .. (275.13,93.07) .. controls (274.13,112.07) and (275.27,114.07) .. (275.2,136) .. controls (256.47,147.4) and (262.8,142.4) .. (246.8,154) -- cycle ;
            	\draw   (148.4,56.8) -- (148.4,134.4) -- (119.6,152.4) -- (119.6,74.8) -- cycle ;
            	\draw   (275.2,58.4) -- (275.6,136) -- (148.4,134.4) -- (148.4,56.8) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (249.2,169.6) -- (248.8,159.2) -- (105.2,156.8) -- (105.6,168) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (288.64,142.4) -- (288.8,131.2) -- (248.8,159.2) -- (249.2,169.6) -- cycle ;
            	\path  [shading=_nd9msjuji,_a9815sq71] (127.5,48.4) -- (77.66,48.4) .. controls (76.57,48.4) and (75.68,46.88) .. (75.68,45) .. controls (75.68,43.12) and (76.57,41.6) .. (77.66,41.6) -- (127.5,41.6) .. controls (128.59,41.6) and (129.48,43.12) .. (129.48,45) .. controls (129.48,46.88) and (128.59,48.4) .. (127.5,48.4) .. controls (126.4,48.4) and (125.51,46.88) .. (125.51,45) .. controls (125.51,43.12) and (126.4,41.6) .. (127.5,41.6) ;
            	\draw   (127.5,48.4) -- (77.66,48.4) .. controls (76.57,48.4) and (75.68,46.88) .. (75.68,45) .. controls (75.68,43.12) and (76.57,41.6) .. (77.66,41.6) -- (127.5,41.6) .. controls (128.59,41.6) and (129.48,43.12) .. (129.48,45) .. controls (129.48,46.88) and (128.59,48.4) .. (127.5,48.4) .. controls (126.4,48.4) and (125.51,46.88) .. (125.51,45) .. controls (125.51,43.12) and (126.4,41.6) .. (127.5,41.6) ; 
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (266.32,125.2) -- (266.72,141.2) -- (255.92,148.4) -- (255.52,132.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 200; green, 199; blue, 193 }  ,fill opacity=1 ] (266.67,127.4) -- (266.72,141.2) -- (257.67,146.73) -- (257.33,133.73) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 137; green, 244; blue, 236 }  ,fill opacity=0.66 ] (119.6,152.4) .. controls (120.13,141.4) and (120.8,128.4) .. (120.13,104.73) .. controls (160.47,129.4) and (189.47,78.4) .. (246.47,105.4) .. controls (245.47,124.4) and (246.47,132.07) .. (246.4,154) .. controls (186.8,152.73) and (180.13,153.07) .. (119.6,152.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 80; green, 217; blue, 227 }  ,fill opacity=0.45 ] (120.13,104.73) .. controls (123,95.47) and (137.8,100.4) .. (148.8,92.4) .. controls (197.13,101.4) and (235.47,70.4) .. (275.13,93.07) .. controls (268.47,101.73) and (258.8,95.73) .. (247.13,108.4) .. controls (209.8,76.07) and (150,131.8) .. (120.13,104.73) -- cycle ;
            	\draw   (275.2,58.4) -- (275.6,136) -- (246.4,154) -- (246.4,76.4) -- cycle ;
            	\path  [shading=_w8uukm956,_ynl78vq5u] (277.77,144.13) -- (263.9,144.13) .. controls (262.72,144.13) and (261.76,142.49) .. (261.76,140.47) .. controls (261.76,138.44) and (262.72,136.8) .. (263.9,136.8) -- (277.77,136.8) .. controls (278.95,136.8) and (279.91,138.44) .. (279.91,140.47) .. controls (279.91,142.49) and (278.95,144.13) .. (277.77,144.13) .. controls (276.59,144.13) and (275.63,142.49) .. (275.63,140.47) .. controls (275.63,138.44) and (276.59,136.8) .. (277.77,136.8) ; 
            	\draw   (277.77,144.13) -- (263.9,144.13) .. controls (262.72,144.13) and (261.76,142.49) .. (261.76,140.47) .. controls (261.76,138.44) and (262.72,136.8) .. (263.9,136.8) -- (277.77,136.8) .. controls (278.95,136.8) and (279.91,138.44) .. (279.91,140.47) .. controls (279.91,142.49) and (278.95,144.13) .. (277.77,144.13) .. controls (276.59,144.13) and (275.63,142.49) .. (275.63,140.47) .. controls (275.63,138.44) and (276.59,136.8) .. (277.77,136.8) ; 
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (244.8,112.73) -- (244.93,151.67) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (246.4,153) -- (119.73,151.53) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.28 ] (119.6,74.8) -- (148.4,56.8) -- (119.6,152.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.28 ] (148.4,56.8) -- (211.8,57.6) -- (173.47,134.73) -- (148.4,134.4) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (273.47,108.07) -- (273.93,134.33) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.28 ] (105.6,168) -- (249.2,169.6) -- (105.2,156.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 137; green, 244; blue, 236 }  ,fill opacity=0.55 ] (127.2,43.8) .. controls (149.6,50) and (154.4,83.6) .. (162.4,98.8) .. controls (156,108) and (152.8,97.6) .. (139.2,102) .. controls (147.6,58.8) and (122.8,49.6) .. (127.2,43.8) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (228.96,90) .. controls (245.36,87.2) and (250.96,88) .. (260.56,92.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (192.16,99.6) .. controls (206.96,94.4) and (214.56,92.4) .. (235.36,98) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (166.96,98) .. controls (182.56,96) and (182.16,98) .. (196.96,94.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (162.4,98.8) .. controls (175.76,98.8) and (175.76,102.4) .. (161.36,104.8) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (171.2,98) .. controls (183.76,99.2) and (178.16,104.8) .. (160.96,106.8) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (141.36,99.2) .. controls (132.16,99.2) and (134.16,106) .. (142.56,106) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.55 ]   (134,104.6) .. controls (124.8,104.6) and (138.96,110) .. (147.36,110) ;
            	\draw [color={rgb, 255:red, 80; green, 227; blue, 222 }  ,draw opacity=0.57 ]   (127.5,48.4) .. controls (144.16,72) and (140.96,85.6) .. (141.36,99.2) ;
            	\draw [color={rgb, 255:red, 80; green, 227; blue, 222 }  ,draw opacity=0.57 ]   (129.48,45) .. controls (147.36,54.8) and (162.32,100) .. (164.16,106) ;
            	\draw [color={rgb, 255:red, 80; green, 227; blue, 222 }  ,draw opacity=0.57 ]   (129.48,45) .. controls (146.14,68.6) and (145.36,88.4) .. (145.76,102) ;
            	\draw [color={rgb, 255:red, 80; green, 227; blue, 222 }  ,draw opacity=0.57 ]   (144.7,68) .. controls (155.36,93.2) and (152.56,92.4) .. (155.36,102.8) ;
            	\draw   (246.4,76.4) -- (246.8,154) -- (119.6,152.4) -- (119.6,74.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 137; green, 244; blue, 236 }  ,fill opacity=0.55 ] (278.4,138.2) .. controls (300.8,144.4) and (300.64,144.8) .. (308.64,160) .. controls (302.24,169.2) and (310.64,158.8) .. (297.04,163.2) .. controls (279.84,137.6) and (274,144) .. (278.4,138.2) -- cycle ;
            	\draw [color={rgb, 255:red, 80; green, 227; blue, 222 }  ,draw opacity=0.57 ]   (278.7,142.8) .. controls (285.84,148.4) and (291.84,150.8) .. (297.04,163.2) ;
            	\draw [color={rgb, 255:red, 80; green, 227; blue, 222 }  ,draw opacity=0.57 ]   (280.68,139.4) .. controls (298.56,149.2) and (305.2,155.2) .. (307.04,161.2) ;
            	\draw [color={rgb, 255:red, 80; green, 227; blue, 222 }  ,draw opacity=0.57 ]   (280.68,139.4) .. controls (294.64,151.2) and (295.44,148.8) .. (303.04,160.8) ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Tại một trại tôm ở Trảng Bàng, do sự cố mất điện tạm thời, khi hệ thống hoạt động trở lại $\left( t=0 \right)$, mực nước trong bể hình hộp chữ nhật (diện tích đáy $S = %s$ $m^2$) đang ở mức $%s$ mét. Để bù đắp lượng oxy thiếu hụt, máy bơm hoạt động với công suất tăng cường theo thời gian: $V_{\text{vao}} = %st + %s$ $\left( m^3/\text{giờ} \right)$. Hệ thống xả tự động vẫn vận hành theo công thức: $V_{\text{ra}} = \frac{%sh(t)}{t+%s}$ $\left( m^3/\text{giờ} \right)$ để đảm bảo áp suất đáy, với $h(t)$ là chiều cao mực nước tại thời điểm $t$ (tính bằng mét). Sau $%s$ giờ vận hành kể từ khi có điện lại, mực nước trong bể tăng bao nhiêu so với lúc ban đầu? (làm tròn kết quả đến hàng phần trăm).}{%s}'''
                                 %(latex(S), latex(h0_val).replace('.',','), latex(a0), latex(b0), latex(S), latex(k), latex(T),hinhve))

                # Các đáp án
                da_d = ('\\True $%s$' % kq_str)
                da_s1 = ('$%s$' % fmt_num(sai1))
                da_s2 = ('$%s$' % fmt_num(sai2))
                da_s3 = ('$%s$' % fmt_num(sai3))

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Chuẩn bị số liệu cho lời giải
                a1_ltx = latex(a1).replace('.', ',')
                b1_ltx = latex(b1).replace('.', ',')
                c_t2_ltx = latex(c_t2).replace('.', ',')
                c_t1_ltx = latex(c_t1).replace('.', ',')
                c_t0_ltx = latex(c_t0).replace('.', ',')

                loigiai = ('''Thể tích nước tại thời điểm $t$ là: $V = S \\cdot h(t)$ \\\\
            Tốc độ biến thiên thể tích nước trong bể là: $V'\\left( t \\right) = S \\cdot h'\\left( t \\right) = V_{\\text{vao}} - V_{\\text{ra}}$ \\\\
            Thay các dữ kiện vào ta có phương trình: $%s \\cdot h'\\left( t \\right) = \\left( %st + %s \\right) - \\frac{%sh(t)}{t+%s}$ \\\\
            $\\Leftrightarrow h'\\left( t \\right) + \\frac{1}{t+%s} h\\left( t \\right) = %st + %s \\Leftrightarrow h'\\left( t \\right) \\left( t+%s \\right) + h\\left( t \\right) = \\left( %st + %s \\right) \\left( t+%s \\right)$ \\\\
            $\\Leftrightarrow [\\left( t+%s \\right) h\\left( t \\right)]' = %st^2 + %st + %s$ \\\\
            $\\Rightarrow \\left( t+%s \\right) h\\left( t \\right) = \\int \\left( %st^2 + %st + %s \\right) dt = \\frac{%st^3}{3} + \\frac{%st^2}{2} + %st + C$ \\\\
            Với điều kiện ban đầu $h(0) = %s$, ta tìm được $C = %s$. \\\\
            Vậy hàm số mực nước là: $h(t) = \\left( \\frac{%st^3}{3} + \\frac{%st^2}{2} + %st + %s \\right) \\cdot \\frac{1}{t+%s}$. \\\\
            Tại thời điểm $t = %s$, ta có: $h(%s) = %s$ (m). \\\\
            Sự thay đổi so với ban đầu: $\\Delta h = h(%s) - h(0) = %s - %s \\approx %s$ (m).'''
                           %(latex(S), latex(a0), latex(b0), latex(S), latex(k),
                             latex(k), a1_ltx, b1_ltx, latex(k), a1_ltx, b1_ltx, latex(k),
                             latex(k), latex(c_t2).replace('.',','), latex(c_t1).replace('.',','), latex(c_t0).replace('.',','),
                             latex(k), latex(c_t2).replace('.',','), latex(c_t1).replace('.',','), latex(c_t0).replace('.',','),
                             latex(c_t2).replace('.',','), latex(c_t1).replace('.',','), latex(c_t0).replace('.',','),
                             latex(h0_val).replace('.',','), latex(C_val).replace('.',','),
                             latex(c_t2).replace('.',','), latex(c_t1).replace('.',','), latex(c_t0).replace('.',','), latex(C_val).replace('.',','), latex(k),
                             latex(T), latex(T), latex(h_2).replace('.',','),
                             latex(T), latex(h_2).replace('.',','), latex(h0_val).replace('.',','), kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

