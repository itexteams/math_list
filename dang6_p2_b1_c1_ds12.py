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


def bt_dang6_p2_b1_c1_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng các số hạng trong đa thức (tránh in ra kiểu + -5x)
            def format_term(coef, var_str, is_first=False):
                if coef == 0: return ""
                sign = "+" if coef > 0 else "-"
                abs_coef = abs(coef)

                if is_first:
                    sign_str = "-" if coef < 0 else ""
                else:
                    sign_str = f" {sign} "

                coef_str = ""
                if abs_coef != 1 or var_str == "":
                    coef_str = str(abs_coef)

                return f"{sign_str}{coef_str}{var_str}"

            x = symbols('x')

            # BỘ DỮ LIỆU RANDOM
            # Chọn các cặp nghiệm (r1, r2) cùng tính chẵn lẻ để hệ số b luôn là số nguyên
            root_pairs = [(1, 3), (1, 5), (1, 7), (1, 9), (2, 4), (2, 6), (3, 5), (-1, 3), (-3, 1), (-5, -1)]
            r1, r2 = random.choice(root_pairs)
            if r1 > r2: 
                r1, r2 = r2, r1 # Đảm bảo r1 < r2

            # Xây dựng hệ số từ nghiệm: f'(x) = (x - r1)(x - r2) = x^2 - (r1+r2)x + r1*r2
            # f'(x) = x^2 + 2bx + c
            b = - (r1 + r2) // 2
            c = r1 * r2
            d = random.randint(-10, 10) # Hệ số tự do d random ngẫu nhiên

            # Tạo chuỗi hiển thị hàm số f(x) = 1/3 x^3 + bx^2 + cx + d
            fx_str = "\\frac{1}{3}x^3"
            fx_str += format_term(b, "x^2")
            fx_str += format_term(c, "x")
            fx_str += format_term(d, "")

            # Biểu thức tính toán qua Sympy
            fx_expr = Rational(1, 3) * x**3 + b * x**2 + c * x + d
            fx_deriv_expr = x**2 + 2 * b * x + c

            # Tính các giá trị cực trị
            y_max = fx_expr.subs(x, r1)
            y_min = fx_expr.subs(x, r2)

            # Nội dung câu hỏi
            noidungcauhoi = "Cho hàm số $f(x) = %s$." % fx_str

            ######################################################################## Nhận biết (Đạo hàm) ############################

            # Tạo biểu thức đạo hàm sai (đổi dấu c)
            fprime_false = x**2 + 2 * b * x - c if c != 0 else x**2 - 2 * b * x + 1

            nb_da_1_d = "\\True Hàm số đã cho có đạo hàm là $f'(x) = %s$" % latex(fx_deriv_expr)
            loigiai_nb_1_d = "Ta có $f'(x) = \\left( %s \\right)' = %s$. Phát biểu đúng." % (fx_str, latex(fx_deriv_expr))

            nb_da_1_s = "Hàm số đã cho có đạo hàm là $f'(x) = %s$" % latex(fprime_false)
            loigiai_nb_1_s = "Ta có đạo hàm đúng phải là $f'(x) = \\left( %s \\right)' = %s$. Phát biểu sai." % (fx_str, latex(fx_deriv_expr))

            ######################################################################## Thông hiểu (Nghiệm f'(x)=0) ####################

            th_da_1_d = "\\True Phương trình $f'(x)=0$ có tập nghiệm là $S = \\{%s; %s\\}$" % (r1, r2)
            loigiai_th_1_d = "Ta có $f'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\\\ x = %s \\end{array} \\right.$. Vậy tập nghiệm $S = \\{%s; %s\\}$. Phát biểu đúng." % (latex(fx_deriv_expr), r1, r2, r1, r2)

            # Tập nghiệm sai (đổi dấu r1)
            th_da_1_s = "Phương trình $f'(x)=0$ có tập nghiệm là $S = \\{%s; %s\\}$" % (-r1, r2)
            loigiai_th_1_s = "Giải phương trình $f'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow x \\in \\{%s; %s\\}$. Tập nghiệm đề bài cho là sai." % (latex(fx_deriv_expr), r1, r2)

            ######################################################################## Vận dụng (Khoảng nghịch biến) ##################

            vd_da_1_d = "\\True Hàm số đã cho nghịch biến trên khoảng $(%s; %s)$" % (r1, r2)
            loigiai_vd_1_d = "Ta có $f'(x) < 0 \\Leftrightarrow %s < 0 \\Leftrightarrow %s < x < %s$. Do đó hàm số nghịch biến trên khoảng $(%s; %s)$. Phát biểu đúng." % (latex(fx_deriv_expr), r1, r2, r1, r2)

            vd_da_1_s = "Hàm số đã cho đồng biến trên khoảng $(%s; %s)$" % (r1, r2)
            loigiai_vd_1_s = "Xét dấu đạo hàm, ta có $f'(x) < 0 \\Leftrightarrow x \\in (%s; %s)$. Do đó trên khoảng này hàm số nghịch biến chứ không phải đồng biến. Phát biểu sai." % (r1, r2)

            ######################################################################## Vận dụng cao (Giá trị cực tiểu) #################

            vdc_da_1_d = "\\True Giá trị cực tiểu của hàm số đã cho bằng $%s$" % latex(y_min)
            loigiai_vdc_1_d = "Hàm số đạt cực tiểu tại $x = %s$. Giá trị cực tiểu là $y_{CT} = f(%s) = %s$. Phát biểu đúng." % (r2, r2, latex(y_min))

            vdc_da_1_s = "Giá trị cực tiểu của hàm số đã cho bằng $%s$" % latex(y_max) # Cố tình lấy giá trị cực đại để lừa
            loigiai_vdc_1_s = "Hàm số đạt cực tiểu tại $x = %s$, khi đó giá trị cực tiểu đúng phải là $y_{CT} = f(%s) = %s$. Số $%s$ thực chất là giá trị cực đại đạt tại $x = %s$. Phát biểu sai." % (r2, r2, latex(y_min), latex(y_max), r1)

            ######################################################################## Trộn và xuất ############################################

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi bộ đáp án có từ 1 đến 3 lựa chọn đúng
            while True:
                nb_choice = random.choice([(nb_da_1_d, loigiai_nb_1_d), (nb_da_1_s, loigiai_nb_1_s)])
                th_choice = random.choice([(th_da_1_d, loigiai_th_1_d), (th_da_1_s, loigiai_th_1_s)])
                vd_choice = random.choice([(vd_da_1_d, loigiai_vd_1_d), (vd_da_1_s, loigiai_vd_1_s)])
                vdc_choice = random.choice([(vdc_da_1_d, loigiai_vdc_1_d), (vdc_da_1_s, loigiai_vdc_1_s)])

                answers = [nb_choice[0], th_choice[0], vd_choice[0], vdc_choice[0]]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gắn đáp án và lời giải tương ứng
            ans_nb, sol_nb = nb_choice
            ans_th, sol_th = th_choice
            ans_vd, sol_vd = vd_choice
            ans_vdc, sol_vdc = vdc_choice

            # Xuất câu hỏi với đáp án và lời giải đã được kết hợp chuẩn xác
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+
                       str(noidungcauhoi)+ '\n'
                       '\\choiceTFn \n'
                       '{'+str(ans_nb)+'}\n'
                       '{'+str(ans_th)+'}\n'
                       '{'+str(ans_vd)+'}\n'
                       '{'+str(ans_vdc)+'}\n'
                       '\\loigiai{ \n'
                       '\\begin{enumEX}[a)]{1} \n'
                       '\\item '+str(sol_nb)+'\n'
                       '\\item '+str(sol_th)+'\n'
                       '\\item '+str(sol_vd)+'\n'
                       '\\item '+str(sol_vdc)+'\n'
                       '\\end{enumEX}} \n'
                       '\\end{ex}\n\\end{minipage}\n\n')
            return content

