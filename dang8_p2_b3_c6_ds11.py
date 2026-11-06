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


def bt_dang8_p2_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo các giá trị ngẫu nhiên cho bài toán
            # w: trắng, r: đỏ, b: xanh
            w = random.randint(4, 6)
            r = random.randint(5, 7)
            b = random.randint(8, 10)
            tong = w + r + b
            chon = 5

            # Tính toán các giá trị xác suất
            n_omega = binomial(tong, chon)

            # Câu a: n(Omega)
            da_a_val = n_omega

            # Câu b: Xác suất 5 viên màu xanh
            n_5_xanh = binomial(b, chon)
            p_5_xanh = Rational(n_5_xanh, n_omega)

            # Câu c: Xác suất ít nhất 1 viên xanh
            n_khong_xanh = binomial(w + r, chon)
            p_it_nhat_1_xanh = 1 - Rational(n_khong_xanh, n_omega)
            threshold_c = 0.94
            # Chuyển threshold sang dạng chuỗi có dấu phẩy
            threshold_c_str = str(threshold_c).replace('.', ',')

            # Câu d: Điều kiện cấp số cộng x-y, y-z, z-x
            # 2(y-z) = (x-y) + (z-x) <=> 2y - 2z = -y + z <=> 3y = 3z <=> y = z
            # Với x+y+z=5 và x,y,z >= 1:
            # TH1: y=z=1 => x=3. Số cách: C(w,3)*C(r,1)*C(b,1)
            # TH2: y=z=2 => x=1. Số cách: C(w,1)*C(r,2)*C(b,2)
            n_th1 = binomial(w, 3) * binomial(r, 1) * binomial(b, 1)
            n_th2 = binomial(w, 1) * binomial(r, 2) * binomial(b, 2)
            n_d = n_th1 + n_th2
            p_d = Rational(n_d, n_omega)

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Một hộp chứa các viên bi có kích thước và khối lượng như nhau gồm %s viên bi trắng, %s viên bi đỏ và %s viên bi xanh. Lấy ngẫu nhiên đồng thời %s viên bi từ hộp, trong đó có $x$ viên bi trắng, $y$ viên bi đỏ và $z$ viên bi xanh.''' 
                             %(w, r, b, chon))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                # --- NHẬN BIẾT (Câu a) ---
                nb_da_1_d = '\\True Số phần tử của không gian mẫu là $n(\\Omega) = C_{%s}^{%s}$' % (tong, chon)
                nb_da_1_s = 'Số phần tử của không gian mẫu là $n(\\Omega) = A_{%s}^{%s}$' % (tong, chon)
                nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
                loigiai_nb_1 = 'Số phần tử của không gian mẫu là số cách chọn %s viên bi từ %s viên bi: $n(\\Omega) = C_{%s}^{%s} = %s$.' % (chon, tong, tong, chon, n_omega)

                # --- THÔNG HIỂU (Câu b) ---
                p_b_sai = Rational(random.randint(1, 10), 3000) # Một giá trị sai ngẫu nhiên
                th_da_1_d = '\\True Xác suất lấy được %s viên bi đều màu xanh là $%s$' % (chon, latex(p_5_xanh))
                th_da_1_s = 'Xác suất lấy được %s viên bi đều màu xanh là $%s$' % (chon, latex(p_b_sai))
                th_da_1 = random.choice([th_da_1_d, th_da_1_s])
                loigiai_th_1 = 'Số cách lấy %s viên bi màu xanh là $C_{%s}^{%s} = %s$. \\\\ Xác suất cần tìm là $P = \\frac{%s}{%s} = %s$.' % (chon, b, chon, n_5_xanh, n_5_xanh, n_omega, latex(p_5_xanh))

                # --- VẬN DỤNG (Câu c) ---
                val_c = float(p_it_nhat_1_xanh)
                is_less = val_c < threshold_c
                c_status = '\\True ' if is_less else ''
                vd_da_1_d = c_status + 'Xác suất lấy được %s viên bi có ít nhất một viên bi màu xanh nhỏ hơn $%s$' % (chon, threshold_c_str)

                c_status_s = '' if is_less else '\\True '
                vd_da_1_s = c_status_s + 'Xác suất lấy được %s viên bi có ít nhất một viên bi màu xanh lớn hơn $%s$' % (chon, threshold_c_str)
                vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])

                p_c_val_str = str(round(val_c, 4)).replace('.', ',')
                loigiai_vd_1 = 'Gọi $A$ là biến cố "Lấy được %s viên bi có ít nhất một viên xanh". \\\\Biến cố đối $\\overline{A}$ là "Lấy được %s viên bi không có viên màu xanh nào" (tức là chỉ lấy từ %s viên trắng và %s viên đỏ). \\\\ Ta có $n(\\overline{A}) = C_{%s}^{%s} = %s$. \\\\ Xác suất biến cố $A$ là $P(A) = 1 - P(\\overline{A}) = 1 - \\frac{%s}{%s} = %s \\approx %s$.' % (chon, chon, w, r, w+r, chon, n_khong_xanh, n_khong_xanh, n_omega, latex(p_it_nhat_1_xanh), p_c_val_str)

                # --- VẬN DỤNG CAO (Câu d) ---
                vdc_da_1_d = '\\True Xác suất lấy được %s viên đủ cả ba màu, đồng thời ba số $x-y, y-z, z-x$ theo thứ tự lập thành cấp số cộng bằng $%s$' % (chon, latex(p_d))
                vdc_da_1_s = 'Xác suất lấy được %s viên đủ cả ba màu, đồng thời ba số $x-y, y-z, z-x$ theo thứ tự lập thành cấp số cộng bằng $%s$' % (chon, latex(p_d + Rational(1, 100)))
                vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])

                loigiai_vdc_1 = 'Để $x-y, y-z, z-x$ lập thành cấp số cộng thì \\\\$2(y-z) = (x-y) + (z-x) \\Leftrightarrow 2y - 2z = -y + z \\Leftrightarrow 3y = 3z \\Leftrightarrow y = z$. \\\\ Vì lấy %s viên đủ 3 màu nên $x, y, z \\geq 1$ và $x+y+z=5$. \\\\ TH1: $y=z=1 \\Rightarrow x=3$. Số cách: $C_{%s}^3 \\cdot C_{%s}^1 \\cdot C_{%s}^1 = %s \\cdot %s \\cdot %s = %s$. \\\\ TH2: $y=z=2 \\Rightarrow x=1$. Số cách: $C_{%s}^1 \\cdot C_{%s}^2 \\cdot C_{%s}^2 = %s \\cdot %s \\cdot %s = %s$. \\\\ Tổng số cách thuận lợi: %s + %s = %s. \\\\ Xác suất: $P = \\frac{%s}{%s} = %s$.' % (chon, w, r, b, binomial(w,3), r, b, n_th1, w, r, b, w, binomial(r,2), binomial(b,2), n_th2, n_th1, n_th2, n_d, n_d, n_omega, latex(p_d))

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

