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


def bt_dang70_p3_b2_c1_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random độ dài dây thép L (dm) sao cho L chia hết cho 4
        L = random.choice([12, 16, 20, 24, 28, 32, 36, 40, 44, 48])
        S_val = Rational(L, 4)
        S_num = float(S_val)

        # Tính toán chính xác độ dài cạnh đáy a để V_max đạt cực đại
        a_num = S_num * (5 - math.sqrt(13)) / 3
        h_num = math.sqrt(S_num**2 - 2 * S_num * a_num + 0.5 * a_num**2)
        V_max = (1/3) * (a_num**2) * h_num

        # Làm tròn đến hàng phần trăm và chuyển dấu chấm thành dấu phẩy
        kq3 = Decimal(f"{V_max:.8f}").quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq = str(kq3).replace('.', ',')

        val_correct = float(kq3)

        # Tạo các phương án sai không trùng đáp án đúng và không bị âm
        s_opts = []
        deltas = [0.15, 0.32, 0.45, -0.15, -0.28, -0.42, 0.60, -0.55, 0.75, -0.70]
        random.shuffle(deltas)
        for delta in deltas:
            opt = round(val_correct + delta, 2)
            if opt > 0:
                opt_str = str(Decimal(f"{opt:.2f}")).replace('.', ',')
                if opt_str != kq and opt_str not in s_opts:
                    s_opts.append(opt_str)

        das1 = '$%s$' % s_opts[0]
        das2 = '$%s$' % s_opts[1]
        das3 = '$%s$' % s_opts[2]

        du = ['$%s$' % kq]
        da = random.choice(du)

        # Câu hỏi
        noidungcauhoi = ('''Bạn An có một đoạn dây thép dài $%s$ dm muốn uốn thành một kim tự tháp có dạng chóp tứ giác đều (đoạn dây thép được uốn thành 4 cạnh bên và 4 cạnh đáy của kim tự tháp). Hỏi thể tích lớn nhất của kim tự tháp bạn An có thể làm được là bao nhiêu? (đơn vị: $\\text{dm}^3$, kết quả làm tròn đến hàng phần chục).'''
                         % (latex(L)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Dữ liệu cho lời giải
        c_S = latex(S_val)
        c_2S = latex(2 * S_val)
        c_S2 = latex(S_val**2)
        c_4S2 = latex(4 * S_val**2)
        c_10S = latex(10 * S_val)
        c_5S = latex(5 * S_val)
        c_S_sqrt13 = latex(S_val)

        a_val_approx = str(Decimal(f"{a_num:.2f}")).replace('.', ',')

        # Nội dung lời giải chi tiết
        loigiai = ('''Gọi $a$ (dm) là độ dài cạnh đáy và $b$ (dm) là độ dài cạnh bên của chóp tứ giác đều ($a > 0, b > 0$).\\\\
                     Vì đoạn dây thép dài $%s$ dm được uốn thành $4$ cạnh bên và $4$ cạnh đáy nên ta có:\\\\
                     $4a + 4b = %s \\Leftrightarrow a + b = %s \\Leftrightarrow b = %s - a$.\\\\
                     Điều kiện: $0 < a < %s$.\\\\
                     Đáy của kim tự tháp là hình vuông cạnh $a$ nên diện tích đáy là $S_{\\text{đáy}} = a^2$.\\\\
                     Nửa đường chéo đáy là $\\frac{a\\sqrt{2}}{2}$.\\\\
                     Chiều cao $h$ của kim tự tháp là:\\\\
                     $h = \\sqrt{b^2 - \\left(\\frac{a\\sqrt{2}}{2}\\right)^2} = \\sqrt{(%s - a)^2 - \\frac{a^2}{2}} = \\sqrt{%s - %s a + \\frac{a^2}{2}}$.\\\\
                     Thể tích của kim tự tháp là:\\\\
                     $V = \\frac{1}{3} S_{\\text{đáy}} \\cdot h = \\frac{1}{3} a^2 \\sqrt{%s - %s a + \\frac{a^2}{2}}$.\\\\
                     Xét hàm số $f(a) = V^2 = \\frac{1}{9} a^4 \\left(%s - %s a + \\frac{a^2}{2}\\right) = \\frac{1}{9} \\left( %s a^4 - %s a^5 + \\frac{1}{2} a^6 \\right)$ trên khoảng $(0; %s)$.\\\\
                     Đạo hàm:\\\\
                     $f'(a) = \\frac{1}{9} \\left( %s a^3 - %s a^4 + 3a^5 \\right) = \\frac{a^3}{9} (3a^2 - %s a + %s)$.\\\\
                     Cho $f'(a) = 0 \\Leftrightarrow 3a^2 - %s a + %s = 0$ (vì $a > 0$).\\\\
                     Giải phương trình bậc hai trên, ta chọn nghiệm $a = \\frac{%s - %s \\sqrt{13}}{3} \\approx %s$ (thỏa mãn $0 < a < %s$).\\\\
                     Lập bảng biến thiên, ta thấy hàm số $f(a)$ (và do đó thể tích $V$) đạt giá trị lớn nhất tại $a \\approx %s$.\\\\
                     Khi đó, thể tích lớn nhất của kim tự tháp là $V_{\\max} \\approx %s$ dm$^3$.'''
                     % (latex(L), latex(L), c_S, c_S, c_S,
                        c_S, c_S2, c_2S,
                        c_S2, c_2S,
                        c_S2, c_2S, c_S2, c_2S, c_S,
                        c_4S2, c_10S, c_10S, c_4S2,
                        c_10S, c_4S2,
                        c_5S, c_S_sqrt13, a_val_approx, c_S,
                        a_val_approx,
                        kq))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

