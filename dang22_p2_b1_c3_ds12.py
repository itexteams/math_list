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


def bt_dang22_p2_b1_c3_ds12(self):
                # Khai báo biến ký hiệu
                x = symbols('x')

                # --- BƯỚC 1: RANDOM CÁC GIÁ TRỊ ---
                # Chọn a là số chẵn để a/2 nguyên cho đẹp, b và c là số nguyên
                a = random.choice([2, 4, 6, -2, -4])
                b = random.choice([val for val in range(-5, 6) if val != 0])
                c = random.randint(-5, 5)
                k_val = random.randint(1, 3) # Giá trị tính f(k) ở câu c

                f_prime = a*x + b
                f_x = integrate(f_prime, x) + c
                f_k_value = f_x.subs(x, k_val)
                nguyen_ham_f = integrate(f_x, x)

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Biết hàm số $f(x)$ thỏa mãn các điều kiện $f'(x) = %s$ và đồ thị hàm số $y = f(x)$ đi qua điểm $M(0; %s)$.''' 
                                 % (latex(f_prime), latex(c)))

                ########################################################################
                # Nhận biết: Nghiệm f'(x) và khoảng đơn điệu
                ########################################################################
                root = -Rational(b, a)
                huong_db = "đồng biến trên khoảng $\\left( %s; +\\infty \\right)$" % latex(root) if a > 0 else "nghịch biến trên khoảng $\\left( %s; +\\infty \\right)$" % latex(root)

                nb_da_1_d = r'''\True $f'(x) = 0$ có một nghiệm $x = %s$''' % (latex(root))
                nb_da_1_s = r'''$f'(x) = 0$ có một nghiệm $x = %s$''' % (latex(-root))
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = (r'''Ta có $f'(x)=0 \Leftrightarrow %s = 0 \Leftrightarrow x = %s$. Vì hệ số $a=%s$ nên hàm số %s.''' 
                                % (latex(f_prime), latex(root), a, huong_db))

                ########################################################################
                # Thông hiểu: Phương trình tiếp tuyến tại M(0;c)
                ########################################################################
                pt_tt = b*x + c

                th_da_1_d = r'\True Phương trình tiếp tuyến của đồ thị tại $M(0; %s)$ là $y = %s$' % (c, latex(pt_tt))
                th_da_1_s = r'Phương trình tiếp tuyến của đồ thị tại $M(0; %s)$ là $y = %s$' % (c, latex(a*x + c))
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = (r'''Ta có $f'(0) = %s$. Phương trình tiếp tuyến tại $M(0; %s)$ là $y = f'(0)(x-0) + f(0) = %s x + %s$.''' 
                                % (b, c, b, c))

                ########################################################################
                # Vận dụng: Tìm f(x) và tính f(k)
                ########################################################################
                vd_da_1_d = r'\True Giá trị của $f(%s)$ bằng $%s$' % (k_val, latex(f_k_value))
                vd_da_1_s = r'Giá trị của $f(%s)$ bằng $%s$' % (k_val, latex(f_k_value + 1))
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = (r'''Ta có $f(x) = \int f'(x)\text{d}x = %s + C$. Vì $f(0)=%s$ nên $C=%s$. Suy ra $f(x) = %s$, do đó $f(%s) = %s$.''' 
                                % (latex(integrate(f_prime, x)), c, c, latex(f_x), k_val, latex(f_k_value)))

                ########################################################################
                # Vận dụng cao: Nguyên hàm của f(x)
                ########################################################################
                vdc_da_1_d = r'\True Một nguyên hàm của hàm số $f(x)$ là $F(x) = %s$' % (latex(nguyen_ham_f))
                vdc_da_1_s = r'Một nguyên hàm của hàm số $f(x)$ là $F(x) = %s$' % (latex(f_x)) 
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                loigiai_vdc_1 = (r'''Ta có $\int f(x)\text{d}x = \int (%s)\text{d}x = %s + C$.''' 
                                 % (latex(f_x), latex(nguyen_ham_f)))

                # --- LOGIC CHỌN ĐÁP ÁN ĐÚNG/SAI ---
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    choice_nb = random.choice(list_nb_da_1)
                    choice_th = random.choice(list_th_da_1)
                    choice_vd = random.choice(list_vd_da_1)
                    choice_vdc = random.choice(list_vdc_da_1)

                    current_answers = [choice_nb, choice_th, choice_vd, choice_vdc]
                    if 1 <= count_true_answers(current_answers) <= 3:
                        break

                # Xuất nội dung theo định dạng LaTeX
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                    '\\choiceTFn \n'
                    '{' + str(choice_nb) + '}\n'
                    '{' + str(choice_th) + '}\n'
                    '{' + str(choice_vd) + '}\n'
                    '{' + str(choice_vdc) + '}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item ' + str(loigiai_nb_1) + '\n'
                    '\\item ' + str(loigiai_th_1) + '\n'
                    '\\item ' + str(loigiai_vd_1) + '\n'
                    '\\item ' + str(loigiai_vdc_1) + '\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n \\end{minipage} \n\n')
                return content

