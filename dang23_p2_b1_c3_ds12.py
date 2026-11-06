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


def bt_dang23_p2_b1_c3_ds12(self):
                # Khai báo biến ký hiệu
                x = symbols('x')

                # --- BƯỚC 1: RANDOM CÁC GIÁ TRỊ ---
                # Chọn a là số chẵn, b khác 0 để bài toán đẹp
                a = random.choice([-6, -4, -2, 2, 4, 6])
                b = random.choice([val for val in range(-5, 6) if val != 0])

                f_x = a*x + b
                x_val_a = 2
                x_val_c1 = 1
                x_val_c2 = 2
                y_val_c1 = 2 # G(1) = 2

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Cho hàm số $f(x)=%s$.''' % (latex(f_x)))

                ########################################################################
                # Nhận biết: Tính chất F'(x) = f(x)
                ########################################################################
                f_at_2 = a * x_val_a + b
                nb_da_1_d = r'''\True $F'(%s) = f(%s) = %s$''' % (x_val_a, x_val_a, f_at_2)
                nb_da_1_s = r'''$F'(%s) = f'(%s) = %s$''' % (x_val_a, x_val_a, a)
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = (r'''Vì $F(x)$ là một nguyên hàm của $f(x)$ nên $F'(x) = f(x)$. Suy ra $F'(%s) = f(%s) = %s \cdot %s + %s = %s$.''' 
                                % (x_val_a, x_val_a, a, x_val_a, b, f_at_2))

                ########################################################################
                # Thông hiểu: Kiểm tra một nguyên hàm cụ thể
                ########################################################################
                F_antideriv = integrate(f_x, x)
                th_da_1_d = r'\True $F(x) = %s$ là một nguyên hàm của $f(x)$ trên $\mathbb{R}$' % (latex(F_antideriv))
                th_da_1_s = r'$F(x) = %s$ là một nguyên hàm của $f(x)$ trên $\mathbb{R}$' % (latex(a*x**2 + b*x))
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = (r'''Ta có $\left(%s\right)' = %s = f(x)$. Vậy đây là một nguyên hàm.''' 
                                % (latex(F_antideriv), latex(f_x)))

                ########################################################################
                # Vận dụng: Tìm hằng số C và tính giá trị G(x)
                ########################################################################
                val_at_x1 = (a/2)*(x_val_c1**2) + b*x_val_c1
                C_val = y_val_c1 - val_at_x1
                G_x = (a/2)*x**2 + b*x + C_val
                G_at_2 = (a/2)*(x_val_c2**2) + b*x_val_c2 + C_val

                vd_da_1_d = r'\True Gọi $G(x)$ là nguyên hàm của $f(x)$ thỏa mãn $G(%s)=%s$. Khi đó $G(%s)=%s$' % (x_val_c1, y_val_c1, x_val_c2, int(G_at_2))
                vd_da_1_s = r'Gọi $G(x)$ là nguyên hàm của $f(x)$ thỏa mãn $G(%s)=%s$. Khi đó $G(%s)=%s$' % (x_val_c1, y_val_c1, x_val_c2, int(G_at_2 + 2))
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = (r'''$G(x) = \int f(x)\text{d}x = %s + C$. Vì $G(%s)=%s \Rightarrow %s + C = %s \Rightarrow C = %s$. Do đó $G(x) = %s$. Vậy $G(%s) = %s$.''' 
                                % (latex(F_antideriv), x_val_c1, y_val_c1, latex(val_at_x1), y_val_c1, latex(C_val), latex(G_x), x_val_c2, int(G_at_2)))

                ########################################################################
                # Vận dụng cao: Biến đổi f(-x)
                ########################################################################
                f_neg_x = a*(-x) + b
                integ_f_neg_x = integrate(f_neg_x, x)
                F_neg_x = F_antideriv.subs(x, -x)

                vdc_da_1_d = r'\True $\int f(-x)\text{d}x = %s + C$' % (latex(integ_f_neg_x))
                vdc_da_1_s = r'$\int f(-x)\text{d}x = %s + C$' % (latex(F_neg_x))
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                loigiai_vdc_1 = (r'''Ta có $f(-x) = %s$. Suy ra $\int f(-x)\text{d}x = \int (%s)\text{d}x = %s + C$.''' 
                                 % (latex(f_neg_x), latex(f_neg_x), latex(integ_f_neg_x)))

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

                # Xuất nội dung theo định dạng LaTeX (giống hệt dang22)
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

