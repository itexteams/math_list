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


def bt_dang7_p2_b2_c4_ds11(self):
            # Khai báo biến
            # --- HÀM BỔ TRỢ ĐỊNH DẠNG SỐ KIỂU VIỆT NAM ---
            def format_num_vn(num, precision=3):
                """
                Chuyển số sang chuỗi: dấu chấm thành dấu phẩy, 
                nếu là số nguyên (phần thập phân = 0) thì không hiện .0
                """
                num_rounded = round(float(num), precision)
                # Định dạng :g giúp loại bỏ các số 0 thừa ở cuối và phần thập phân nếu bằng 0
                formatted = "{:g}".format(num_rounded)
                return formatted.replace('.', ',')

            # Khai báo biến ký hiệu
            t = symbols('t')

            # --- BƯỚC 1: RANDOM CÁC THÔNG SỐ CỦA BÀI TOÁN ---
            A = random.randint(20, 40)  # Giới hạn dân số
            C = random.randint(3, 8)    # Hằng số ở mẫu
            B = random.randint(5, 15)   # Hằng số ở tử
            t_target = 24               # Năm 2024

            f_t = (A*t + B) / (t + C)
            v_t = diff(f_t, t)

            # Tính toán các giá trị
            limit_val = A # Số nguyên
            diff_const = A*C - B # Số nguyên
            v_t_target = v_t.subs(t, t_target)
            t_max = sqrt(diff_const) - C

            # Định dạng các số thực để đưa vào chuỗi
            v_val_str = format_num_vn(v_t_target, 3)
            v_val_wrong_str = format_num_vn(float(v_t_target) + 0.1, 3)
            t_max_approx_str = format_num_vn(t_max, 2)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Số dân của một thị trấn sau $t$ năm kể từ năm 2000 được mô tả bởi hàm số $f(t)=\frac{%s t + %s}{t + %s}, t > 0$, trong đó $f(t)$ được tính bằng nghìn người. Tốc độ tăng dân số của thị trấn vào năm thứ $t_0$ kể từ năm 2000 là $v(t_0) = \lim_{t \to t_0} \frac{f(t) - f(t_0)}{t - t_0}$ (tính bằng nghìn người/năm).''' 
                             % (latex(A), latex(B), latex(C)))

            ########################################################################
            # Nhận biết
            nb_da_1_d = r'\True Giới hạn của hàm số dân số khi $t \to +\infty$ là %s (nghìn người)' % (format_num_vn(limit_val))
            nb_da_1_s = r'Giới hạn của hàm số dân số khi $t \to +\infty$ là %s (nghìn người)' % (format_num_vn(limit_val + 2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''Ta có $\lim_{t \to +\infty} f(t) = \lim_{t \to +\infty} \frac{%st + %s}{t + %s} = %s$.''' 
                            % (latex(A), latex(B), latex(C), format_num_vn(limit_val)))

            ########################################################################
            # Thông hiểu
            th_da_1_d = r'\True Khi thời gian $t$ càng lớn, số dân của thị trấn sẽ tiến dần đến %s nghìn người' % (format_num_vn(limit_val))
            th_da_1_s = r'Khi thời gian $t$ càng lớn, số dân của thị trấn sẽ tăng vô hạn'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Vì $\lim_{t \to +\infty} f(t) = %s$ nên khi thời gian $t$ càng lớn, số dân thị trấn tiến sát ngưỡng %s nghìn người.''' 
                            % (format_num_vn(limit_val), format_num_vn(limit_val)))

            ########################################################################
            # Vận dụng
            vd_da_1_d = r'\True Tốc độ tăng dân số vào năm 2024 xấp xỉ %s nghìn người/năm' % (v_val_str)
            vd_da_1_s = r'Tốc độ tăng dân số vào năm 2024 xấp xỉ %s nghìn người/năm' % (v_val_wrong_str)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Tốc độ tăng dân số là $v(t) = f'(t) = \frac{%s}{(t + %s)^2}$. Tại năm 2024 ($t=%s$), ta có $v(%s) = \frac{%s}{(%s + %s)^2} \approx %s$.''' 
                            % (latex(diff_const), latex(C), latex(t_target), latex(t_target), latex(diff_const), latex(t_target), latex(C), v_val_str))

            ########################################################################
            # Vận dụng cao
            num_years = math.floor(float(t_max)) if float(t_max) > 0 else 0
            vdc_da_1_d = r'\True Có %s năm kể từ năm 2000 mà tốc độ tăng dân số lớn hơn 1000 người/năm' % (num_years)
            vdc_da_1_s = r'Có %s năm kể từ năm 2000 mà tốc độ tăng dân số lớn hơn 1000 người/năm' % (num_years + 2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Để tốc độ > 1 nghìn người/năm: $v(t) > 1 \Leftrightarrow \frac{%s}{(t + %s)^2} > 1 \Leftrightarrow (t + %s)^2 < %s$. \\ Suy ra $0 < t < \sqrt{%s} - %s \approx %s$. Vậy có %s năm thỏa mãn.''' 
                             % (latex(diff_const), latex(C), latex(C), latex(diff_const), latex(diff_const), latex(C), t_max_approx_str, num_years))

            # --- BƯỚC 2: XỬ LÝ RANDOM ĐÁP ÁN ĐÚNG/SAI THEO MẪU ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # --- BƯỚC 3: XUẤT NỘI DUNG ---
            content = (r'\begin{minipage}{\textwidth} ' + '\n' +
                r'\begin{ex}' + '\n' +
                str(noidungcauhoi) + '\n' +
                r'\choiceTFn' + '\n' +
                '{' + nb_sel + '}\n' +
                '{' + th_sel + '}\n' +
                '{' + vd_sel + '}\n' +
                '{' + vdc_sel + '}\n' +
                r'\loigiai{' + '\n' +
                r'\begin{enumEX}[a)]{1}' + '\n' +
                r'\item ' + loigiai_nb_1 + '\n' +
                r'\item ' + loigiai_th_1 + '\n' +
                r'\item ' + loigiai_vd_1 + '\n' +
                r'\item ' + loigiai_vdc_1 + '\n' +
                r'\end{enumEX}}' + '\n' +
                r'\end{ex}' + '\n' +
                r'\end{minipage}' + '\n\n')
            return content

