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


def bt_dang28_p1_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1 & 3: Random các thông số cho bài toán
                # y = log(mx - m*x0 + a) xác định trên [k; +inf)
                a = random.randint(2, 6)  # Tham số tự do a
                x0 = 1 
                k_den = random.randint(2, 4) # Mẫu số của k (ví dụ 2, 3, 4)
                k_num = 1 
                k = Rational(k_num, k_den)

                # Tính toán giá trị giới hạn của m cho trường hợp m > 0
                # Điều kiện: 1 - a/m < k  => 1 - k < a/m => m < a / (1 - k)
                limit_val = float(a / (1 - k))

                # m nguyên dương và m < limit_val
                # Nếu limit_val là số nguyên (ví dụ 4), thì m chỉ lấy đến 3.
                if limit_val.is_integer():
                    m_pos_max = int(limit_val) - 1
                else:
                    m_pos_max = math.floor(limit_val)

                # Tập các giá trị m nguyên là {0, 1, 2, ..., m_pos_max}
                kq_val = m_pos_max + 1 

                # Bước 4: Tạo các phương án sai không trùng đáp án đúng
                da_dung = str(kq_val)
                s_vals = set()
                while len(s_vals) < 3:
                    sai = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    if sai >= 0 and str(sai) != da_dung:
                        s_vals.add(str(sai))

                list_sai = list(s_vals)

                # Câu hỏi
                expr_tex = f"mx - m + {a}"
                interval_tex = f"\\left[ \\frac{{{k_num}}}{{{k_den}}}; +\\infty \\right)"

                noidungcauhoi = (f"Số các giá trị nguyên của tham số $m$ để hàm số $y = \\log({expr_tex})$ xác định trên ${interval_tex}$ là")

                # Các đáp án
                da_d = '\\True $' + da_dung + '$'
                da_s1 = '$' + list_sai[0] + '$'
                da_s2 = '$' + list_sai[1] + '$'
                da_s3 = '$' + list_sai[2] + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f'''Điều kiện xác định: ${expr_tex} > 0 \\Leftrightarrow m(x - 1) + {a} > 0 \\quad (1)$.\\\\
            Trường hợp 1. $m = 0$.\\\\
            $(1) \\Leftrightarrow {a} > 0$ (luôn đúng với mọi $x \\in {interval_tex}$). Vậy $m=0$ thỏa mãn.\\\\
            Trường hợp 2. $m > 0$.\\\\
            $(1) \\Leftrightarrow x - 1 > -\\frac{{{a}}}{{m}} \\Leftrightarrow x > 1 - \\frac{{{a}}}{{m}}$.\\\\
            Để hàm số xác định trên ${interval_tex}$ thì:\\\\
            $1 - \\frac{{{a}}}{{m}} < \\frac{{{k_num}}}{{{k_den}}} \\Leftrightarrow 1 - \\frac{{{k_num}}}{{{k_den}}} < \\frac{{{a}}}{{m}} \\Leftrightarrow \\frac{{{k_den - k_num}}}{{{k_den}}} < \\frac{{{a}}}{{m}} \\Leftrightarrow m < {latex(a / (1-k))}$.\\\\
            Vì $m \\in \\mathbb{{Z}}^+$ nên $m \\in \\{{1; 2; \\dots; {m_pos_max} \\}}$.\\\\
            Trường hợp 3. $m < 0$.\\\\
            $(1) \\Leftrightarrow x - 1 < -\\frac{{{a}}}{{m}} \\Leftrightarrow x < 1 - \\frac{{{a}}}{{m}}$.\\\\
            Khi đó tập xác định của hàm số là $D = \\left( -\\infty; 1 - \\frac{{{a}}}{{m}} \\right)$.\\\\
            Do đó ${interval_tex} \\not\\subset D$, suy ra không có giá trị $m < 0$ nào thỏa mãn.\\\\
            Từ các trường hợp trên, ta có ${kq_val}$ giá trị $m$ nguyên thỏa mãn.''')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

