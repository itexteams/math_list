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


def bt_dang21_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Hệ số gốc của bài toán thực tế đảm bảo cực đại tại t = 270 là 55740 con
                # Giải hệ: 540*b + c = 729 và 72900*b + 270*c = 109350 -> b = 2, c = -351
                b_val = 2
                c_val = -351

                # Danh sách các ngày ngẫu nhiên để hỏi ở cuối bài (Ngày hỏi, Số ngày t tương ứng trong năm 2024)
                # Tháng 10 có 244 + 30 = 274 ngày trước đó. Tháng 11 có 244 + 30 + 31 = 305 ngày trước đó.
                list_ngay = [
                    ('15/10/2024', 244 + 31 + 15), # t = 290
                    ('25/10/2024', 244 + 31 + 25), # t = 300
                    ('05/11/2024', 244 + 31 + 30 + 5), # t = 310
                    ('15/11/2024', 244 + 31 + 30 + 15), # t = 320
                    ('25/11/2024', 244 + 31 + 30 + 25), # t = 330 (Gốc)
                    ('05/12/2024', 244 + 31 + 30 + 31 + 5) # t = 341
                ]

                ngay_hoi, t2 = random.choice(list_ngay)

                # Tính số lượng cá thể tại ngày t2 (đơn vị: con)
                f_t2 = -1/300 * (t2**3) + b_val * (t2**2) + c_val * t2 + 12000

                # Đổi sang đơn vị "nghìn con"
                f_t2_nghin = f_t2 / 1000.0

                # Làm tròn đến hàng phần chục (hàng phần mười)
                kq3 = Decimal(str(f_t2_nghin)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$ nghìn con' % (kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu quanh đáp án đúng
                kq_float = float(kq3)
                s_candidates = [
                    round(kq_float + 4.2, 1),
                    round(kq_float + 8.5, 1),
                    round(kq_float - 5.3, 1) if kq_float > 10 else round(kq_float + 12.1, 1),
                    round(kq_float - 9.1, 1) if kq_float > 15 else round(kq_float + 15.4, 1),
                    round(f_t2 / 1000.0 + 2.0, 1),
                    round(55740 / 1000.0, 1)
                ]

                s = []
                for val in s_candidates:
                    val_str = str(val).replace('.', ',')
                    s.append('$%s$ nghìn con' % (val_str))

                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi sử dụng %s
                noidungcauhoi = ('''Trong khoảng thời gian từ ngày 01/01/2024 đến hết ngày 30/12/2024 nhóm nghiên cứu đã quan sát sự phát triển của một quần thể sinh vật X. Kết quả nghiên cứu chỉ ra rằng, tại ngày thứ $t$ của năm 2024 (tính từ ngày 01/01/2024) số cá thể sinh vật X trong quần thể được ước lượng bởi hàm số $f(t) = -\\frac{1}{300}t^3 + bt^2 + ct + 12\\,000$ (con), $0 \\le t \\le 365$ và ngày 26/09/2024 là ngày có số lượng cá thể sinh vật X nhiều nhất với $55\\,740$ con. Ngày %s số lượng cá thể sinh vật X được ước lượng khoảng bao nhiêu nghìn con? (Kết quả làm tròn đến hàng phần chục).'''
                                 % (ngay_hoi))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính toán các giá trị trung gian phục vụ chuỗi lời giải chi tiết
                f_t2_int = int(round(f_t2))

                # Nội dung lời giải chi tiết từng bước theo định dạng bắt buộc
                loigiai = ('''Năm 2024 là năm nhuận nên tháng 2 có $29$ ngày.\\\\
                           Số ngày tính từ ngày 01/01/2024 đến ngày 26/09/2024 là:\\\\
                           $31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 26 = 270$ ngày.\\\\
                           Do đó, ngày 26/09/2024 tương ứng với $t = 270$.\\\\
                           Theo giả thiết, tại ngày $t = 270$ số lượng cá thể đạt nhiều nhất (đạt cực đại) nên điểm $t = 270$ là điểm cực đại của hàm số $f(t)$.\\\\
                           Ta có đạo hàm: $f\'(t) = -\\frac{1}{100}t^2 + 2bt + c$.\\\\
                           Vì hàm số đạt cực đại tại $t = 270$ nên $f\'(270) = 0$ và $f(270) = 55\\,740$, ta có hệ phương trình:\\\\
                           $$\\left\\{\\begin{aligned} & f\'(270) = 0 \\\\ & f(270) = 55\\,740 \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} & -\\frac{1}{100} \\cdot 270^2 + 2b \\cdot 270 + c = 0 \\\\ & -\\frac{1}{300} \\cdot 270^3 + b \\cdot 270^2 + c \\cdot 270 + 12\\,000 = 55\\,740 \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} & 540b + c = 729 \\\\ & 72\\,900b + 270c = 109\\,350 \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} & b = 2 \\\\ & c = -351 \\end{aligned}\\right.$$\\\\
                           Suy ra hàm số cần tìm là: $f(t) = -\\frac{1}{300}t^3 + 2t^2 - 351t + 12\\,000$.\\\\
                           Số ngày tính từ ngày 01/01/2024 đến ngày %s là $%s$ ngày, tương ứng với $t = %s$.\\\\
                           Số lượng cá thể sinh vật X tại ngày $t = %s$ là:\\\\
                           $f(%s) = -\\frac{1}{300} \\cdot %s^3 + 2 \\cdot %s^2 - 351 \\cdot %s + 12\\,000 \\approx %s$ (con).\\\\
                           Đổi sang đơn vị nghìn con và làm tròn đến hàng phần chục ta được:\\\\
                           $\\frac{%s}{1000} \\approx %s$ nghìn con.\\\\
                           Vậy số lượng cá thể sinh vật X được ước lượng khoảng $%s$ nghìn con.'''
                           % (ngay_hoi, latex(t2), latex(t2), latex(t2),
                              latex(t2), latex(t2), latex(t2), latex(t2), str(f_t2_int),
                              str(f_t2_int), kq, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

