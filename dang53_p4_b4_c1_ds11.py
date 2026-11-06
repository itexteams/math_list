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


def bt_dang53_p4_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thiết lập ngẫu nhiên vế phải của phương trình
                # Giá trị gốc là 5/8. Có thể chọn giá trị khác như 7/8 để phương trình vẫn cho nghiệm đẹp.
                vp_chon = random.choice([Rational(5, 8), Rational(7, 8)])

                if vp_chon == Rational(5, 8):
                    vp_latex = "\\frac{5}{8}"
                    cos_val_latex = "-\\frac{1}{2}"
                    nghiem_goc = "\\pm \\frac{\\pi}{3} + k\\pi"
                    tap_nghiem = "\\left\\{\\frac{\\pi}{3}; \\frac{2\\pi}{3}; \\frac{4\\pi}{3}; \\frac{5\\pi}{3}\\right\\}"
                    kq = "4\\pi"

                    # Các phương án nhiễu tương ứng với trường hợp 1
                    s = [
                        '\\frac{9\\pi}{8}',
                        '\\frac{12\\pi}{3}',
                        '\\frac{9\\pi}{4}',
                        '2\\pi',
                        '3\\pi'
                    ]
                else:
                    vp_latex = "\\frac{7}{8}"
                    cos_val_latex = "\\frac{1}{2}"
                    nghiem_goc = "\\pm \\frac{\\pi}{6} + k\\pi"
                    tap_nghiem = "\\left\\{\\frac{\\pi}{6}; \\frac{5\\pi}{6}; \\frac{7\\pi}{6}; \\frac{11\\pi}{6}\\right\\}"
                    kq = "4\\pi" # Tổng các nghiệm đối xứng qua pi trên khoảng (0; 2pi) vẫn bằng 4pi

                    # Các phương án nhiễu tương ứng với trường hợp 2
                    s = [
                        '\\frac{5\\pi}{2}',
                        '2\\pi',
                        '\\frac{7\\pi}{3}',
                        '\\frac{11\\pi}{4}',
                        '5\\pi'
                    ]

                # Đáp án đúng
                du = ['$%s$' % kq]
                da = random.choice(du)

                # Chọn phương án sai ngẫu nhiên từ danh sách nhiễu
                s_formatted = ['$%s$' % item for item in s if item != kq]
                das1 = random.choice(s_formatted)
                s_formatted.remove(das1)
                das2 = random.choice(s_formatted)
                s_formatted.remove(das2)
                das3 = random.choice(s_formatted)

                # Câu hỏi sử dụng định dạng %s
                noidungcauhoi = ('''Tính tổng tất cả các nghiệm thuộc khoảng $(0;2\\pi)$ của phương trình $\\sin^4 \\frac{x}{2} + \\cos^4 \\frac{x}{2} = %s$.'''
                                 % (vp_latex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải sử dụng định dạng %s
                loigiai = ('''$\\sin^4 \\frac{x}{2} + \\cos^4 \\frac{x}{2} = %s \\Leftrightarrow \\left(\\sin^2 \\frac{x}{2} + \\cos^2 \\frac{x}{2}\\right)^2 - 2\\sin^2 \\frac{x}{2} \\cdot \\cos^2 \\frac{x}{2} = %s$ \\\\
            $\\Leftrightarrow 1 - \\frac{1}{2}\\sin^2 x = %s \\Leftrightarrow 1 - \\frac{1}{4}(1 - \\cos 2x) = %s \\Leftrightarrow \\cos 2x = %s \\Leftrightarrow x = %s, k \\in \\mathbb{Z}$. \\\\
            Mà $x \\in (0;2\\pi)$ nên $x \\in %s$. \\\\
            Khi đó tổng các nghiệm thuộc khoảng $(0;2\\pi)$ của phương trình là $%s$.'''
                           % (vp_latex, vp_latex, vp_latex, vp_latex, cos_val_latex, nghiem_goc, tap_nghiem, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

