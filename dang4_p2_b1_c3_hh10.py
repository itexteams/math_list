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


def bt_dang4_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y, t = symbols('x y t')

            # B1-Nghiên cứu đề bài và khởi tạo dữ liệu ngẫu nhiên
            # Random hệ số cho Delta 1: a1*x + b1*y + c1 = 0
            a1 = randint(-5, 5)
            while a1 == 0: a1 = randint(-5, 5)
            b1 = randint(-5, 5)
            while b1 == 0: b1 = randint(-5, 5)
            c1 = randint(-10, 10)

            # Random hệ số cho Delta 2: x = x0 + u1*t, y = y0 + u2*t
            x0 = randint(-5, 5)
            y0 = randint(-5, 5)
            u1 = randint(-5, 5)
            while u1 == 0: u1 = randint(-5, 5)
            u2 = randint(-5, 5)
            while u2 == 0: u2 = randint(-5, 5)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai đường thẳng $\\Delta_1 : %s = 0$ và $\\Delta_2 : \\begin{cases} x = %s \\\\ y = %s \\end{cases}$.''' 
                             %(latex(a1*x + b1*y + c1), latex(x0 + u1*t), latex(y0 + u2*t)))

            ########################################################################
            # Nhận biết - Kiểm tra vectơ pháp tuyến Delta 1
            ########################################################################
            n1_dung = (a1, b1)
            n1_sai = (a1, -b1) if b1 != -b1 else (b1, a1+1)

            nb_da_1_d = '\\True Đường thẳng $\\Delta_1$ có một vectơ pháp tuyến là $\\vec{n}(%s;%s)$' %(latex(n1_dung[0]), latex(n1_dung[1]))
            nb_da_1_s = 'Đường thẳng $\\Delta_1$ có một vectơ pháp tuyến là $\\vec{n}(%s;%s)$' %(latex(n1_sai[0]), latex(n1_sai[1]))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Đường thẳng $\\Delta_1$ có phương trình tổng quát là $%s = 0$, do đó nó có một vectơ pháp tuyến là $\\vec{n}_1 = (a; b) = (%s; %s)$.''' 
                            %(latex(a1*x + b1*y + c1), latex(a1), latex(b1)))

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu - Kiểm tra vectơ pháp tuyến Delta 2
            ########################################################################
            # u2 = (u1, u2) -> n2 = (u2, -u1)
            n2_dung = (u2, -u1)
            n2_sai = (u1, u2) # Sai vì đây là vectơ chỉ phương

            th_da_1_d = '\\True Đường thẳng $\\Delta_2$ có một vectơ pháp tuyến là $\\vec{n}(%s;%s)$' %(latex(n2_dung[0]), latex(n2_dung[1]))
            th_da_1_s = 'Đường thẳng $\\Delta_2$ có một vectơ pháp tuyến là $\\vec{n}(%s;%s)$' %(latex(n2_sai[0]), latex(n2_sai[1]))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Đường thẳng $\\Delta_2$ có vectơ chỉ phương là $\\vec{u}_2 = (%s; %s)$. Một vectơ pháp tuyến $\\vec{n}_2$ phải vuông góc với $\\vec{u}_2$, ta có thể chọn $\\vec{n}_2 = (%s; %s)$.''' 
                            %(latex(u1), latex(u2), latex(u2), latex(-u1)))

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng - Phương trình tham số Delta 1
            ########################################################################
            # Rút y theo x=t: y = (-a1*t - c1) / b1
            y_ts = simplify((-a1*t - c1)/Rational(b1))

            vd_da_1_d = '\\True Một phương trình tham số của đường thẳng $\\Delta_1$ là $\\begin{cases} x = t \\\\ y = %s \\end{cases}$' %(latex(y_ts))
            vd_da_1_s = 'Một phương trình tham số của đường thẳng $\\Delta_1$ là $\\begin{cases} x = t \\\\ y = %s \\end{cases}$' %(latex(simplify(y_ts + 1)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Để tìm phương trình tham số của $\\Delta_1$, ta có thể đặt $x = t$. Thay vào phương trình tổng quát:\\\\ $%s \\cdot t + %s \\cdot y + %s = 0 \\Leftrightarrow %s y = %s t %s \\Leftrightarrow y = %s$. \\\\ Vậy phương trình tham số là $\\begin{cases} x = t \\\\ y = %s \\end{cases}$.''' 
                            %(latex(a1), latex(b1), latex(c1), latex(b1), latex(-a1), latex(-c1), latex(y_ts), latex(y_ts)))

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao - Phương trình tổng quát Delta 2
            ########################################################################
            # Khử t: u2*(x - x0) - u1*(y - y0) = 0
            pt_tq = simplify(u2*(x - x0) - u1*(y - y0))

            vdc_da_1_d = '\\True Phương trình tổng quát của đường thẳng $\\Delta_2$ là $%s = 0$' %(latex(pt_tq))
            vdc_da_1_s = 'Phương trình tổng quát của đường thẳng $\\Delta_2$ là $%s = 0$' %(latex(pt_tq + randint(1, 5)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Từ phương trình tham số của $\\Delta_2$, ta rút $t$ từ phương trình đầu: $t = \\frac{x - %s}{%s}$. Thế vào phương trình thứ hai: $y = %s + %s \\cdot \\left( \\frac{x - %s}{%s} \\right)$. \\\\Nhân cả hai vế với $%s$ ta được: \\\\ $%s(y - %s) = %s(x - %s) \\Leftrightarrow %s = 0$.''' 
                             %(latex(x0), latex(u1), latex(y0), latex(u2), latex(x0), latex(u1), latex(u1), latex(u1), latex(y0), latex(u2), latex(x0), latex(pt_tq)))

            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                temp_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(temp_answers) <= 3:
                    break

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

