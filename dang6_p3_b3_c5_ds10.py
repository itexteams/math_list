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


def bt_dang6_p3_b3_c5_ds10(self):
            while True:
                # Giới hạn n nhỏ (3-5) để tổng a+b không vượt quá 9999
                a = random.choice([x for x in range(-3, 4) if x != 0])
                a1 = random.choice([x for x in range(-3, 4) if x != 0])
                b_val = random.choice([2, 3, 5, 7])
                n = random.randint(3, 5)

                # Sử dụng sympy để khai triển biểu thức
                from sympy import sqrt, expand
                expr = expand((a + sqrt(b_val))**n - (a1 - sqrt(b_val))**n)

                # Tách phần nguyên (a_coeff) và phần chứa căn (b_coeff)
                # Giả sử expr = a_coeff + b_coeff * sqrt(b_val)
                a_coeff = int(expr.subs(sqrt(b_val), 0))
                b_coeff = int((expr - a_coeff) / sqrt(b_val))

                # Tính tổng a + b
                sum_ab = a_coeff + b_coeff

                # Khống chế kết quả < 9999 (có thể lấy trị tuyệt đối nếu bạn muốn số dương)
                if -9999 < sum_ab < 9999:
                    break

            # Nội dung câu hỏi
            noidungcauhoi = (r'Cho biểu thức $P = (%s+\sqrt{%s})^%s - (%s-\sqrt{%s})^%s$. '
                             r'Biết $P$ được viết dưới dạng $a + b\sqrt{%s}$ với $a, b \in \mathbb{Z}$. '
                             r'Tổng $S = a + b$ bằng bao nhiêu' 
                             % (latex(a), latex(b_val), latex(n), latex(a1), latex(b_val), latex(n), latex(b_val)))

            # Đáp án đúng và nhiễu
            da_d = '\\True $%s$' % (latex(sum_ab))
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, 2, -2, 5])
                nhieu = sum_ab + offset
                if nhieu != sum_ab:
                    s_set.add('$%s$' % (latex(nhieu)))

            list_ans = [da_d] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải
            bt1 = expand((a + sqrt(b_val))**n)
            bt2 = expand((a1 - sqrt(b_val))**n)
            loigiai = (r'Ta có: \\ '
                       r'$(%s + \sqrt{%s})^%s = %s$. \\ '
                       r'$(%s - \sqrt{%s})^%s = %s$. \\ '
                       r'Suy ra $P = (%s) - (%s) = %s$. \\ '
                       r'Do đó $a = %s$ và $b = %s$. \\ '
                       r'Vậy tổng $a + b = %s + (%s) = %s$.'
                       % (latex(a), latex(b_val), latex(n), latex(bt1),
                          latex(a1), latex(b_val), latex(n), latex(bt2),
                          latex(bt1), latex(bt2), latex(expr),
                          latex(a_coeff), latex(b_coeff),
                          latex(a_coeff), latex(b_coeff), latex(sum_ab)))

            # Đáp án ngắn (Điền tổng sum_ab)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(sum_ab))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + dapan +
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('--', '+')

            return content

