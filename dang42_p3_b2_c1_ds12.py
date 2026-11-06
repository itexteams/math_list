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


def bt_dang42_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                x = sp.Symbol('x')

                # Random các thông số tọa độ. 
                # Đảm bảo parabol nằm hoàn toàn bên ngoài và phía trên đường tròn để tồn tại khoảng cách hợp lý.
                xc = random.randint(4, 7)
                yc = random.randint(1, 3)
                R = random.randint(1, 2)
                xv = random.randint(2, 6)
                yv = yc + R + random.randint(2, 5)

                # Tính toán đa thức khoảng cách f(x) = AC^2
                f = (x - xc)**2 + ((x - xv)**2 + yv - yc)**2
                f_expand = sp.expand(f)
                f_prime = sp.diff(f_expand, x)

                # Tìm nghiệm thực của phương trình đạo hàm f'(x) = 0
                f_prime_poly = sp.Poly(f_prime, x)
                roots = f_prime_poly.nroots()
                real_roots = [float(sp.re(r)) for r in roots if abs(sp.im(r)) < 1e-5]

                # Tìm giá trị x làm f(x) nhỏ nhất
                min_val = float('inf')
                best_x = 0
                for r in real_roots:
                    val = float(f_expand.subs(x, r))
                    if val < min_val:
                        min_val = val
                        best_x = r

                # Khoảng cách ngắn nhất
                min_dist = math.sqrt(min_val) - R

                # Làm tròn theo yêu cầu đề bài
                x_approx_num = round(best_x, 3)
                f_approx_num = round(min_val, 3)
                kq_num = round(min_dist, 2)

                # Đổi dấu chấm thành phẩy cho chuẩn định dạng Việt Nam
                x_approx = f"{x_approx_num:.3f}".replace('.', ',')
                f_approx = f"{f_approx_num:.3f}".replace('.', ',')
                kq_str = f"{kq_num:.2f}".replace('.', ',')

                # Hàm xử lý chuỗi latex đảm bảo chuẩn cặp ngoặc \left( \right)
                def format_latex_brackets(expr):
                    s = sp.latex(expr)
                    s = s.replace('\\left(', '(').replace('\\right)', ')') # Xóa cũ đề phòng dư thừa
                    s = s.replace('(', '\\left(').replace(')', '\\right)') # Thêm đồng loạt chuẩn quy tắc
                    return s

                f_expand_str = format_latex_brackets(f_expand)
                f_prime_str = format_latex_brackets(f_prime)

                # Tạo các phương án sai (đảm bảo không trùng với đáp án đúng và luôn > 0)
                options_set = set()
                while len(options_set) < 3:
                    variation = round(kq_num + random.choice([-0.25, -0.15, -0.1, 0.1, 0.15, 0.25]), 2)
                    if variation > 0 and variation != kq_num:
                        options_set.add(f"{variation:.2f}".replace('.', ','))

                options_list = list(options_set)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq_str)]
                da = du[0]

                s = ['$%s$' % options_list[0],
                     '$%s$' % options_list[1],
                     '$%s$' % options_list[2]]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]
                hinhve=r'''\scalebox{0.8}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 247; green, 241; blue, 229 }  ,fill opacity=1 ][line width=1]  (62.73,53.67) -- (268.6,53.67) -- (268.6,259.53) -- (62.73,259.53) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]  (62.73,53.67) .. controls (99.23,171.3) and (135.74,171.3) .. (172.24,53.67) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (171.82,211.35) .. controls (171.82,184.91) and (193.25,163.48) .. (219.69,163.48) .. controls (246.13,163.48) and (267.56,184.91) .. (267.56,211.35) .. controls (267.56,237.79) and (246.13,259.22) .. (219.69,259.22) .. controls (193.25,259.22) and (171.82,237.79) .. (171.82,211.35) -- cycle ;
            	\draw  [line width=1]  (62.73,53.67) -- (268.6,53.67) -- (268.6,259.53) -- (62.73,259.53) -- cycle ;
            	\draw [line width=1]    (136.67,131.99) -- (186.94,177.87) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=1]  (216.56,211.35) .. controls (216.56,210.49) and (217.26,209.79) .. (218.12,209.79) .. controls (218.99,209.79) and (219.69,210.49) .. (219.69,211.35) .. controls (219.69,212.22) and (218.99,212.92) .. (218.12,212.92) .. controls (217.26,212.92) and (216.56,212.22) .. (216.56,211.35) -- cycle ;
            	\draw [line width=1]    (186.94,177.87) -- (218.12,209.79) ;
            	\draw [line width=1]    (267.56,211.35) -- (219.69,211.35) ;
            	\draw [line width=1]    (268.6,259.53) -- (294.6,259.42) ;
            	\draw [shift={(298.6,259.4)}, rotate = 179.75] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            	\draw [line width=1]    (62.73,53.67) -- (62.62,32.4) ;
            	\draw [shift={(62.6,28.4)}, rotate = 89.7] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            	\draw (203.83,215) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (117,115) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (179.5,155) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (236.5,215) node [anchor=north west][inner sep=0.75pt]    {$R$};
            	\draw (43.5,248) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (281,239) node [anchor=north west][inner sep=0.75pt]    {$x$};
            	\draw (44.5,28) node [anchor=north west][inner sep=0.75pt]    {$y$};	
            \end{tikzpicture} }'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một khu vườn được chia làm hai mảnh đất để trồng hoa màu khác nhau. Mảnh đất hình tròn có phương trình $\left(x - %s\right)^2 + \left(y - %s\right)^2 = %s$ được sử dụng để trồng rau còn mảnh đất hình parabol có phương trình $y = \left(x - %s\right)^2 + %s$ để trồng ngô (minh họa trong hệ trục tọa độ $Oxy$ với đơn vị là $1$ m). Người ta muốn tạo một lối đi $AB$ để di chuyển qua lại giữa hai mảnh đất này. Biết lối đi là khoảng cách ngắn nhất giữa hai mảnh đất. Độ dài ngắn nhất của lối đi này bằng bao nhiêu mét? (Kết quả làm tròn đến chữ số thập phân thứ hai sau dấu phẩy).}{%s}.'''
                                 % (xc, yc, R**2, xv, yv, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Từ phương trình đường tròn $\\left(x - %s\\right)^2 + \\left(y - %s\\right)^2 = %s$, ta xác định được tâm $C\\left(%s; %s\\right)$ và bán kính $R = %s$. \\\\
                Gọi $A\\left(x; \\left(x - %s\\right)^2 + %s\\right)$ là điểm trên parabol. Khi đó khoảng cách ngắn nhất từ $A$ đến miền đường tròn bằng $AC - %s$, với $C\\left(%s; %s\\right)$ là tâm đường tròn. \\\\
                Khi đó $d\\left(A, \\left(C\\right)\\right) = AC - %s$. Do bán kính không đổi, ta chỉ cần tìm $AC$ nhỏ nhất. \\\\
                Ta có $AC^2 = \\left(x - %s\\right)^2 + \\left(\\left(x - %s\\right)^2 + %s - %s\\right)^2 = %s$. \\\\
                Đặt $f\\left(x\\right) = AC^2 = %s$. \\\\
                Ta có $f'\\left(x\\right) = %s$. \\\\
                Giải gần đúng phương trình $f'\\left(x\\right) = 0$ được $x \\approx %s$. \\\\
                Suy ra $f\\left(x\\right)$ đạt giá trị nhỏ nhất tại $x \\approx %s$. \\\\
                Khi đó khoảng cách ngắn nhất từ $A$ đến miền đường tròn là: \\\\
                $d_{min} = \\sqrt{f\\left(%s\\right)} - %s \\approx \\sqrt{%s} - %s \\approx %s$ (m). \\\\
                Vậy độ dài ngắn nhất của lối đi là $%s$ m.'''
                           % (xc, yc, R**2, xc, yc, R,
                              xv, yv, R, xc, yc,
                              R,
                              xc, xv, yv, yc, f_expand_str,
                              f_expand_str,
                              f_prime_str,
                              x_approx,
                              x_approx,
                              x_approx, R, f_approx, R, kq_str,
                              kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

