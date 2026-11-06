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


def bt_dang22_p3_b3_c5_ds10(self):
            while True:
                # Random hệ số a, b và số mũ n
                a = random.randint(-4, 4)
                b = random.randint(-4, 4)
                n = random.randint(4, 12)

                # Tránh trường hợp hệ số bằng 0 làm mất biến
                if a == 0: a = 1
                if b == 0: b = 1

                # Tính tổng các hệ số S = (a + b)^n
                kq_val = (a + b)**n

                # Khống chế kết quả theo yêu cầu: -999 < kq_val < 9999
                if -999 < kq_val < 9999:
                    break

            # Hàm hỗ trợ định dạng hiển thị ax và by
            def format_term(coeff, var):
                if coeff == 1: return var
                if coeff == -1: return f"-{var}"
                return f"{coeff}{var}"

            ax_tex = format_term(a, "x")
            by_tex = format_term(b, "y")

            # Xử lý dấu nối giữa hai hạng tử
            sign = "+" if b > 0 else "" # Nếu b âm dấu trừ đã có sẵn trong by_tex
            bieu_thuc = r"\left( %s %s %s \right)^{%s}" % (ax_tex, sign, by_tex, latex(n))

            # Câu hỏi
            noidungcauhoi = ('''Tổng các hệ số trong khai triển nhị thức Niu-tơn của biểu thức $P(x,y) = %s$ bằng bao nhiêu?''' % bieu_thuc)

            # Đáp án đúng dạng số nguyên
            da_dung = '\\True $%s$' % (latex(kq_val))

            # Tạo các phương án nhiễu (số nguyên)
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 2, -2, 10, -10])
                nhieu = kq_val + offset
                if nhieu != kq_val:
                    s_set.add('$%s$' % (latex(nhieu)))

            list_ans = [da_dung] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải chi tiết
            loigiai = ('''Tổng các hệ số của đa thức $P(x, y)$ khi khai triển nhị thức Niu-tơn được tính bằng giá trị của đa thức tại $x = 1$ và $y = 1$.\\\\
                         Thay $x = 1, y = 1$ vào biểu thức $P(x, y) = %s$, ta có:\\\\
                         $S = P(1, 1) = (%d \\cdot 1 + (%d) \\cdot 1)^{%s} = (%d)^{%s} = %s$.'''
                       % (bieu_thuc, a, b, latex(n), (a + b), latex(n), latex(kq_val)))

            # Đáp án ngắn (Điền số nguyên cụ thể)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_val))

            # Xuất nội dung và dọn dẹp lỗi hiển thị dấu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + dapan +
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n'
            ).replace('+-', '-').replace('++', '+')

            return content

