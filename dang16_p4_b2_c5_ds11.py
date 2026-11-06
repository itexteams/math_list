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


def bt_dang16_p4_b2_c5_ds11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':


                base = 2
                n = random.randint(3, 8) # Chỉ số căn thức
                k_val = base**n           # Hằng số để log2(k^(1/n)) = 1

                m = random.randint(1, 5)  # Số mũ của a trong căn
                p = random.randint(1, 5)  # Số mũ của b trong căn
                u = random.randint(1, 2)  # Số mũ của a dưới mẫu
                v = random.randint(1, 2)  # Số mũ của b dưới mẫu

                # Tính x: hệ số của log2(a)
                # log2(a^(m/n) / a^u) = (m/n - u) * log2(a)
                x_frac = Rational(m, n) - u

                y_coeff_log2 = Rational(p, n) - v
                y_frac = 2 * y_coeff_log2

                # Tính giá trị biểu thức P = x * y
                P_val = x_frac * y_frac

                # --- BƯỚC 4: ĐIỀU CHỈNH ĐÁP ÁN ---
                kq = latex(P_val)
                da_d = '$P = %s$' % kq

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Tạo ngẫu nhiên các phân số có mẫu số nhỏ
                    sai_tu = random.randint(-15, 15)
                    sai_mau = random.randint(1, 10)
                    if sai_tu == 0: continue
                    val = Rational(sai_tu, sai_mau)
                    if val != P_val:
                        s.add('$P = %s$' % latex(val))

                list_sai = list(s)

                # Nội dung câu hỏi
                # Trình bày biểu thức: \frac{\sqrt[n]{k \cdot a^m \cdot b^p}}{a^u \cdot b^v}
                # Tinh chỉnh hiển thị latex
                a_m = 'a^{%s}' % m if m > 1 else 'a'
                b_p = 'b^{%s}' % p if p > 1 else 'b'
                a_u = 'a^{%s}' % u if u > 1 else 'a'
                b_v = 'b^{%s}' % v if v > 1 else 'b'

                bieu_thuc_tu = r'\sqrt[%s]{%s %s %s}' % (n, k_val, a_m, b_p)
                bieu_thuc_mau = r'%s %s' % (a_u, b_v)

                noidungcauhoi = (
                    r'Cho hai số thực dương $a, b$. Nếu viết $\log_{2} \frac{%s}{%s} = 1 + x \log_{2} a + y \log_{4} b$ '
                    r'với ($x, y \in \mathbb{Q}$). Tính $P = xy$.'
                    % (bieu_thuc_tu, bieu_thuc_mau)
                )

                # Nội dung lời giải chi tiết
                loigiai = (
                    r'Ta có: $\log_{2} \frac{\sqrt[%s]{%s %s %s}}{%s %s} = \log_{2} (%s^{\frac{1}{%s}}) + \log_{2} a^{\frac{%s}{%s}} + \log_{2} b^{\frac{%s}{%s}} - \log_{2} %s - \log_{2} %s$ \\'
                    r'$ = 1 + \frac{%s}{%s} \log_{2} a + \frac{%s}{%s} \log_{2} b - %s \log_{2} a - %s \log_{2} b$ \\'
                    r'$ = 1 + \left( \frac{%s}{%s} - %s \right) \log_{2} a + \left( \frac{%s}{%s} - %s \right) \log_{2} b$ \\'
                    r'$ = 1 + %s \log_{2} a + %s \log_{2} b$. \\'
                    r'Vì $\log_{2} b = 2 \log_{4} b$ nên biểu thức trở thành: \\'
                    r'$ 1 + %s \log_{2} a + %s \cdot (2 \log_{4} b) = 1 + %s \log_{2} a + %s \log_{4} b$. \\'
                    r'Khi đó $x = %s$ và $y = %s \Rightarrow P = xy = %s$.'
                    % (n, k_val, a_m, b_p, a_u, b_v, k_val, n, m, n, p, n, a_u, b_v,
                       m, n, p, n, u, v,
                       m, n, u, p, n, v,
                       latex(x_frac), latex(y_coeff_log2),
                       latex(x_frac), latex(y_coeff_log2), latex(x_frac), latex(y_frac),
                       latex(x_frac), latex(y_frac), latex(P_val))
                )

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_1 = ['\\True ' + da_d, list_sai[0], list_sai[1], list_sai[2]]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

