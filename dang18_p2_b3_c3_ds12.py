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


def bt_dang18_p2_b3_c3_ds12(self):
                # Khai báo biến
                x = symbols('x')

                # B3: Suy nghĩ tìm cách random bài toán
                # Tạo f(x) = -ax^2 + (a+k+m)x + n và g(x) = mx + n
                a_val = random.randint(1, 2)
                k_val = random.randint(1, 2)
                m_val = random.randint(1, 2)
                n_val = random.randint(1, 2)

                f_expr = -a_val*x**2 + (a_val + k_val + m_val)*x + n_val
                g_expr = m_val*x + n_val

                # Tính diện tích (H) thực tế để dùng cho phương án và lời giải
                dt_h = integrate(f_expr - g_expr, (x, 0, 1))

                # TikZ code (Xử lý dấu %% để tránh lỗi format)
                tikz_code = r"""\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1, scale=0.6]
                \draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (171.7,137.69) .. controls (171.7,81.43) and (204.92,35.82) .. (245.91,35.82) .. controls (286.89,35.82) and (320.11,81.43) .. (320.11,137.69) .. controls (320.11,193.96) and (286.89,239.57) .. (245.91,239.57) .. controls (204.92,239.57) and (171.7,193.96) .. (171.7,137.69) -- cycle ;
                \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (305.31,76.63) .. controls (314.6,93.65) and (320.11,114.79) .. (320.11,137.69) .. controls (320.11,193.96) and (286.89,239.57) .. (245.91,239.57) .. controls (204.92,239.57) and (171.7,193.96) .. (171.7,137.69) .. controls (171.7,129.31) and (172.44,121.17) .. (173.83,113.38) -- cycle ;
                \draw    (139,123.02) -- (361.2,61.81) ;
                \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (166.67,120.51) -- (384.67,120.51) -- (384.67,244.6) -- (166.67,244.6) -- cycle ; 
                \draw    (142.35,145.99) -- (367.58,145.99) ;
                \draw [shift={(369.58,145.99)}, rotate = 180] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
                \draw  [dash pattern={on 4.5pt off 4.5pt}]  (305.31,76.63) -- (305.86,145.66) ;
                \draw    (173.83,179.62) -- (173.83,13.92) ;
                \draw [shift={(173.83,11.92)}, rotate = 90] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
                \draw (225.46,55.34) node [anchor=north west][inner sep=0.75pt]    {$( H)$};
                \draw (215.92,8.38) node [anchor=north west][inner sep=0.75pt]    {$y=f( x)$};
                \draw (322.49,78.82) node [anchor=north west][inner sep=0.75pt]    {$y=g( x)$};
                \draw (154.48,12.58) node [anchor=north west][inner sep=0.75pt]    {$y$};
                \draw (346.49,149.25) node [anchor=north west][inner sep=0.75pt]    {$x$};
                \draw (154.24,147.57) node [anchor=north west][inner sep=0.75pt]    {$O$};
                \draw (296.18,146.73) node [anchor=north west][inner sep=0.75pt]    {$1$};
                \end{tikzpicture}"""

                # Nội dung câu hỏi theo phong cách immini của dang18 nhưng bao bọc bởi template dang17
                noidungcauhoi = (r'''\immini{Cho các hàm số $y = f(x) = %s$ và $y = g(x) = %s$ liên tục trên đoạn $[0;1]$ và có đồ thị như hình bên. Hình phẳng $(H)$ giới hạn bởi đồ thị các hàm số $y=f(x), y=g(x)$ và hai đường thẳng $x=0, x=1$.}{%s}''' 
                                % (latex(f_expr), latex(g_expr), tikz_code))

                ########################################################################
                # a) Nhận biết: Công thức diện tích cơ bản
                ########################################################################
                nb_da_1_d = r'''\True Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y=f(x)$, trục hoành và hai đường thẳng $x=0, x=1$ là $S = \int_0^1 f(x) \text{d}x$'''
                nb_da_1_s = r'''Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y=f(x)$, trục hoành và hai đường thẳng $x=0, x=1$ là $S = \int_0^1 f^2(x) \text{d}x$'''
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                loigiai_nb_1 = r'''Dựa vào đồ thị, trên đoạn $[0;1]$ hàm số $f(x)$ luôn nằm phía trên trục hoành nên $S = \int_0^1 |f(x)| \text{d}x = \int_0^1 f(x) \text{d}x$.'''

                ########################################################################
                # b) Thông hiểu: Công thức thể tích vật thể tròn xoay
                ########################################################################
                th_da_1_d = r'''\True Thể tích vật thể tròn xoay khi quay hình phẳng giới hạn bởi $y=f(x)$, trục hoành và $x=0, x=1$ quanh $Ox$ là $V = \pi \int_0^1 f^2(x) \text{d}x$'''
                th_da_1_s = r'''Thể tích vật thể tròn xoay khi quay hình phẳng giới hạn bởi $y=f(x)$, trục hoành và $x=0, x=1$ quanh $Ox$ là $V = \int_0^1 f^2(x) \text{d}x$'''
                list_th_da_1 = [th_da_1_d, th_da_1_s]
                loigiai_th_1 = r'''Công thức thể tích vật thể tròn xoay tạo thành khi quay quanh trục $Ox$ là $V = \pi \int_a^b f^2(x) \text{d}x$.'''

                ########################################################################
                # c) Vận dụng: Tính diện tích hình phẳng (H)
                ########################################################################
                vd_da_1_d = r'''\True Diện tích hình phẳng $(H)$ là $S = \int_0^1 [f(x) - g(x)] \text{d}x = %s$''' % (latex(dt_h))
                vd_da_1_s = r'''Diện tích hình phẳng $(H)$ là $S = \int_0^1 [g(x) - f(x)] \text{d}x$'''
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                loigiai_vd_1 = r'''Trên đoạn $[0;1]$, đồ thị $f(x)$ nằm phía trên đồ thị $g(x)$. Do đó $S = \int_0^1 [f(x) - g(x)] \text{d}x = \int_0^1 (%s) \text{d}x = %s$.''' % (latex(f_expr - g_expr), latex(dt_h))

                ########################################################################
                # d) Vận dụng cao: Công thức thể tích cho miền giới hạn bởi 2 đồ thị
                ########################################################################
                vdc_da_1_d = r'''\True Thể tích vật thể tròn xoay khi quay $(H)$ quanh trục $Ox$ là $V = \pi \int_0^1 [f^2(x) - g^2(x)] \text{d}x$'''
                vdc_da_1_s = r'''Thể tích vật thể tròn xoay khi quay $(H)$ quanh trục $Ox$ là $V = \pi \int_0^1 [f(x) - g(x)]^2 \text{d}x$'''
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                loigiai_vdc_1 = r'''Vì $f(x) \ge g(x) \ge 0$ trên đoạn $[0;1]$, thể tích tròn xoay khi quay miền $(H)$ quanh $Ox$ là $V = \pi \int_0^1 |f^2(x) - g^2(x)| \text{d}x = \pi \int_0^1 [f^2(x) - g^2(x)] \text{d}x$.'''

                # --- Trình bày kết quả và chọn đáp án ---
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    ans_a = random.choice(list_nb_da_1)
                    ans_b = random.choice(list_th_da_1)
                    ans_c = random.choice(list_vd_da_1)
                    ans_d = random.choice(list_vdc_da_1)
                    if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                        break

                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + 
                    '\n\\choiceTFn \n'
                    '{' + str(ans_a) + '}\n'
                    '{' + str(ans_b) + '}\n'
                    '{' + str(ans_c) + '}\n'
                    '{' + str(ans_d) + '}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item ' + str(loigiai_nb_1) + '\n'
                    '\\item ' + str(loigiai_th_1) + '\n'
                    '\\item ' + str(loigiai_vd_1) + '\n'
                    '\\item ' + str(loigiai_vdc_1) + '\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n \\end{minipage}\n\n')

                return content

