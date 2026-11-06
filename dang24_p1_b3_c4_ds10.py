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


def bt_dang24_p1_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM THÔNG SỐ CƠ BẢN ---
                a = randint(1, 3) 
                b = randint(a + 1, a + 4) # Đảm bảo b > a

                val_a2 = a**2
                val_b2 = b**2

                # Hệ số phương trình trùng phương: x^4 - (a^2+b^2)x^2 + a^2b^2
                he_so_x2 = -(val_a2 + val_b2)
                he_so_tu_do = val_a2 * val_b2

                # Chuỗi hàm số f(x)
                fx_str = f"x^4 {he_so_x2:+d}x^2 {he_so_tu_do:+d}"

                # Các nghiệm sắp xếp từ bé đến lớn: -b < -a < a < b
                n1, n2, n3, n4 = -b, -a, a, b

                # --- BƯỚC 2: RANDOM DẤU BẤT PHƯƠNG TRÌNH ---
                loai_dau = random.choice([0, 1, 2, 3])

                dau_latex = ""       
                ket_luan_dau = ""    
                da_dung = ""         
                da_nhieu_1 = ""      
                da_nhieu_2 = ""      
                da_nhieu_3 = ""      

                # Cấu trúc dấu ngoặc sử dụng \left \right
                if loai_dau == 0: # Dấu <
                    dau_latex = "<"
                    ket_luan_dau = "<"
                    da_dung = f"$\\left({n1}; {n2}\\right) \\cup \\left({n3}; {n4}\\right)$"
                    da_nhieu_1 = f"$\\left[{n1}; {n2}\\right] \\cup \\left[{n3}; {n4}\\right]$" 
                    da_nhieu_2 = f"$\\left({n1}; {n2}\\right)$"
                    da_nhieu_3 = f"$\\left(-\\infty; {n1}\\right) \\cup \\left({n2}; {n3}\\right) \\cup \\left({n4}; +\\infty\\right)$"

                elif loai_dau == 1: # Dấu >
                    dau_latex = ">"
                    ket_luan_dau = ">"
                    da_dung = f"$\\left(-\\infty; {n1}\\right) \\cup \\left({n2}; {n3}\\right) \\cup \\left({n4}; +\\infty\\right)$"
                    da_nhieu_1 = f"$\\left(-\\infty; {n1}\\right] \\cup \\left[{n2}; {n3}\\right] \\cup \\left[{n4}; +\\infty\\right]$"
                    da_nhieu_2 = f"$\\left({n1}; {n2}\\right) \\cup \\left({n3}; {n4}\\right)$"
                    da_nhieu_3 = f"$\\mathbb{{R}} \\setminus \\left\\{{ {n1}; {n2}; {n3}; {n4} \\right\\}}$"

                elif loai_dau == 2: # Dấu <=
                    dau_latex = "\\le"
                    ket_luan_dau = "\\le"
                    da_dung = f"$\\left[{n1}; {n2}\\right] \\cup \\left[{n3}; {n4}\\right]$"
                    da_nhieu_1 = f"$\\left({n1}; {n2}\\right) \\cup \\left({n3}; {n4}\\right)$"
                    da_nhieu_2 = f"$\\left[{n2}; {n3}\\right]$"
                    da_nhieu_3 = f"$\\left(-\\infty; {n1}\\right] \\cup \\left[{n2}; {n3}\\right] \\cup \\left[{n4}; +\\infty\\right]$"

                elif loai_dau == 3: # Dấu >=
                    dau_latex = "\\ge"
                    ket_luan_dau = "\\ge"
                    da_dung = f"$\\left(-\\infty; {n1}\\right] \\cup \\left[{n2}; {n3}\\right] \\cup \\left[{n4}; +\\infty\\right]$"
                    da_nhieu_1 = f"$\\left(-\\infty; {n1}\\right) \\cup \\left({n2}; {n3}\\right) \\cup \\left({n4}; +\\infty\\right)$"
                    da_nhieu_2 = f"$\\left[{n1}; {n2}\\right] \\cup \\left[{n3}; {n4}\\right]$"
                    da_nhieu_3 = f"$\\left[{n2}; {n3}\\right]$"

                # --- BƯỚC 3: TRỘN ĐÁP ÁN ---
                du = [da_dung]
                da = random.choice(du)
                s = [da_nhieu_1, da_nhieu_2, da_nhieu_3]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                list_1 = ['\\True ' + str(da), str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # --- BƯỚC 4: NỘI DUNG HIỂN THỊ ---
                noidungcauhoi = ('''Tập nghiệm của bất phương trình $%s %s 0$ là''' % (fx_str, dau_latex))

                # Bảng xét dấu đóng khung hoàn toàn
                bang_xet_dau = r"""\begin{center}
            \begin{tabular}{|c|ccccccccccc|}
            \hline
            $x$ & $-\infty$ & & $%s$ & & $%s$ & & $%s$ & & $%s$ & & $+\infty$ \\ \hline
            $x^2-%s$ & & $+$ & $|$ & $+$ & $|$ & $-$ & $0$ & $+$ & $|$ & $+$ \\ \hline
            $x^2-%s$ & & $+$ & $0$ & $-$ & $|$ & $-$ & $|$ & $-$ & $0$ & $+$ \\ \hline
            $f(x)$ & & $+$ & $0$ & $-$ & $0$ & $+$ & $0$ & $-$ & $0$ & $+$ \\ \hline
            \end{tabular}
            \end{center}""" % (n1, n2, n3, n4, val_a2, val_b2)

                ket_luan_text = da_dung.replace("$", "")

                loigiai = ('''Ta có $%s = (x^2 - %s)(x^2 - %s) = 0 \\Leftrightarrow \\left[ \\begin{aligned} &x^2 = %s \\\\ &x^2 = %s \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} &x = \\pm %s \\\\ &x = \\pm %s \\end{aligned} \\right.$.\\\\
            Đặt $f(x) = %s$.\\\\
            Bảng xét dấu:
            %s
            Dựa vào bảng xét dấu, ta thấy tập nghiệm của bất phương trình $f(x) %s 0$ là $%s$.'''
                % (fx_str, val_a2, val_b2, val_a2, val_b2, a, b, fx_str, bang_xet_dau, ket_luan_dau, ket_luan_text))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

