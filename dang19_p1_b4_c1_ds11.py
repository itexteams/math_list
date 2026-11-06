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


def bt_dang19_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo tính ngẫu nhiên cho bài toán (B3)
            lisdang = ['1', '2', '3']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dạng gốc: tan 3x = tan x
                a, b = 3, 1
                # Điều kiện: 3x != pi/2 + k*pi => x != pi/6 + k*pi/3  và  x != pi/2 + k*pi
                # Nghiệm họ 1: 3x = x + k*pi => 2x = k*pi => x = k*pi/2
                # Với k lẻ (k=1) -> x = pi/2 (vi phạm đk cosx != 0) -> loại. Vậy chỉ nhận k chẵn => k = 2m => x = m*pi
                da_text = 'x = k\\pi, k \\in \\mathbb{Z}'
                das1 = 'x = \\frac{k\\pi}{2}, k \\in \\mathbb{Z}' # Bẫy chưa loại nghiệm
                das2 = 'x = k2\\pi, k \\in \\mathbb{Z}'
                das3 = 'x = \\frac{k\\pi}{6}, k \\in \\mathbb{Z}'

                dk_str = '\\left\\{\\begin{aligned} & \\cos 3x \\ne 0 \\\\ & \\cos x \\ne 0 \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} & x \\ne \\frac{\\pi}{6} + \\frac{k\\pi}{3} \\\\ & x \\ne \\frac{\\pi}{2} + k\\pi \\end{aligned}\\right. (*)'
                loigiai_buoc = 'Ta có $\\tan 3x = \\tan x \\Leftrightarrow 3x = x + k\\pi \\Leftrightarrow x = \\frac{k\\pi}{2}, k \\in \\mathbb{Z}$. Kết hợp điều kiện (*) suy ra $x = k\\pi, k \\in \\mathbb{Z}$'

            elif dang == '2':
                # Dạng 2: tan 5x = tan x
                a, b = 5, 1
                # Nghiệm họ 1: 5x = x + k*pi => 4x = k*pi => x = k*pi/4
                # Điều kiện loại các điểm làm cos x = 0 hoặc cos 5x = 0 (tức là loại các giá trị có dạng pi/2 + m*pi)
                # Do đó các điểm x = pi/4, 3pi/4 thỏa mãn, x = pi/2 bị loại, x = pi thỏa mãn,...
                # Rút gọn lại thành x = k*pi/4 với k không chia hết cho 2 (tức là k lẻ) không đúng, loại k = 2, 6, 10...
                da_text = 'x = \\frac{k\\pi}{4} \\text{ (với } k \\text{ không chia hết cho 2)}, k \\in \\mathbb{Z}'
                das1 = 'x = \\frac{k\\pi}{4}, k \\in \\mathbb{Z}'
                das2 = 'x = \\frac{k\\pi}{2}, k \\in \\mathbb{Z}'
                das3 = 'x = k\\pi, k \\in \\mathbb{Z}'

                dk_str = '\\left\\{\\begin{aligned} & \\cos 5x \\ne 0 \\\\ & \\cos x \\ne 0 \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} & x \\ne \\frac{\\pi}{10} + \\frac{k\\pi}{5} \\\\ & x \\ne \\frac{\\pi}{2} + k\\pi \\end{aligned}\\right. (*)'
                loigiai_buoc = 'Ta có $\\tan 5x = \\tan x \\Leftrightarrow 5x = x + k\\pi \\Leftrightarrow x = \\frac{k\\pi}{4}, k \\in \\mathbb{Z}$. Kết hợp điều kiện (*) ta loại bỏ các nghiệm làm cho mẫu số bằng $0$, suy ra $x = \\frac{k\\pi}{4}$ với $k$ không chia hết cho $2, k \\in \\mathbb{Z}$'

            else:
                # Dạng 3: tan 5x = tan 3x
                a, b = 5, 3
                # Nghiệm: 5x = 3x + k*pi => 2x = k*pi => x = k*pi/2. 
                # Loại điểm cos 3x = 0 và cos 5x = 0 => x = k*pi (nhận m*pi)
                da_text = 'x = k\\pi, k \\in \\mathbb{Z}'
                das1 = 'x = \\frac{k\\pi}{2}, k \\in \\mathbb{Z}'
                das2 = 'x = \\frac{k\\pi}{8}, k \\in \\mathbb{Z}'
                das3 = 'x = \\frac{k\\pi}{4}, k \\in \\mathbb{Z}'

                dk_str = '\\left\\{\\begin{aligned} & \\cos 5x \\ne 0 \\\\ & \\cos 3x \\ne 0 \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} & x \\ne \\frac{\\pi}{10} + \\frac{k\\pi}{5} \\\\ & x \\ne \\frac{\\pi}{6} + \\frac{k\\pi}{3} \\end{aligned}\\right. (*)'
                loigiai_buoc = 'Ta có $\\tan 5x = \\tan 3x \\Leftrightarrow 5x = 3x + k\\pi \\Leftrightarrow x = \\frac{k\\pi}{2}, k \\in \\mathbb{Z}$. Kết hợp điều kiện (*) loại bỏ các nghiệm trùng với điều kiện xác định, suy ra $x = k\\pi, k \\in \\mathbb{Z}$'

            # Định dạng nội dung câu hỏi sử dụng định dạng chuỗi %s
            noidungcauhoi = ('''Nghiệm của phương trình $\\tan %sx = \\tan %sx$ là''' 
                             % (latex(a), latex(b)))

            # Trình bày đầy đủ lời giải tự động theo từng bước rõ ràng như hình ảnh gốc (B1 & B7)
            loigiai = ('''Ta có $\\tan %sx = \\tan %sx \\Leftrightarrow %sx = %sx + k\\pi \\Leftrightarrow x = \\frac{k\\pi}{%s}, k \\in \\mathbb{Z}$.\\\\
            Trình bày lại\\\\
            ĐK: $%s$\\\\
            %s.''' 
                       % (latex(a), latex(b), latex(a), latex(b), latex(a-b), dk_str, loigiai_buoc))

            # Các đáp án trắc nghiệm (Đảm bảo tuyệt đối không có dấu chấm ở cuối các phương án) (B4 & B6)
            da_d = ('\\True $' + str(da_text) + '$')
            da_s1 = '$' + str(das1) + '$'
            da_s2 = '$' + str(das2) + '$'
            da_s3 = '$' + str(das3) + '$'

            # Trộn thứ tự ngẫu nhiên các phương án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Định dạng xuất câu trắc nghiệm theo mẫu minipage
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('1x','x')
            return content

