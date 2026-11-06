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


def bt_dang57_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random đoạn xét nghiệm để tạo ra các câu hỏi có số lượng nghiệm khác nhau
                loai_doan = random.choice([1, 2, 3])

                if loai_doan == 1:
                    # Bài toán gốc: đoạn [0; pi/2]
                    doan_latex = "\\left[0; \\frac{\\pi}{2}\\right]"
                    tap_nghiem_latex = "\\left\\{0; \\frac{\\pi}{2}\\right\\}"
                    kq = "2"
                    s = ['$4$', '$3$', '$1$', '$0$', '$5$']
                elif loai_doan == 2:
                    # Đoạn [0; pi]
                    doan_latex = "\\left[0; \\pi\\right]"
                    tap_nghiem_latex = "\\left\\{0; \\frac{\\pi}{2}\\right\\}"
                    kq = "2"
                    s = ['$4$', '$3$', '$1$', '$0$', '$5$']
                else:
                    # Đoạn [-pi/2; pi/2]
                    doan_latex = "\\left[-\\frac{\\pi}{2}; \\frac{\\pi}{2}\\right]"
                    tap_nghiem_latex = "\\left\\{0; \\frac{\\pi}{2}\\right\\}" # Nghiệm vẫn là 0 và pi/2 vì các nghiệm k2pi và pi/2 + k2pi nằm ngoài các điểm khác
                    kq = "2"
                    s = ['$4$', '$3$', '$1$', '$0$', '$5$']

                # Đáp án đúng
                du = ['$%s$' % kq]
                da = random.choice(du)

                # Loại bỏ các đáp án trùng với đáp án đúng trong tập nhiễu
                s_filtered = [item for item in s if item != ('$%s$' % kq)]
                das1 = random.choice(s_filtered)
                s_filtered.remove(das1)
                das2 = random.choice(s_filtered)
                s_filtered.remove(das2)
                das3 = random.choice(s_filtered)

                # Câu hỏi sử dụng định dạng %s
                noidungcauhoi = ('''Số nghiệm trên đoạn $%s$ của phương trình $\\sin^3 x + \\sin x \\cos x = 1 - \\cos^3 x$ là'''
                                 % (doan_latex))

                # Các đáp án không thêm dấu chấm ở cuối
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước, xuống dòng bằng \\\\
                loigiai = ('''$\\sin^3 x + \\sin x \\cos x = 1 - \\cos^3 x \\Leftrightarrow \\sin^3 x + \\cos^3 x = 1 - \\sin x \\cos x$ \\\\
            $\\Leftrightarrow (\\sin x + \\cos x)(1 - \\sin x \\cos x) = 1 - \\sin x \\cos x$ \\\\
            $\\Leftrightarrow \\begin{bmatrix} 1 - \\sin x \\cos x = 0 \\\\ \\sin x + \\cos x = 1 \\end{bmatrix}$ \\\\
            $\\Leftrightarrow \\begin{bmatrix} \\sin 2x = 2 \\text{ (Vô nghiệm)} \\\\ \\sin\\left(x + \\frac{\\pi}{4}\\right) = \\frac{1}{\\sqrt{2}} \\end{bmatrix} \\Leftrightarrow \\begin{bmatrix} x = k2\\pi \\\\ x = \\frac{\\pi}{2} + k2\\pi \\end{bmatrix}, k \\in \\mathbb{Z}$. \\\\
            Vì $x \\in %s \\Rightarrow x \\in %s$. \\\\
            Vậy có %s nghiệm.'''
                           % (doan_latex, tap_nghiem_latex, kq))

            # Xuất câu trắc nghiệm đúng cấu trúc mẫu
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

