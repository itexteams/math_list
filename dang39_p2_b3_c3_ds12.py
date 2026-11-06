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


def bt_dang39_p2_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            x = symbols('x')

            # Random hệ số a (đảm bảo a > 0 để giữ nguyên dáng đồ thị)
            # a_coeff có thể là 1, 2, 3, 4 hoặc các phân số 1/2, 3/2, 5/2...
            a_coeff = Rational(random.randint(1, 4), random.randint(1, 2))

            # Tính toán S_A và S_B dựa trên hệ số a
            S_A = a_coeff * Rational(63, 4)
            S_B = a_coeff * Rational(16, 3)

            # Random giá trị f(-2)
            k = random.randint(-15, 15)
            m = random.choice([1, 2, 3, 4])
            val_f_minus2 = Rational(k, m)

            # Tính các giá trị f(1), f(3) và tích phân từ -2 đến 3
            val_f_1 = val_f_minus2 + S_A
            val_f_3 = val_f_1 - S_B
            int_val = S_A - S_B

            # =====================================================================
            # 2. NỘI DUNG CÂU HỎI
            # =====================================================================
            noidungcauhoi = ('''Cho hàm số $y=f(x)$ là hàm đa thức bậc bốn có đồ thị của hàm số $y=f'(x)$ như hình dưới đây. Biết $f\\left(-2\\right)=%s$, diện tích hình phẳng (A), (B) lần lượt bằng $%s$ và $%s$. \\\\
            \\begin{center}
            \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\draw [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]    (96.72,113.6) .. controls (117.12,56.8) and (139.52,39.6) .. (181.12,112.8) ;
            	\\draw [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]    (181.12,112.8) .. controls (218.72,178) and (234.72,170.4) .. (250.72,113.6) ;
            	\\draw [line width=1]    (86.8,168.8) .. controls (90.13,141.47) and (97.47,78.8) .. (129.47,65.47) .. controls (161.47,52.13) and (193.47,158.8) .. (223.47,159.47) .. controls (253.47,160.13) and (258.8,50.8) .. (261.47,23.47) ;
            	\\draw [line width=1]    (57.87,113.47) -- (285.8,113.6) ;
            	\\draw [shift={(289.8,113.6)}, rotate = 180.03] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            	\\draw [line width=1]    (152.4,170.6) -- (151.43,22.6) ;
            	\\draw [shift={(151.4,18.6)}, rotate = 89.62] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            	\\draw (131.6,119) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\\draw (270.8,119) node [anchor=north west][inner sep=0.75pt]    {$x$};
            	\\draw (134.4,19) node [anchor=north west][inner sep=0.75pt]    {$y$};
            	\\draw (72.8,91) node [anchor=north west][inner sep=0.75pt]    {$-2$};
            	\\draw (176,90.6) node [anchor=north west][inner sep=0.75pt]    {$1$};
            	\\draw (255,93.8) node [anchor=north west][inner sep=0.75pt]    {$3$};
                \\draw (115,85) node [anchor=north west][inner sep=0.75pt]    {$(A)$};
            	\\draw (205,122) node [anchor=north west][inner sep=0.75pt]    {$(B)$};
            \\end{tikzpicture}
            \\end{center}''' % (latex(val_f_minus2), latex(S_A), latex(S_B)))

            # =====================================================================
            # 3. TẠO CÁC MỨC ĐỘ CÂU HỎI
            # =====================================================================

            # --- NHẬN BIẾT ---
            if val_f_minus2 > val_f_3:
                str_d_nb = 'f\\left(-2\\right) > f\\left(3\\right)'
                str_s_nb = 'f\\left(-2\\right) < f\\left(3\\right)'
                dau = '>'
            elif val_f_minus2 < val_f_3:
                str_d_nb = 'f\\left(-2\\right) < f\\left(3\\right)'
                str_s_nb = 'f\\left(-2\\right) > f\\left(3\\right)'
                dau = '<'
            else:
                str_d_nb = 'f\\left(-2\\right) = f\\left(3\\right)'
                str_s_nb = 'f\\left(-2\\right) > f\\left(3\\right)'
                dau = '='

            nb_da_1_d = '\\True $%s$' % str_d_nb
            nb_da_1_s = '$%s$' % str_s_nb
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Ta có diện tích $S_A = \\int_{-2}^1 f'(x) \\mathrm{d}x = f\\left(1\\right) - f\\left(-2\\right) = %s \\Rightarrow f\\left(1\\right) = f\\left(-2\\right) + %s = %s$. \\\\
            Diện tích $S_B = -\\int_{1}^3 f'(x) \\mathrm{d}x = -\\left(f\\left(3\\right) - f\\left(1\\right)\\right) = %s \\Rightarrow f\\left(3\\right) = f\\left(1\\right) - %s = %s$. \\\\
            Vì $f\\left(-2\\right) = %s$ và $f\\left(3\\right) = %s$ nên $f\\left(-2\\right) %s f\\left(3\\right)$.''' 
            % (latex(S_A), latex(S_A), latex(val_f_1), latex(S_B), latex(S_B), latex(val_f_3), latex(val_f_minus2), latex(val_f_3), dau))


            # --- THÔNG HIỂU ---
            # Nhiễu: Học sinh quên dấu trừ, cộng S_A và S_B thay vì trừ
            val_int_sai = S_A + S_B

            th_da_1_d = '\\True $\\int_{-2}^{3} f\'(x)\\mathrm{d}x = %s$' % (latex(int_val))
            th_da_1_s = '$\\int_{-2}^{3} f\'(x)\\mathrm{d}x = %s$' % (latex(val_int_sai))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Ta có $\\int_{-2}^{3} f'(x) \\mathrm{d}x = \\int_{-2}^{1} f'(x) \\mathrm{d}x + \\int_{1}^{3} f'(x) \\mathrm{d}x = S_A - S_B = %s - %s = %s$.''' 
            % (latex(S_A), latex(S_B), latex(int_val)))


            # --- VẬN DỤNG ---
            # Nhiễu: Học sinh trừ sai dấu
            val_f_1_sai = val_f_minus2 - S_A

            vd_da_1_d = '\\True $f\\left(1\\right) = %s$' % (latex(val_f_1))
            vd_da_1_s = '$f\\left(1\\right) = %s$' % (latex(val_f_1_sai))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Từ phần trên ta có $\\int_{-2}^1 f'(x) \\mathrm{d}x = f\\left(1\\right) - f\\left(-2\\right) = %s$. \\\\
            Suy ra $f\\left(1\\right) = f\\left(-2\\right) + %s = %s + %s = %s$.''' 
            % (latex(S_A), latex(S_A), latex(val_f_minus2), latex(S_A), latex(val_f_1)))


            # --- VẬN DỤNG CAO ---
            vdc_da_1_d = '\\True Giá trị lớn nhất của hàm số $y=f(x)$ trên đoạn $\\left[ -2; 3 \\right]$ đạt tại $x=1$'
            vdc_da_1_s = 'Giá trị lớn nhất của hàm số $y=f(x)$ trên đoạn $\\left[ -2; 3 \\right]$ đạt tại $x=3$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Từ đồ thị hàm số $f'(x)$, ta thấy: \\\\
            $f'(x) > 0$ với mọi $x \\in \\left(-2; 1\\right)$ nên hàm số đồng biến trên khoảng $\\left(-2; 1\\right)$. \\\\
            $f'(x) < 0$ với mọi $x \\in \\left(1; 3\\right)$ nên hàm số nghịch biến trên khoảng $\\left(1; 3\\right)$. \\\\
            Do đó, hàm số đạt cực đại tại $x=1$. \\\\
            Hàm số liên tục trên đoạn $\\left[ -2; 3 \\right]$, do đó trên đoạn $\\left[ -2; 3 \\right]$, giá trị lớn nhất của hàm số là $f\\left(1\\right)$ đạt tại $x=1$.''')

            # =====================================================================
            # 4. RANDOM LOGIC TRỘN ĐÁP ÁN (1-3 câu True)
            # =====================================================================
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Đóng gói và xáo trộn
            combined_nb = [(nb_da_1, loigiai_nb_1)]
            combined_th = [(th_da_1, loigiai_th_1)]
            combined_vd = [(vd_da_1, loigiai_vd_1)]
            combined_vdc = [(vdc_da_1, loigiai_vdc_1)]

            # =====================================================================
            # 5. XUẤT KẾT QUẢ LATEX
            # =====================================================================
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + combined_nb[0][0] + '}\n'
                '{' + combined_th[0][0] + '}\n'
                '{' + combined_vd[0][0] + '}\n'
                '{' + combined_vdc[0][0] + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + combined_nb[0][1] + '\n'
                '\\item ' + combined_th[0][1] + '\n'
                '\\item ' + combined_vd[0][1] + '\n'
                '\\item ' + combined_vdc[0][1] + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

