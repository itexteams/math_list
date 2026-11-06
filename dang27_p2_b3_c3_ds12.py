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


def bt_dang27_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- B3: SUY NGHĨ TÌM CÁCH RANDOM ---
            # Chọn m là số nguyên dương chẵn để m/2 là số nguyên (giống f(x)=e^x + 2x trong hình)
            m = 2 * random.randint(1, 4) 
            m_half = m // 2
            # Chọn giới hạn tích phân k cho câu c
            k = random.randint(3, 6)
            # Chọn giá trị F(0) = p/q cho câu d
            p = random.choice([3, 5, 7, 1])
            q = 2
            val_F0 = Rational(p, q)
            constant_C = val_F0 - 1 # Vì F(0) = e^0 + m/2*0^2 + C = 1 + C

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $f(x)=e^x + %s x$.''' % (latex(m)))

            ########################################################################
            # Nhận biết: Nguyên hàm cơ bản
            ########################################################################
            nb_da_1_d = r'\True Nguyên hàm của hàm số là $G(x) = \int f(x) \text{d}x = e^x + %s x^2 + C$' % (latex(m_half) if m_half != 1 else "")
            nb_da_1_s = r'Nguyên hàm của hàm số là $G(x) = \int f(x) \text{d}x = e^x + %s x^2 + C$' % (latex(m))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (r'''Nguyên hàm của hàm số là $G(x) = \int (e^x + %sx) \text{d}x = e^x + %s x^2 + C$.''' 
                            % (latex(m), latex(m_half) if m_half != 1 else ""))

            ########################################################################
            # Thông hiểu: Công thức tính thể tích
            ########################################################################
            th_da_1_d = r'\True Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi đồ thị $y=f(x)$, trục hoành, $x=a, x=b$ quanh $Ox$ là $V = \pi \int_a^b f^2(x) \text{d}x$'
            th_da_1_s = r'Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi đồ thị $y=f(x)$, trục hoành, $x=a, x=b$ quanh $Ox$ là $V = \int_a^b f^2(x) \text{d}x$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'''Công thức tính thể tích khối tròn xoay quanh trục $Ox$ là $V = \pi \int_a^b f^2(x) \text{d}x$.'''

            ########################################################################
            # Vận dụng: Tính tích phân xác định
            ########################################################################
            # Giá trị đúng: (e^k + m_half*k^2) - (e^0 + 0) = e^k + m_half*k^2 - 1
            val_int = m_half * (k**2) - 1
            vd_da_1_d = r'\True $\int_0^{%s} f(x) \text{d}x = e^{%s} + %s$' % (latex(k), latex(k), latex(val_int))
            vd_da_1_s = r'$\int_0^{%s} f(x) \text{d}x = e^{%s} + %s$' % (latex(k), latex(k), latex(val_int + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''$\int_0^{%s} f(x) \text{d}x = \left( e^x + %s x^2 \right) \Big|_0^{%s} = e^{%s} + %s - (e^0 + 0) = e^{%s} + %s$.'''
                            % (latex(k), latex(m_half) if m_half != 1 else "", latex(k), latex(k), latex(m_half * k**2), latex(k), latex(val_int)))

            ########################################################################
            # Vận dụng cao: Tìm hằng số C
            ########################################################################
            vdc_da_1_d = r'\True Với $F(x)$ là một nguyên hàm thỏa mãn $F(0)=%s$ thì $F(x) = e^x + %s x^2 + %s$' % (latex(val_F0), latex(m_half) if m_half != 1 else "", latex(constant_C))
            vdc_da_1_s = r'Với $F(x)$ là một nguyên hàm thỏa mãn $F(0)=%s$ thì $F(x) = e^x + %s x^2 - %s$' % (latex(val_F0), latex(m_half) if m_half != 1 else "", latex(constant_C))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Vì $F(x)$ là một nguyên hàm nên $F(x) = e^x + %s x^2 + C$. \\ Khi đó $F(0)=%s \Leftrightarrow e^0 + C = %s \Leftrightarrow 1 + C = %s \Leftrightarrow C = %s$. \\ Vậy $F(x) = e^x + %s x^2 + %s$.'''
                             % (latex(m_half) if m_half != 1 else "", latex(val_F0), latex(val_F0), latex(val_F0), latex(constant_C), latex(m_half) if m_half != 1 else "", latex(constant_C)))

            # --- HÀM ĐẾM SỐ ĐÁP ÁN ĐÚNG ---
            def count_true_answers(answers):
                return sum(r'\True' in ans for ans in answers)

            # Lặp để đảm bảo có từ 1 đến 3 câu đúng
            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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

