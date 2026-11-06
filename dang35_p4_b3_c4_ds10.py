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


def bt_dang35_p4_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random giá trị a trong khoảng 1 đến 5 để x^2 - a^2 có nghĩa (ví dụ a=sqrt(3) như trong hình)
                # Ở đây chọn số nguyên để bài toán đẹp hoặc dùng sp.sqrt
                val_a_sq = random.choice([2, 3, 5, 6, 7, 8])
                a_latex = sp.latex(sp.sqrt(val_a_sq))

                # Random giá trị b để phương trình sqrt(x^2 - a^2) = b - x có nghiệm
                b = random.randint(2, 5)

                # Giải phương trình sqrt(x^2 - val_a_sq) = b - x
                # Điều kiện: b - x >= 0 <=> x <= b
                # Bình phương: x^2 - val_a_sq = (b - x)^2 <=> x^2 - val_a_sq = b^2 - 2bx + x^2
                # <=> 2bx = b^2 + val_a_sq <=> x = (b^2 + val_a_sq) / (2b)
                tu_so = b**2 + val_a_sq
                mau_so = 2 * b
                nghiem_x = Rational(tu_so, mau_so)

                # Kiểm tra điều kiện x <= b: (b^2 + val_a_sq) / 2b <= b <=> b^2 + val_a_sq <= 2b^2 <=> val_a_sq <= b^2
                # Nếu không thỏa mãn, chọn lại b
                while val_a_sq >= b**2:
                    b += 1
                    tu_so = b**2 + val_a_sq
                    mau_so = 2 * b
                    nghiem_x = Rational(tu_so, mau_so)

                # Đáp án đúng
                # Tập xác định D = (-inf; -sqrt(a)] U [sqrt(a); +inf) \ {nghiem_x}
                kq_chuan = r'(-\infty; -%s] \cup [%s; +\infty) \setminus \left\{ %s \right\}' % (a_latex, a_latex, sp.latex(nghiem_x))

                da = '$' + kq_chuan + '$'

                # Tạo các phương án sai (nhiễu)
                s = [
                    '$' + (r'(-\infty; -%s) \cup (%s; +\infty) \setminus \left\{ %s \right\}' % (a_latex, a_latex, sp.latex(nghiem_x))) + '$',
                    '$' + (r'(-\infty; -%s] \cup [%s; +\infty)' % (a_latex, a_latex)) + '$',
                    '$' + (r'[%s; +\infty) \setminus \left\{ %s \right\}' % (a_latex, sp.latex(nghiem_x))) + '$',
                    '$' + (r'\mathbb{R} \setminus \left\{ %s \right\}' % (sp.latex(nghiem_x))) + '$',
                    '$' + (r'(-\infty; -%s] \cup [%s; +\infty) \setminus \left\{ %s \right\}' % (a_latex, a_latex, sp.latex(Rational(tu_so-1, mau_so)))) + '$'
                ]

                # Loại bỏ giá trị trùng nếu vô tình giống đáp án đúng
                s = [item for item in s if item != da]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi (Tương tự cấu trúc ảnh: x - 2 ở tử số không ảnh hưởng TXĐ nhưng giữ đúng form)
                tu_so_tu = random.randint(1, 5)
                noidungcauhoi = ('''Tìm tập xác định của hàm số $y = \\frac{x - %s}{\\sqrt{x^2 - %s} + x - %s}$.'''
                                  %(latex(tu_so_tu), latex(val_a_sq), latex(b)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Hàm số đã cho xác định khi $\\begin{cases} \\sqrt{x^2 - %s} + x - %s \\neq 0 \\\\ x^2 - %s \\ge 0 \\end{cases}$.\\\\
                             Ta có $x^2 - %s \\ge 0 \\Leftrightarrow \\left[ \\begin{matrix} x \\ge %s \\\\ x \\le -%s \\end{matrix} \\right. $.\\\\
                             Xét $\\sqrt{x^2 - %s} + x - %s = 0 \\Leftrightarrow \\sqrt{x^2 - %s} = %s - x \\\\
                             \\Leftrightarrow \\begin{cases} %s - x \\ge 0 \\\\ x^2 - %s = (%s - x)^2 \\end{cases} 
                             \\Leftrightarrow \\begin{cases} x \\le %s \\\\ x^2 - %s = %s - %sx + x^2 \\end{cases} \\\\
                             \\Leftrightarrow \\begin{cases} x \\le %s \\\\ %sx = %s \\end{cases} 
                             \\Leftrightarrow \\begin{cases} x \\le %s \\\\ x = %s \\end{cases} \\Leftrightarrow x = %s$.\\\\
                             Do đó tập xác định của hàm số đã cho là $D = (-\\infty; -%s] \\cup [%s; +\\infty) \\setminus \\left\\{ %s \\right\\}$.'''
                           %(latex(val_a_sq), latex(b), latex(val_a_sq),
                             latex(val_a_sq), a_latex, a_latex,
                             latex(val_a_sq), latex(b), latex(val_a_sq), latex(b),
                             latex(b), latex(val_a_sq), latex(b),
                             latex(b), latex(val_a_sq), latex(b**2), latex(2*b),
                             latex(b), latex(2*b), latex(b**2 + val_a_sq),
                             latex(b), sp.latex(nghiem_x), sp.latex(nghiem_x),
                             a_latex, a_latex, sp.latex(nghiem_x)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

