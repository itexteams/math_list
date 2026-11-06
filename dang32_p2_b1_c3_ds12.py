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


def bt_dang32_p2_b1_c3_ds12(self):
                # --- BƯỚC 1: KHAI BÁO BIẾN VÀ RANDOM ---
                t = symbols('t')
                k_val = random.choice([2, 4, 6])
                r1_val = random.randint(4, 7)
                r2_val = random.randint(10, 14)
                T_limit = r2_val + 1
                t0_val = random.randint(1, 3)
                Q0_val = random.randrange(400, 1000, 50)

                Q_prime = sp.expand(k_val * t * (t - r1_val) * (t - r2_val))
                Q_primitive = integrate(Q_prime, t)
                C_exact = Q0_val - Q_primitive.subs(t, t0_val)
                Q_func = Q_primitive + C_exact

                # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (r'''Tại một khu di tích vào ngày lễ hội hàng năm, tốc độ thay đổi lượng khách tham quan được biểu diễn bằng hàm số $Q'(t) = %s$, trong đó $t$ tính bằng giờ ($0 \le t \le %s$), $Q'(t)$ tính bằng khách/giờ. Sau %s giờ đầu tiên đã có %s người có mặt.''' 
                                 % (latex(Q_prime), latex(T_limit), latex(t0_val), latex(Q0_val)))

                # --- BƯỚC 3: CÁC ĐÁP ÁN VÀ LỜI GIẢI ---
                # NHẬN BIẾT
                nb_da_d = r'\True Hàm số biểu diễn lượng khách tham quan là $Q(t) = %s + C$' % latex(Q_primitive)
                nb_da_s = r'Hàm số biểu diễn lượng khách tham quan là $Q(t) = %s + C$' % latex(diff(Q_prime, t))
                list_nb = [nb_da_d, nb_da_s]
                loigiai_nb = r'''Lượng khách tham quan $Q(t)$ là một nguyên hàm của $Q'(t)$: $Q(t) = \int (%s) \text{d}t = %s + C$.''' % (latex(Q_prime), latex(Q_primitive))

                # THÔNG HIỂU
                t_test = t0_val + 2
                Q_test_val = Q_func.subs(t, t_test)
                th_da_d = r'\True Hằng số $C = %s$ và sau $%s$ giờ có $%s$ khách' % (latex(C_exact), latex(t_test), latex(Q_test_val))
                th_da_s = r'Hằng số $C = %s$ và sau $%s$ giờ có $%s$ khách' % (latex(C_exact + 10), latex(t_test), latex(Q_test_val + 50))
                list_th = [th_da_d, th_da_s]
                loigiai_th = r'''Từ $Q(%s) = %s \Rightarrow %s + C = %s \Rightarrow C = %s$. Khi đó $Q(%s) = %s$.''' % (latex(t0_val), latex(Q0_val), latex(Q_primitive.subs(t, t0_val)), latex(Q0_val), latex(C_exact), latex(t_test), latex(Q_test_val))

                # VẬN DỤNG
                critical_points = [0, r1_val, r2_val, T_limit]
                values_at_points = [Q_func.subs(t, p) for p in critical_points]
                max_Q = max(values_at_points)
                vd_da_d = r'\True Số lượng khách lớn nhất có mặt trong khu di tích là $%s$ người' % latex(max_Q)
                vd_da_s = r'Số lượng khách lớn nhất có mặt trong khu di tích là $%s$ người' % latex(max_Q - 100)
                list_vd = [vd_da_d, vd_da_s]
                loigiai_vd = r'''Khảo sát $Q(t)$ trên $[0; %s]$ ta tìm được GTLN là %s.''' % (T_limit, max_Q)

                # VẬN DỤNG CAO
                Q_double_prime = diff(Q_prime, t)
                roots_Q2 = solve(Q_double_prime, t)
                t_v1, t_v2 = roots_Q2[0], roots_Q2[1]
                val_v1 = round(float(Q_prime.subs(t, t_v1)), 1)
                val_v2 = round(float(Q_prime.subs(t, t_v2)), 1)
                val_end = Q_prime.subs(t, T_limit)
                vdc_da_d = r'\True Tốc độ thay đổi lượng khách lớn nhất tại thời điểm $t = %s$' % latex(T_limit)
                vdc_da_s = r'Tốc độ thay đổi lượng khách lớn nhất tại thời điểm $t = %s$' % latex(round(float(t_v1), 0))
                list_vdc = [vdc_da_d, vdc_da_s]
                loigiai_vdc = r'''Khảo sát $Q'(t)$ trên $[0;%s]$, ta thấy tốc độ đạt GTLN tại $t=%s$ với giá trị $%s$.''' % (T_limit, T_limit, val_end)

                # --- BƯỚC 4: LẶP ĐỂ CHỌN ĐÁP ÁN (1-3 ĐÚNG) ---
                def count_true(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    d1, d2, d3, d4 = random.choice(list_nb), random.choice(list_th), random.choice(list_vd), random.choice(list_vdc)
                    if 1 <= count_true([d1, d2, d3, d4]) <= 3:
                        break

                # --- BƯỚC 5: XUẤT NỘI DUNG ---
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                           '\\choiceTFn \n'
                           '{' + str(d1) + '}\n'
                           '{' + str(d2) + '}\n'
                           '{' + str(d3) + '}\n'
                           '{' + str(d4) + '}\n'
                           '\\loigiai{ \n'
                           '\\begin{enumEX}[a)]{1} \n'
                           '\\item ' + str(loigiai_nb) + '\n'
                           '\\item ' + str(loigiai_th) + '\n'
                           '\\item ' + str(loigiai_vd) + '\n'
                           '\\item ' + str(loigiai_vdc) + '\n'
                           '\\end{enumEX}} \n'
                           '\\end{ex}\n \\end{minipage} \n\n')

                return content

