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


def bt_dang77_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo các hệ số ngẫu nhiên cho Parabol y = x^2 + bx + c1
                # Để đơn giản và giống mẫu, ta giữ hệ số x^2 là 1
                b_p = random.randint(-5, 5)
                c_p = random.randint(-10, -1)

                # Tạo các hệ số cho đường thẳng y = mx + (k - nm) tương đương y = m(x-n) + k
                # Trong đề bài mẫu: y = mx + 3 - 2m => n = 2, k = 3
                n = random.randint(1, 5)
                k = random.randint(1, 5)

                # Phương trình hoành độ giao điểm: x^2 + b_p*x + c_p = mx + k - nm
                # <=> x^2 - (m - b_p)x + c_p - k + nm = 0
                # Đặt hệ số tự do là C = nm + (c_p - k)
                # Để có 2 nghiệm trái dấu thì C < 0 <=> nm + c_p - k < 0

                # Biểu diễn đường thẳng dưới dạng y = mx + constant
                const_line = k - n*n # Đây là phần (3 - 2m) trong đề gốc
                # Để sát đề bài, ta viết y = mx + k - n*m
                line_expr = f"mx + {k} - {n}m" if k >=0 else f"mx {k} - {n}m"

                # Đáp án đúng là m < (k - c_p)/n
                val_limit = (k - c_p) / n
                # Làm tròn để đáp án đẹp nếu cần, ở đây ta dùng số nguyên để dễ làm trắc nghiệm
                limit = int(val_limit)

                # Đáp án đúng
                da_dung = f"$m < {limit}$"

                # Các đáp án nhiễu
                s = [
                    f"$m > {limit}$",
                    f"$m < {limit + random.randint(1, 3)}$",
                    f"$m > {limit - random.randint(1, 3)}$",
                    f"$m < {limit - random.randint(1, 2)}$",
                    f"$m \\le {limit}$",
                    f"$m = {limit}$"
                ]

                # Chọn ngẫu nhiên 3 đáp án sai không trùng đáp án đúng
                random.shuffle(s)
                list_sai = []
                for x in s:
                    if x != da_dung and len(list_sai) < 3:
                        list_sai.append(x)

                # Nội dung câu hỏi
                noidungcauhoi = (f"Giá trị $m$ để đường thẳng $y = {line_expr}$ cắt parabol $y = x^2 {'+' if b_p >=0 else ''} {b_p}x {'+' if c_p >=0 else ''} {c_p}$ tại $2$ điểm phân biệt có hoành độ trái dấu là")

                # Các đáp án
                da_d = ('\\True ' + da_dung)
                list_1 = [da_d] + list_sai
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Phương trình: x^2 + (b_p - m)x + c_p - k + nm = 0
                loigiai = (f"Phương trình hoành độ giao điểm: $x^2 {'+' if b_p >=0 else ''} {b_p}x {c_p} = {line_expr}$ \n"
                           f"$\\Leftrightarrow x^2 - (m {'+' if -b_p >=0 else ''} {-b_p})x + {n}m + {c_p - k} = 0 \\quad (*)$. \n"
                           f"Đường thẳng cắt parabol tại hai điểm phân biệt có hoành độ trái dấu khi và chỉ khi phương trình $(*)$ có hai nghiệm trái dấu \n"
                           f"$\\Leftrightarrow a.c < 0 \\Leftrightarrow {n}m + {c_p - k} < 0 \\Leftrightarrow {n}m < {k - c_p} \\Leftrightarrow m < {limit}$.")

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

