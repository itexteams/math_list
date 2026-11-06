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


def bt_dang7_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các tham số để tạo bài toán tương đương
            # n là số mũ của |x| (chọn mũ lẻ như 1, 3 để giữ nguyên tính chẵn của |x|^n)
            n = random.choice([1, 3])
            # a là hệ số trong góc sin(a*x)
            a = randint(1, 3)

            # Biểu thức hàm số tương ứng
            if n == 1:
                f_str = '\\left| x \\right| \\sin %sx' % (latex(a*x) if a != 1 else 'x')
            else:
                f_str = '\\left| x \\right|^{%s} \\sin %sx' % (latex(n), latex(a*x) if a != 1 else 'x')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=%s$. Khi đó:''' % (f_str))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Tập xác định của hàm số
            nb_da_1_d = 'Tập xác định của hàm số: $D = \\mathbb{R} \\setminus \\{0\\}$'
            nb_da_1_s = '\\True Tập xác định của hàm số: $D = \\mathbb{R}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hàm số $f(x)=%s$ xác định với mọi $x \\in \\mathbb{R}$ vì cả hàm trị tuyệt đối và hàm số sin đều có tập xác định là $\\mathbb{R}$.\\\\ Do đó tập xác định của hàm số là $D = \\mathbb{R}$.''' % (f_str))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: f(-\pi) = -f(\pi) (Đúng vì hàm số lẻ)
            # Tổng quát xét điểm \pi / a để biểu thức góc đẹp
            th_da_1_d = '\\True $f\\left(-\\frac{\\pi}{%s}\\right) = -f\\left(\\frac{\\pi}{%s}\\right)$' % (latex(a) if a != 1 else '1', latex(a) if a != 1 else '1')
            th_da_1_s = '$f\\left(-\\frac{\\pi}{%s}\\right) = f\\left(\\frac{\\pi}{%s}\\right)$' % (latex(a) if a != 1 else '1', latex(a) if a != 1 else '1')
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            val_x0 = '\\pi' if a == 1 else '\\frac{\\pi}{%s}' % latex(a)
            val_abs = '\\pi' if a == 1 else '\\left(\\frac{\\pi}{%s}\\right)' % latex(a)
            if n != 1:
                val_abs = val_abs + '^{%s}' % latex(n)

            loigiai_th_1 = ('''Ta có:\\\\'''
                            '''$f\\left(-%s\\right) = \\left| -%s \\right|^{%s} \\cdot \\sin\\left( %s \\cdot \\left(-%s\\right) \\right) = %s \\cdot \\sin(-\\pi) = 0$.\\\\'''
                            '''$f\\left(%s\\right) = \\left| %s \\right|^{%s} \\cdot \\sin\\left( %s \\cdot %s \\right) = %s \\cdot \\sin(\\pi) = 0$.\\\\'''
                            '''Do đó $0 = -0$ nên $f\\left(-%s\\right) = -f\\left(%s\\right)$.'''
                            % (val_x0, val_x0 if a==1 else '\\frac{\\pi}{'+latex(a)+'}', '1' if n==1 else latex(n), latex(a) if a!=1 else '', val_x0 if a==1 else '\\frac{\\pi}{'+latex(a)+'}', val_abs,
                               val_x0, val_x0 if a==1 else '\\frac{\\pi}{'+latex(a)+'}', '1' if n==1 else latex(n), latex(a) if a!=1 else '', val_x0 if a==1 else '\\frac{\\pi}{'+latex(a)+'}', val_abs,
                               val_x0, val_x0))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: Hàm số đã cho đối xứng qua gốc tọa độ O(0;0)
            vd_da_1_d = '\\True Đồ thị hàm số đã cho đối xứng qua gốc tọa độ $O(0;0)$'
            vd_da_1_s = 'Đồ thị hàm số đã cho đối xứng qua trục tung $Oy$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Vì hàm số đã cho có tập xác định $D = \\mathbb{R}$ là tập đối xứng và thỏa mãn $f(-x) = -f(x)$ với mọi $x \\in \\mathbb{R}$, nên đây là hàm số lẻ.\\\\'''
                            '''Theo tính chất đồ thị, đồ thị của một hàm số lẻ luôn luôn đối xứng qua gốc tọa độ $O(0;0)$.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: f(-x) = -f(x)
            vdc_da_1_d = '\\True $f(-x) = -f(x)$'
            vdc_da_1_s = '$f(-x) = f(x)$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            if n == 1:
                loigiai_vdc_1 = ('''Với mọi $x \\in \\mathbb{R}$, ta có $-x \\in \\mathbb{R}$ và:\\\\'''
                                 '''$f(-x) = \\left| -x \\right| \\sin\\left(%s(-x)\\right) = \\left| x \\right| \\cdot \\left(-\\sin %sx\\right) = -\\left| x \\right| \\sin %sx = -f(x)$.'''
                                 % (latex(a) if a != 1 else '', latex(a) if a != 1 else 'x', latex(a) if a != 1 else 'x'))
            else:
                loigiai_vdc_1 = ('''Với mọi $x \\in \\mathbb{R}$, ta có $-x \\in \\mathbb{R}$ và:\\\\'''
                                 '''$f(-x) = \\left| -x \\right|^{%s} \\sin\\left(%s(-x)\\right) = \\left| x \\right|^{%s} \\cdot \\left(-\\sin %sx\\right) = -\\left| x \\right|^{%s} \\sin %sx = -f(x)$.'''
                                 % (latex(n), latex(a) if a != 1 else '', latex(n), latex(a) if a != 1 else 'x', latex(n), latex(a) if a != 1 else 'x'))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số lượng đáp án đúng ngẫu nhiên nằm trong khoảng từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán dữ liệu tương ứng sau khi lọc điều kiện đạt yêu cầu
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

            # Xuất kết quả cuối cùng theo định dạng khung chương trình mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

