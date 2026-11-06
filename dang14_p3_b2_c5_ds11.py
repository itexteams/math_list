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


def bt_dang14_p3_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo các biến ngẫu nhiên
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các hệ số để triệt tiêu log_a(b)
                # P1 = log_{a^m}(a^n * b^k) = n/m + (k/m)*log_a(b)
                # P2 = log_{a^p}(a^q / b^r) = q/p - (r/p)*log_a(b)
                # Để triệt tiêu: k/m = r/p

                m = 2
                p = Rational(1, 2)

                # Chọn r sao cho k = m * r / p là số nguyên
                # Với m=2, p=1/2 => k = 4r. Chọn r là bội của 1/2
                r_val = random.choice([Rational(1, 2), 1, Rational(3, 2), 2])
                k_val = int(m * r_val / p)

                n_val = random.randint(4, 15)
                q_val = random.randint(1, 5)

                # P3 = log_{b^u}(b^v) = v/u
                u_denom = random.randint(2, 5)
                u_val = Rational(1, u_denom)
                v_val = random.randint(-6, -1)

                # Tính toán các thành phần kết quả
                val1 = Rational(n_val, m) # n/m
                val2 = Rational(q_val, p) # q/p
                val3 = Rational(v_val, u_val) # v/u

                # Đáp án đúng
                ket_qua = val1 + val2 + val3
                da_dung = '$%s$' % latex(ket_qua)

                # Tạo danh sách đáp án sai (B4)
                s = set()
                offsets = [-2, -1, 1, 2, 3, 5]
                random.shuffle(offsets)
                for offset in offsets:
                    sai = ket_qua + offset
                    if sai != ket_qua:
                        s.add('$%s$' % latex(sai))
                    if len(s) == 3:
                        break

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # --- Soạn nội dung câu hỏi (B2) ---
                # Hiển thị số mũ/căn thức đẹp hơn
                str_base2 = r"\sqrt{a}" if p == Rational(1, 2) else "a^{%s}" % latex(p)
                str_base3 = r"\sqrt[%s]{b}" % u_denom
                str_b_term = r"\frac{a}{\sqrt{b}}" if r_val == Rational(1, 2) else r"\frac{a}{b^{%s}}" % latex(r_val)

                noidungcauhoi = (r"Giá trị biểu thức $P = \log_{a^{%s}}(a^{%s}b^{%s}) + \log_{%s}\left(%s\right) + \log_{%s}(b^{%s})$ "
                                 r"(với $0 < a \neq 1; 0 < b \neq 1$) bằng bao nhiêu?" 
                                 % (m, n_val, k_val, str_base2, str_b_term, str_base3, v_val))

                # --- Soạn nội dung lời giải ---
                loigiai = (r"Ta có: $P = \log_{a^{%s}}(a^{%s}b^{%s}) + \log_{a^{1/2}}\left(%s\right) + \log_{b^{1/%s}}(b^{%s})$ \\"
                           r"$= \left( %s + \log_a b \right) + \left( %s - \log_a b \right) + \left( %s \right) = %s$."
                           % (m, n_val, k_val, str_b_term, u_denom, v_val,
                              latex(val1), latex(val2), latex(val3), latex(ket_qua)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(ket_qua))


                # --- Xuất trắc nghiệm ---
                da_d = '\\True ' + str(da_dung)
                list_ans = [da_d, das1, das2, das3]
                random.shuffle(list_ans)

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

