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


def bt_dang39_p3_b2_c4_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng bài toán: lim_{x -> -inf} (ax + c + sqrt(k^2 * x^2 + b*x + d)) = L
        # Để giới hạn hữu hạn khi x -> -inf: a = k
        k_val = random.choice([2, 3])
        k2_val = k_val**2
        a_val = k_val
        c_val = random.choice([1, 2, 3, 4])
        L_val = random.choice([4, 5, 6, 7])
        d_val = random.choice([8, 10, 12, 16])

        # Biểu thức giới hạn: c - b / (2k) = L => b = 2*k*(c - L)
        b_val = 2 * k_val * (c_val - L_val)

        # Giá trị cần tính: 2a - b
        ans_val = 2 * a_val - b_val

        da = '$%s$' % (ans_val)

        # Sinh các đáp án sai
        s_set = set()
        offsets = [-14, -8, -6, -2, 2, 4, 6, 8, 10, 12, 14]
        random.shuffle(offsets)
        for off in offsets:
            val_wrong = ans_val + off
            if val_wrong != ans_val:
                s_set.add('$%s$' % (val_wrong))
            if len(s_set) >= 6:
                break

        s = list(s_set)
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Biểu diễn bx theo dấu
        if b_val > 0:
            bx_str = '+ %sx' % (b_val if b_val != 1 else '')
        elif b_val < 0:
            bx_str = '- %sx' % (-b_val if b_val != -1 else '')
        else:
            bx_str = ''

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho $a, b$ là các số thực thỏa mãn $\\lim\\limits_{x \\to -\\infty} \\left(ax + %s + \\sqrt{%sx^2 %s + %s}\\right) = %s$. Giá trị $2a - b$ bằng bao nhiêu?'''
                         % (c_val, k2_val, bx_str, d_val, L_val))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        hai_k = 2 * k_val
        b_term = '+ \\frac{%s}{x}' % (b_val) if b_val != 0 else ''

        # Khớp chính xác 34 vị trí %s trong chuỗi loigiai
        loigiai = ('''Ta có:
    $$\\lim\\limits_{x \\to -\\infty} \\left(ax + %s + \\sqrt{%sx^2 %s + %s}\\right) = %s + \\lim\\limits_{x \\to -\\infty} \\left(ax + \\sqrt{%sx^2 %s + %s}\\right)$$
    Để giới hạn hữu hạn khi $x \\to -\\infty$, ta phải khử được bậc cao nhất của $x$:\\\\
    Với $x < 0$, ta có $\\sqrt{%sx^2 %s + %s} = -x \\sqrt{%s %s + \\frac{%s}{x^2}}$, do đó:
    $$ax + \\sqrt{%sx^2 %s + %s} = x \\left(a - \\sqrt{%s %s + \\frac{%s}{x^2}}\\right)$$
    Để giới hạn là một số hữu hạn thì:
    $$a - \\sqrt{%s} = 0 \\Leftrightarrow a = %s$$
    Khi $a = %s$, nhân lượng liên hợp ta được:
    \\begin{align*}
    \\lim\\limits_{x \\to -\\infty} \\left(%sx + \\sqrt{%sx^2 %s + %s}\\right) &= \\lim\\limits_{x \\to -\\infty} \\frac{(%sx^2 %s + %s) - (%sx)^2}{\\sqrt{%sx^2 %s + %s} - %sx} \\\\
    &= \\lim\\limits_{x \\to -\\infty} \\frac{bx + %s}{-x\\sqrt{%s + \\frac{b}{x} + \\frac{%s}{x^2}} - %sx} \\\\
    &= \\lim\\limits_{x \\to -\\infty} \\frac{b + \\frac{%s}{x}}{-\\sqrt{%s + \\frac{b}{x} + \\frac{%s}{x^2}} - %s} \\\\
    &= \\frac{b}{-%s - %s} = -\\frac{b}{%s}
    \\end{align*}
    Theo giả thiết, ta có:
    $$%s - \\frac{b}{%s} = %s \\Leftrightarrow -\\frac{b}{%s} = %s \\Leftrightarrow b = %s$$
    Từ đó suy ra $a = %s$ và $b = %s$.\\\\
    Vậy giá trị của biểu thức là:
    $$2a - b = 2 \\cdot (%s) - (%s) = %s$$'''
                   % (c_val, k2_val, bx_str, d_val, c_val, k2_val, bx_str, d_val,
                      k2_val, bx_str, d_val, k2_val, b_term, d_val,
                      k2_val, bx_str, d_val, k2_val, b_term, d_val,
                      k2_val, a_val,
                      a_val,
                      a_val, k2_val, bx_str, d_val, k2_val, bx_str, d_val, a_val, k2_val, bx_str, d_val, a_val,
                      d_val, k2_val, d_val, a_val,
                      d_val, k2_val, d_val, a_val,
                      k_val, k_val, hai_k,
                      c_val, hai_k, L_val, hai_k, L_val - c_val, b_val,
                      a_val, b_val,
                      a_val, b_val, ans_val))
    dapan='\\shortans[0]{$%s$}\n'%(ans_val)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

