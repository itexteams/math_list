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


def bt_dang45_p3_b1_c3_ds12(self):
            # Khai báo biến
            # ==========================================

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tham số
                n = random.randint(1, 5)        # f(0) = n
                m_half = random.randint(2, 5)   # b = m/2
                m = 2 * m_half                  # Hệ số mũ m trong đề bài

                # Tính k dựa trên n và m để C = 0 (giống hệt cấu trúc bài mẫu)
                # k = (m-2)/2 * n^2
                k_val = (m - 2) // 2 * (n**2)

                # Các giá trị a, b
                val_a = n
                val_b = m_half

                # Đáp án đúng
                kq = val_a + val_b

                # B4: Tạo các phương án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = kq + random.choice([-2, -1, 1, 2, 3, 4])
                    if sai != kq and sai > 0:
                        s.add(f'${sai}$')

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                da_d = '\\True ' + f'${kq}$'

                # Nội dung câu hỏi
                noidungcauhoi = (
                    f'Cho hàm số $y = f(x)$ có đạo hàm liên tục trên $\\mathbb{{R}}$ và $f(x) > 0, \\forall x \\in \\mathbb{{R}}$, '
                    f'đồng thời thỏa mãn $f(x) \\cdot f\'(x) - [f(x)]^2 = {k_val}e^{{{m}x}}, \\forall x \\in \\mathbb{{R}}$. '
                    f'Biết $f(0) = {n}$ và $f(1) = a \\cdot e^b$ với $a, b \\in \\mathbb{{Z}}$. Giá trị $a + b$ bằng bao nhiêu?'
                )

                # Nội dung lời giải chi tiết (B2: Viết lại y hệt logic mẫu)
                k2 = 2 * k_val
                m_minus_2 = m - 2
                loigiai = (
                    f'$f(x) \\cdot f\'(x) - [f(x)]^2 = {k_val}e^{{{m}x}} \\Leftrightarrow 2e^{{-2x}} \\left[ f(x) \\cdot f\'(x) - f^2(x) \\right] = {k2}e^{{{m_minus_2}x}}$ \\\\\n'
                    f'$\\Leftrightarrow \\left[ e^{{-2x}} \\cdot f^2(x) \\right]\' = {k2}e^{{{m_minus_2}x}} \\Rightarrow e^{{-2x}} \\cdot f^2(x) = \\frac{{{k2}}}{{{m_minus_2}}} e^{{{m_minus_2}x}} + C = {n**2}e^{{{m_minus_2}x}} + C.$ \\\\\n'
                    f'$f(0) = {n} \\Rightarrow e^0 \\cdot f^2(0) = {n**2}e^0 + C \\Rightarrow {n**2} = {n**2} + C \\Rightarrow C = 0.$ \\\\\n'
                    f'$f(1) = a \\cdot e^b \\Rightarrow e^{{-2}} \\cdot f^2(1) = {n**2}e^{{{m_minus_2}}} \\Rightarrow f^2(1) = {n**2}e^{{{m}}} \\Rightarrow f(1) = {n}e^{{{m_half}}}.$ \\\\\n'
                    f'Vậy $a = {val_a}, b = {val_b} \\Rightarrow a + b = {kq}.$'
                )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq)) 

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Xuất câu trắc nghiệm theo định dạng yêu cầu
                content = (
                    '\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                    '\\loigiai{' + str(loigiai) + '}\n'
                    '\\end{ex}\n \\end{minipage} \n\n' )
            return content  

