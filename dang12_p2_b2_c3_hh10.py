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


def bt_dang12_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y = symbols('x y')

            # 1. Tạo các hệ số ngẫu nhiên cho đường thẳng d: a1*x + b1*y + c1 = 0
            # Chọn hệ số sao cho số liệu đẹp (nguyên hoặc phân số đơn giản)
            a1 = random.choice([1, 2, 3])
            b1 = random.choice([-3, -2, -1, 1, 2, 3])
            c1 = random.randint(-5, 5)

            # Tạo đường thẳng k: a2*x + b2*y + c2 = 0 
            # Để câu d giải ra số đẹp, ta chọn a2, b2 sao cho a1^2 + b1^2 = a2^2 + b2^2
            # Một cặp phổ biến là (a, b) và (b, a) hoặc (a, -b)
            a2 = b1 if b1 > 0 else -b1
            b2 = a1
            c2 = random.randint(1, 10)

            # Chọn tọa độ điểm A(x0, y0)
            x0 = random.randint(-4, 4)
            y0 = random.randint(-4, 4)

            # --- Tính toán các giá trị đáp án ---

            # a) Kiểm tra tính cắt nhau: a1*b2 - a2*b1 != 0
            cat_nhau = (a1 * b2 - a2 * b1 != 0)

            # b) Hình chiếu H(Hx, Hy) của A lên d
            # Đường thẳng qua A vuông góc d: b1*(x - x0) - a1*(y - y0) = 0
            dt_vuong_goc = b1*(x - x0) - a1*(y - y0)
            he_pt_h = [a1*x + b1*y + c1, dt_vuong_goc]
            res_h = solve(he_pt_h, [x, y])
            Hx, Hy = res_h[x], res_h[y]

            # c) Điểm đối xứng A' qua d: H là trung điểm AA'
            Ax_prime = 2*Hx - x0
            Ay_prime = 2*Hy - y0

            # d) Điểm M có hoành độ xB, cách đều d và k
            xB = random.randint(-5, 5)
            y_val = symbols('y_val')
            # Phương trình khoảng cách (đã khử mẫu do mẫu bằng nhau): 
            # |a1*xB + b1*y_val + c1| = |a2*xB + b2*y_val + c2|
            eq1 = (a1*xB + b1*y_val + c1) - (a2*xB + b2*y_val + c2)
            eq2 = (a1*xB + b1*y_val + c1) + (a2*xB + b2*y_val + c2)
            sol_y = solve(eq1, y_val) + solve(eq2, y_val) # Trả về list các nghiệm
            yM = sol_y[0] if sol_y else Rational(1, 2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai đường thẳng $d: %s = 0$; $k: %s = 0$ và điểm $A\\left( %s; %s \\right)$.''' 
                             %(latex(a1*x + b1*y + c1), latex(a2*x + b2*y + c2), latex(x0), latex(y0)))

            ########################################################################
            # NHẬN BIẾT: Xét vị trí tương đối
            if cat_nhau:
                nb_da_1_d = '\\True Hai đường thẳng $d$ và $k$ cắt nhau'
                nb_da_1_s = 'Hai đường thẳng $d$ và $k$ song song với nhau'
            else:
                nb_da_1_d = '\\True Hai đường thẳng $d$ và $k$ song song'
                nb_da_1_s = 'Hai đường thẳng $d$ và $k$ cắt nhau'

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Đường thẳng $d$ có vectơ pháp tuyến là $\\vec{n}_d = \\left( %s; %s \\right)$. \\\\
                            Đường thẳng $k$ có vectơ pháp tuyến là $\\vec{n}_k = \\left( %s; %s \\right)$. \\\\
                            Ta thấy $%s \\cdot \\left( %s \\right) - %s \\cdot \\left( %s \\right) = %s \\neq 0$ nên hai đường thẳng cắt nhau.'''
                            %(latex(a1), latex(b1), latex(a2), latex(b2), latex(a1), latex(b2), latex(a2), latex(b1), latex(a1*b2 - a2*b1)))

            ########################################################################
            # THÔNG HIỂU: Tìm hình chiếu H
            th_da_1_d = '\\True Toạ độ hình chiếu vuông góc của $A$ trên đường thẳng $d$ là $H\\left( %s; %s \\right)$' %(latex(Hx), latex(Hy))
            th_da_1_s = 'Toạ độ hình chiếu vuông góc của $A$ trên đường thẳng $d$ là $H\\left( %s; %s \\right)$' %(latex(Hx + 1), latex(Hy))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Gọi $\\Delta$ là đường thẳng đi qua điểm $A\\left( %s; %s \\right)$ và vuông góc với đường thẳng $d$. \\\\
                            Phương trình của đường thẳng $\\Delta$ là: $%s\\left( x - \\left( %s \\right) \\right) - %s\\left( y - \\left( %s \\right) \\right) = 0 \\Leftrightarrow %s = 0$. \\\\
                            Tọa độ hình chiếu $H$ là nghiệm của hệ phương trình: \\\\
                            $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. \\\\
                            Vậy $H\\left( %s; %s \\right)$.'''
                            %(latex(x0), latex(y0), latex(b1), latex(x0), latex(a1), latex(y0), latex(simplify(dt_vuong_goc)), 
                              latex(a1*x + b1*y + c1), latex(simplify(dt_vuong_goc)), latex(Hx), latex(Hy), latex(Hx), latex(Hy)))

            ########################################################################
            # VẬN DỤNG: Điểm đối xứng A'
            vd_da_1_d = '\\True Điểm đối xứng của $A$ qua đường thẳng $d$ có toạ độ là $A\'\\left( %s; %s \\right)$' %(latex(Ax_prime), latex(Ay_prime))
            vd_da_1_s = 'Điểm đối xứng của $A$ qua đường thẳng $d$ có toạ độ là $A\'\\left( %s; %s \\right)$' %(latex(Ax_prime), latex(Ay_prime + 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì $A\'$ đối xứng với $A$ qua đường thẳng $d$ nên $H$ là trung điểm của đoạn thẳng $AA\'$. \\\\
                            Ta có hệ thức: $\\begin{cases} x_{A\'} = 2x_H - x_A = 2 \\cdot \\left( %s \\right) - \\left( %s \\right) = %s \\\\ y_{A\'} = 2y_H - y_A = 2 \\cdot \\left( %s \\right) - \\left( %s \\right) = %s \\end{cases}$. \\\\
                            Vậy $A\'\\left( %s; %s \\right)$.'''
                            %(latex(Hx), latex(x0), latex(Ax_prime), latex(Hy), latex(y0), latex(Ay_prime), latex(Ax_prime), latex(Ay_prime)))

            ########################################################################
            # VẬN DỤNG CAO: Điểm cách đều hai đường thẳng
            vdc_da_1_d = '\\True Điểm $M$ có hoành độ bằng $%s$ cách đều hai đường thẳng có tọa độ là $M\\left( %s; %s \\right)$' %(latex(xB), latex(xB), latex(yM))
            vdc_da_1_s = 'Điểm $M$ có hoành độ bằng $%s$ cách đều hai đường thẳng có tọa độ là $M\\left( %s; %s \\right)$' %(latex(xB), latex(xB), latex(yM - 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Gọi tọa độ điểm $M$ là $M\\left( %s; y \\right)$. Theo giả thiết $M$ cách đều hai đường thẳng $d$ và $k$ nên: \\\\
                            $d\\left( M, d \\right) = d\\left( M, k \\right) \\Leftrightarrow \\frac{\\left| %s \\cdot \\left( %s \\right) + %s y + %s \\right|}{\\sqrt{%s^2 + \\left( %s \\right)^2}} = \\frac{\\left| %s \\cdot \\left( %s \\right) + %s y + %s \\right|}{\\sqrt{%s^2 + %s^2}}$ \\\\
                            Vì $\\sqrt{%s^2 + \\left( %s \\right)^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s}$ nên phương trình trở thành: \\\\
                            $\\left| %s y + %s \\right| = \\left| %s y + %s \\right|$. \\\\
                            Giải phương trình ta thu được giá trị $y = %s$. \\\\
                            Vậy tọa độ điểm cần tìm là $M\\left( %s; %s \\right)$.'''
                            %(latex(xB), latex(a1), latex(xB), latex(b1), latex(c1), latex(a1), latex(b1),
                              latex(a2), latex(xB), latex(b2), latex(c2), latex(a2), latex(b2),
                              latex(a1), latex(b1), latex(a2), latex(b2), latex(a1**2 + b1**2),
                              latex(b1), latex(a1*xB + c1), latex(b2), latex(a2*xB + c2), latex(yM), latex(xB), latex(yM)))

            # Kiểm tra số lượng đáp án đúng (từ 1 đến 3)
            def count_true(ans_list):
                return sum('\\True' in a for a in ans_list)

            while True:
                da_a = random.choice(list_nb_da_1)
                da_b = random.choice(list_th_da_1)
                da_c = random.choice(list_vd_da_1)
                da_d = random.choice(list_vdc_da_1)
                if 1 <= count_true([da_a, da_b, da_c, da_d]) <= 3:
                    break

            # Xuất kết quả theo mẫu content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(da_a) + '}\n'
                '{' + str(da_b) + '}\n'
                '{' + str(da_c) + '}\n'
                '{' + str(da_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

