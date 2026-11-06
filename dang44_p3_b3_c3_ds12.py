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


def bt_dang44_p3_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bộ các giá trị (Cạnh hình vuông a, tọa độ điểm M(m;m), khoảng cách MA=MC=c) 
                # Được lựa chọn từ các bộ số Pytago để đảm bảo nghiệm luôn đẹp
                triples = [
                    (7, 3, 5),      # a=7, m=3, c=5 (Bài toán gốc)
                    (14, 6, 10),    # a=14, m=6, c=10
                    (17, 5, 13),    # a=17, m=5, c=13
                    (23, 8, 17),    # a=23, m=8, c=17
                    (31, 7, 25)     # a=31, m=7, c=25
                ]
                a, m, c = random.choice(triples)

                # Các giá trị tính toán phụ cho lời giải
                d = a - m
                quad_b = 2 * a
                quad_c = a**2 - c**2
                m_other = a - m

                # Tính toán diện tích (Sử dụng Rational của Sympy để có phân số chính xác tuyệt đối)
                S1_expr = Rational(a**3, 6*d)
                Sg_expr = Rational(m**3, 3*d)
                Strang_expr = Rational(a**2 + a*m + m**2, 3)
                S_final_expr = Rational(2*a**2 - a*m - m**2, 3)

                # Làm tròn đáp án đúng đến hàng phần chục
                S_float = float(S_final_expr)
                S_dec = Decimal(S_float).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq = str(S_dec).replace('.', ',')

                # Các đáp án trắc nghiệm (sinh ra phương án nhiễu)
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                s = [
                    '$%s$' % str(Decimal(S_float + 1).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(S_float + 2).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(S_float - 1).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(S_float - 2).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(S_float + 0.5).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(S_float - 0.5).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                ]

                # Loại bỏ đáp án nhiễu nếu vô tình trùng với đáp án đúng
                s = list(set(s))
                if f'${kq}$' in s:
                    s.remove(f'${kq}$')

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 107 }  ,fill opacity=1 ][line width=1]  (59.4,37) -- (201,37) -- (201,178.6) -- (59.4,178.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (200.99,178.8) .. controls (153.91,95.5) and (106.71,95.43) .. (59.4,178.6) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (59,179.01) .. controls (141.85,131.91) and (141.99,84.57) .. (59.4,37) ;
            	\draw  [line width=1]  (200.99,178.8) .. controls (153.91,95.5) and (106.71,95.43) .. (59.4,178.6) ;
            	\draw  [line width=1]  (59.4,37) -- (201.12,37) -- (201.12,178.72) -- (59.4,178.72) -- cycle ;
            	\draw (43.5,175) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (199,173.5) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (201.5,21) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (42.5,21) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (117.5,120) node [anchor=north west][inner sep=0.75pt]    {$M$};
            \end{tikzpicture}'''

                # Câu hỏi
                noidungcauhoi = (r'''\immini{Cho hình vuông $OABC$ có cạnh bằng $%s$ và điểm $M$ nằm bên trong hình vuông sao cho $MA = MC = %s$. Parabol $\left(P_1\right)$ đi qua các điểm $O, A, M$ và parabol $\left(P_2\right)$ đi qua các điểm $O, C, M$. Diện tích phần tô đậm trong hình vẽ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).}{%s}'''
                                 % (a, c, hinhve))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Chọn hệ trục tọa độ $Oxy$ sao cho $O\\left(0;0\\right)$, $A\\left(%s;0\\right)$, $C\\left(0;%s\\right)$, $B\\left(%s;%s\\right)$.\\\\
                Vì $MA=MC$ nên $M$ thuộc đường trung trực của $AC$ (đường thẳng $y=x$), suy ra $M\\left(m;m\\right)$ với $0 < m < %s$.\\\\
                Ta có $MA = %s \\Rightarrow \\left(m-%s\\right)^2 + m^2 = %s^2 \\Leftrightarrow 2m^2 - %sm + %s = 0 \\Leftrightarrow m = %s$ hoặc $m = %s$.\\\\
                Dựa vào hình vẽ, $M$ gần $O$ hơn nên chọn $m = %s$.\\\\
                Parabol $\\left(P_1\\right)$ đi qua $O, A, M$ có phương trình dạng $y = k_1x\\left(x-%s\\right)$.\\\\
                Vì $M\\left(%s;%s\\right) \\in \\left(P_1\\right) \\Rightarrow %s = k_1 \\cdot %s\\left(%s-%s\\right) \\Rightarrow k_1 = -\\frac{1}{%s}$.\\\\
                Suy ra $\\left(P_1\\right): y = \\frac{1}{%s}\\left(%s x - x^2\\right)$.\\\\
                Tương tự, parabol $\\left(P_2\\right)$ đi qua $O, C, M$ có phương trình $\\left(P_2\\right): x = \\frac{1}{%s}\\left(%s y - y^2\\right)$.\\\\
                Gọi $S_1$ là diện tích hình phẳng giới hạn bởi $\\left(P_1\\right)$ và trục $Ox$, ta có:\\\\
                $S_1 = \\int\\limits_0^{%s} \\frac{1}{%s}\\left(%s x - x^2\\right) \\mathrm{\\,d}x = %s$.\\\\
                Do tính đối xứng, diện tích hình phẳng giới hạn bởi $\\left(P_2\\right)$ và trục $Oy$ là $S_2 = S_1 = %s$.\\\\
                Phần giao nhau của hai hình phẳng này là diện tích giới hạn bởi $\\left(P_1\\right)$ và $\\left(P_2\\right)$. Do tính đối xứng qua $y=x$, diện tích phần giao nhau là:\\\\
                $S_g = 2 \\int\\limits_0^{%s} \\left[ \\frac{1}{%s}\\left(%s x - x^2\\right) - x \\right] \\mathrm{\\,d}x = \\frac{2}{%s} \\int\\limits_0^{%s} \\left(%s x - x^2\\right) \\mathrm{\\,d}x = %s$.\\\\
                Diện tích phần không tô đậm trong hình vuông là $S_{\\text{trắng}} = S_1 + S_2 - S_g = 2 \\cdot %s - %s = %s$.\\\\
                Diện tích phần tô đậm là $S = S_{OABC} - S_{\\text{trắng}} = %s^2 - %s = %s \\approx %s$.'''
                % (a, a, a, a,
                   a,
                   c, a, c, quad_b, quad_c, m, m_other,
                   m,
                   a,
                   m, m, m, m, m, a, d,
                   d, a,
                   d, a,
                   a, d, a, latex(S1_expr),
                   latex(S1_expr),
                   m, d, a, d, m, m, latex(Sg_expr),
                   latex(S1_expr), latex(Sg_expr), latex(Strang_expr),
                   a, latex(Strang_expr), latex(S_final_expr), kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

