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


def bt_dang30_p1_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                n = 10
                # Random 10 cân nặng (từ 2.500 kg đến 4.500 kg)
                # Dùng chuỗi và Decimal để tránh sai số dấu phẩy động
                data_raw = [Decimal(str(randint(2500, 4500))) / Decimal('1000') for _ in range(n)]

                # Tạo chuỗi cho bảng dữ liệu đề bài (2 dòng, 5 cột)
                table_vals = [str(val).replace('.', ',') for val in data_raw]
                row1 = " & ".join(table_vals[:5])
                row2 = " & ".join(table_vals[5:])

                bang_du_lieu = ('''\\begin{center}
                \\begin{tabular}{|c|c|c|c|c|}
                \\hline
                %s \\\\
                \\hline
                %s \\\\
                \\hline
                \\end{tabular}
                \\end{center}''' % (row1, row2))

                # Sắp xếp mảng để xử lý tính toán Toán học
                data_sorted = sorted(data_raw)
                sorted_vals = [str(val).replace('.', ',') for val in data_sorted]
                sorted_str = " \\quad ".join(sorted_vals)

                # Tính Q2 (Trung bình cộng của phần tử thứ 5 và thứ 6)
                q2_val = (data_sorted[4] + data_sorted[5]) / Decimal('2')
                q2_str = str(q2_val.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP).normalize()).replace('.', ',')

                # Tính Q1, Q3 (Theo chuẩn Toán SGK: nửa trái 5 phần tử, nửa phải 5 phần tử)
                q1_val = data_sorted[2]
                q3_val = data_sorted[7]
                q1_str = str(q1_val).replace('.', ',')
                q3_str = str(q3_val).replace('.', ',')

                left_half_str = "; ".join(sorted_vals[:5])
                right_half_str = "; ".join(sorted_vals[5:])

                # Tính Khoảng tứ phân vị Delta Q
                delta_q_val = q3_val - q1_val
                delta_q_str_full = str(delta_q_val).replace('.', ',')

                # Kết quả làm tròn đến hàng phần mười
                kq_round = delta_q_val.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_round).replace('.', ',')

                # Các đáp án trắc nghiệm nhiễu
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = [
                    '$%s$' % str(kq_round + Decimal('0.1')).replace('.', ','),
                    '$%s$' % str(kq_round - Decimal('0.1')).replace('.', ','),
                    '$%s$' % str(kq_round + Decimal('0.2')).replace('.', ','),
                    '$%s$' % str(kq_round - Decimal('0.2')).replace('.', ','),
                    '$%s$' % str(kq_round + Decimal('1.0')).replace('.', ','),
                    '$%s$' % str(kq_round - Decimal('1.0')).replace('.', ',')
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Mẫu số liệu sau đây cho biết cân nặng của $%s$ trẻ sơ sinh (đơn vị kg)
                %s
                Khoảng tứ phân vị của mẫu số liệu này \\textit{Kết quả làm tròn đến hàng phần mười} bằng''' % (n, bang_du_lieu))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Đã chuẩn hóa logic Toán)
                loigiai = ('''Sắp xếp cân nặng theo thứ tự không giảm ta được: \\\\
                %s \\\\
                Mẫu số liệu này gồm $10$ giá trị, có hai phần tử chính giữa là $%s$ và $%s$. Do đó \\\\
                $Q_2 = \\frac{%s + %s}{2} = %s$. \\\\
                Nửa số liệu bên trái là $%s$ gồm $5$ giá trị, phần tử chính giữa là $%s$. Do đó $Q_1 = %s$. \\\\
                Nửa số liệu bên phải là $%s$ gồm $5$ giá trị, phần tử chính giữa là $%s$. Do đó $Q_3 = %s$. \\\\
                Vậy khoảng tứ phân vị là $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s \\approx %s$.''' % (
                    sorted_str,
                    sorted_vals[4], sorted_vals[5],
                    sorted_vals[4], sorted_vals[5], q2_str,
                    left_half_str, sorted_vals[2], q1_str,
                    right_half_str, sorted_vals[7], q3_str,
                    q3_str, q1_str, delta_q_str_full, kq
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


