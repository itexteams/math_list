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


def bt_dang25_p3_b3_c5_ds10(self):
            while True:
                # n phải là số chẵn để có 1 số hạng chính giữa
                # Chọn n = 4 hoặc 6 để hệ số không quá lớn
                n = random.choice([4, 6])
                k = n // 2 # Vị trí số hạng chính giữa (số hạng thứ k+1)

                a = random.randint(1, 6)
                b = random.randint(1, 6)

                # Tính hệ số: H = C_n^k * a^(n-k) * b^k
                # Vì n-k = k nên H = C_n^k * (a*b)^k
                val_c = math.comb(n, k)
                kq_val = val_c * (a**k) * (b**k)

                # Khống chế kết quả theo yêu cầu: -999 < kq_val < 9999
                if 0 < kq_val < 9999:
                    break

            # Định dạng hiển thị ax và by
            ax_tex = f"{a}x" if a != 1 else "x"
            by_tex = f"{b}y" if b != 1 else "y"
            bieu_thuc = r"\left( %s + %s \right)^{%s}" % (ax_tex, by_tex, n)

            # Câu hỏi
            noidungcauhoi = ('''Hệ số của số hạng chính giữa trong khai triển nhị thức Niu-tơn của $%s$ bằng bao nhiêu?''' % bieu_thuc)

            # Đáp án đúng (Số nguyên)
            da_dung = '\\True $%s$' % (latex(kq_val))

            # Tạo các phương án nhiễu
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, 100, 2, 5])
                nhieu = kq_val + offset
                if nhieu != kq_val and nhieu > 0:
                    s_set.add('$%s$' % (latex(nhieu)))

            list_ans = [da_dung] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải chi tiết
            loigiai = ('''Khai triển nhị thức Niu-tơn $%s$ có $%s+1 = %s$ số hạng.\\\\
                         Số hạng chính giữa là số hạng thứ $\\frac{%s}{2} + 1 = %s$.\\\\
                         Công thức số hạng tổng quát: $T_{k+1} = C_{%s}^{k} (ax)^{%s-k} (by)^{k}$.\\\\
                         Với $k = %s$, ta có số hạng chính giữa là:\\\\
                         $T_{%s} = C_{%s}^{%s} (%s)^{%s} (%s)^{%s} = %s x^{%s} y^{%s}$.\\\\
                         Vậy hệ số cần tìm là $%s$.'''
                       % (bieu_thuc, n, n+1, n, k+1, n, n, k, k+1, n, k, 
                          ax_tex, k, by_tex, k, latex(kq_val), k, k, latex(kq_val)))

            # Đáp án ngắn (Kết quả số nguyên kq_val)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_val))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + dapan +
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

