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


def bt_dang20_p3_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Ta cố định thương là (2x^2 - 3x + 6), chia cho (x + 1)
        # Đa thức chia có dạng: (2x^2 - 3x + 6)*(x + 1) - rem = 2x^3 - x^2 + 3x + 6 - rem
        # Sinh ngẫu nhiên phần dư 'rem' là một số nguyên tố nhỏ (ví dụ: 2, 3, 5) để số lượng ước vừa phải
        rem = random.choice([2, 3, 5])

        # Tính hệ số tự do của đa thức tử số: 6 - rem
        c_free = 6 - rem

        # Tìm các ước nguyên của rem
        divisors = []
        for i in range(1, rem + 1):
            if rem % i == 0:
                divisors.extend([i, -i])
        divisors.sort()

        # Các nghiệm x tương ứng: x + 1 = d => x = d - 1
        roots = [d - 1 for d in divisors]
        roots.sort()

        # Số lượng số nguyên x thỏa mãn chính là số lượng ước số
        kq_num = len(divisors)
        da = '$%s$' % latex(kq_num)

        # Tạo các phương án sai xung quanh đáp án đúng (không trùng với kq_num và luôn > 0)
        s_candi = [kq_num + 2, kq_num + 4, kq_num - 2, kq_num + 6, kq_num * 2]
        s_candi = list(set([v for v in s_candi if v != kq_num and v > 0]))

        s = []
        for val in random.sample(s_candi, 3):
            s.append('$%s$' % latex(val))

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Tạo chuỗi danh sách các ước và nghiệm hiển thị trong lời giải
        divisors_str = "; ".join(("%s" % d if d < 0 else "%s" % d) for d in divisors)
        roots_str = ", ".join(str(r) for r in roots)

        cases_left = " \\\\ ".join("x + 1 = %s" % d for d in divisors)
        cases_right = " \\\\ ".join("x = %s" % r for r in roots)

        # Định dạng dấu phép toán tử số tùy thuộc vào dấu của c_free
        if c_free >= 0:
            poly_str = "2x^3 - x^2 + 3x + %s" % c_free
        else:
            poly_str = "2x^3 - x^2 + 3x %s" % c_free

        # Câu hỏi
        noidungcauhoi = ('''Có bao nhiêu số nguyên $x$ để mệnh đề chứa biến $P(x)$: "$\\left(%s\\right) : \\left(x + 1\\right)$" đúng?'''
                            % (poly_str))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tạo nội dung lời giải chi tiết từng bước
        loigiai = ('''Với điều kiện $x \\neq -1$, thực hiện phép chia đa thức cho đa thức ta được: \\\\
    $\\frac{%s}{x + 1} = 2x^2 - 3x + 6 - \\frac{%s}{x + 1}$. \\\\
    Để mệnh đề chứa biến $P(x)$ nhận giá trị đúng (tức là phép chia hết xảy ra trên tập số nguyên), biểu thức kết quả phải nhận giá trị nguyên. \\\\
    Vì $x \\in \\mathbb{Z}$ nên $\\left(2x^2 - 3x + 6\\right) \\in \\mathbb{Z}$, do đó ta bắt buộc phải có: \\\\
    $\\frac{%s}{x + 1} \\in \\mathbb{Z} \\Rightarrow \\left(x + 1\\right) \\in \\text{Ư}\\left(%s\\right)$. \\\\
    Tập hợp các ước nguyên của $%s$ là: $\\{%s\\}$. \\\\
    Ta có các trường hợp sau: \\\\
    $\\left[ \\begin{matrix} %s \\end{matrix} \\right. \\Leftrightarrow \\left[ \\begin{matrix} %s \\end{matrix} \\right.$ \\\\
    Thử lại, các giá trị của $x$ tìm được đều thỏa mãn điều kiện xác định $x \\neq -1$. \\\\
    Tập các giá trị thỏa mãn yêu cầu bài toán là $x \\in \\{%s\\}$. \\\\
    Vậy có tất cả $%s$ giá trị $x$ nguyên thỏa mãn.'''
                    % (poly_str, latex(rem), latex(rem), latex(rem), latex(rem), divisors_str, cases_left, cases_right, roots_str, latex(kq_num)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
    return content

