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


def bt_dang36_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số a và b sao cho biểu thức trong căn luôn >= 0 với mọi x thuộc R
                # Do -1 <= sin x <= 1 nên ta chọn a >= 2 để a - sin(x) >= 1 > 0
                a = random.randint(3, 6)
                b = random.randint(2, 5)

                chuoi_can = f"{a} + {b}\\cot^2 x - \\sin x"
                chuoi_bpt_can = f"{a} + {b}\\cot^2 x - \\sin x \\ge 0"
                chuoi_luon_dung = f"{a} + {b}\\cot^2 x - \\sin x \\ge 0, \\forall x \\in \\mathbb{{R}}"

                # Tập xác định đúng của bài toán
                dap_an_dung = "D = \\mathbb{R} \\setminus \\left\\{ \\frac{k\\pi}{2}, k \\in \\mathbb{Z} \\right\\}"

                # Các phương án sai
                cac_phuong_an_sai = [
                    "D = \\mathbb{R} \\setminus \\left\\{ -\\frac{k\\pi}{2}, k \\in \\mathbb{Z} \\right\\}",
                    "D = \\mathbb{R}",
                    "D = \\mathbb{R} \\setminus \\left\\{ k\\pi, k \\in \\mathbb{Z} \\right\\}",
                    "D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z} \\right\\}"
                ]

                # Trộn ngẫu nhiên các đáp án sai
                s = random.sample(cac_phuong_an_sai, 3)
                das1 = f"${s[0]}$"
                das2 = f"${s[1]}$"
                das3 = f"${s[2]}$"

                da = f"${dap_an_dung}$"

                # Câu hỏi
                noidungcauhoi = ('''Tìm tập xác định $D$ của hàm số $y = \\sqrt{%s} + \\cot \\left( \\frac{\\pi}{2} + x \\right)$.'''
                                 % (chuoi_can))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước y hệt cấu trúc của ảnh gốc
                loigiai = ('''Hàm số $y = \\sqrt{%s} + \\cot \\left( \\frac{\\pi}{2} + x \\right)$ xác định khi và chỉ khi các điều kiện sau thỏa mãn đồng thời: \\\\
            + $%s$, $\\cot \\left( \\frac{\\pi}{2} + x \\right)$ xác định và $\\cot x$ xác định. \\\\
            Ta có $\\begin{cases} %s \\\\ 1 - \\sin 2x \\ge 0 \\Rightarrow %s - \\sin x \\ge 0 \\end{cases} \\Rightarrow %s$. \\\\
            + $\\cot \\left( \\frac{\\pi}{2} + x \\right)$ xác định $\\Leftrightarrow \\sin \\left( \\frac{\\pi}{2} + x \\right) \\neq 0 \\Leftrightarrow \\frac{\\pi}{2} + x \\neq k\\pi \\Leftrightarrow x \\neq -\\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{{Z}}$. \\\\
            $\\cot x$ xác định $\\Leftrightarrow \\sin x \\neq 0 \\Leftrightarrow x \\neq k\\pi, k \\in \\mathbb{{Z}}$. \\\\
            Do đó hàm số xác định $\\begin{cases} x \\neq -\\frac{\\pi}{2} + k\\pi \\\\ \\\\ x \\neq k\\pi \\end{cases} \\Leftrightarrow x \\neq \\frac{{k\\pi}}{{2}}, k \\in \\mathbb{{Z}}$. \\\\
            Vậy tập xác định $%s$.'''
                           % (chuoi_can, chuoi_bpt_can, chuoi_bpt_can, a, chuoi_luon_dung, dap_an_dung))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

