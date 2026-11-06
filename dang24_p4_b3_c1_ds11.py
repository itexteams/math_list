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


def bt_dang24_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số của cot(ax) để tạo nhiều câu hỏi khác nhau. Trong hình mẫu, a = 2.
                # Ta chọn ngẫu nhiên a là một số chẵn từ 2 đến 6 để giữ đúng bản chất gộp nghiệm đẹp mắt.
                a = random.choice([2, 4, 6])

                # Điều kiện xác định: sin(ax) != 0 và cos(x) != 0
                # sin(ax) != 0 <=> ax != k*pi <=> x != k*pi/a
                # cos(x) != 0 <=> x != pi/2 + k*pi
                # Với a chẵn, họ nghiệm x != k*pi/a đã bao hàm cả họ nghiệm x != pi/2 + k*pi

                # Chuỗi Latex hiển thị hàm số
                ham_so = 'y = \\cot %sx - \\tan x' % (latex(a))

                # Chuỗi đáp án đúng
                da_dung = '\\mathbb{R} \\setminus \\{k\\frac{\\pi}{%s}, k \\in \\mathbb{Z}\\}' % (latex(a))

                # Các đáp án nhiễu (đảm bảo không trùng đáp án đúng bằng cách lấy các giá trị khác mẫu số)
                s = [
                    '\\mathbb{R} \\setminus \\{\\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}\\}',
                    '\\mathbb{R} \\setminus \\{k\\pi, k \\in \\mathbb{Z}\\}',
                    '\\mathbb{R} \\setminus \\{\\frac{\\pi}{4} + k\\frac{\\pi}{2}, k \\in \\mathbb{Z}\\}',
                    '\\mathbb{R} \\setminus \\{k2\\pi, k \\in \\mathbb{Z}\\}',
                    '\\mathbb{R} \\setminus \\{\\frac{\\pi}{%s} + k\\pi, k \\in \\mathbb{Z}\\}' % (latex(a))
                ]

                # Loại bỏ phần tử nếu lỡ trùng với đáp án đúng để tránh trùng lặp
                if da_dung in s:
                    s.remove(da_dung)

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi
                noidungcauhoi = ('Tìm tập xác định của hàm số $%s$.' % (ham_so))

                # Các đáp án
                da_d = ('\\True $' + str(da_dung) + '$')
                da_s1 = ('$' + str(das1) + '$')
                da_s2 = ('$' + str(das2) + '$')
                da_s3 = ('$' + str(das3) + '$')

                # Đưa vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết, rõ ràng từng bước sử dụng định dạng hệ phương trình như hình gốc
                loigiai = ('''Hàm số xác định khi $\\begin{cases} \\sin %sx \\neq 0 \\\\ \\cos x \\neq 0 \\end{cases} \\Leftrightarrow \\begin{cases} x \\neq k\\frac{\\pi}{%s} \\\\ x \\neq \\frac{\\pi}{2} + k\\pi \\end{cases} \\Leftrightarrow x \\neq k\\frac{\\pi}{%s} (k \\in \\mathbb{Z})$'''
                           % (latex(a), latex(a), latex(a)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

