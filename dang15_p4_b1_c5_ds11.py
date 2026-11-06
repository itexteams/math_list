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


def bt_dang15_p4_b1_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Khởi tạo các giá trị ngẫu nhiên cho các chỉ số căn và số mũ
                # Biểu thức mẫu: căn bậc a của (2^b * căn bậc c của (2^d * căn bậc e của 2^f))
                x = 2 # Cơ số mặc định là 2 như trong hình

                a = random.randint(2, 5) # Chỉ số căn ngoài cùng
                c = random.randint(2, 5) # Chỉ số căn giữa
                e = random.randint(2, 5) # Chỉ số căn trong cùng

                b = random.randint(1, 4) # Số mũ của x ở lớp 1
                d = random.randint(1, 4) # Số mũ của x ở lớp 2
                f = random.randint(1, 4) # Số mũ của x ở lớp 3

                # Tính toán phân số m/n bằng Sympy để tự động tối giản
                # Công thức: b/a + d/(a*c) + f/(a*c*e)
                phan_so = Rational(b, a) + Rational(d, a * c) + Rational(f, a * c * e)

                m = phan_so.p # Tử số tối giản
                n = phan_so.q # Mẫu số tối giản

                # Tính giá trị P
                kq_dung = m**2 + n**2

                # 2. Tạo các đáp án nhiễu
                s = set()
                while len(s) < 3:
                    sai = kq_dung + random.choice([-20, -10, 10, 20, 15, -15, 30, 50])
                    if sai > 0 and sai != kq_dung:
                        s.add(f'${sai}$')

                list_sai = list(s)
                da_d = '\\True $' + str(kq_dung) + '$'

                # Trộn đáp án
                list_1 = [da_d] + list_sai
                random.shuffle(list_1)

                # 3. Nội dung câu hỏi (sử dụng LaTeX)
                # Tạo chuỗi hiển thị số mũ/căn cho đẹp
                hien_thi_8 = f"{x}^{b}" if b > 1 else f"{x}"
                if x == 2 and b == 3: hien_thi_8 = "8" # Giống hệt đề bài mẫu nếu b=3

                # Tạo biểu thức căn thức LaTeX
                # Biểu thức: \sqrt[a]{x^b \sqrt[c]{x^d \sqrt[e]{x^f}}}
                val_e = f"\\sqrt[{e}]{{{x}^{f}}}" if f > 1 else f"\\sqrt[{e}]{{{x}}}"
                val_c = f"\\sqrt[{c}]{{{x}^{d}{val_e}}}" if d > 1 else f"\\sqrt[{c}]{{{x}{val_e}}}"
                bieu_thuc_latex = f"\\sqrt[{a}]{{{hien_thi_8}{val_c}}}"

                noidungcauhoi = (f"Cho biểu thức ${bieu_thuc_latex} = {x}^{{\\frac{{m}}{{n}}}}$, trong đó "
                                 f"$\\frac{{m}}{{n}}$ là phân số tối giản. Tính $P = m^2 + n^2$.")

                # 4. Nội dung lời giải chi tiết
                # Bước trung gian để giải thích
                buoc1 = f"{x}^{{\\frac{{{b}}}{{{a}}}}} \\cdot {x}^{{\\frac{{{d}}}{{{a*c}}}}} \\cdot {x}^{{\\frac{{{f}}}{{{a*c*e}}}}}"
                tong_mu = f"\\frac{{{b}}}{{{a}}} + \\frac{{{d}}}{{{a*c}}} + \\frac{{{f}}}{{{a*c*e}}}"

                loigiai = (f"Ta có: ${bieu_thuc_latex} = {buoc1} = {x}^{{{tong_mu}}} = {x}^{{\\frac{{{m}}}{{{n}}}}}$.\\\\\n"
                           f"Vì $\\frac{{{m}}}{{{n}}}$ tối giản nên $\\Rightarrow \\begin{{cases}} m = {m} \\\\ n = {n} \\end{{cases}}$.\\\\\n"
                           f"Suy ra $P = m^2 + n^2 = {m}^2 + {n}^2 = {kq_dung}$.")

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

