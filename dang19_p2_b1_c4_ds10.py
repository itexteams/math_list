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


def bt_dang19_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Tạo tham số ngẫu nhiên cho bài toán
            # Hàm f(x) = (x - k) / (x^2 - (a+b)x + ab)
            # Ở đây ảnh gốc là x^2 - 4x (nghiệm 0 và 4). Ta sẽ random các nghiệm này.
            a_val = 0
            b_val = random.choice([2, 3, 4, 5, 6]) # Random số 4 trong đề thành b_val
            k_val = 1 # Số 1 trên tử số

            expr_tu = x - k_val
            expr_mau = x**2 - b_val*x

            noidungcauhoi = ('''Cho hàm số $f(x)=\\dfrac{%s}{%s}$ có tập xác định là $\\mathscr{D}_f$.''' 
                             %(latex(expr_tu), latex(expr_mau)))

            ########################################################################
            # Nhận biết 
            ########################################################################
            nb_da_1_d = '\\True Hàm số $f(x)$ xác định $\\Leftrightarrow %s \\neq 0$' %(latex(expr_mau))
            nb_da_1_s = 'Hàm số $f(x)$ xác định $\\Leftrightarrow %s = 0$' %(latex(expr_mau))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Hàm số $f(x)$ xác định khi và chỉ khi mẫu số khác $0$, tức là $%s \\neq 0$.''' %(latex(expr_mau)))

            ########################################################################
            # Thông hiểu
            ########################################################################
            th_da_1_d = '\\True Hàm số xác định tại $x = %s$' %(latex(k_val))
            th_da_1_s = 'Hàm số không xác định tại $x = %s$' %(latex(k_val))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Thay $x=%s$ vào mẫu số: $%s^2 - %s(%s) = %s \\neq 0$. Vậy hàm số xác định tại $x=%s$.''' 
                            %(k_val, k_val, b_val, k_val, k_val**2 - b_val*k_val, k_val))

            ########################################################################
            # Vận dụng
            ########################################################################
            # TXĐ của f(x) là R \ {0; b_val}
            tx_d_f = '\\mathbb{R} \\setminus \\{0; %s\\}' %(b_val)
            th_da_2_d = '\\True Tập xác định của hàm số $f(x)$ là $\\mathscr{D}_f = %s$' %(tx_d_f)
            th_da_2_s = 'Tập xác định của hàm số $f(x)$ là $\\mathscr{D}_f = \\mathbb{R} \\setminus \\{%s\\}$' %(b_val)
            list_vd_da_1 = [th_da_2_d, th_da_2_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Hàm số $f(x)$ xác định $\\Leftrightarrow %s \\neq 0 \\Leftrightarrow \\begin{cases} x \\neq 0 \\\\ x \\neq %s \\end{cases}$. Vậy $\\mathscr{D}_f = %s$.''' 
                            %(latex(expr_mau), b_val, tx_d_f))

            ########################################################################
            # Vận dụng cao
            ########################################################################
            # g(x) = sqrt(2x - m) -> Dg = [m/2; +inf)
            # Để Dg subset Df thì m/2 > b_val (số lớn nhất trong các giá trị bị loại)
            m_threshold = 2 * b_val
            # Tìm số giá trị nguyên m trong [-10, 10] sao cho m > 2*b_val
            m_values = [m for m in range(-10, 11) if m > m_threshold]
            count_m = len(m_values)

            vdc_da_1_d = '\\True Gọi $\\mathscr{D}_g$ là tập xác định của hàm số $g(x)=\\sqrt{2x-m}$. Có %s giá trị nguyên của $m \\in [-10;10]$ để $\\mathscr{D}_g \\subset \\mathscr{D}_f$' %(count_m)
            vdc_da_1_s = 'Gọi $\\mathscr{D}_g$ là tập xác định của hàm số $g(x)=\\sqrt{2x-m}$. Có %s giá trị nguyên của $m \\in [-10;10]$ để $\\mathscr{D}_g \\subset \\mathscr{D}_f$' %(count_m + 1)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Hàm số $g(x)$ xác định $\\Leftrightarrow 2x-m \\geq 0 \\Leftrightarrow x \\geq \\dfrac{m}{2} \\Rightarrow \\mathscr{D}_g = \\left[ \\dfrac{m}{2}; +\\infty \\right)$. \\\\ Để $\\mathscr{D}_g \\subset \\mathscr{D}_f \\Leftrightarrow \\dfrac{m}{2} > %s \\Leftrightarrow m > %s$. \\\\ Vì $m \\in [-10; 10]$ và $m > %s$ nên $m \\in \\{%s\\}$. Vậy có %s giá trị nguyên.''' 
                             %(b_val, m_threshold, m_threshold, ", ".join(map(str, m_values)) if m_values else "rỗng", count_m))

            # Logic chọn đáp án Đúng/Sai (từ 1 đến 3 câu đúng)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    break

            # Nội dung xuất ra
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(d1) + '}\n'
                '{' + str(d2) + '}\n'
                '{' + str(d3) + '}\n'
                '{' + str(d4) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

