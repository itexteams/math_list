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


def bt_dang5_p3_b4_c1_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Xét phương trình dạng cos(a*x) = cos(x) với a là số nguyên dương lẻ (a >= 3)
        # Nghiệm:
        # 1) (a - 1)x = k2pi => x = k2pi / (a - 1)
        # 2) (a + 1)x = l2pi => x = l2pi / (a + 1)
        # Tập hợp các điểm biểu diễn là các điểm dạng e^(i*2*pi*m / n) trong đó m in Z
        # Các góc trong nửa khoảng [0, 2pi) là:
        # { 2*pi*k / (a - 1) } hợp với { 2*pi*l / (a + 1) }
        a_val = choice([3, 5, 7, 9])

        u = a_val - 1
        v = a_val + 1

        # Tìm tập hợp các điểm phân biệt trên đường tròn lượng giác [0, 2pi)
        pts = set()
        for k in range(u):
            pts.add(frac(k, u))
        for l in range(v):
            pts.add(frac(l, v))

        so_diem = len(pts)

        # Rút gọn phân số bước giải
        u_div_2 = u // 2
        v_div_2 = v // 2

        if u_div_2 == 1:
            str_nghiem_1 = "k\\pi"
        else:
            str_nghiem_1 = "\\dfrac{k\\pi}{%d}" % (u_div_2)

        if v_div_2 == 1:
            str_nghiem_2 = "l\\pi"
        else:
            str_nghiem_2 = "\\dfrac{l\\pi}{%d}" % (v_div_2)

        kq_str = str(so_diem)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho phương trình lượng giác $\\cos %sx = \\cos x$. Trên đường tròn lượng giác, có bao nhiêu điểm biểu diễn các nghiệm của phương trình đã cho?'''
                         % (str(a_val)))

        # Nội dung lời giải
        loigiai = ('''Phương trình đã cho tương đương với: \\\\
                   $\\cos %sx = \\cos x \\Leftrightarrow \\left[\\begin{array}{l} %sx = x + k2\\pi \\\\ %sx = -x + k2\\pi \\end{array}\\right. \\Leftrightarrow \\left[\\begin{array}{l} %sx = k2\\pi \\\\ %sx = k2\\pi \\end{array}\\right. \\Leftrightarrow \\left[\\begin{array}{l} x = %s \\\\ x = %s \\end{array}\\right. (k \\in \\mathbb{Z})$. \\\\
                   Biểu diễn các nghiệm trên đường tròn lượng giác trong nửa khoảng $[0; 2\\pi)$: \\\\
                   + Với họ nghiệm $x = %s$, có $%s$ điểm biểu diễn tương ứng với $k \\in \\{0, 1, \\dots, %s\\}$. \\\\
                   + Với họ nghiệm $x = %s$, có $%s$ điểm biểu diễn tương ứng với $k \\in \\{0, 1, \\dots, %s\\}$. \\\\
                   Tổng hợp lại và loại bỏ các điểm trùng nhau, ta được tất cả $%s$ điểm phân biệt biểu diễn các nghiệm của phương trình trên đường tròn lượng giác.'''
                   % (str(a_val),
                      str(a_val), str(a_val),
                      str(u), str(v),
                      str_nghiem_1, str_nghiem_2,
                      str_nghiem_1, str(u), str(u - 1),
                      str_nghiem_2, str(v), str(v - 1),
                      str(so_diem)
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' + '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n' + '\\end{ex}\n \\end{minipage} \n\n')

    return content

