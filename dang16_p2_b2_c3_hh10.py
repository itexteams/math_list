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


def bt_dang16_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y, a_sym = symbols('x y a')

            # --- BƯỚC 1: TẠO DỮ LIỆU NGẪU NHIÊN ---
            # Đường thẳng d1: a1*x + b1*y + c1 = 0
            # Đường thẳng d2: a2*x + b2*y + c2 = 0
            while True:
                a1 = random.randint(1, 4)
                b1 = random.randint(-5, -1)
                c1 = random.randint(1, 10)

                a2 = random.randint(-5, -1)
                b2 = random.randint(1, 4)
                c2 = random.randint(-20, -10)

                # Kiểm tra để hai đường không song song/trùng nhau (tích vô hướng và định thức)
                det = a1*b2 - a2*b1
                if det != 0:
                    break

            d1_expr = a1*x + b1*y + c1
            d2_expr = a2*x + b2*y + c2

            # --- BƯỚC 2: TÍNH TOÁN CÁC THÔNG SỐ ---

            # a) Kiểm tra vuông góc
            is_perpendicular = (a1*a2 + b1*b2 == 0)

            # b) Tìm giao điểm I
            sol = solve([d1_expr, d2_expr], [x, y])
            xI = sol[x]
            yI = sol[y]

            # c) Tính góc giữa hai đường thẳng
            cos_phi = abs(a1*a2 + b1*b2) / (sqrt(a1**2 + b1**2) * sqrt(a2**2 + b2**2))
            phi_rad = math.acos(float(cos_phi))
            phi_deg = round(math.degrees(phi_rad))

            # d) Tam giác OAB vuông cân tại B (A thuộc Ox, B thuộc d2)
            # B(xb, yb) thuộc d2 => yb = (-a2*xb - c2)/b2
            xb = symbols('xb')
            yb = (-a2*xb - c2)/b2
            # A(a_val, 0)
            # Vector BO = (-xb, -yb), Vector BA = (a_val - xb, -yb)
            # Điều kiện 1: BO = BA => xb^2 + yb^2 = (a_val-xb)^2 + yb^2 => xb^2 = (a_val-xb)^2 => a_val = 2*xb (vì A khác O)
            # Điều kiện 2: BO vuông góc BA => -xb*(a_val-xb) + (-yb)*(-yb) = 0 => -xb*(2*xb-xb) + yb^2 = 0 => -xb^2 + yb^2 = 0
            eq_B = -xb**2 + yb**2
            sol_B = solve(eq_B, xb)
            # Lọc các điểm B thực và thỏa mãn A khác O (xb khác 0)
            points_B = [val for val in sol_B if val != 0]
            num_B = len(points_B)

            # Hàm chuyển đổi số thập phân sang dấu phẩy kiểu Việt Nam
            def format_vn(val):
                s = str(val)
                return s.replace('.', ',')

            # --- BƯỚC 3: NỘI DUNG CÂU HỎI VÀ ĐÁP ÁN ---
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $\\left( Oxy \\right)$, cho hai đường thẳng $d_1 : %s = 0$ và $d_2 : %s = 0$.''' 
                             % (latex(d1_expr), latex(d2_expr)))

            # --- NHẬN BIẾT (Câu a) ---
            nb_da_d = '\\True $d_1 \\perp d_2$.' if is_perpendicular else '$d_1 \\perp d_2$'
            nb_da_s = '\\True $d_1$ không vuông góc với $d_2$.' if not is_perpendicular else '$d_1$ không vuông góc với $d_2$'
            list_nb = [nb_da_d, nb_da_s]
            nb_da = random.choice(list_nb)
            loigiai_nb = ('''Đường thẳng $d_1$ có vectơ pháp tuyến $\\vec{n}_1 = \\left( %s; %s \\right)$, $d_2$ có vectơ pháp tuyến $\\vec{n}_2 = \\left( %s; %s \\right)$. \\\\
                          Ta có $\\vec{n}_1 \\cdot \\vec{n}_2 = %s \\cdot \\left( %s \\right) + \\left( %s \\right) \\cdot %s = %s$. \\\\
                          Vì tích vô hướng $%s %s$ nên $d_1$ %s vuông góc với $d_2$.''' 
                          % (a1, b1, a2, b2, a1, a2, b1, b2, a1*a2+b1*b2, 
                             '=' if is_perpendicular else '\\neq', 0, '' if is_perpendicular else 'không'))

            # --- THÔNG HIỂU (Câu b) ---
            coords_I = '\\left( %s; %s \\right)' % (latex(xI), latex(yI))
            th_da_d = '\\True $I' + coords_I + '$ là tọa độ giao điểm của $2$ đường thẳng $d_1$ và $d_2$'
            th_da_s = '$I' + '\\left( %s; %s \\right)' % (latex(xI+1), latex(yI)) + '$ là tọa độ giao điểm của $2$ đường thẳng $d_1$ và $d_2$'
            list_th = [th_da_d, th_da_s]
            th_da = random.choice(list_th)
            loigiai_th = ('''Tọa độ giao điểm của $d_1$ và $d_2$ là nghiệm của hệ phương trình: \\\\
                          $\\left\\{ \\begin{aligned} & %s = 0 \\\\ & %s = 0 \\end{aligned} \\right. \\Leftrightarrow \\left\\{ \\begin{aligned} & x = %s \\\\ & y = %s \\end{aligned} \\right.$. \\\\
                          Vậy giao điểm là $I%s$.''' 
                          % (latex(d1_expr), latex(d2_expr), latex(xI), latex(yI), coords_I))

            # --- VẬN DỤNG (Câu c) ---
            val_angle = phi_deg
            vd_da_d = '\\True Góc giữa $2$ đường thẳng $d_1$ và $d_2$ bằng $%s^\\circ$' % val_angle
            vd_da_s = 'Góc giữa $2$ đường thẳng $d_1$ và $d_2$ bằng $%s^\\circ$' % (180 - val_angle if val_angle != 90 else 45)
            list_vd = [vd_da_d, vd_da_s]
            vd_da = random.choice(list_vd)
            loigiai_vd = ('''Gọi $\\varphi$ là góc giữa hai đường thẳng, ta có: \\\\
                          $\\cos \\varphi = \\frac{\\left| \\vec{n}_1 \\cdot \\vec{n}_2 \\right|}{\\left| \\vec{n}_1 \\right| \\cdot \\left| \\vec{n}_2 \\right|} = \\frac{\\left| %s \\right|}{\\sqrt{%s^2 + \\left( %s \\right)^2} \\cdot \\sqrt{\\left( %s \\right)^2 + %s^2}} = %s$. \\\\
                          Suy ra $\\varphi \\approx %s^\\circ$.''' 
                          % (a1*a2+b1*b2, a1, b1, a2, b2, latex(cos_phi), val_angle))

            # --- VẬN DỤNG CAO (Câu d) ---
            vdc_da_d = '\\True Gọi $A$ là điểm thuộc trục hoành (khác gốc tọa độ $O$) và $B$ là điểm thuộc đường thẳng $d_2$ sao cho tam giác $OAB$ vuông cân tại $B$. Khi đó, có $%s$ điểm $B$ thỏa mãn yêu cầu bài toán' % num_B
            vdc_da_s = 'Gọi $A$ là điểm thuộc trục hoành (khác gốc tọa độ $O$) và $B$ là điểm thuộc đường thẳng $d_2$ sao cho tam giác $OAB$ vuông cân tại $B$. Khi đó, có $%s$ điểm $B$ thỏa mãn yêu cầu bài toán' % (num_B + 1)
            list_vdc = [vdc_da_d, vdc_da_s]
            vdc_da = random.choice(list_vdc)
            loigiai_vdc = ('''Giả sử $A\\left( a; 0 \\right) \\in Ox \\left( a \\neq 0 \\right)$ và $B\\left( x_B; y_B \\right) \\in d_2$. \\\\
                           Tam giác $OAB$ vuông cân tại $B$ nên $BA = BO$ và $\\vec{BA} \\cdot \\vec{BO} = 0$. \\\\
                           Từ $BA = BO$ và $A \\in Ox, O \\in Ox$ suy ra $x_B = \\frac{a}{2} \\Rightarrow a = 2x_B$. \\\\
                           Khi đó $\\vec{BO} = \\left( -x_B; -y_B \\right)$ và $\\vec{BA} = \\left( x_B; -y_B \\right)$. \\\\
                           $\\vec{BA} \\cdot \\vec{BO} = 0 \\Leftrightarrow -x_B^2 + y_B^2 = 0 \\Leftrightarrow y_B^2 = x_B^2 \\Leftrightarrow \\left[ \\begin{aligned} & y_B = x_B \\\\ & y_B = -x_B \\end{aligned} \\right.$. \\\\
                           Thay vào phương trình $d_2$ ta tìm được các giá trị $x_B$ tương ứng. \\\\
                           Vì $a \\neq 0$ nên $x_B \\neq 0$. Số điểm $B$ thỏa mãn là $%s$.''' % num_B)

            # --- XÁO TRỘN VÀ ĐÓNG GÓI ---
            shuffled_ans = [nb_da, th_da, vd_da, vdc_da]
            shuffled_sols = [loigiai_nb, loigiai_th, loigiai_vd, loigiai_vdc]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_ans[0]) + '}\n'
                '{' + str(shuffled_ans[1]) + '}\n'
                '{' + str(shuffled_ans[2]) + '}\n'
                '{' + str(shuffled_ans[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_sols[0]) + '\n'
                '\\item ' + str(shuffled_sols[1]) + '\n'
                '\\item ' + str(shuffled_sols[2]) + '\n'
                '\\item ' + str(shuffled_sols[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

