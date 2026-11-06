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


def bt_dang24_p1_b1_c2_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tổng số sinh viên (N) chẵn để giống form mẫu
                N = random.choice([40, 50, 60, 80, 100])

                # Tạo tần số ngẫu nhiên cho 5 nhóm sao cho tổng bằng N
                f1 = random.randint(4, N // 5)
                f2 = random.randint(N // 6, N // 4)
                f3 = random.randint(N // 4, int(N / 2.5))
                f4 = random.randint(N // 6, N // 4)
                f5 = N - (f1 + f2 + f3 + f4)

                # Đảm bảo f5 không quá nhỏ hoặc âm
                while f5 <= 2:
                    f1 = random.randint(4, N // 5)
                    f2 = random.randint(N // 6, N // 4)
                    f3 = random.randint(N // 4, int(N / 2.5))
                    f4 = random.randint(N // 6, N // 4)
                    f5 = N - (f1 + f2 + f3 + f4)

                freqs = [f1, f2, f3, f4, f5]
                cf = [f1, f1+f2, f1+f2+f3, f1+f2+f3+f4, N]

                # Tìm nhóm chứa Q1
                pos1 = N / 4
                L1 = 0
                cf_before1 = 0
                f_Q1 = 1
                for i in range(5):
                    if pos1 <= cf[i]:
                        L1 = i
                        cf_before1 = cf[i-1] if i > 0 else 0
                        f_Q1 = freqs[i]
                        break

                # Tìm nhóm chứa Q3
                pos3 = 3 * N / 4
                L3 = 0
                cf_before3 = 0
                f_Q3 = 1
                for i in range(5):
                    if pos3 <= cf[i]:
                        L3 = i
                        cf_before3 = cf[i-1] if i > 0 else 0
                        f_Q3 = freqs[i]
                        break

                # Tính toán chính xác phân số bằng module Fraction
                q1_exact = Fraction(L1) + Fraction(N - 4*cf_before1, 4*f_Q1)
                q3_exact = Fraction(L3) + Fraction(3*N - 4*cf_before3, 4*f_Q3)

                q1_num = q1_exact.numerator
                q1_den = q1_exact.denominator
                q1_frac_str = "\\frac{%s}{%s}" % (q1_num, q1_den) if q1_den != 1 else str(q1_num)

                q3_num = q3_exact.numerator
                q3_den = q3_exact.denominator
                q3_frac_str = "\\frac{%s}{%s}" % (q3_num, q3_den) if q3_den != 1 else str(q3_num)

                q1_val = float(q1_exact)
                q3_val = float(q3_exact)
                delta_q = q3_val - q1_val

                # Làm tròn đến 2 chữ số thập phân
                q1_round = round(q1_val, 2)
                q3_round = round(q3_val, 2)
                delta_q_round = round(delta_q, 2)

                # Chuyển đổi định dạng dấu phẩy theo chuẩn VN
                q1_round_str = str(f"{q1_round:.2f}").replace('.', ',')
                q3_round_str = str(f"{q3_round:.2f}").replace('.', ',')
                kq = str(f"{delta_q_round:.2f}").replace('.', ',')

                # Các đáp án sai (nhiễu)
                d1 = str(f"{delta_q_round - 0.14:.2f}").replace('.', ',')
                d2 = str(f"{delta_q_round + 0.17:.2f}").replace('.', ',')
                d3 = str(f"{delta_q_round - 0.08:.2f}").replace('.', ',')
                d4 = str(f"{delta_q_round + 0.23:.2f}").replace('.', ',')

                # Đưa vào list và chọn để không bị trùng
                s = [d1, d2, d3, d4]

                du = [kq]
                da = random.choice(du)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Tính toán các chỉ số mảng phần tử cho lời giải
                half_N = N // 2
                q1_idx = math.ceil(N / 4)
                q3_idx = math.ceil(3 * N / 4)
                right_start = half_N + 1

                # Câu hỏi
                noidungcauhoi = ('''Một thư viện ghi lại số giờ đọc sách của $%s$ sinh viên trong một ngày và thu được mẫu số liệu ghép nhóm sau:
            \\begin{center}
            \\begin{tabular}{|c|c|c|c|c|c|}
            \\hline
            \\textbf{Nhóm giờ} & $[0; 1)$ & $[1; 2)$ & $[2; 3)$ & $[3; 4)$ & $[4; 5)$ \\\\
            \\hline
            \\textbf{Số sinh viên} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            Khoảng tứ phân vị của mẫu số liệu ghép nhóm gần nhất với giá trị nào sau đây?''' 
                                 % (N, f1, f2, f3, f4, f5))

                # Các đáp án định dạng chuẩn
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Giả sử mẫu số liệu gốc là $x_1; x_2; ...; x_{%s}$ được xếp theo thứ tự không giảm.\\\\
            Xét nửa bên trái mẫu số liệu gốc là $x_1; x_2; ...; x_{%s}$. Tứ phân vị thứ nhất của mẫu số liệu gốc là $x_{%s} \\in [%s; %s)$ nên tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là $Q_1 = %s + \\frac{\\frac{%s}{4} - %s}{%s} \\cdot 1 = %s \\approx %s$ (giờ).\\\\
            Xét nửa bên phải mẫu số liệu gốc là $x_{%s}; x_{%s}; ...; x_{%s}$.\\\\
            Tứ phân vị thứ ba của mẫu số liệu gốc là $x_{%s} \\in [%s; %s)$ nên tứ phân vị thứ ba của mẫu số liệu ghép nhóm là $Q_3 = %s + \\frac{3 \\cdot \\frac{%s}{4} - %s}{%s} \\cdot 1 = %s \\approx %s$ (giờ).\\\\
            Khoảng tứ phân vị của mẫu số liệu ghép nhóm: $\\Delta Q = Q_3 - Q_1 \\approx %s$ (giờ).''' 
                           % (N, 
                              half_N, q1_idx, L1, L1+1, L1, N, cf_before1, f_Q1, q1_frac_str, q1_round_str,
                              right_start, right_start + 1, N,
                              q3_idx, L3, L3+1, L3, N, cf_before3, f_Q3, q3_frac_str, q3_round_str,
                              kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                       '\\choice \n'
                       '{'+str(list_1[0])+'}\n'
                       '{'+str(list_1[1])+'}\n'
                       '{'+str(list_1[2])+'}\n'
                       '{'+str(list_1[3])+'}\n'
                       '\\loigiai{'+str(loigiai)+'}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

