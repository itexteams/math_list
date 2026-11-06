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


def bt_dang46_p4_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random dấu của vế phải để tạo ra 2 bài toán khác nhau
                # Loai 1: vế phải là -sqrt(2) (Bài gốc)
                # Loai 2: vế phải là sqrt(2)
                loai = random.choice([1, 2])

                if loai == 1:
                    vp_goc = '-\\sqrt{2}'
                    vp_rut_gon = '-\\frac{\\sqrt{2}}{2}'
                    phi_goc = -pi/4

                    # Họ nghiệm chính xác: 8x = -pi/4 + k2pi hoặc 8x = 5pi/4 + k2pi
                    # => x = -pi/32 + kpi/4 hoặc x = 5pi/32 + kpi/4
                    t1 = latex(Rational(-1, 32)) + '\\pi'
                    t2 = latex(Rational(5, 32)) + '\\pi'

                    da_str = '\\left[ \\begin{aligned} & x = -\\frac{\\pi}{32} + k\\frac{\\pi}{4} \\\\ & x = \\frac{5\\pi}{32} + k\\frac{\\pi}{4} \\end{aligned} \\right. \\quad (k \\in \\mathbb{Z})'

                    # Các phương án sai
                    s = [
                        '\\left[ \\begin{aligned} & x = \\frac{\\pi}{32} + k\\frac{\\pi}{4} \\\\ & x = -\\frac{5\\pi}{32} + k\\frac{\\pi}{4} \\end{aligned} \\right. \\quad (k \\in \\mathbb{Z})',
                        '\\left[ \\begin{aligned} & x = \\frac{\\pi}{16} + k\\frac{\\pi}{8} \\\\ & x = \\frac{3\\pi}{16} + k\\frac{\\pi}{8} \\end{aligned} \\right. \\quad (k \\in \\mathbb{Z})',
                        '\\left[ \\begin{aligned} & x = \\frac{\\pi}{8} + k\\frac{\\pi}{8} \\\\ & x = \\frac{3\\pi}{8} + k\\frac{\\pi}{8} \\end{aligned} \\right. \\quad (k \\in \\mathbb{Z})'
                    ]
                else:
                    vp_goc = '\\sqrt{2}'
                    vp_rut_gon = '\\frac{\\sqrt{2}}{2}'
                    phi_goc = pi/4

                    # Họ nghiệm chính xác: 8x = pi/4 + k2pi hoặc 8x = 3pi/4 + k2pi
                    # => x = pi/32 + kpi/4 hoặc x = 3pi/32 + kpi/4
                    t1 = '\\frac{\\pi}{32}'
                    t2 = '\\frac{3\\pi}{32}'

                    da_str = '\\left[ \\begin{aligned} & x = \\frac{\\pi}{32} + k\\frac{\\pi}{4} \\\\ & x = \\frac{3\\pi}{32} + k\\frac{\\pi}{4} \\end{aligned} \\right. \\quad (k \\in \\mathbb{Z})'

                    # Các phương án sai
                    s = [
                        '\\left[ \\begin{aligned} & x = -\\frac{\\pi}{32} + k\\frac{\\pi}{4} \\\\ & x = \\frac{5\\pi}{32} + k\\frac{\\pi}{4} \\end{aligned} \\right. \\quad (k \\in \\mathbb{Z})',
                        '\\left[ \\begin{aligned} & x = \\frac{\\pi}{16} + k\\frac{\\pi}{8} \\\\ & x = \\frac{3\\pi}{16} + k\\frac{\\pi}{8} \\end{aligned} \\right. \\quad (k \\in \\mathbb{Z})',
                        '\\left[ \\begin{aligned} & x = \\frac{\\pi}{8} + k\\frac{\\pi}{8} \\\\ & x = \\frac{3\\pi}{8} + k\\frac{\\pi}{8} \\end{aligned} \\right. \\quad (k \\in \\mathbb{Z})'
                    ]

                da = '$%s$' % da_str

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Giải phương trình $8 \\cdot \\cos 2x \\cdot \\sin 2x \\cdot \\cos 4x = %s$.'''
                                 % (vp_goc))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết trình bày từng bước theo bản gốc
                loigiai = ('''Ta có: \\\\
                           $8 \\cdot \\cos 2x \\cdot \\sin 2x \\cdot \\cos 4x = %s \\Leftrightarrow 4 \\cdot \\sin 4x \\cdot \\cos 4x = %s \\Leftrightarrow 2 \\cdot \\sin 8x = %s \\Leftrightarrow \\sin 8x = %s$ \\\\
                           $\\Leftrightarrow \\sin 8x = \\sin \\left( %s \\right) \\Leftrightarrow \\left[ \\begin{aligned} & x = %s + k\\frac{\\pi}{4} \\\\ & x = %s + k\\frac{\\pi}{4} \\end{aligned} \\right. \\quad (k \\in \\mathbb{Z})$. \\\\
                           Vậy phương trình có nghiệm $%s$.'''
                           % (vp_goc, vp_goc, vp_goc, vp_rut_gon,
                              latex(phi_goc), t1, t2, da_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

