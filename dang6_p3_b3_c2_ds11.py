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


def bt_dang6_p3_b3_c2_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # --- RANDOM CÁC THAM SỐ ĐẦU VÀO ---
        # Giá trị ban đầu (triệu đồng): từ 2.000 đến 5.000 triệu đồng
        A = random.choice([2000, 2500, 3000, 3500, 4000, 4500, 5000])
        # Tỉ lệ giảm hàng năm (phần trăm): [10, 30], là bội số của 5
        r_pt = random.choice([10, 15, 20, 25, 30])
        # Số năm sử dụng: từ 4 đến 7 năm
        n = randint(4, 7)
        # -----------------------------------

        # Tỉ lệ giảm và công bội
        r = Rational(r_pt, 100)
        q = 1 - r  # q = 1 - r/100

        # Giá trị sau năm thứ nhất (số hạng đầu u1 của cấp số nhân)
        u1 = A * q

        # Giá trị sau n năm sử dụng: un = u1 * q^(n - 1)
        un_exact = u1 * (q**(n - 1))

        # Làm tròn kết quả đến hàng đơn vị (triệu đồng)
        kq_val = round(float(un_exact))
        kq = str(kq_val)

        # Các đáp án trắc nghiệm
        du = ['$%s$' % (kq)]
        da = random.choice(du)

        # Sinh các đáp án sai/nhiễu
        # (Đảm bảo các giá trị nhiễu khác nhau, nguyên dương và hợp lý)
        delta1 = random.choice([50, 100, 150])
        delta2 = random.choice([200, 250, 300])
        delta3 = random.choice([350, 400, 500])

        s = [
            '$%s$' % (kq_val + delta1),
            '$%s$' % (max(1, kq_val - delta1)),
            '$%s$' % (kq_val + delta2),
            '$%s$' % (max(1, kq_val - delta2)),
            '$%s$' % (kq_val + delta3),
            '$%s$' % (max(1, kq_val - delta3))
        ]
        # Lọc bỏ giá trị trùng với đáp án đúng nếu có
        s = list(set([opt for opt in s if opt != '$%s$' % (kq)]))

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Một công ty xây dựng mua một chiếc máy ủi với giá $%s$ triệu đồng. Cứ sau mỗi năm sử dụng, giá trị của chiếc máy ủi này lại giảm $%s\\%%$ so với giá trị của nó trong năm liền trước đó. Giá trị còn lại của chiếc máy ủi đó sau $%s$ năm sử dụng là bao nhiêu triệu đồng? (làm tròn kết quả đến hàng đơn vị).'''
                        % (latex(A), latex(r_pt), latex(n)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Gọi $u_n$ là giá trị còn lại của chiếc máy ủi sau năm thứ $n$ sử dụng ($n \\ge 1$).\\\\
    Sau năm thứ nhất, giá trị của máy ủi là:
    \\[ u_1 = %s \\cdot \\left(1 - \\frac{%s}{100}\\right) = %s \\cdot %s = %s\\text{ (triệu đồng)}. \\]
    Vì sau mỗi năm giá trị máy giảm $%s\\%%$ so với năm trước đó, nên dãy số $(u_n)$ lập thành một cấp số nhân có số hạng đầu $u_1 = %s$ (triệu đồng) và công bội $q = 1 - \\frac{%s}{100} = %s$.\\\\
    Giá trị còn lại của chiếc máy ủi sau $%s$ năm sử dụng là số hạng thứ $%s$ của cấp số nhân:
    \\[ u_{%s} = u_1 \\cdot q^{%s} = %s \\cdot \\left(%s\\right)^{%s} \\approx %s\\text{ (triệu đồng)}. \\]
    Vậy sau $%s$ năm sử dụng, chiếc máy ủi còn lại khoảng $%s$ triệu đồng.'''
                % (latex(A), latex(r_pt), latex(A), latex(q), latex(u1),
                    latex(r_pt), latex(u1), latex(r_pt), latex(q),
                    latex(n), latex(n),
                    latex(n), latex(n - 1), latex(u1), latex(q), latex(n - 1), latex(kq),
                    latex(n), latex(kq)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
            '\\loigiai{' + str(loigiai) + '}\n'
            '\\end{ex}\n \\end{minipage} \n\n')
    return content 

