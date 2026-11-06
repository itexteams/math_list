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


def bt_dang38_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Khởi tạo các hệ số ngẫu nhiên
                # Hàm số có dạng: y = (a*x + b) / sqrt(x^2 + B*x + m + C)
                a = random.randint(1, 5)
                b = random.randint(1, 10)

                # Để tam thức bậc hai có dạng (x - k)^2 + m - K, ta chọn B là số chẵn
                k = random.randint(-6, 6)
                if k == 0: k = 3 # Tránh trường hợp B = 0 để bài toán hay hơn
                B = 2 * k

                # Chọn hằng số C trong biểu thức m + C
                C = random.randint(-15, 15)

                # 2. Tính toán logic
                # Biểu thức dưới căn: x^2 + B*x + m + C = (x + k)^2 + m + C - k^2
                # Để xác định trên R thì (x + k)^2 + m + C - k^2 > 0 với mọi x
                # => m + C - k^2 > 0  => m > k^2 - C

                K_limit = k**2 - C

                # 3. Các đáp án trắc nghiệm
                da_dung = f'm > {K_limit}'

                # Tạo danh sách các phương án sai (đảm bảo không trùng phương án đúng)
                s = [
                    f'm < {K_limit}',
                    f'm \\ge {K_limit}',
                    f'm \\le {K_limit}',
                    f'm > {K_limit + random.randint(1, 5)}',
                    f'm > {K_limit - random.randint(1, 5)}',
                    f'm < {K_limit + 2}'
                ]

                # Loại bỏ phương án trùng nếu lỡ có
                if da_dung in s:
                    s.remove(da_dung)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # 4. Nội dung câu hỏi
                # Biểu thức dưới căn để hiển thị: x^2 + Bx + m + C
                # Xử lý dấu của B và C để hiển thị LaTeX đẹp
                sign_B = "+" if B > 0 else ""
                sign_C = "+" if C > 0 else ""
                expr_denom = f"x^2 {sign_B} {B}x + m {sign_C} {C}"
                # Dọn dẹp chuỗi nếu B hoặc C = 0 hoặc có dấu +-
                expr_denom = expr_denom.replace("+ -", "- ").replace(" 1x", " x")

                noidungcauhoi = (f'Tìm giá trị của $m$ để hàm số $y = \\frac{{{a}x + {b}}}{{\\sqrt{{{expr_denom}}}}}$ xác định trên $\\mathbb{{R}}$.')

                # 5. Các đáp án
                da_d = ('\\True $' + str(da_dung) + '$')
                da_s1 = f'${das1}$'
                da_s2 = f'${das2}$'
                da_s3 = f'${das3}$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # 6. Nội dung lời giải
                # Biểu diễn (x + k)^2: nếu k âm thì (x - |k|)^2
                show_k = f"x + {k}" if k > 0 else f"x - {abs(k)}"
                val_check = C - k**2
                sign_val = "+" if val_check > 0 else ""

                loigiai = (f'''Hàm số xác định khi ${expr_denom} > 0 \\Leftrightarrow ({show_k})^2 + m {sign_val} {val_check} > 0$. \\\\
                          Để hàm số xác định với mọi $x \\in \\mathbb{{R}} \\Leftrightarrow ({show_k})^2 + m {sign_val} {val_check} > 0$ đúng với mọi $x \\in \\mathbb{{R}}$. \\\\
                          $\\Leftrightarrow m {sign_val} {val_check} > 0 \\Leftrightarrow m > {K_limit}$. \\\\
                          Vậy $m > {K_limit}$ thỏa mãn yêu cầu bài toán.''')

            # 7. Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

