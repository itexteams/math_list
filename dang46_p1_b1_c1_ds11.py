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


def bt_dang46_p1_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập thông số random bài toán
                # Chọn ngẫu nhiên mẫu số chung (thường là 3, 4 hoặc 6)
                mau = random.choice([3, 4, 6])

                # Hai góc cơ bản đại diện cho 2 điểm cuối riêng biệt trên đường tròn lượng giác
                # Ví dụ: g1_base = 1 (tức pi/mau), g2_base = -5 (tức -5pi/mau)
                if mau == 6:
                    g1_base = 2    # 2pi/6 = pi/3
                    g2_base = -5   # -5pi/6
                elif mau == 3:
                    g1_base = 1    # pi/3
                    g2_base = -2   # -2pi/3
                else:
                    g1_base = 1    # pi/4
                    g2_base = -3   # -3pi/4

                # Tạo các số nguyên k ngẫu nhiên để dịch chuyển k*2*pi (tương đương k * 2 * mau)
                k1 = random.choice([-2, -1, 1, 2])
                k2 = random.choice([-2, -1, 1, 2])

                # Sinh bộ 4 tử số cho alpha, beta, gamma, delta
                # Trong đó:
                # Cặp 1 (trùng điểm cuối với g2_base): alpha và delta
                tử_alpha = g2_base
                tử_delta = g2_base + k2 * 2 * mau

                # Cặp 2 (trùng điểm cuối với g1_base): beta và gamma
                tử_beta = g1_base
                tử_gamma = g1_base + k1 * 2 * mau

                # Rút gọn các phân số bằng SymPy để hiển thị đẹp mắt
                frac_alpha = Rational(tử_alpha, mau)
                frac_beta = Rational(tử_beta, mau)
                frac_gamma = Rational(tử_gamma, mau)
                frac_delta = Rational(tử_delta, mau)

                # Hàm chuyển phân số thành chuỗi hiển thị dạng mẫu pi
                def format_cung(f):
                    if f.p == 1:
                        return '\\frac{\\pi}{%s}' % latex(f.q)
                    elif f.p == -1:
                        return '-\\frac{\\pi}{%s}' % latex(f.q)
                    elif f.q == 1:
                        return '%s\\pi' % latex(f.p)
                    else:
                        if f.p > 0:
                            return '\\frac{%s\\pi}{%s}' % (latex(f.p), latex(f.q))
                        else:
                            return '-\\frac{%s\\pi}{%s}' % (latex(abs(f.p)), latex(f.q))

                str_alpha = format_cung(frac_alpha)
                str_beta = format_cung(frac_beta)
                str_gamma = format_cung(frac_gamma)
                str_delta = format_cung(frac_delta)

                # Đáp án đúng
                da_dung = '$\\beta$ và $\\gamma$; $\\alpha$ và $\\delta$'
                da_d = ('\\True ' + da_dung)

                # B4: Tạo các phương án nhiễu không trùng đáp án đúng
                da_s1 = '$\\alpha$, $\\beta$, $\\gamma$'
                da_s2 = '$\\beta$, $\\gamma$, $\\delta$'
                da_s3 = '$\\alpha$ và $\\beta$; $\\gamma$ và $\\delta$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Câu hỏi
                noidungcauhoi = ('''Cho bốn cung (trên một đường tròn định hướng): $\\alpha = %s$, $\\beta = %s$, $\\gamma = %s$, $\\delta = %s$. Các cung nào có điểm cuối trùng nhau?'''
                                 % (str_alpha, str_beta, str_gamma, str_delta))

                # Lời giải chi tiết từng bước biến đổi phân tích k2pi
                # Phân tích gamma
                k1_val = int((frac_gamma - frac_beta) / 2)
                dau_k1 = '+' if k1_val >= 0 else '-'
                str_giai_gamma = '%s + %s \\cdot 2\\pi' % (str_beta, latex(abs(k1_val))) if k1_val >= 0 else '%s - %s \\cdot 2\\pi' % (str_beta, latex(abs(k1_val)))

                # Phân tích delta
                k2_val = int((frac_delta - frac_alpha) / 2)
                str_giai_delta = '%s + %s \\cdot 2\\pi' % (str_alpha, latex(abs(k2_val))) if k2_val >= 0 else '%s - %s \\cdot 2\\pi' % (str_alpha, latex(abs(k2_val)))

                loigiai = ('''Để hai cung lượng giác có điểm cuối trùng nhau thì hiệu số đo giữa chúng phải là một bội nguyên của $2\\pi$ (có dạng $k2\\pi$ với $k \\in \\mathbb{Z}$). \\\\
            Ta xét và phân tích các cung lượng giác đề bài cho: \\\\
            Ta có: $\\gamma = %s = %s$. Do đó, hai cung $\\beta$ và $\\gamma$ có điểm cuối trùng nhau. \\\\
            Mặt khác: $\\delta = %s = %s$. Do đó, hai cung $\\alpha$ và $\\delta$ có điểm cuối trùng nhau. \\\\
            Vậy các cặp cung có điểm cuối trùng nhau là $\\beta$ và $\\gamma$; $\\alpha$ và $\\delta$.'''
                           % (str_gamma, str_giai_gamma, str_delta, str_giai_delta))

            # Xuất câu trắc nghiệm định dạng minipage TeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

