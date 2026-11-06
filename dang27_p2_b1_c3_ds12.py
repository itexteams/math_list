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


def bt_dang27_p2_b1_c3_ds12(self):
                # Khai báo biến ký hiệu
                x = symbols('x')

                # --- BƯỚC 1: RANDOM CÁC GIÁ TRỊ ---
                # Chọn a chia hết cho 3, b chia hết cho 2 để nguyên hàm đẹp
                a_val = 3 * random.randint(1, 3)
                b_val = 2 * random.randint(-3, 3)
                if b_val == 0: b_val = 2
                c_val = random.randint(1, 5)

                f_func = a_val*x**2 + b_val*x + c_val
                x0_val = 1
                y0_val = random.randint(1, 5)

                # Tính toán các giá trị bằng Sympy
                F_inf = integrate(f_func, x) 
                C_const = y0_val - F_inf.subs(x, x0_val)
                F_specific = F_inf + C_const
                F_at_neg1 = F_specific.subs(x, -1)
                int_F = integrate(F_specific, x)
                f_shifted = f_func.subs(x, x - 1).expand()
                int_f_shifted = integrate(f_shifted, x)

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Cho hàm số $f(x)=%s$. Gọi $F(x)$ là một nguyên hàm của hàm số $f(x)$ thỏa mãn $F(%s)=%s$.''' 
                                 % (latex(f_func), latex(x0_val), latex(y0_val)))

                ########################################################################
                # Nhận biết: Kiểm tra họ nguyên hàm
                ########################################################################
                nb_da_1_d = r'\True Họ nguyên hàm của hàm số là $\int f(x)\text{d}x = %s + C$' % (latex(F_inf))
                nb_da_1_s = r'Họ nguyên hàm của hàm số là $\int f(x)\text{d}x = %s + C$' % (latex(f_func + F_inf))
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = (r'''Ta có $\int f(x)\text{d}x = \int (%s)\text{d}x = %s + C$.''' 
                                % (latex(f_func), latex(F_inf)))

                ########################################################################
                # Thông hiểu: Tính giá trị F(-1)
                ########################################################################
                th_da_1_d = r'\True Giá trị của $F(-1)$ bằng $%s$' % (latex(F_at_neg1))
                th_da_1_s = r'Giá trị của $F(-1)$ bằng $%s$' % (latex(F_at_neg1 + 2))
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = (r'''Ta có $F(x) = %s + C$. Vì $F(%s)=%s \Rightarrow %s + C = %s \Rightarrow C = %s$. Khi đó $F(x) = %s$. Suy ra $F(-1) = %s$.''' 
                                % (latex(F_inf), latex(x0_val), latex(y0_val), latex(F_inf.subs(x, x0_val)), latex(y0_val), latex(C_const), latex(F_specific), latex(F_at_neg1)))

                ########################################################################
                # Vận dụng: Nguyên hàm của hàm F(x)
                ########################################################################
                vd_da_1_d = r'\True Một nguyên hàm của hàm số $F(x)$ là $G(x) = %s$' % (latex(int_F))
                vd_da_1_s = r'Một nguyên hàm của hàm số $F(x)$ là $G(x) = %s$' % (latex(integrate(F_inf, x)))
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = (r'''Ta có $\int F(x)\text{d}x = \int (%s)\text{d}x = %s + C$.''' 
                                % (latex(F_specific), latex(int_F)))

                ########################################################################
                # Vận dụng cao: Nguyên hàm của f(x-1)
                ########################################################################
                vdc_da_1_d = r'\True Nguyên hàm của hàm số $f(x-1)$ là $%s + C$' % (latex(int_f_shifted))
                vdc_da_1_s = r'Nguyên hàm của hàm số $f(x-1)$ là $%s + C$' % (latex(int_f_shifted + x))
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                loigiai_vdc_1 = (r'''Ta có $f(x-1) = %s$. Suy ra $\int f(x-1)\text{d}x = \int (%s)\text{d}x = %s + C$.''' 
                                 % (latex(f_shifted), latex(f_shifted), latex(int_f_shifted)))

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

                # Xuất nội dung theo định dạng LaTeX (đồng bộ 100% với dang22)
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

