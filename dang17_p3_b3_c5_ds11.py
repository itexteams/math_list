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


def bt_dang17_p3_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến và danh sách dạng (ở đây chỉ có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Random dân số năm 2019 (S) từ 90.0 đến 99.0 triệu người
                s_val = round(random.uniform(90.0, 99.9), 1)

                # Random tỉ lệ tăng dân số (i) từ 1.0% đến 1.5%
                i_val = round(random.uniform(1.0, 1.4), 2)

                # Số năm (n) - thường lấy mốc 10 năm cho giống đề bài gốc (2019 - 2009)
                n_val = 10
                year_now = 2019
                year_past = year_now - n_val

                # --- Tính toán đáp án đúng ---
                # Công thức: A = S / e^(n*i)
                # Lưu ý: i ở đây là tỉ lệ %, nên khi tính phải chia 100
                i_decimal = i_val / 100
                kq_raw = s_val / math.exp(n_val * i_decimal)

                # Làm tròn đến 1 chữ số thập phân theo quy tắc ROUND_HALF_UP
                kq_round = Decimal(str(kq_raw)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Chuyển định dạng số thập phân sang dấu phẩy cho tiếng Việt
                s_str = str(s_val).replace('.', ',')
                i_str = str(i_val).replace('.', ',')
                kq_str = str(kq_round).replace('.', ',')

                # --- B4: Điều chỉnh các phương án sai ---
                # Tạo các phương án sai quanh đáp án đúng, đảm bảo không trùng
                da_dung_float = float(kq_round)
                s_distractors = set()
                while len(s_distractors) < 3:
                    # Tạo sai số ngẫu nhiên từ -5 đến 5 (tránh số 0)
                    offset = random.choice([-3.2, -2.5, -1.1, 1.4, 2.6, 3.8, 5.1])
                    sai = Decimal(str(da_dung_float + offset)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    if sai != kq_round:
                        s_distractors.add(str(sai).replace('.', ','))

                list_sai = list(s_distractors)

                # --- B2: Viết lại nội dung câu hỏi (LaTeX) ---
                noidungcauhoi = ('''Dân số thế giới được ước tính theo công thức $S = A.e^{ni}$, trong đó $A$ là dân số của năm lấy làm mốc, $S$ là dân số sau $n$ năm, $i$ là tỉ lệ tăng dân số hằng năm. Dân số Việt Nam năm $%s$ là $%s$ triệu người, tỉ lệ tăng dân số hằng năm từ $%s$ đến nay là $%s$ptr. Hỏi dân số Việt Nam năm $%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 %(latex(year_now), s_str, latex(year_past), i_str, latex(year_past)))

                # Đáp án đúng và sai
                da_d = '\\True $%s$ triệu người' % kq_str
                da_s1 = '$%s$ triệu người' % list_sai[0]
                da_s2 = '$%s$ triệu người' % list_sai[1]
                da_s3 = '$%s$ triệu người' % list_sai[2]

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải ---
                loigiai = ('''Áp dụng công thức $S = A.e^{ni}$ trong đó: $S = %s$ triệu người, $n = %s$ năm, $i = %s$ptr. \\\\
                             Ta có số dân Việt Nam năm $%s$ là: $A = \\frac{S}{e^{ni}} = \\frac{%s}{e^{%s \\cdot %s \\text{ptr}}} \\approx %s$ triệu người.'''
                           %(s_str, latex(n_val), i_str, latex(year_past), s_str, latex(n_val), i_str, kq_str))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq_str))

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('ptr','\\%')
            return content

