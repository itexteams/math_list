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


def bt_dang44_p4_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Để nghiệm m1, m2 là số nguyên, ta cần Delta' = m^2 - (2b+c)m + (b^2 - ac) = 0 có nghiệm nguyên
                # Gọi 2 nghiệm đó là m1 và m2 (giả sử m1 < m2)
                # Theo hệ thức Vi-et: 
                # m1 + m2 = 2*b_val + c_val
                # m1 * m2 = b_val^2 - c_val * a_val

                # Ta chọn m1, m2 trước để đảm bảo số nguyên đẹp
                m1 = randint(-5, 5)
                m2 = m1 + randint(2, 10) # Đảm bảo m2 > m1

                # Chọn c_val sao cho (m1 + m2 - c_val) chia hết cho 2 (để b_val là số nguyên)
                c_val = randint(1, 5)
                if (m1 + m2 - c_val) % 2 != 0:
                    c_val += 1

                b_val = (m1 + m2 - c_val) // 2

                # Từ m1 * m2 = b_val^2 - c_val * a_val => a_val = (b_val^2 - m1 * m2) / c_val
                # Để a_val nguyên và dương, ta cần (b_val^2 - m1 * m2) chia hết cho c_val
                # Nếu không chia hết, ta dùng vòng lặp nhỏ để điều chỉnh
                while (b_val**2 - m1 * m2) % c_val != 0 or (b_val**2 - m1 * m2) // c_val <= 0:
                    m1 = randint(-5, 5)
                    m2 = m1 + randint(2, 10)
                    c_val = randint(1, 5)
                    if (m1 + m2 - c_val) % 2 != 0: c_val += 1
                    b_val = (m1 + m2 - c_val) // 2

                a_val = (b_val**2 - m1 * m2) // c_val

                # Biểu thức Delta' theo m: m^2 - (m1+m2)m + m1*m2
                m_sym = symbols('m')
                expr_delta = m_sym**2 - (m1 + m2)*m_sym + m1*m2

                # Đáp án đúng
                da_dung = '$%s \\le m \\le %s$' % (latex(m1), latex(m2))

                # Tạo các đáp án sai
                s = [
                    '$%s < m \\le %s$' % (latex(m1), latex(m2)),
                    '$m \\le %s$' % (latex(m2)),
                    '$%s \\le m < %s$' % (latex(m1), latex(m2)),
                    '$m \\ge %s$' % (latex(m1)),
                    '$m < %s \\cup m > %s$' % (latex(m1), latex(m2)),
                    'Vô nghiệm'
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('''Tìm giá trị của $m$ để hàm số $y = \\sqrt{(m + %s)x^2 - 2(m - %s)x + %s}$ có tập xác định $D = \\mathbb{R}$.'''
                                 % (latex(a_val), latex(b_val), latex(c_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Khai triển Delta' để viết vào lời giải
                delta_tri = 'm^2 - %sm %s %s' % (latex(m1+m2), '+' if m1*m2 >=0 else '', latex(m1*m2))

                loigiai = ('''Hàm số xác định $\\Leftrightarrow (m + %s)x^2 - 2(m - %s)x + %s \\ge 0 \\quad (*)$.\\\\
            Hàm số có tập xác định $D = \\mathbb{R}$ khi và chỉ khi $(*)$ đúng với $\\forall x \\in \\mathbb{R}$.\\\\
            +) $m = -%s$: $(*)$ trở thành: $%sx + %s \\ge 0$ không đúng với $\\forall x \\in \\mathbb{R}$. Suy ra $m = -%s$ loại.\\\\
            +) $m \\neq -%s$: $(*)$ đúng với $\\forall x \\in \\mathbb{R} \\Leftrightarrow \\begin{cases} \\Delta' = (m - %s)^2 - %s(m + %s) \\le 0 \\\\ m + %s > 0 \\end{cases}$ \\\\
            $\\Leftrightarrow \\begin{cases} %s \\le 0 \\\\ m > -%s \\end{cases} \\Leftrightarrow \\begin{cases} %s \\le m \\le %s \\\\ m > -%s \\end{cases} \\Leftrightarrow %s \\le m \\le %s$.\\\\
            Vậy với $%s \\le m \\le %s$ thì hàm số đã cho có tập xác định $D = \\mathbb{R}$.'''
                           % (latex(a_val), latex(b_val), latex(c_val),
                              latex(a_val), latex(2*(a_val + b_val)), latex(c_val), latex(a_val),
                              latex(a_val), latex(b_val), latex(c_val), latex(a_val), latex(a_val),
                              delta_tri, latex(a_val), latex(m1), latex(m2), latex(a_val), latex(m1), latex(m2),
                              latex(m1), latex(m2)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','+').replace('- -','+')
            return content

