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


def bt_dang60_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các số trong bài toán để đảm bảo nước không bị tràn
                while True:
                    a = random.randint(4, 6)
                    b = random.randint(3, 5)
                    L = random.randint(40, 60)
                    Q = random.randint(30, 60) * 10
                    t = random.randint(2, 4)
                    w = 2 * a
                    V_max = 0.5 * math.pi * a * b * L
                    # Thể tích nước bơm vào phải nhỏ hơn thể tích tối đa và chia hết cho L để số đẹp
                    if Q * t < V_max - 50 and (Q * t) % L == 0:
                        break

                Q_times_t = Q * t
                S_0_val = int(Q_times_t / L)
                a_sq = a * a
                b_sq = b * b

                # Tìm h bằng phương pháp chặt nhị phân để giải phương trình diện tích
                A_target = S_0_val
                low = -b
                high = 0
                for _ in range(100):
                    mid = (low + high) / 2
                    A_mid = a * mid * math.sqrt(1 - (mid/b)**2) + a * b * math.asin(mid/b) + a * b * math.pi / 2
                    if A_mid < A_target:
                        low = mid
                    else:
                        high = mid

                y_ans = (low + high) / 2
                h_ans = y_ans + b

                # Tính tốc độ dâng của mực nước
                S_surf = L * 2 * a * math.sqrt(1 - (y_ans/b)**2)
                h_prime_dm = Q / S_surf
                h_prime_cm = h_prime_dm * 10

                kq = str(Decimal(float(h_prime_cm)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                h_prime_cm_f = float(Decimal(float(h_prime_cm)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da= random.choice(du)
                s = [
                    '$%s$'%(str(Decimal(float(h_prime_cm_f + 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$'%(str(Decimal(float(h_prime_cm_f + 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$'%(str(Decimal(float(h_prime_cm_f + 0.3)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$'%(str(Decimal(float(abs(h_prime_cm_f - 0.1))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$'%(str(Decimal(float(abs(h_prime_cm_f - 0.2))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$'%(str(Decimal(float(abs(h_prime_cm_f - 0.3))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','))
                ]

                # Đảm bảo các phương án sai không trùng đáp án đúng
                s = list(set(s))
                if da in s: s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=(r'''\scalebox{0.8}{  \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 149; green, 227; blue, 209 }  ,fill opacity=1 ] (262.06,77.71) -- (434.65,75.59) -- (337.04,158.35) -- (121.54,159.76) -- cycle ;
            	\draw  [fill={rgb, 255:red, 181; green, 108; blue, 46 }  ,fill opacity=1 ] (434.65,75.59) -- (436.07,168.96) -- (373.73,244.17) -- (371.7,132.89) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (340.58,131.47) .. controls (346.94,128.29) and (352.09,122.51) .. (359.68,117.32) .. controls (367.96,111.66) and (378.59,106.53) .. (383.02,102.47) .. controls (385.88,106.17) and (389.06,93.67) .. (392.21,91.15) .. controls (396.4,87.81) and (406.01,83.54) .. (409.9,80.54) .. controls (420.07,72.68) and (431.82,56.49) .. (434.65,63.57) .. controls (433.24,64.98) and (436.07,55.08) .. (434.65,75.59) .. controls (408.48,98.93) and (390.8,117.32) .. (371.7,132.89) .. controls (354.02,132.18) and (369.58,132.89) .. (340.58,131.47) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.36 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (133.34,136.39) .. controls (154.55,116.62) and (188.5,93.28) .. (257.11,60.74) .. controls (251.91,65.94) and (265.2,69.27) .. (262.06,77.71) .. controls (216.8,107.89) and (157.52,132.4) .. (126.4,163.52) .. controls (117.2,150.79) and (134.75,146.32) .. (133.34,136.39) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (109,135.86) .. controls (112,134.36) and (110.7,126.52) .. (122.56,127.95) .. controls (128.62,124.2) and (134.98,120.07) .. (138.99,117.32) .. controls (147.27,111.66) and (160.73,102.29) .. (165.16,98.23) .. controls (178.6,93.28) and (189.59,91.55) .. (192.75,89.03) .. controls (196.93,85.69) and (214.33,78.59) .. (218.21,75.59) .. controls (228.39,67.72) and (239.32,61.64) .. (246.5,60.74) .. controls (242.26,59.32) and (252.16,57.91) .. (257.82,64.98) .. controls (244.92,76.49) and (229.53,85.49) .. (195.58,99.64) .. controls (166.58,117.32) and (144.45,128.16) .. (133.34,136.39) .. controls (115.66,135.68) and (120.6,136.42) .. (109,135.86) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (109,135.86) .. controls (115.65,136.41) and (123.9,136.55) .. (133.34,136.39) .. controls (125.58,227.1) and (350.23,232.19) .. (340.58,131.47) .. controls (350.79,131.45) and (361.63,132.89) .. (371.7,132.89) .. controls (373.11,188.06) and (373.02,202.44) .. (373.73,244.17) .. controls (228.73,247) and (185.56,242.38) .. (110.6,244.64) .. controls (111.31,204.33) and (109.66,183.34) .. (109,135.86) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 61; green, 220; blue, 135 }  ,fill opacity=1 ]   (135.2,156.37) .. controls (148.78,231.63) and (328.16,228.8) .. (338.91,152.97) ;
            	\draw    (133.34,136.39) -- (340.58,131.47) ;
            	\draw    (133.34,136.39) -- (133.34,115.31) ;
            	\draw    (340.58,131.47) -- (340.58,110.39) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (138.05,156.46) -- (336.08,154.11) ;
            	\draw  [dash pattern={on 4.5pt off 4.5pt}]  (132.37,115.31) -- (339.6,110.39) ;
            	\draw  [dash pattern={on 4.5pt off 4.5pt}]  (237.62,112.85) -- (237.62,214.65) ;
            	\draw (216.04,168.85) node [anchor=north west][inner sep=0.75pt]    {$h$};
            	\draw (187.63,137) node [anchor=north west][inner sep=0.75pt]    {$%s-h$};
            	\draw (283.38,82) node [anchor=north west][inner sep=0.75pt]    {$L$};
            	\draw (232,95) node [anchor=north west][inner sep=0.75pt]    {$%s$};
            	\draw (320.8,90) node [anchor=north west][inner sep=0.75pt]    {$%s$};
            \end{tikzpicture} }'''%(latex(b),latex(w),latex(L)))
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một máng nước được thiết kế sao cho mặt cắt vuông góc là một nửa hình elip. Biết miệng máng nước có chiều rộng là $%s$ dm và độ sâu tối đa của máng là $%s$ dm. Biết máng có chiều dài $%s$ dm. Ban đầu máng cạn nước. Người ta mở cống cho nước chảy vào chiếc máng này với lưu lượng không đổi là $%s$ $\text{dm}^3$/phút. Sau $%s$ phút bơm nước thì tốc độ dâng lên của mực nước trong kênh là bao nhiêu cm/phút? (Kết quả làm tròn đến hàng phần chục).}{%s}'''
                                 % (latex(w), latex(b), latex(L), latex(Q), latex(t),
                                    hinhve))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Xử lý các số được làm tròn để hiển thị mượt mà trong lời giải
                h_rounded = str(Decimal(float(h_ans)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).replace('.', ',')
                int_val = str(Decimal(float(S_0_val/(2*a))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                h_prime_dm_round = str(Decimal(float(h_prime_dm)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # Nội dung lời giải
                loigiai = ('''Tại $%s$ phút, thể tích nước bơm vào là $V = %s \\cdot %s = %s$ (dm$^3$). \\\\
                Gọi mặt cắt ngang của phần nước là $S_0$. Ta có $S_0 = \\frac{V}{L} = \\frac{%s}{%s} = %s$ (dm$^2$).\\\\
                Chọn hệ trục tọa độ $Oxy$ với gốc $O$ tại tâm của elip hoàn chỉnh, trục $Ox$ dọc theo miệng máng. \\\\
                Phương trình elip là: $\\frac{x^2}{%s} + \\frac{y^2}{%s} = 1$. \\\\
                Gọi $h$ là chiều cao mực nước từ đáy lên. Tung độ bề mặt nước là $y = h - %s$.\\\\
                Thay $y = h - %s$ vào phương trình elip, ta có: $x_0 = %s \\sqrt{1 - \\frac{\\left(h-%s\\right)^2}{%s}}$.\\\\
                Diện tích bề mặt nước tại thời điểm đó là:\\\\ $S_{\\text{bề mặt}} = 2x_0 \\cdot L = 2 \\cdot %s \\sqrt{1 - \\frac{\\left(h-%s\\right)^2}{%s}} \\cdot %s = %s \\sqrt{1 - \\frac{\\left(h-%s\\right)^2}{%s}}$.\\\\
                Mặt khác, diện tích mặt cắt ngang của nước là: $S_0 = \\int_{-%s}^{h-%s} 2x \\, \\text{d}y = %s \\int_{-%s}^{h-%s} \\sqrt{1 - \\frac{y^2}{%s}} \\, \\text{d}y$.\\\\
                Theo giả thiết $S_0 = %s$, ta có: $%s \\int_{-%s}^{h-%s} \\sqrt{1 - \\frac{y^2}{%s}} \\, \\text{d}y = %s \\Rightarrow \\int_{-%s}^{h-%s} \\sqrt{1 - \\frac{y^2}{%s}} \\, \\text{d}y = %s$.\\\\
                Sử dụng máy tính giải phương trình trên, ta được $h \\approx %s$ (dm).\\\\
                Tốc độ dâng của mực nước là: \\\\
                $h'\\left(t\\right) = \\frac{V'\\left(t\\right)}{S_{\\text{bề mặt}}} = \\frac{%s}{%s \\sqrt{1 - \\frac{\\left(h-%s\\right)^2}{%s}}} \\approx %s$ (dm/phút) $\\approx %s$ (cm/phút).'''
                % (latex(t), latex(Q), latex(t), latex(Q_times_t),
                   latex(Q_times_t), latex(L), latex(S_0_val),
                   latex(a_sq), latex(b_sq),
                   latex(b),
                   latex(b), latex(a), latex(b), latex(b_sq),
                   latex(a), latex(b), latex(b_sq), latex(L), latex(2*a*L), latex(b), latex(b_sq),
                   latex(b), latex(b), latex(2*a), latex(b), latex(b), latex(b_sq),
                   latex(S_0_val), latex(2*a), latex(b), latex(b), latex(b_sq), latex(S_0_val), latex(b), latex(b), latex(b_sq), int_val,
                   h_rounded,
                   latex(Q), latex(2*a*L), latex(b), latex(b_sq), h_prime_dm_round, kq)
                )
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

