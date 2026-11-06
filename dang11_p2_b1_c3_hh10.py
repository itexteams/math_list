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


def bt_dang11_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo các điểm và biến
            x, y, t = symbols('x y t')

            # Bước 1: Thiết lập các thông số cố định từ đề bài để tính toán
            # Có thể random các giá trị này nếu muốn bài toán thay đổi số liệu hoàn toàn
            xA, yA = -1, 0
            xB, yB = 1, 2
            xC, yC = 3, 3

            # Tính toán các thành phần hình học
            # 1. Đường thẳng AB
            uAB = (xB - xA, yB - yA) # Vector AB = (2, 2)
            # Rút gọn vector chỉ phương
            v_cp = (1, 1) 

            # 2. Đường trung trực AB
            midAB_x, midAB_y = Rational(xA + xB, 2), Rational(yA + yB, 2) # (0, 1)
            # Vector pháp tuyến chính là vector AB(2, 2) hoặc (1, 1)
            n_truc = (xB - xA, yB - yA)
            c_truc = -(n_truc[0]*midAB_x + n_truc[1]*midAB_y)
            # Phương trình: 2x + 2y - 2 = 0 <=> x + y - 1 = 0

            # 3. Đường trung tuyến BM (M là trung điểm AC)
            midAC_x, midAC_y = Rational(xA + xC, 2), Rational(yA + yC, 2) # (1, 3/2)
            # Đường thẳng qua B(1, 2) và M(1, 1.5) có xB = xM = 1 nên là đường thẳng x = 1
            # Dạng tổng quát: x - 1 = 0

            # 4. Điểm D thuộc AB sao cho CD = 5
            # Tham số hóa D theo AB: x = -1 + t, y = t
            t_val = symbols('t_val')
            xD_t = xA + v_cp[0]*t_val
            yD_t = yA + v_cp[1]*t_val
            dist_sq = (xD_t - xC)**2 + (yD_t - yC)**2
            sol_t = solve(dist_sq - 5**2, t_val)
            # Với t=7, D = (6, 7). Với t=0, D = (-1, 0)
            # Đề bài yêu cầu hoành độ dương nên lấy D(6, 7)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng $Oxy$, cho ba điểm $A(%s; %s)$, $B(%s; %s)$ và $C(%s; %s)$.''' 
                             %(latex(xA), latex(yA), latex(xB), latex(yB), latex(xC), latex(yC)))

            ########################################################################
            # a) Phương trình tham số AB
            # Đúng: x = -1 + t, y = t
            da_a_d = '\\True Phương trình tham số của đường thẳng $AB$ là $\\begin{cases} x = -1 + t \\\\ y = t \\end{cases}$'
            da_a_s = 'Phương trình tham số của đường thẳng $AB$ là $\\begin{cases} x = 1 + t \\\\ y = 2 - t \\end{cases}$'
            list_da_a = [da_a_d, da_a_s]

            loigiai_a = ('''Ta có $\\vec{AB} = (%s; %s) = 2(1; 1)$. Đường thẳng $AB$ đi qua điểm $A(%s; %s)$ và có vectơ chỉ phương $\\vec{u} = (1; 1)$ nên có phương trình tham số là $\\begin{cases} x = %s + t \\\\ y = %s + t \\end{cases}$.'''
                         %(latex(xB-xA), latex(yB-yA), latex(xA), latex(yA), latex(xA), latex(yA)))

            ########################################################################
            # b) Đường trung trực AB
            # Đúng: x + y - 1 = 0. Đề bài cho x + y - 2 = 0 (Sai)
            da_b_d = '\\True Phương trình đường trung trực của đoạn $AB$ là $x + y - 1 = 0$'
            da_b_s = 'Phương trình đường trung trực của đoạn $AB$ là $x + y - 2 = 0$'
            list_da_b = [da_b_d, da_b_s]

            loigiai_b = ('''Gọi $I$ là trung điểm của $AB$, ta có $I\\left( \\frac{%s + %s}{2}; \\frac{%s + %s}{2} \\right) = (%s; %s)$. \\\\
                         Đường trung trực của $AB$ đi qua $I(%s; %s)$ và nhận $\\vec{AB} = (%s; %s)$ làm vectơ pháp tuyến. \\\\
                         Phương trình đường trung trực: $%s(x - %s) + %s(y - %s) = 0 \\Leftrightarrow x + y - 1 = 0$.'''
                         %(latex(xA), latex(xB), latex(yA), latex(yB), latex(midAB_x), latex(midAB_y), 
                           latex(midAB_x), latex(midAB_y), latex(xB-xA), latex(yB-yA),
                           latex(v_cp[0]), latex(midAB_x), latex(v_cp[1]), latex(midAB_y)))

            ########################################################################
            # c) Đường trung tuyến BM
            # Đúng: x - 1 = 0. Đề bài cho x + y - 3 = 0 (Sai)
            da_c_d = '\\True Phương trình đường trung tuyến $BM$ là $x - 1 = 0$'
            da_c_s = 'Phương trình đường trung tuyến $BM$ là $x + y - 3 = 0$'
            list_da_c = [da_c_d, da_c_s]

            loigiai_c = ('''Gọi $M$ là trung điểm của $AC$, ta có $M\\left( \\frac{%s + %s}{2}; \\frac{%s + %s}{2} \\right) = \\left( %s; %s \\right)$. \\\\
                         Đường trung tuyến $BM$ đi qua $B(%s; %s)$ và $M\\left( %s; %s \\right)$. \\\\
                         Vì cả $B$ và $M$ đều có hoành độ bằng $1$ nên phương trình đường thẳng $BM$ là $x - 1 = 0$.'''
                         %(latex(xA), latex(xC), latex(yA), latex(yC), latex(midAC_x), latex(midAC_y),
                           latex(xB), latex(yB), latex(midAC_x), latex(midAC_y)))

            ########################################################################
            # d) Điểm D
            # Đúng: (6, 7)
            da_d_d = '\\True Điểm $D$ có hoành độ dương thuộc đường thẳng $AB$ thoả mãn $CD = 5$ có toạ độ là $(6; 7)$'
            da_d_s = 'Điểm $D$ có hoành độ dương thuộc đường thẳng $AB$ thoả mãn $CD = 5$ có toạ độ là $(2; 3)$'
            list_da_d = [da_d_d, da_d_s]

            loigiai_d = ('''Vì $D \\in AB$ nên toạ độ điểm $D$ có dạng $D(-1 + t; t)$. \\\\
                         Ta có $CD = 5 \\Leftrightarrow CD^2 = 25 \\Leftrightarrow (-1 + t - 3)^2 + (t - 3)^2 = 25$ \\\\
                         $\\Leftrightarrow (t - 4)^2 + (t - 3)^2 = 25 \\Leftrightarrow 2t^2 - 14t = 0 \\Leftrightarrow \\left[ \\begin{aligned} & t = 0 \\\\ & t = 7 \\end{aligned} \\right.$ \\\\
                         Với $t = 0 \\Rightarrow D(-1; 0)$ (loại vì hoành độ không dương). \\\\
                         Với $t = 7 \\Rightarrow D(6; 7)$ (nhận). Vậy $D(6; 7)$.''')

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp chọn ngẫu nhiên các phương án để đảm bảo số lượng câu đúng từ 1 đến 3
            while True:
                sel_a = random.choice(list_da_a)
                sel_b = random.choice(list_da_b)
                sel_c = random.choice(list_da_c)
                sel_d = random.choice(list_da_d)

                answers = [sel_a, sel_b, sel_c, sel_d]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(sel_a) + '}\n'
                '{' + str(sel_b) + '}\n'
                '{' + str(sel_c) + '}\n'
                '{' + str(sel_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

