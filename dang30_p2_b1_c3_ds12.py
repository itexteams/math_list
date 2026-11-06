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


def bt_dang30_p2_b1_c3_ds12(self):
                # --- BƯỚC 1: KHAI BÁO BIẾN VÀ RANDOM ---
                t = symbols('t')
                a_val = random.choice([Rational(1, 2), 1, Rational(3, 2), 2])
                b_val = random.randint(2, 6)
                h0 = random.randint(10, 20)
                T_year = random.choice([5, 6, 8, 10])

                # Tính toán các hàm số
                h_prime = a_val * t + b_val
                h_t_no_C = integrate(h_prime, t) # Nguyên hàm h(t) chưa có C
                h_T_val = h_t_no_C.subs(t, T_year) + h0 # Chiều cao tại năm T
                growth_val = h_T_val - h0 # Lượng tăng thêm

                # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (r'''Một vườn ươm cây cảnh bán một cây sau %s năm trồng và uốn tạo dáng. Tốc độ tăng trưởng của cây đó trong suốt %s năm được tính xấp xỉ bởi công thức $h'(t) = %s$, trong đó $h(t)$ (cm) là chiều cao của cây sau $t$ (năm). Cây con khi được trồng cao %s cm.''' 
                                 % (T_year, T_year, latex(h_prime), h0))

                # --- BƯỚC 3: CÁC ĐÁP ÁN VÀ LỜI GIẢI (CẤU TRÚC GIỐNG DANG29) ---

                # NHẬN BIẾT
                nb_da_1_d = r'''\True Ta có $h(t)$ là một nguyên hàm của hàm số $h'(t) = %s$''' % latex(h_prime)
                nb_da_1_s = r'''Ta có $h'(t)$ là một nguyên hàm của hàm số $h(t)$ trên đoạn $[0;%s]$ ''' % T_year
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                loigiai_nb_1 = r'''Theo định nghĩa, chiều cao $h(t)$ là nguyên hàm của tốc độ tăng trưởng $h'(t)$.'''

                # THÔNG HIỂU
                h_t_wrong = h_prime + h0
                th_da_1_d = r'\True Công thức tính chiều cao của cây tại thời điểm $t$ là $h(t) = %s + C$' % latex(h_t_no_C)
                th_da_1_s = r'Công thức tính chiều cao của cây tại thời điểm $t$ là $h(t) = %s + C$' % latex(h_t_wrong)
                list_th_da_1 = [th_da_1_d, th_da_1_s]
                loigiai_th_1 = r'Ta có $h(t) = \int (%s) \text{d}t = %s + C$.' % (latex(h_prime), latex(h_t_no_C))

                # VẬN DỤNG
                vd_da_1_d = r'\True Sau %s năm, chiều cao của cây đó là $%s$ cm' % (T_year, latex(h_T_val))
                vd_da_1_s = r'Sau %s năm, chiều cao của cây đó là $%s$ cm' % (T_year, latex(h_T_val + 5))
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                loigiai_vd_1 = (r'''Vì $h(0) = %s \Rightarrow C = %s$. Vậy $h(t) = %s + %s$. \\ Khi đó $h(%s) = %s$ cm.''' 
                                % (h0, h0, latex(h_t_no_C), h0, T_year, latex(h_T_val)))

                # VẬN DỤNG CAO
                vdc_da_1_d = r'\True Sau %s năm chiều cao của cây tăng thêm là $%s$ cm' % (T_year, latex(growth_val))
                vdc_da_1_s = r'Sau %s năm chiều cao của cây tăng thêm là $%s$ cm' % (T_year, latex(h_T_val))
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                loigiai_vdc_1 = (r'''Lượng tăng thêm sau %s năm được tính bởi: \\ $h(%s) - h(0) = %s - %s = %s$ cm.''' 
                                 % (T_year, T_year, latex(h_T_val), h0, latex(growth_val)))

                # --- BƯỚC 4: LẶP ĐỂ CHỌN ĐÁP ÁN (1-3 ĐÚNG) ---
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    nb_da_1 = random.choice(list_nb_da_1)
                    th_da_1 = random.choice(list_th_da_1)
                    vd_da_1 = random.choice(list_vd_da_1)
                    vdc_da_1 = random.choice(list_vdc_da_1)

                    answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                    if 1 <= count_true_answers(answers) <= 3:
                        break

                # --- BƯỚC 5: XÁO TRỘN VÀ XUẤT NỘI DUNG ---
                # Giữ nguyên thứ tự để khớp với danh sách lời giải a, b, c, d
                shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

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

