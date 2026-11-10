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


def bt_dang49_p1_b1_c3_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Danh sách các bộ 3 phép đo (a1, d1, a2, d2, a3, d3) chia hết, đẹp, các sai số tương đối khác nhau hoàn toàn
        ds_bo_so = [
            (40, Decimal('0.20'), 120, Decimal('0.48'), 250, Decimal('1.50')),
            (50, Decimal('0.25'), 100, Decimal('0.30'), 200, Decimal('1.00')),
            (60, Decimal('0.36'), 150, Decimal('0.45'), 300, Decimal('1.50')),
            (50, Decimal('0.15'), 125, Decimal('0.50'), 200, Decimal('0.60')),
            (80, Decimal('0.40'), 160, Decimal('0.48'), 240, Decimal('1.44')),
            (40, Decimal('0.16'), 100, Decimal('0.50'), 250, Decimal('0.75')),
            (50, Decimal('0.30'), 120, Decimal('0.36'), 200, Decimal('1.20'))
        ]
        a1, d1, a2, d2, a3, d3 = random.choice(ds_bo_so)
    
        # Tính sai số tương đối cho từng phép đo
        r1 = d1 / Decimal(str(a1))
        r2 = d2 / Decimal(str(a2))
        r3 = d3 / Decimal(str(a3))
    
        pct1 = r1 * Decimal('100')
        pct2 = r2 * Decimal('100')
        pct3 = r3 * Decimal('100')
    
        # Định dạng chuỗi hiển thị dấu phẩy theo chuẩn Việt Nam
        str_a1 = str(a1)
        str_d1 = f"{d1:.2f}".replace('.', ',')
        str_r1 = f"{r1}".replace('.', ',')
        str_pct1 = f"{pct1}".replace('.', ',')
    
        str_a2 = str(a2)
        str_d2 = f"{d2:.2f}".replace('.', ',')
        str_r2 = f"{r2}".replace('.', ',')
        str_pct2 = f"{pct2}".replace('.', ',')
    
        str_a3 = str(a3)
        str_d3 = f"{d3:.2f}".replace('.', ',')
        str_r3 = f"{r3}".replace('.', ',')
        str_pct3 = f"{pct3}".replace('.', ',')
    
        # Tạo bảng biểu diễn LaTeX
        bang_du_lieu = '''\\begin{center}
    \\begin{tabular}{|c|c|}
    \\hline
    \\textbf{Phép đo} & \\textbf{Kết quả} \\\\
    \\hline
    I & $%s \\pm %s$ \\\\
    \\hline
    II & $%s \\pm %s$ \\\\
    \\hline
    III & $%s \\pm %s$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (str_a1, str_d1, str_a2, str_d2, str_a3, str_d3)
    
        # Tìm phép đo có sai số tương đối nhỏ nhất
        min_r = min(r1, r2, r3)
        if min_r == r1:
            phep_do_min = 'Phép đo I'
        elif min_r == r2:
            phep_do_min = 'Phép đo II'
        else:
            phep_do_min = 'Phép đo III'
    
        # Các đáp án trắc nghiệm (không thêm dấu chấm ở cuối phương án)
        da = phep_do_min
        tap_phuong_an = ['Phép đo I', 'Phép đo II', 'Phép đo III', 'Cả ba bằng nhau']
        tap_sai = [p for p in tap_phuong_an if p != da]
    
        das1 = tap_sai[0]
        das2 = tap_sai[1]
        das3 = tap_sai[2]
    
        # Câu hỏi
        noidungcauhoi = ('''Ba phép đo được cho trong bảng:
    %s
    Phép đo có sai số tương đối nhỏ nhất là'''
                         % bang_du_lieu
                         )
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải
        loigiai = ('''Phép đo I: $\\frac{%s}{%s} = %s$, tức $%s$ phần trăm.\\\\
    Phép đo II: $\\frac{%s}{%s} = %s$, tức $%s$ phần trăm.\\\\
    Phép đo III: $\\frac{%s}{%s} = %s$, tức $%s$ phần trăm.\\\\
    Sai số tương đối nhỏ nhất là của %s.'''
                   % (str_d1, str_a1, str_r1, str_pct1,
                      str_d2, str_a2, str_r2, str_pct2,
                      str_d3, str_a3, str_r3, str_pct3,
                      phep_do_min.lower())
                   )
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n'
               '{' + str(list_1[1]) + '}\n'
               '{' + str(list_1[2]) + '}\n'
               '{' + str(list_1[3]) + '}\n'
               '{' + str(list_1[0]) + '}\n'
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
    