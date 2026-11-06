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


def bt_dang21_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            a, b, c, d = symbols('a b c d')

            # Random các tham số
            x1 = random.randint(-2, 2)
            delta_x = random.choice([2, 4])
            x2 = x1 + delta_x

            # Lựa chọn hệ số a sao cho giá trị y đẹp
            if delta_x == 2:
                a_val = random.choice([Rational(1,4), Rational(1,2), 1, 2])
            else:
                a_val = random.choice([Rational(1,8), Rational(1,4), Rational(1,2)])

            y1 = random.randint(-3, 3)

            # Xác định các hệ số b, c, d theo cực trị x1, x2 và giá trị y1
            b_val = -Rational(3, 2) * a_val * (x1 + x2)
            c_val = 3 * a_val * x1 * x2
            d_val = y1 - (a_val * x1**3 + b_val * x1**2 + c_val * x1)
            y2 = a_val * x2**3 + b_val * x2**2 + c_val * x2 + d_val

            # Tạo một hoành độ trung gian để đặt câu hỏi ở mức vận dụng cao
            x3 = (x1 + x2) // 2
            expr_d = a*(x3**3) + b*(x3**2) + c*x3 + d
            expr_latex = latex(expr_d).replace(' ', '')
            val_true = a_val*(x3**3) + b_val*(x3**2) + c_val*x3 + d_val

            # Đóng khung bảng biến thiên bằng TikZ (tkz-tab)
            bbt_str = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[lgt=1.5, espcl=3]
            {$x$ / 0.8, $f'(x)$ / 0.8, $f(x)$ / 2.5}
            {$-\\infty$, $%s$, $%s$, $+\\infty$}
            \\tkzTabLine{, +, 0, -, 0, +}
            \\tkzTabVar{-/ $-\\infty$, +/ $%s$, -/ $%s$, +/ $+\\infty$}
            \\end{tikzpicture}
            \\end{center}''' % (latex(x1), latex(x2), latex(y1), latex(y2)))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=ax^3+bx^2+cx+d$ ($a,b,c,d \\in \\mathbb{R}$), xác định và liên tục trên $\\mathbb{R}$ và có bảng biến thiên như sau:
            %s''' % bbt_str)

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đồ thị hàm số đã cho có điểm cực đại là $\\left(%s; %s\\right)$' % (latex(x1), latex(y1))
            nb_da_1_s = 'Đồ thị hàm số đã cho có điểm cực đại là $\\left(%s; %s\\right)$' % (latex(x1), latex(y2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Dựa vào bảng biến thiên, tại $x = %s$, đạo hàm $f'(x)$ đổi dấu từ dương sang âm nên hàm số đạt cực đại tại $x = %s$ với giá trị cực đại là $y = %s$. \\\\
            Vậy điểm cực đại của đồ thị hàm số là $\\left(%s; %s\\right)$.''' % (latex(x1), latex(x1), latex(y1), latex(x1), latex(y1)))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Đồ thị hàm số đã cho đồng biến trên khoảng $\\left(-\\infty; %s\\right)$' % latex(x1)
            th_da_1_s = 'Đồ thị hàm số đã cho nghịch biến trên khoảng $\\left(-\\infty; %s\\right)$' % latex(x1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Dựa vào bảng biến thiên, ta thấy $f'(x) > 0$ trên các khoảng $\\left(-\\infty; %s\\right)$ và $\\left(%s; +\\infty\\right)$. \\\\
            Do đó, hàm số đồng biến trên khoảng $\\left(-\\infty; %s\\right)$.''' % (latex(x1), latex(x2), latex(x1)))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Hàm số đã cho không có giá trị nhỏ nhất trên $\\mathbb{R}$'
            vd_da_1_s = 'Giá trị nhỏ nhất của hàm số đã cho bằng $%s$' % latex(y2)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Dựa vào bảng biến thiên, ta có $\\lim\\limits_{x \\to -\\infty} f(x) = -\\infty$ nên hàm số không có giá trị nhỏ nhất trên $\\mathbb{R}$. \\\\
            Giá trị $%s$ chỉ là giá trị cực tiểu, không phải giá trị nhỏ nhất.''' % latex(y2))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            val_false = val_true + random.choice([-2, -1, 1, 2])
            vdc_da_1_d = '\\True Ta có $%s = %s$' % (expr_latex, latex(val_true))
            vdc_da_1_s = 'Ta có $%s = %s$' % (expr_latex, latex(val_false))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            # Khởi tạo phương trình bằng SymPy để sinh chuỗi LaTeX đẹp nhất
            eq1 = a*x1**3 + b*x1**2 + c*x1 + d
            eq2 = a*x2**3 + b*x2**2 + c*x2 + d
            eq3 = 3*a*x1**2 + 2*b*x1 + c
            eq4 = 3*a*x2**2 + 2*b*x2 + c

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Dựa vào bảng biến thiên, đồ thị hàm số đi qua các điểm cực trị $(%s; %s)$ và $(%s; %s)$. \\\\
            Ta có hệ phương trình: \\\\
            $\\left\\{\\begin{matrix} f(%s) = %s \\\\ f(%s) = %s \\\\ f'(%s) = 0 \\\\ f'(%s) = 0 \\end{matrix}\\right.
            \\Leftrightarrow \\left\\{\\begin{matrix} %s = %s \\\\ %s = %s \\\\ %s = 0 \\\\ %s = 0 \\end{matrix}\\right.
            \\Leftrightarrow \\left\\{\\begin{matrix} a = %s \\\\ b = %s \\\\ c = %s \\\\ d = %s \\end{matrix}\\right.$. \\\\
            Khi đó, thay vào biểu thức ta có: $%s = %s$.''' % (
                latex(x1), latex(y1), latex(x2), latex(y2),
                latex(x1), latex(y1), latex(x2), latex(y2), latex(x1), latex(x2),
                latex(eq1), latex(y1),
                latex(eq2), latex(y2),
                latex(eq3),
                latex(eq4),
                latex(a_val), latex(b_val), latex(c_val), latex(d_val),
                expr_latex, latex(val_true)
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

