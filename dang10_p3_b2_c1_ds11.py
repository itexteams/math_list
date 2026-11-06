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


def bt_dang10_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Sàng lọc bộ dữ liệu sao cho kết quả cuối cùng của biểu thức A luôn là SỐ NGUYÊN
                # Các bộ dữ liệu: (chuỗi latex góc, giá trị cos góc, giá trị kết quả dạng chuỗi)
                bo_du_lieu = [
                    ('\\frac{\\pi}{3}', Rational(1, 2), '3'),
                    ('\\frac{\\pi}{2}', 0, '2'),
                    ('\\frac{2\\pi}{3}', Rational(-1, 2), '1'),
                    ('0', 1, '4'),
                    ('\\pi', -1, '0')
                ]

                goc_latex, cos_val, kq_latex = random.choice(bo_du_lieu)

                # Đáp án đúng
                da = '$%s$' % kq_latex

                # Tạo các phương án nhiễu (luôn là số nguyên và không trùng với đáp án đúng)
                s = []
                cac_phuong_an_nhieu = ['0', '1', '2', '3', '4', '5', '-1', '-2']
                for phan_tu in cac_phuong_an_nhieu:
                    val_sai = '$%s$' % phan_tu
                    if val_sai != da and val_sai not in s:
                        s.append(val_sai)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\alpha - \\beta = %s$. Giá trị của biểu thức sau: $A = (\\cos \\alpha + \\cos \\beta)^2 + (\\sin \\alpha + \\sin \\beta)^2$ bằng bao nhiêu?'''
                                 % goc_latex)

                # Các đáp án trắc nghiệm hình thức \choice
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuỗi hiển thị bước tính toán cuối cùng trong lời giải
                if cos_val == Rational(1, 2):
                    buoc_cuoi = '2 + 2 \\cdot \\frac{1}{2} = 3'
                elif cos_val == 0:
                    buoc_cuoi = '2 + 2 \\cdot 0 = 2'
                elif cos_val == Rational(-1, 2):
                    buoc_cuoi = '2 + 2 \\cdot \\left(-\\frac{1}{2}\\right) = 1'
                elif cos_val == 1:
                    buoc_cuoi = '2 + 2 \\cdot 1 = 4'
                else:
                    buoc_cuoi = '2 + 2 \\cdot (-1) = 0'

                # Nội dung lời giải chi tiết từng bước theo nguyên mẫu
                loigiai = ('''$A = \\cos^2 \\alpha + \\cos^2 \\beta + 2\\cos \\alpha \\cos \\beta + \\sin^2 \\alpha + \\sin^2 \\beta + 2\\sin \\alpha \\sin \\beta$ \\\\
                           $= 2 + 2\\cos \\alpha \\cos \\beta + 2\\sin \\alpha \\sin \\beta = 2 + 2\\cos(\\alpha - \\beta) = 2 + 2\\cos %s = %s$.'''
                           % (goc_latex, buoc_cuoi))

                dapan = '\\shortans[0]{$%s$}\n' % (str(kq_latex))

            # Xuất câu trắc nghiệm (Tùy chỉnh chọn mẫu hiển thị tự luận ngắn hoặc trắc nghiệm 4 lựa chọn)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

