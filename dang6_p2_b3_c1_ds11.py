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


def bt_dang6_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các hệ số a, b dương cho hàm số f(x) = tan(a*x) - b*x
            a = randint(1, 3)
            b = randint(1, 3)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=\\tan %s - %s$. Khi đó:''' 
                             %(latex(a*x) if a != 1 else 'x', latex(b*x) if b != 1 else 'x'))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Tập xác định của hàm số
            if a == 1:
                nb_da_1_d = '\\True Tập xác định của hàm số: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
                nb_da_1_s = 'Tập xác định của hàm số: $D = \\mathbb{R} \\setminus \\left\\{ k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
            else:
                nb_da_1_d = '\\True Tập xác định của hàm số: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{%s} + \\frac{k\\pi}{%s} \\mid k \\in \\mathbb{Z} \\right\\}$' %(latex(2*a), latex(a))
                nb_da_1_s = 'Tập xác định của hàm số: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{k\\pi}{%s} \\mid k \\in \\mathbb{Z} \\right\\}$' %(latex(a))

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            if a == 1:
                loigiai_nb_1 = ('''Hàm số xác định khi $\\cos x \\ne 0 \\Leftrightarrow x \\ne \\frac{\\pi}{2} + k\\pi$ ($k \\in \\mathbb{Z}$).\\\\ Do đó tập xác định của hàm số là $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$.''')
            else:
                loigiai_nb_1 = ('''Hàm số xác định khi $\\cos %sx \\ne 0 \\Leftrightarrow %sx \\ne \\frac{\\pi}{2} + k\\pi \\Leftrightarrow x \\ne \\frac{\\pi}{%s} + \\frac{k\\pi}{%s}$ ($k \\in \\mathbb{Z}$).\\\\ Do đó tập xác định của hàm số là $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{%s} + \\frac{k\\pi}{%s} \\mid k \\in \\mathbb{Z} \\right\\}$.'''
                                %(latex(a), latex(a), latex(2*a), latex(a), latex(2*a), latex(a)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Giá trị tại điểm đối xứng (f(pi/3) = f(-pi/3) là mệnh đề Sai vì f lẻ)
            if a == 1:
                th_da_1_d = '$f\\left(\\frac{\\pi}{3}\\right) = f\\left(-\\frac{\\pi}{3}\\right)$'
                th_da_1_s = '\\True $f\\left(\\frac{\\pi}{3}\\right) = -f\\left(-\\frac{\\pi}{3}\\right)$'
            elif a == 2:
                th_da_1_d = '$f\\left(\\frac{\\pi}{6}\\right) = f\\left(-\\frac{\\pi}{6}\\right)$'
                th_da_1_s = '\\True $f\\left(\\frac{\\pi}{6}\\right) = -f\\left(-\\frac{\\pi}{6}\\right)$'
            else:
                th_da_1_d = '$f\\left(\\frac{\\pi}{9}\\right) = f\\left(-\\frac{\\pi}{9}\\right)$'
                th_da_1_s = '\\True $f\\left(\\frac{\\pi}{9}\\right) = -f\\left(-\\frac{\\pi}{9}\\right)$'

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Tính giá trị cụ thể để giải thích
            val_x0 = '3' if a == 1 else ('6' if a == 2 else '9')
            val_tan = '\\sqrt{3}'
            val_b_str = '\\frac{%s\\pi}{%s}' %(latex(b), val_x0)

            loigiai_th_1 = ('''Ta có $f\\left(\\frac{\\pi}{%s}\\right) = \\tan\\left(%s \\cdot \\frac{\\pi}{%s}\\right) - %s \\cdot \\frac{\\pi}{%s} = %s - %s$.\\\\'''
                            '''Mặt khác, $f\\left(-\\frac{\\pi}{%s}\\right) = \\tan\\left(-%s \\cdot \\frac{\\pi}{%s}\\right) - %s \\cdot \\left(-\\frac{\\pi}{%s}\\right) = -%s + %s = -\\left(%s - %s\\right)$.\\\\'''
                            '''Do đó $f\\left(\\frac{\\pi}{%s}\\right) = -f\\left(-\\frac{\\pi}{%s}\\right)$.'''
                            %(val_x0, latex(a), val_x0, latex(b), val_x0, val_tan, val_b_str,
                              val_x0, latex(a), val_x0, latex(b), val_x0, val_tan, val_b_str, val_tan, val_b_str,
                              val_x0, val_x0))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: Mối quan hệ tổng quát f(-x) = -f(x)
            vd_da_1_d = '\\True $f(-x) = -f(x)$'
            vd_da_1_s = '$f(-x) = f(x)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Với mọi $x \\in D$, ta có $-x \\in D$ và:\\\\'''
                            '''$f(-x) = \\tan\\left(%s(-x)\\right) - %s(-x) = -\\tan %sx + %sx = -\\left(\\tan %sx - %sx\\right) = -f(x)$.'''
                            %(latex(a) if a != 1 else '', latex(b) if b != 1 else '', latex(a) if a != 1 else 'x', latex(b*x) if b != 1 else 'x', latex(a) if a != 1 else 'x', latex(b*x) if b != 1 else 'x'))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Đồ thị hàm số đối xứng qua Oy (Sai vì đây là hàm lẻ, đồ thị đối xứng qua gốc tọa độ O)
            vdc_da_1_d = 'Đồ thị hàm số đối xứng với nhau qua trục $Oy$'
            vdc_da_1_s = '\\True Đồ thị hàm số đối xứng với nhau qua gốc tọa độ $O$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Vì hàm số có tập xác định $D$ đối xứng qua gốc tọa độ và $f(-x) = -f(x)$ với mọi $x \\in D$, nên đây là một hàm số lẻ.\\\\'''
                             '''Do đó, đồ thị của hàm số luôn đối xứng với nhau qua gốc tọa độ $O$ (không phải đối xứng qua trục $Oy$).''')

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm tra để đảm bảo số đáp án đúng nằm trong khoảng [1, 3]
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại giá trị được chọn sau khi lọc thỏa mãn điều kiện
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

            # Xuất câu hỏi và lời giải chi tiết theo đúng cấu trúc mẫu
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

