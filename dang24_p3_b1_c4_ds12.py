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


def bt_dang24_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Bước 3: Suy nghĩ tìm cách random bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số đề bài
                # Tỷ lệ sản phẩm lỗi (2% -> 1-4%)
                p_loi_val = random.randint(1, 4) 
                p_a = Rational(p_loi_val, 100)
                p_not_a = 1 - p_a

                # Hệ thống 1: Phát hiện đúng (95% -> 90-98%), Báo nhầm (1% -> 1-3%)
                p1_dung_val = random.randint(90, 98)
                p1_nham_val = random.randint(1, 3)
                p_m_a = Rational(p1_dung_val, 100)
                p_m_not_a = Rational(p1_nham_val, 100)

                # Hệ thống 2: Phát hiện đúng (90% -> 85-95%), Báo nhầm (5% -> 4-6%)
                p2_dung_val = random.randint(85, 95)
                p2_nham_val = random.randint(4, 6)
                p_n_a = Rational(p2_dung_val, 100)
                p_n_not_a = Rational(p2_nham_val, 100)

                # Tính toán các thành phần xác suất
                # P(not A * M * N) = P(not A) * P(M|not A) * P(N|not A)
                p_not_amn = p_not_a * p_m_not_a * p_n_not_a

                # P(A * M * N) = P(A) * P(M|A) * P(N|A)
                p_amn = p_a * p_m_a * p_n_a

                # Xác suất điều kiện: P(not A | MN) = P(not A * M * N) / (P(A * M * N) + P(not A * M * N))
                p_final = p_not_amn / (p_amn + p_not_amn)

                # Làm tròn đến hàng phần nghìn (3 chữ số thập phân)
                val_float = float(p_final)
                val_rounded = Decimal(str(val_float)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                # Định dạng kết quả 0,0ab để lấy a và b
                # Ví dụ 0.028 -> a=2, b=8
                str_val = "{:.3f}".format(val_rounded)
                # Lấy chữ số thứ 2 và thứ 3 sau dấu phẩy (vị trí 3 và 4 trong chuỗi "0.0ab")
                a = int(str_val[3])
                b = int(str_val[4])
                kq_dung = a + b

                # Bước 4: Điều chỉnh các phương án sai
                s = set()
                while len(s) < 3:
                    sai = kq_dung + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    if sai != kq_dung and sai > 0:
                        s.add(sai)

                list_sai = list(s)
                da_d = '\\True ' + str(kq_dung)
                da_s1 = str(list_sai[0])
                da_s2 = str(list_sai[1])
                da_s3 = str(list_sai[2])

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Câu hỏi
                noidungcauhoi = (
                    'Một nhà máy sản xuất sản phẩm A có tỷ lệ sản phẩm bị lỗi là %s\\%%. Nhà máy sử dụng hai hệ thống kiểm tra chất lượng độc lập để phát hiện lỗi: \n'
                    'Hệ thống 1: Xác suất phát hiện chính xác sản phẩm lỗi là %s\\%%. Xác suất báo lỗi nhầm trên một sản phẩm không lỗi là %s\\%%. \n'
                    'Hệ thống 2: Xác suất phát hiện chính xác sản phẩm lỗi là %s\\%%. Xác suất báo lỗi nhầm trên một sản phẩm không lỗi là %s\\%%. \n'
                    'Chọn ngẫu nhiên một sản phẩm. Biết rằng sản phẩm này bị cả hai hệ thống kiểm tra đều báo lỗi. '
                    'Tính xác suất để sản phẩm này thực tế không bị lỗi. Kết quả xác suất này sau khi đã làm tròn đến hàng phần nghìn '
                    'là số có dạng $0,0ab$. Giá trị của $a+b$ bằng bao nhiêu?'
                    % (latex(p_loi_val), latex(p1_dung_val), latex(p1_nham_val), latex(p2_dung_val), latex(p2_nham_val))
                )

                # Lời giải chi tiết theo mẫu hình ảnh
                loigiai = (
                    'Gọi $A$ là biến cố chọn được sản phẩm lỗi. \\\\ '
                    'Gọi $M, N$ lần lượt là biến cố hệ thống 1 kết luận sản phẩm lỗi, hệ thống 2 kết luận sản phẩm lỗi. \\\\ '
                    'Ta cần tính xác suất điều kiện: $P(\\bar{A}| MN) = \\frac{P(\\bar{A}MN)}{P(MN)}$. \\\\ '
                    'Ta có $P(A) = %s\\%% = %s \\Rightarrow P(\\bar{A}) = 1 - P(A) = %s$ và: \\\\ '
                    '$P(M|A) = %s\\%% = %s; P(M|\\bar{A}) = %s\\%% = %s$. \\\\ '
                    '$P(N|AM) = P(N|A) = %s\\%% = %s; P(N|\\bar{A}M) = P(N|\\bar{A}) = %s\\%% = %s$ (do hai hệ thống độc lập). \\\\ '
                    'Ta có: $P(MN) = P(AMN \\cup \\bar{A}MN) = P(AMN) + P(\\bar{A}MN)$. \\\\ '
                    'Mặt khác: \\\\ '
                    '$P(\\bar{A}MN) = P(\\bar{A}).P(M|\\bar{A}).P(N|\\bar{A}) = %s \\cdot %s \\cdot %s = %s$. \\\\ '
                    '$P(AMN) = P(A).P(M|A).P(N|A) = %s \\cdot %s \\cdot %s = %s$. \\\\ '
                    'Vậy $P(\\bar{A}| MN) = \\frac{%s}{%s + %s} = \\frac{%s}{%s} \\approx %s$. \\\\ '
                    'Từ kết quả làm tròn $0,0%s%s$, ta có $a = %s, b = %s$. \\\\ '
                    'Suy ra $a + b = %s$.'
                    % (p_loi_val, latex(float(p_a)), latex(float(p_not_a)),
                       p1_dung_val, latex(float(p_m_a)), p1_nham_val, latex(float(p_m_not_a)),
                       p2_dung_val, latex(float(p_n_a)), p2_nham_val, latex(float(p_n_not_a)),
                       latex(float(p_not_a)), latex(float(p_m_not_a)), latex(float(p_n_not_a)), latex(float(p_not_amn)),
                       latex(float(p_a)), latex(float(p_m_a)), latex(float(p_n_a)), latex(float(p_amn)),
                       latex(float(p_not_amn)), latex(float(p_amn)), latex(float(p_not_amn)),
                       latex(p_not_amn), latex(p_amn + p_not_amn), str_val.replace('.', ','),
                       a, b, a, b, kq_dung)
                )
                dapan=' \\shortans[0]{$%s$} '%(kq_dung)

            # Xuất câu trắc nghiệm theo đúng cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

