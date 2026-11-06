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


def bt_dang18_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến và chọn dạng
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo tọa độ điểm M(x0; y0) sao cho |x0| != |y0|
                x0 = randint(1, 6)
                y0 = randint(1, 6)
                while abs(x0) == abs(y0):
                    y0 = randint(1, 6)

                kq = 3

                # Đáp án đúng
                da_d = ('\\True ' + '$%s$' % (kq))

                # Tạo các phương án sai
                s = [1, 2, 4, 0]
                random.shuffle(s)
                da_s1 = '$%s$' % (s[0])
                da_s2 = '$%s$' % (s[1])
                da_s3 = '$%s$' % (s[2])

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- XỬ LÝ LOGIC HIỂN THỊ DẤU CHO PHƯƠNG TRÌNH ---
                # Tổng x0 + y0 (phục vụ trường hợp b = a => x + y = a)
                a1 = x0 + y0
                # Hiệu x0 - y0 (phục vụ trường hợp b = -a => x - y = a)
                a2 = x0 - y0

                # Hàm xử lý hiển thị phương trình dạng x + y - a = 0 hoặc x - y - a = 0
                # Chuyển đổi từ x + y = a sang dạng chuẩn Ax + By + C = 0
                def format_eq(prefix, val):
                    # prefix là "x + y" hoặc "x - y"
                    # Nếu val = 3 => x + y - 3 = 0
                    # Nếu val = -1 => x + y + 1 = 0
                    sign = "-" if val > 0 else "+"
                    return "%s %s %s = 0" % (prefix, sign, abs(val))

                pt_tong = format_eq("x + y", a1)
                pt_hieu = format_eq("x - y", a2)
                # ------------------------------------------------

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho điểm $M(%s;%s)$. Số đường thẳng đi qua điểm $M$ và chắn trên hai trục tọa độ hai đoạn thẳng có độ dài bằng nhau là'''
                                 % (latex(x0), latex(y0)))

                # Nội dung lời giải chi tiết
                loigiai = ('''Xét đường thẳng $d$ đi qua gốc tọa độ $O$, khi đó $d$ có dạng $y = kx$. \\\\
                             Vì $M(%s;%s) \\in d$ nên $%s = k \\cdot %s \\Rightarrow k = %s$, do đó $d: y = %sx$ hay $%sx - %sy = 0$. \\\\
                             Xét đường thẳng $d$ không đi qua gốc tọa độ $O$, gọi phương trình đường thẳng $d$ theo đoạn chắn là $\\frac{x}{a} + \\frac{y}{b} = 1$ với $a, b \\neq 0$. \\\\
                             Theo giả thiết, độ dài hai đoạn thẳng chắn trên hai trục bằng nhau nên $|a| = |b| \\Leftrightarrow \\left[ \\begin{array}{l} b = a \\\\ b = -a \\end{array} \\right.$. \\\\
                             + Với $b = a$, ta có $d: \\frac{x}{a} + \\frac{y}{a} = 1 \\Leftrightarrow x + y = a$. \\\\
                             Vì $M(%s;%s) \\in d$ nên $%s + %s = a \\Rightarrow a = %s$. Khi đó $d: %s$. \\\\
                             + Với $b = -a$, ta có $d: \\frac{x}{a} + \\frac{y}{-a} = 1 \\Leftrightarrow x - y = a$. \\\\
                             Vì $M(%s;%s) \\in d$ nên $%s - %s = a \\Rightarrow a = %s$. Khi đó $d: %s$. \\\\
                             Vậy có tất cả $3$ đường thẳng thỏa mãn yêu cầu bài toán: $%sx - %sy = 0$, $%s$, $%s$.'''
                           % (latex(x0), latex(y0), latex(y0), latex(x0), latex(Rational(y0, x0)), latex(Rational(y0, x0)), latex(y0), latex(x0),
                              latex(x0), latex(y0), latex(x0), latex(y0), latex(a1), pt_tong,
                              latex(x0), latex(y0), latex(x0), latex(y0), latex(a2), pt_hieu,
                              latex(y0), latex(x0), pt_tong, pt_hieu
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

