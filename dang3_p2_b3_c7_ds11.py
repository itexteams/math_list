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


def bt_dang3_p2_b3_c7_ds11(self):
            # Khai báo biến
            x = symbols('x')

            # Bước 1: Random các hệ số bài toán
            # f(x) = A*sin(x) + B*cos(x) + C*x (với B = A hoặc B = -A)
            A = random.randint(1, 9)
            B = A * random.choice([1, -1]) 
            C = random.choice([-9,-8,-7,-6,-5,-4, -3, -2, -1, 1, 2, 3, 4,5,6,7,8,9])

            A_tex = latex(A) if A != 1 else ""

            B_abs = abs(B)
            B_tex_abs = latex(B_abs) if B_abs != 1 else ""
            B_sign = "+" if B > 0 else "-"

            C_tex_abs = latex(abs(C)) if abs(C) != 1 else ""
            C_sign = "+" if C > 0 else "-"

            # Biểu diễn f(x)
            f_tex = '%s \\sin x %s %s \\cos x %s %s x' % (A_tex, B_sign, B_tex_abs, C_sign, C_tex_abs)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x) = %s$.''' % f_tex)

            ######################################################################## Nhận biết ############################################
            # f'(x) = A*cos(x) - B*sin(x) + C
            minus_B = -B
            minus_B_sign = "+" if minus_B > 0 else "-"
            minus_B_tex_abs = latex(abs(minus_B)) if abs(minus_B) != 1 else ""

            f_prime_val = '%s \\cos x %s %s \\sin x %s %s' % (A_tex, minus_B_sign, minus_B_tex_abs, C_sign, latex(abs(C)))
            f_prime_val_sai = '%s \\cos x %s %s \\sin x %s %s' % (A_tex, B_sign, B_tex_abs, C_sign, latex(abs(C)))

            # Các đáp án
            nb_da_1_d = '''\\True $f'(x) = %s$''' % f_prime_val
            nb_da_1_s = '''$f'(x) = %s$''' % f_prime_val_sai
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '''\\True $f'(x) = %s$''' % f_prime_val
            nb_da_2_s = '''$f'(x) = %s$''' % f_prime_val_sai
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $f'(x) = \\left( %s \\right)' = %s$.''' % (f_tex, f_prime_val))
            loigiai_nb_2 = ('''Ta có $f'(x) = \\left( %s \\right)' = %s$.''' % (f_tex, f_prime_val))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # f''(x) = -A*sin(x) - B*cos(x)
            minus_A_tex = f"-{A_tex}" if A_tex else "-"
            f_double_prime_val = '%s \\sin x %s %s \\cos x' % (minus_A_tex, minus_B_sign, minus_B_tex_abs)
            f_double_prime_val_sai = '%s \\sin x %s %s \\cos x' % (A_tex, minus_B_sign, minus_B_tex_abs) # Sai dấu của A

            # Các đáp án
            th_da_1_d = '''\\True $f''(x) = %s$''' % f_double_prime_val
            th_da_1_s = '''$f''(x) = %s$''' % f_double_prime_val_sai
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '''\\True $f''(x) = %s$''' % f_double_prime_val
            th_da_2_s = '''$f''(x) = %s$''' % f_double_prime_val_sai
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $f''(x) = \\left( %s \\right)' = %s$.''' % (f_prime_val, f_double_prime_val))
            loigiai_th_2 = ('''Ta có $f''(x) = \\left( %s \\right)' = %s$.''' % (f_prime_val, f_double_prime_val))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Xử lý toán học cho Vận dụng và Vận dụng cao ########
            interval_type = random.choice([1, 2])
            ask_max = random.choice([True, False])

            A_sqrt2_tex = f"{A_tex}\\sqrt{{2}}"
            C_tail = f"{C_sign} {latex(abs(C))}" if C != 0 else ""
            val_max_sqrt_tex = f"{A_sqrt2_tex} {C_tail}".strip()
            val_max_sqrt_sai_tex = f"{latex(A+1) if A+1!=1 else ''}\\sqrt{{2}} {C_tail}".strip()

            tan_val = -1 if B == A else 1
            tan_str = "-1" if B == A else "1"
            sign_angle = "+" if B == A else "-"
            loigiai_vdc_base = f"Ta có $f'(x) = {f_prime_val} = {A_sqrt2_tex}\\cos\\left(x {sign_angle} \\frac{{\\pi}}{{4}}\\right) {C_tail}$."

            if interval_type == 1:
                interval_tex = "\\left[ 0; \\frac{\\pi}{2} \\right]"
                if tan_val == -1:
                    vd_da_1_d_temp = '\\True Phương trình $f\'\'(x) = 0$ vô nghiệm trên đoạn $%s$' % interval_tex
                    vd_da_1_s_temp = 'Phương trình $f\'\'(x) = 0$ có một nghiệm duy nhất trên đoạn $%s$' % interval_tex
                    loigiai_vd_1_temp = ('''Xét phương trình $f\'\'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\tan x = %s$.\\\\
                    Vì $x \\in %s$ nên $\\tan x \\ge 0$. Do đó phương trình vô nghiệm trên đoạn $%s$.''' % (f_double_prime_val, tan_str, interval_tex, interval_tex))
                else:
                    vd_da_1_d_temp = '\\True Phương trình $f\'\'(x) = 0$ có một nghiệm duy nhất trên đoạn $%s$' % interval_tex
                    vd_da_1_s_temp = 'Phương trình $f\'\'(x) = 0$ vô nghiệm trên đoạn $%s$' % interval_tex
                    loigiai_vd_1_temp = ('''Xét phương trình $f\'\'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\tan x = %s$.\\\\
                    Trên đoạn $%s$, phương trình có một nghiệm duy nhất $x = \\frac{\\pi}{4}$.''' % (f_double_prime_val, tan_str, interval_tex))

                if ask_max:
                    if B == A:
                        val_max = A + C
                        vdc_da_1_d_temp = '\\True Giá trị lớn nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_max))
                        vdc_da_1_s_temp = 'Giá trị lớn nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_max + random.choice([1, 2])))
                        loigiai_vdc_1_temp = loigiai_vdc_base + ('''\\\\
                        Vì $x \\in %s \\Rightarrow x + \\frac{\\pi}{4} \\in \\left[ \\frac{\\pi}{4}; \\frac{3\\pi}{4} \\right] \\Rightarrow \\cos\\left(x + \\frac{\\pi}{4}\\right) \\le \\cos\\left(\\frac{\\pi}{4}\\right) = \\frac{\\sqrt{2}}{2}$.\\\\
                        Do đó $f\'(x) \\le %s \\cdot \\frac{\\sqrt{2}}{2} %s = %s$. Vậy giá trị lớn nhất bằng $%s$.''' % (interval_tex, A_sqrt2_tex, C_tail, latex(val_max), latex(val_max)))
                    else:
                        vdc_da_1_d_temp = '\\True Giá trị lớn nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, val_max_sqrt_tex)
                        vdc_da_1_s_temp = 'Giá trị lớn nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, val_max_sqrt_sai_tex)
                        loigiai_vdc_1_temp = loigiai_vdc_base + ('''\\\\
                        Vì $x \\in %s \\Rightarrow x - \\frac{\\pi}{4} \\in \\left[ -\\frac{\\pi}{4}; \\frac{\\pi}{4} \\right] \\Rightarrow \\cos\\left(x - \\frac{\\pi}{4}\\right) \\le 1$.\\\\
                        Do đó $f\'(x) \\le %s \\cdot 1 %s = %s$. Vậy giá trị lớn nhất bằng $%s$.''' % (interval_tex, A_sqrt2_tex, C_tail, val_max_sqrt_tex, val_max_sqrt_tex))
                else:
                    if B == A:
                        val_min = -A + C
                        vdc_da_1_d_temp = '\\True Giá trị nhỏ nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_min))
                        vdc_da_1_s_temp = 'Giá trị nhỏ nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_min + random.choice([-1, -2])))
                        loigiai_vdc_1_temp = loigiai_vdc_base + ('''\\\\
                        Vì $x \\in %s \\Rightarrow x + \\frac{\\pi}{4} \\in \\left[ \\frac{\\pi}{4}; \\frac{3\\pi}{4} \\right] \\Rightarrow \\cos\\left(x + \\frac{\\pi}{4}\\right) \\ge \\cos\\left(\\frac{3\\pi}{4}\\right) = -\\frac{\\sqrt{2}}{2}$.\\\\
                        Do đó $f\'(x) \\ge %s \\cdot \\left(-\\frac{\\sqrt{2}}{2}\\right) %s = %s$. Vậy giá trị nhỏ nhất bằng $%s$.''' % (interval_tex, A_sqrt2_tex, C_tail, latex(val_min), latex(val_min)))
                    else:
                        val_min = A + C
                        vdc_da_1_d_temp = '\\True Giá trị nhỏ nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_min))
                        vdc_da_1_s_temp = 'Giá trị nhỏ nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_min + random.choice([-1, -2])))
                        loigiai_vdc_1_temp = loigiai_vdc_base + ('''\\\\
                        Vì $x \\in %s \\Rightarrow x - \\frac{\\pi}{4} \\in \\left[ -\\frac{\\pi}{4}; \\frac{\\pi}{4} \\right] \\Rightarrow \\cos\\left(x - \\frac{\\pi}{4}\\right) \\ge \\cos\\left(\\pm\\frac{\\pi}{4}\\right) = \\frac{\\sqrt{2}}{2}$.\\\\
                        Do đó $f\'(x) \\ge %s \\cdot \\frac{\\sqrt{2}}{2} %s = %s$. Vậy giá trị nhỏ nhất bằng $%s$.''' % (interval_tex, A_sqrt2_tex, C_tail, latex(val_min), latex(val_min)))
            else:
                interval_tex = "\\left[ -\\frac{\\pi}{2}; 0 \\right]"
                if tan_val == -1:
                    vd_da_1_d_temp = '\\True Phương trình $f\'\'(x) = 0$ có một nghiệm duy nhất trên đoạn $%s$' % interval_tex
                    vd_da_1_s_temp = 'Phương trình $f\'\'(x) = 0$ vô nghiệm trên đoạn $%s$' % interval_tex
                    loigiai_vd_1_temp = ('''Xét phương trình $f\'\'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\tan x = %s$.\\\\
                    Trên đoạn $%s$, phương trình có một nghiệm duy nhất $x = -\\frac{\\pi}{4}$.''' % (f_double_prime_val, tan_str, interval_tex))
                else:
                    vd_da_1_d_temp = '\\True Phương trình $f\'\'(x) = 0$ vô nghiệm trên đoạn $%s$' % interval_tex
                    vd_da_1_s_temp = 'Phương trình $f\'\'(x) = 0$ có một nghiệm duy nhất trên đoạn $%s$' % interval_tex
                    loigiai_vd_1_temp = ('''Xét phương trình $f\'\'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\tan x = %s$.\\\\
                    Vì $x \\in %s$ nên $\\tan x \\le 0$. Do đó phương trình vô nghiệm trên đoạn $%s$.''' % (f_double_prime_val, tan_str, interval_tex, interval_tex))

                if ask_max:
                    if B == A:
                        vdc_da_1_d_temp = '\\True Giá trị lớn nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, val_max_sqrt_tex)
                        vdc_da_1_s_temp = 'Giá trị lớn nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, val_max_sqrt_sai_tex)
                        loigiai_vdc_1_temp = loigiai_vdc_base + ('''\\\\
                        Vì $x \\in %s \\Rightarrow x + \\frac{\\pi}{4} \\in \\left[ -\\frac{\\pi}{4}; \\frac{\\pi}{4} \\right] \\Rightarrow \\cos\\left(x + \\frac{\\pi}{4}\\right) \\le 1$.\\\\
                        Do đó $f\'(x) \\le %s \\cdot 1 %s = %s$. Vậy giá trị lớn nhất bằng $%s$ (đạt được khi $x = -\\frac{\\pi}{4}$).''' % (interval_tex, A_sqrt2_tex, C_tail, val_max_sqrt_tex, val_max_sqrt_tex))
                    else:
                        val_max = A + C
                        vdc_da_1_d_temp = '\\True Giá trị lớn nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_max))
                        vdc_da_1_s_temp = 'Giá trị lớn nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_max + random.choice([1, 2])))
                        loigiai_vdc_1_temp = loigiai_vdc_base + ('''\\\\
                        Vì $x \\in %s \\Rightarrow x - \\frac{\\pi}{4} \\in \\left[ -\\frac{3\\pi}{4}; -\\frac{\\pi}{4} \\right] \\Rightarrow \\cos\\left(x - \\frac{\\pi}{4}\\right) \\le \\cos\\left(-\\frac{\\pi}{4}\\right) = \\frac{\\sqrt{2}}{2}$.\\\\
                        Do đó $f\'(x) \\le %s \\cdot \\frac{\\sqrt{2}}{2} %s = %s$. Vậy giá trị lớn nhất bằng $%s$.''' % (interval_tex, A_sqrt2_tex, C_tail, latex(val_max), latex(val_max)))
                else:
                    if B == A:
                        val_min = A + C
                        vdc_da_1_d_temp = '\\True Giá trị nhỏ nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_min))
                        vdc_da_1_s_temp = 'Giá trị nhỏ nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_min + random.choice([-1, -2])))
                        loigiai_vdc_1_temp = loigiai_vdc_base + ('''\\\\
                        Vì $x \\in %s \\Rightarrow x + \\frac{\\pi}{4} \\in \\left[ -\\frac{\\pi}{4}; \\frac{\\pi}{4} \\right] \\Rightarrow \\cos\\left(x + \\frac{\\pi}{4}\\right) \\ge \\cos\\left(\\pm\\frac{\\pi}{4}\\right) = \\frac{\\sqrt{2}}{2}$.\\\\
                        Do đó $f\'(x) \\ge %s \\cdot \\frac{\\sqrt{2}}{2} %s = %s$. Vậy giá trị nhỏ nhất bằng $%s$.''' % (interval_tex, A_sqrt2_tex, C_tail, latex(val_min), latex(val_min)))
                    else:
                        val_min = -A + C
                        vdc_da_1_d_temp = '\\True Giá trị nhỏ nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_min))
                        vdc_da_1_s_temp = 'Giá trị nhỏ nhất của hàm số $f\'(x)$ trên đoạn $%s$ bằng $%s$' % (interval_tex, latex(val_min + random.choice([-1, -2])))
                        loigiai_vdc_1_temp = loigiai_vdc_base + ('''\\\\
                        Vì $x \\in %s \\Rightarrow x - \\frac{\\pi}{4} \\in \\left[ -\\frac{3\\pi}{4}; -\\frac{\\pi}{4} \\right] \\Rightarrow \\cos\\left(x - \\frac{\\pi}{4}\\right) \\ge \\cos\\left(-\\frac{3\\pi}{4}\\right) = -\\frac{\\sqrt{2}}{2}$.\\\\
                        Do đó $f\'(x) \\ge %s \\cdot \\left(-\\frac{\\sqrt{2}}{2}\\right) %s = %s$. Vậy giá trị nhỏ nhất bằng $%s$.''' % (interval_tex, A_sqrt2_tex, C_tail, latex(val_min), latex(val_min)))


            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = vd_da_1_d_temp
            vd_da_1_s = vd_da_1_s_temp
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = vd_da_1_d_temp
            vd_da_2_s = vd_da_1_s_temp
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = loigiai_vd_1_temp
            loigiai_vd_2 = loigiai_vd_1_temp

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = vdc_da_1_d_temp
            vdc_da_1_s = vdc_da_1_s_temp
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = vdc_da_1_d_temp
            vdc_da_2_s = vdc_da_1_s_temp
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = loigiai_vdc_1_temp
            loigiai_vdc_2 = loigiai_vdc_1_temp

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('--', '+').replace('-+', '-').replace('++', '+')
            return content

