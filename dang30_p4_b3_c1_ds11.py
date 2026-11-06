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


def bt_dang30_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số trên tử số để tạo sự đa dạng
                a = random.randint(1, 5)

                # Chọn ngẫu nhiên loại hàm ở mẫu và tập nghiệm tương ứng
                # 0: sin(x) - 1 != 0 -> sin(x) != 1 -> x != \pi/2 + k2\pi
                # 1: sin(x) + 1 != 0 -> sin(x) != -1 -> x != -\pi/2 + k2\pi
                # 2: cos(x) - 1 != 0 -> cos(x) != 1 -> x != k2\pi
                # 3: cos(x) + 1 != 0 -> cos(x) != -1 -> x != \pi + k2\pi
                loai_mau = random.choice([0, 1, 2, 3])

                chuoi_tu = f"{a} - \\cos x" if a != 1 else "1 - \\cos x"

                if loai_mau == 0:
                    chuoi_mau = "\\sin x - 1"
                    pt_mau = "\\sin x - 1 \\neq 0"
                    pt_he_qua = "\\sin x \\neq 1"
                    nghiem_bpt = "x \\neq \\frac{\\pi}{2} + k2\\pi"
                    dap_an_dung = "\\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k2\\pi \\right\\}"
                    cac_phuong_an_sai = [
                        "\\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ k\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ k2\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ \\pi + k2\\pi \\right\\}"
                    ]
                elif loai_mau == 1:
                    chuoi_mau = "\\sin x + 1"
                    pt_mau = "\\sin x + 1 \\neq 0"
                    pt_he_qua = "\\sin x \\neq -1"
                    nghiem_bpt = "x \\neq -\\frac{\\pi}{2} + k2\\pi"
                    dap_an_dung = "\\mathbb{R} \\setminus \\left\\{ -\\frac{\\pi}{2} + k2\\pi \\right\\}"
                    cac_phuong_an_sai = [
                        "\\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ k\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ k2\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k2\\pi \\right\\}"
                    ]
                elif loai_mau == 2:
                    chuoi_tu = f"{a} - \\sin x" if a != 1 else "1 - \\sin x"
                    chuoi_mau = "\\cos x - 1"
                    pt_mau = "\\cos x - 1 \\neq 0"
                    pt_he_qua = "\\cos x \\neq 1"
                    nghiem_bpt = "x \\neq k2\\pi"
                    dap_an_dung = "\\mathbb{R} \\setminus \\left\\{ k2\\pi \\right\\}"
                    cac_phuong_an_sai = [
                        "\\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ k\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k2\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ \\pi + k2\\pi \\right\\}"
                    ]
                else:
                    chuoi_tu = f"{a} - \\sin x" if a != 1 else "1 - \\sin x"
                    chuoi_mau = "\\cos x + 1"
                    pt_mau = "\\cos x + 1 \\neq 0"
                    pt_he_qua = "\\cos x \\neq -1"
                    nghiem_bpt = "x \\neq \\pi + k2\\pi"
                    dap_an_dung = "\\mathbb{R} \\setminus \\left\\{ \\pi + k2\\pi \\right\\}"
                    cac_phuong_an_sai = [
                        "\\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ k\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ k2\\pi \\right\\}",
                        "\\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k2\\pi \\right\\}"
                    ]

                # Lấy ngẫu nhiên 3 phương án sai không trùng nhau
                s = random.sample(cac_phuong_an_sai, 3)
                das1 = f"${s[0]}$"
                das2 = f"${s[1]}$"
                das3 = f"${s[2]}$"

                da = f"${dap_an_dung}$"

                # Câu hỏi
                noidungcauhoi = ('''Tìm tập xác định của hàm số $y = \\frac{%s}{%s}$.'''
                                 % (chuoi_tu, chuoi_mau))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước theo mẫu cấu trúc gốc của ảnh
                loigiai = ('''Điều kiện xác định của hàm số $y = \\frac{%s}{%s}$ là \\\\ $%s \\Leftrightarrow %s \\Leftrightarrow %s \\, (k \\in \\mathbb{{Z}})$. \\\\ Vậy tập xác định của hàm số là $%s$.'''
                           % (chuoi_tu, chuoi_mau, pt_mau, pt_he_qua, nghiem_bpt, dap_an_dung))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

