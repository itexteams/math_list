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


def bt_dang29_p4_b3_c4_ds10(self):
            # Khai báo biến
            # Khởi tạo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Random a (số dưới căn) và b (số ngoài căn)
            a = random.randint(2, 15)
            b = random.randint(2, 5)

            # Hàm số dạng: y = (x - b) / (sqrt(x^2 - a) + x - b)
            # Phương trình mẫu = 0: sqrt(x^2 - a) = b - x

            # Giá trị x tiềm năng giải từ phương trình hệ quả: x^2 - a = (b - x)^2
            # x^2 - a = b^2 - 2bx + x^2  => 2bx = a + b^2 => x = (a + b^2) / (2b)
            x_sol = Rational(a + b**2, 2*b)

            # Kiểm tra điều kiện x <= b và x^2 - a >= 0
            is_nghiem = True if x_sol <= b and (x_sol**2 - a >= 0) else False

            # B2: Viết lại bài toán và lời giải
            noidungcauhoi = r"Tìm tập xác định của hàm số $y = \frac{x-%s}{\sqrt{x^2-%s} + x - %s}$." % (b, a, b)

            # Thiết lập các tập hợp con
            txd_can = r"(-\infty; -\sqrt{%s}] \cup [\sqrt{%s}; +\infty)" % (a, a)
            txd_tron = r"(-\infty; -\sqrt{%s}) \cup (\sqrt{%s}; +\infty)" % (a, a)
            diem_loai = r" \setminus \left\{ %s \right\}" % latex(x_sol)

            # Đáp án đúng
            if is_nghiem:
                da_d = r"\True $%s %s$" % (txd_can, diem_loai)
            else:
                da_d = r"\True $%s$" % txd_can

            # Các đáp án nhiễu
            s1 = r"$%s$" % txd_tron
            s2 = r"$%s %s$" % (txd_tron, diem_loai)
            s3 = r"$(-\infty; -\sqrt{%s}) \cup \left(\sqrt{%s}; %s\right)$" % (a, a, latex(x_sol))

            list_1 = [da_d, s1, s2, s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            if is_nghiem:
                chuoi_nghiem = r"$\Leftrightarrow x = %s$ (thỏa mãn $x \leq %s$ và $x^2-%s \geq 0$)." % (latex(x_sol), b, a)
                ket_luan = r"D = %s \setminus \left\{ %s \right\}" % (txd_can, latex(x_sol))
            else:
                chuoi_nghiem = r"$\Leftrightarrow x = %s$ (không thỏa mãn $x \leq %s$). Phương trình vô nghiệm." % (latex(x_sol), b)
                ket_luan = r"D = %s" % txd_can

            loigiai = r"""Hàm số xác định khi: $\begin{cases} \sqrt{x^2 - %s} + x - %s \neq 0 \\ x^2 - %s \geq 0 \end{cases}$ \\
            + Điều kiện căn thức: $x^2 - %s \geq 0 \Leftrightarrow x \in %s$. \\
            + Xét phương trình mẫu số: $\sqrt{x^2 - %s} = %s - x$ \\
            $\Leftrightarrow \begin{cases} %s - x \geq 0 \\ x^2 - %s = (%s - x)^2 \end{cases} \Leftrightarrow \begin{cases} x \leq %s \\ 2(%s)x = %s + %s^2 \end{cases}$ %s \\
            Vậy tập xác định là $%s$.""" % (a, b, a, a, txd_can, a, b, b, a, b, b, b, a, b, chuoi_nghiem, ket_luan)

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

