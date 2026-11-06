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


def bt_dang55_p4_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random vế phải hợp lệ để đưa về phương trình bậc 2 của sin(2x) đẹp
                vp_val = random.choice([Rational(7, 16), Rational(13, 16), Rational(1, 4)])

                if vp_val == Rational(7, 16):
                    vp_latex = "\\frac{7}{16}"
                    hieu_latex = "\\frac{9}{16}"
                    sin2x_val = "\\pm \\frac{\\sqrt{3}}{2}"
                    nghiem_dung = "x = \\pm \\frac{\\pi}{6} + k\\frac{\\pi}{2}"

                    # Lời giải chi tiết nhánh hệ phương trình nghiệm cho bài toán gốc
                    nhanh_nghiem = ('''\\begin{bmatrix} x = \\pm \\frac{\\pi}{6} + k\\pi \\\\ \\\\ x = \\frac{\\pi}{3} + k\\pi \\\\ \\\\ x = \\frac{2\\pi}{3} + k\\pi \\end{bmatrix} \\Leftrightarrow x = \\pm \\frac{\\pi}{6} + k\\frac{\\pi}{2}''')

                    # Các phương án nhiễu (không chứa dấu chấm ở cuối)
                    s = [
                        '$x = \\pm \\frac{\\pi}{3} + k\\frac{\\pi}{2}$',
                        '$x = \\pm \\frac{\\pi}{4} + k\\frac{\\pi}{2}$',
                        '$x = \\pm \\frac{\\pi}{5} + k\\frac{\\pi}{2}$'
                    ]
                elif vp_val == Rational(13, 16):
                    vp_latex = "\\frac{13}{16}"
                    hieu_latex = "\\frac{3}{16}"
                    sin2x_val = "\\pm \\frac{1}{2}"
                    nghiem_dung = "x = \\pm \\frac{\\pi}{12} + k\\frac{\\pi}{2}"
                    nhanh_nghiem = ('''\\begin{bmatrix} x = \\pm \\frac{\\pi}{12} + k\\pi \\\\ \\\\ x = \\pm \\frac{5\\pi}{12} + k\\pi \\end{bmatrix} \\Leftrightarrow x = \\pm \\frac{\\pi}{12} + k\\frac{\\pi}{2}''')

                    s = [
                        '$x = \\pm \\frac{\\pi}{6} + k\\frac{\\pi}{2}$',
                        '$x = \\pm \\frac{\\pi}{4} + k\\frac{\\pi}{2}$',
                        '$x = \\pm \\frac{\\pi}{3} + k\\frac{\\pi}{2}$'
                    ]
                else: # vp_val == Rational(1, 4)
                    vp_latex = "\\frac{1}{4}"
                    hieu_latex = "\\frac{3}{4}"
                    sin2x_val = "\\pm 1"
                    nghiem_dung = "x = \\frac{\\pi}{4} + k\\frac{\\pi}{2}"
                    nhanh_nghiem = ('''2x = \\frac{\\pi}{2} + k\\pi \\Leftrightarrow x = \\frac{\\pi}{4} + k\\frac{\\pi}{2}''')

                    s = [
                        '$x = \\pm \\frac{\\pi}{6} + k\\frac{\\pi}{2}$',
                        '$x = \\pm \\frac{\\pi}{3} + k\\frac{\\pi}{2}$',
                        '$x = \\pm \\frac{\\pi}{4} + k\\pi$'
                    ]

                # Đáp án đúng
                du = ['$%s$' % nghiem_dung]
                da = random.choice(du)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Giải phương trình $\\sin^6 x + \\cos^6 x = %s$.''' % vp_latex)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $\\sin^6 x + \\cos^6 x = %s \\Leftrightarrow \\sin^4 x - \\sin^2 x \\cos^2 x + \\cos^4 x = %s$ \\\\
            $\\Leftrightarrow (\\sin^2 x + \\cos^2 x)^2 - 3\\sin^2 x \\cos^2 x = %s \\Leftrightarrow 1 - \\frac{3}{4}\\sin^2 2x = %s$ \\\\
            $\\Leftrightarrow \\frac{3}{4}\\sin^2 2x = %s \\Leftrightarrow \\sin 2x = %s$ \\\\
            $\\Leftrightarrow %s$.''' 
                           % (vp_latex, vp_latex, vp_latex, vp_latex, hieu_latex, sin2x_val, nhanh_nghiem))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

