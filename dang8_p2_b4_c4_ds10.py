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


def bt_dang8_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Thiết lập các hệ số ngẫu nhiên để bài toán luôn có nghiệm đẹp
            # Phương trình dạng: sqrt(x^2 + ax + b) = sqrt(c - dx)
            # Để đơn giản và sát với đề mẫu: sqrt(x^2 + a*x + b) = sqrt(c - x)
            # Squaring: x^2 + (a+1)x + (b-c) = 0
            while True:
                a = random.randint(1, 4)
                c = random.randint(1, 5)
                # Chọn b sao cho biệt thức Delta của x^2 + (a+1)x + (b-c) là số chính phương
                # Và đảm bảo x^2 + ax + b luôn dương (Delta < 0)
                # Ở đây mình chọn các bộ số cụ thể để đảm bảo tính giáo dục
                a, b, c = 2, 4, 2 # Giữ nguyên như đề bài hoặc có thể random trong list
                break

            expr_left = x**2 + a*x + b
            expr_right = c - x
            pt_squared = simplify(expr_left - expr_right)

            # Tính toán các giá trị phục vụ lời giải
            condition_val = c
            roots = solve(pt_squared, x)
            roots_in_z = [r for r in roots if r.is_integer]
            num_roots = len([r for r in roots if r <= condition_val])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $\\sqrt{%s} = \\sqrt{%s}$ (*).''' 
                             %(latex(expr_left), latex(expr_right)))

            ########################################################################
            # Nhận biết: Điều kiện xác định
            nb_da_1_d = r'\True Điều kiện $x \leq %s$' % (latex(condition_val))
            nb_da_1_s = 'Điều kiện $x \\geq %s$' % (latex(condition_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Điều kiện xác định của phương trình là:\\\\
                            $\\begin{cases} %s \\geq 0 \\\\ %s \\geq 0 \\end{cases} 
                            \\Leftrightarrow \\begin{cases} x \\in \\mathbb{R} \\text{ (vì } \\Delta < 0) \\\\ x \\leq %s \\end{cases} 
                            \\Leftrightarrow x \\leq %s$.''' 
                            %(latex(expr_left), latex(expr_right), latex(condition_val), latex(condition_val)))

            ########################################################################
            # Thông hiểu: Bình phương hai vế
            th_da_1_d = r'\True Bình phương hai vế phương trình (*) ta được $%s = 0$' % (latex(pt_squared))
            th_da_1_s = 'Bình phương hai vế phương trình (*) ta được $%s = %s$' % (latex(expr_left), latex(c+x))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Bình phương hai vế của phương trình (*), ta có: \\\\
                            $(\\sqrt{%s})^2 = (\\sqrt{%s})^2$ \\\\
                            $\\Leftrightarrow %s = %s$ \\\\
                            $\\Leftrightarrow %s = 0$.''' 
                            %(latex(expr_left), latex(expr_right), latex(expr_left), latex(expr_right), latex(pt_squared)))

            ########################################################################
            # Vận dụng: Số lượng nghiệm
            vd_da_1_d = r'\True Phương trình (*) có %s nghiệm phân biệt' % (len(roots))
            vd_da_1_s = 'Phương trình (*) vô nghiệm'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Giải phương trình $%s = 0$, ta tìm được các nghiệm là $x = %s$. \\\\
                            Đối chiếu với điều kiện $x \\leq %s$, ta thấy cả hai nghiệm đều thỏa mãn. \\\\
                            Vậy phương trình có $%s$ nghiệm phân biệt.''' 
                            %(latex(pt_squared), ", x = ".join([latex(r) for r in roots]), latex(condition_val), len(roots)))

            ########################################################################
            # Vận dụng cao: Tập hợp số của nghiệm
            vdc_da_1_d = r'\True Các nghiệm của phương trình (*) thuộc $\mathbb{Z}$'
            vdc_da_1_s = r'Phương trình (*) có nghiệm duy nhất thuộc $\mathbb{N}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Dựa trên kết quả giải phương trình, tập nghiệm của phương trình là $S = \\{%s\\}$. \\\\
                            Vì $%s$ là các số nguyên nên các nghiệm này đều thuộc tập hợp số nguyên $\\mathbb{Z}$.''' 
                            %(", ".join([latex(r) for r in roots]), "  \\text{và} ".join([latex(r) for r in roots])))

            # --- HÀM XỬ LÝ TRUE/FALSE GIỐNG MẪU ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Gán kết quả cuối cùng
            shuffled_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

