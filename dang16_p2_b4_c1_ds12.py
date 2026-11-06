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


def bt_dang16_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số cực trị x0 và x1 để b và c là số nguyên (x0 và x1 phải cùng tính chẵn lẻ)
            x0 = random.choice([-2, -1, 1, 2])
            x1 = x0 + random.choice([-4, -2, 2, 4])
            d_val = random.randint(-3, 3)

            # Tính b, c dựa trên định lý Vi-ét cho phương trình đạo hàm y' = 3(x-x0)(x-x1)
            b_val = -3 * (x0 + x1) // 2
            c_val = 3 * x0 * x1

            # Tính giá trị cực trị y0 tại x0
            y0 = x0**3 + b_val*x0**2 + c_val*x0 + d_val

            # Phân loại x_max, x_min để xác định cực đại, cực tiểu
            x_max = min(x0, x1)
            x_min = max(x0, x1)
            y_max = x_max**3 + b_val*x_max**2 + c_val*x_max + d_val
            y_min = x_min**3 + b_val*x_min**2 + c_val*x_min + d_val

            d_str = f"+ {d_val}" if d_val > 0 else (f"- {-d_val}" if d_val < 0 else "")
            f_generic_str = f"x^3 + bx^2 + cx {d_str}".strip()

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = f(x) = %s$ đạt cực trị bằng $%s$ tại $x = %s$ (với $b$ và $c$ là hằng số).'''
                             %(f_generic_str, latex(y0), latex(x0)))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            sum_bc = b_val + c_val
            sum_bc_wrong = sum_bc + random.choice([-2, 2, 3])

            nb_da_1_d = '\\True Giá trị của $b+c$ bằng $%s$' % latex(sum_bc)
            nb_da_1_s = 'Giá trị của $b+c$ bằng $%s$' % latex(sum_bc_wrong)

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Tính toán các vế phương trình để hiển thị trong lời giải
            b, c = symbols('b c')
            eq1_lhs = 3*x0**2 + 2*x0*b + c
            eq2_lhs = x0**3 + x0**2*b + x0*c + d_val
            eq1_simplified_lhs = 2*x0*b + c
            eq1_simplified_rhs = -3*x0**2
            eq2_simplified_lhs = x0**2*b + x0*c
            eq2_simplified_rhs = y0 - x0**3 - d_val

            loigiai_nb_1 = ('''Ta có $f'(x) = 3x^2 + 2bx + c$. \\\\
            Hàm số đạt cực trị bằng $%s$ tại $x = %s$ nên: \\\\
            $\\left\\{\\begin{matrix} f'(%s) = 0 \\\\ f(%s) = %s \\end{matrix}\\right. \\Leftrightarrow \\left\\{\\begin{matrix} %s = 0 \\\\ %s = %s \\end{matrix}\\right. \\Leftrightarrow \\left\\{\\begin{matrix} %s = %s \\\\ %s = %s \\end{matrix}\\right. \\Leftrightarrow \\left\\{\\begin{matrix} b = %s \\\\ c = %s \\end{matrix}\\right.$. \\\\
            Khi đó $b+c = %s$.''' % (
                latex(y0), latex(x0),
                latex(x0), latex(x0), latex(y0),
                latex(eq1_lhs), latex(eq2_lhs), latex(y0),
                latex(eq1_simplified_lhs), latex(eq1_simplified_rhs),
                latex(eq2_simplified_lhs), latex(eq2_simplified_rhs),
                latex(b_val), latex(c_val),
                latex(sum_bc)
            ))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            x1_wrong = x1 + random.choice([-1, 1, 2])
            if x1_wrong == x0: x1_wrong += 1

            th_da_1_d = '\\True Hàm số $y=f(x)$ đạt cực trị tại $x = %s$' % latex(x1)
            th_da_1_s = 'Hàm số $y=f(x)$ đạt cực trị tại $x = %s$' % latex(x1_wrong)

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Hàm số cụ thể và đạo hàm
            f_expr = x**3 + b_val*x**2 + c_val*x + d_val
            f_prime = diff(f_expr, x)

            loigiai_th_1 = ('''Với $b = %s$ và $c = %s$ vừa tìm được, hàm số là $f(x) = %s$. \\\\
            Đạo hàm $f'(x) = %s$. \\\\
            $f'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\\\ x = %s \\end{array} \\right.$. \\\\
            Do đó hàm số đạt cực trị tại $x = %s$ và $x = %s$.''' % (
                latex(b_val), latex(c_val),
                latex(f_expr), latex(f_prime), latex(f_prime), latex(x0), latex(x1), latex(x0), latex(x1)
            ))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            is_max_q = random.choice([True, False])
            if is_max_q:
                vd_da_1_d = '\\True Giá trị cực đại của hàm số đã cho bằng $%s$' % latex(y_max)
                vd_da_1_s = 'Giá trị cực đại của hàm số đã cho bằng $%s$' % latex(y_min)
                loigiai_vd_1 = ('''Do hệ số $a = 1 > 0$ nên hàm số đạt cực đại tại nghiệm nhỏ hơn của phương trình $f'(x)=0$, tức là tại $x = %s$. \\\\
            Giá trị cực đại là $y_{CĐ} = f(%s) = %s$.''' % (latex(x_max), latex(x_max), latex(y_max)))
            else:
                vd_da_1_d = '\\True Giá trị cực tiểu của hàm số đã cho bằng $%s$' % latex(y_min)
                vd_da_1_s = 'Giá trị cực tiểu của hàm số đã cho bằng $%s$' % latex(y_max)
                loigiai_vd_1 = ('''Do hệ số $a = 1 > 0$ nên hàm số đạt cực tiểu tại nghiệm lớn hơn của phương trình $f'(x)=0$, tức là tại $x = %s$. \\\\
            Giá trị cực tiểu là $y_{CT} = f(%s) = %s$.''' % (latex(x_min), latex(x_min), latex(y_min)))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            is_increasing_q = random.choice([True, False])

            if is_increasing_q:
                u_val = x_min
                v_val = x_min + random.randint(1, 2)
                vdc_da_1_d = '\\True Hàm số $y=f(x)$ đồng biến trên khoảng $(%s; %s)$' % (latex(u_val), latex(v_val))
                vdc_da_1_s = 'Hàm số $y=f(x)$ đồng biến trên khoảng $(%s; %s)$' % (latex(x_max), latex(x_min))
            else:
                vdc_da_1_d = '\\True Hàm số $y=f(x)$ nghịch biến trên khoảng $(%s; %s)$' % (latex(x_max), latex(x_min))
                vdc_da_1_s = 'Hàm số $y=f(x)$ nghịch biến trên khoảng $(%s; %s)$' % (latex(x_min), latex(x_min + 1))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Bảng biến thiên của hàm số $f(x)$: \\\\
            \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/1,$f'(x)$/0.7,$f(x)$/2.1}
            {$-\\infty$,$%s$,$%s$,$+\\infty$}
            \\tkzTabLine{,+,0,-,0,+}
            \\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$}
            \\end{tikzpicture} \\\\
            Dựa vào bảng biến thiên, hàm số đồng biến trên các khoảng $(-\\infty; %s)$ và $(%s; +\\infty)$, nghịch biến trên khoảng $(%s; %s)$.''' % (
                latex(x_max), latex(x_min),
                latex(y_max), latex(y_min),
                latex(x_max), latex(x_min), latex(x_max), latex(x_min)
            ))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

