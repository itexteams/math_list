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


def bt_dang35_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                A = random.randint(2, 9)            # Hệ số gốc là 5
                B = random.randint(-9, 9)           # Hệ số gốc là -2
                while B == 0: B = random.randint(-9, 9)

                a_root = random.randint(-5, 5)      # Nghiệm a mong muốn
                K = A * a_root + 2 * A + B          # Giá trị K ở vế phải g(a)+g'(a)=K

                # Biểu thức trong đề bài
                expr_integral = (A*symbols('x') + B)

                # --- B4: Điều chỉnh phương án sai ---
                kq = a_root
                s = set()
                while len(s) < 3:
                    sai = kq + random.choice([-3, -2, -1, 1, 2, 3])
                    if sai != kq:
                        s.add(f'${latex(sai)}$')

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]
                da_dung = f'${latex(kq)}$'

                # --- B2: Viết lại nội dung câu hỏi ---
                noidungcauhoi = (f"Cho hàm số $f(x), g(x)$ liên tục trên tập $\\mathbb{{R}}$, trong đó $f(x) > 0 (\\forall x \\in \\mathbb{{R}})$. Biết rằng "
                                 f"$\\int f(x) \\text{{d}} x = f(x) + C$ và $\\int f(x) \\cdot g(x) \\text{{d}} x = ({latex(expr_integral)}) \\cdot f(x) + C$. "
                                 f"Số thực $a$ thỏa mãn $g(a) + g'(a) = {K}$ bằng bao nhiêu?")

                # Các đáp án
                da_d = '\\True ' + da_dung
                da_s1 = das1
                da_s2 = das2 
                da_s3 = das3 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải chi tiết ---
                loigiai = (f"Ta có $\\int f(x) \\text{{d}} x = f(x) + C \\Rightarrow f(x) = f'(x)$.\\\\ "
                           f"Lấy đạo hàm hai vế của đẳng thức thứ hai:\\\\ "
                           f"$\\int f(x) \\cdot g(x) \\text{{d}} x = ({latex(expr_integral)}) \\cdot f(x) + C \\Rightarrow f(x) \\cdot g(x) = [({latex(expr_integral)}) \\cdot f(x)]'$\\\\ "
                           f"$\\Leftrightarrow f(x) \\cdot g(x) = {A} \\cdot f(x) + ({latex(expr_integral)}) \\cdot f'(x)$\\\\ "
                           f"Vì $f(x) = f'(x)$ nên:\\\\ "
                           f"$\\Leftrightarrow f(x) \\cdot g(x) = {A} \\cdot f(x) + ({latex(expr_integral)}) \\cdot f(x)$\\\\ "
                           f"$\\Leftrightarrow f(x) \\cdot g(x) = f(x) \\cdot ({A} + {latex(expr_integral)})$\\\\ "
                           f"$\\Leftrightarrow g(x) = {latex(simplify(A + expr_integral))}$ (vì $f(x) > 0$).\\\\ "
                           f"Suy ra $g'(x) = {A}$.\\\\ "
                           f"Theo giả thiết: $g(a) + g'(a) = {K} \\Leftrightarrow ({A}a + {A+B}) + {A} = {K}$\\\\ "
                           f"$\\Leftrightarrow {A}a + {2*A+B} = {K} \\Leftrightarrow {A}a = {K - (2*A+B)} \\Leftrightarrow a = {kq}$.")
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

