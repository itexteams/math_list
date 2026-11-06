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


def bt_dang54_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random vế phải của phương trình là số chính phương (4 hoặc 9)
                vp_so = random.choice([4, 9])

                if vp_so == 9:
                    vp_latex = "9"
                    tan_val = "\\pm\\sqrt{3}"
                    nghiem_dung = "x = \\pm\\frac{\\pi}{3} + k\\pi"

                    # Danh sách phương án nhiễu (không chứa dấu chấm ở cuối)
                    s = [
                        '$x = \\pm\\frac{\\pi}{3} + k2\\pi$',
                        '$x = \\pm\\frac{\\pi}{6} + k\\pi$',
                        '$x = \\pm\\frac{\\pi}{6} + k2\\pi$',
                        '$x = \\frac{\\pi}{3} + k\\pi$',
                        '$x = -\\frac{\\pi}{3} + k\\pi$'
                    ]
                else:
                    vp_latex = "4"
                    tan_val = "\\pm\\sqrt{2}"
                    nghiem_dung = "x = \\pm\\arctan(\\sqrt{2}) + k\\pi"

                    s = [
                        '$x = \\pm\\arctan(\\sqrt{2}) + k2\\pi$',
                        '$x = \\pm\\frac{\\pi}{4} + k\\pi$',
                        '$x = \\pm\\frac{\\pi}{3} + k\\pi$',
                        '$x = \\arctan(\\sqrt{2}) + k\\pi$',
                        '$x = -\\arctan(\\sqrt{2}) + k\\pi$'
                    ]

                # Đáp án đúng
                du = ['$%s$' % nghiem_dung]
                da = random.choice(du)

                # Lấy ngẫu nhiên các đáp án sai và loại bỏ để không trùng nhau
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Phương trình $\\frac{\\sin^2 x - \\cos^2 x + \\cos^4 x}{\\cos^2 x - \\sin^2 x + \\sin^4 x} = %s$ có nghiệm là'''
                                 % (vp_latex))

                # Các đáp án mang cấu trúc trắc nghiệm chuẩn
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết, dùng \\\\ khi xuống dòng
                loigiai = ('''Điều kiện: $\\cos^2 x - \\sin^2 x + \\sin^4 x \\neq 0 \\Leftrightarrow x \\neq \\frac{\\pi}{2} + k\\pi$ \\\\
            Ta có $\\frac{\\sin^2 x - \\cos^2 x + \\cos^4 x}{\\cos^2 x - \\sin^2 x + \\sin^4 x} = %s \\Leftrightarrow \\frac{1 - 2\\cos^2 x + \\cos^4 x}{1 - 2\\sin^2 x + \\sin^4 x} = %s$ \\\\
            $\\Leftrightarrow \\frac{(1 - \\cos^2 x)^2}{(1 - \\sin^2 x)^2} = %s \\Leftrightarrow \\frac{\\sin^4 x}{\\cos^4 x} = %s \\Leftrightarrow \\tan^4 x = %s \\Leftrightarrow \\tan x = %s \\Leftrightarrow %s$ (thỏa mãn điều kiện).'''
                           % (vp_latex, vp_latex, vp_latex, vp_latex, vp_latex, tan_val, nghiem_dung))

            # Xuất câu trắc nghiệm định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

