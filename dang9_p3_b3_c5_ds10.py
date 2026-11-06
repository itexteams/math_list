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


def bt_dang9_p3_b3_c5_ds10(self):
            while True:
                # Random các giá trị đầu vào
                # Giới hạn n nhỏ (5-12) để dễ kiểm soát hệ số
                n = randint(5, 12)
                # k là chỉ số bậc của b trong C(n, k) * (ax)^(n-k) * b^k
                # Để x có bậc n-k, ta chọn k ngẫu nhiên
                k = randint(1, n - 1)
                a = random.choice([x for x in range(-3, 4) if x != 0])
                b = random.choice([x for x in range(-3, 4) if x != 0])

                # Tính hệ số hs = C(n, k) * a^(n-k) * b^k
                val_c = math.comb(n, k)
                hs = val_c * (a**(n - k)) * (b**k)

                # Điều kiện: -999 < hs < 9999
                if -999 < hs < 9999:
                    break

            # Tạo xâu hiển thị ax
            ax_str = latex(a) + "x" if a != 1 else "x"
            if a == -1: ax_str = "-x"

            # Câu hỏi
            noidungcauhoi = ('''Hệ số của số hạng chứa $x^{%s}$ trong khai triển $(%s %+d)^{%s}$ bằng bao nhiêu?'''
                             % (latex(n - k), ax_str, b, latex(n)))

            # Nội dung lời giải
            loigiai = ('''Số hạng tổng quát của khai triển là: $T_{k+1} = C_{%s}^{k} \\cdot (%s x)^{%s-k} \\cdot (%d)^{k} = C_{%s}^{k} \\cdot (%s)^{%s-k} \\cdot (%d)^{k} \\cdot x^{%s-k}$.\\\\ \n'''
                       '''Để có số hạng chứa $x^{%s}$ thì $%s-k = %s \\Leftrightarrow k = %s$.\\\\ \n'''
                       '''Hệ số của $x^{%s}$ là: $C_{%s}^{%s} \\cdot (%s)^{%s} \\cdot (%d)^{%s} = %s$.'''
                       %(latex(n), latex(a), latex(n), b, latex(n), latex(a), latex(n), b, latex(n),
                         latex(n - k), latex(n), latex(n - k), latex(k),
                         latex(n - k), latex(n), latex(k), latex(a), latex(n - k), b, latex(k), latex(hs)))

            # Đáp án đúng (Số nguyên)
            da_dung = '$%s$' % (latex(hs))

            # Tạo các phương án nhiễu (số nguyên)
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, 2, -2, 5, -5])
                nhieu_val = hs + offset
                if nhieu_val != hs:
                    s_set.add('$%s$' % (latex(nhieu_val)))

            list_ans = ['\\True ' + da_dung] + list(s_set)
            random.shuffle(list_ans)

            # Đáp án ngắn (Số nguyên cụ thể)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(hs))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n'
                       ).replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+').replace('1x', 'x').replace('x^{1}', 'x')

            return content

