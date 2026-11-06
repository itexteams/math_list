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


def bt_dang30_p4_b2_c5_ds11(self):
            # Khai báo biến
            # Chọn ngẫu nhiên một số n chẵn trong khoảng từ 1000 đến 3000
            n_val = random.randrange(100, 2500, 2) 
            k1 = n_val // 2
            k2 = n_val + 1

            # Chọn cơ số A và số B ngẫu nhiên (thường là năm học)
            A = random.randint(2015, 2025)
            B = A + 1

            # ---------------------------------------------------------
            # B4: Tạo các phương án sai (không trùng đáp án đúng)
            # ---------------------------------------------------------
            kq = n_val
            s = {kq + 1, kq - 1, kq + 2, kq - 2, kq + 10, k2} # Dùng set để tránh trùng
            if kq in s: s.remove(kq)
            s_list = list(s)
            random.shuffle(s_list)

            das1 = s_list[0]
            das2 = s_list[1]
            das3 = s_list[2]

            # ---------------------------------------------------------
            # B2: Viết lại bài toán theo mẫu code Python
            # ---------------------------------------------------------

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Tìm số nguyên dương $n$ thỏa mãn
            $\log_{%s} %s + 2^2 \log_{\sqrt{%s}} %s + 3^2 \log_{\sqrt[3]{%s}} %s + \dots + n^2 \log_{\sqrt[n]{%s}} %s = %s^2 \cdot %s^2 \log_{%s} %s$.'''
                            % (A, B, A, B, A, B, A, B, k1, k2, A, B))

            # Đáp án
            da_d = r'\True $%s$' % kq
            da_s1 = r'$%s$' % das1
            da_s2 = r'$%s$' % das2
            da_s3 = r'$%s$' % das3

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = (r'''Ta có biến đổi: $k^2 \log_{\sqrt[k]{%s}} %s = k^2 \cdot k \log_{%s} %s = k^3 \log_{%s} %s$. \\
                Phương trình đã cho tương đương với:
                \begin{align*}
                & (1^3 + 2^3 + 3^3 + \dots + n^3) \log_{%s} %s = %s^2 \cdot %s^2 \log_{%s} %s \\
                \Leftrightarrow & 1^3 + 2^3 + 3^3 + \dots + n^3 = (%s \cdot %s)^2 \\
                \Leftrightarrow & \left[ \frac{n(n+1)}{2} \right]^2 = (%s \cdot %s)^2 \\
                \Leftrightarrow & \frac{n(n+1)}{2} = %s \cdot %s \\
                \Leftrightarrow & n^2 + n - %s = 0 \\
                \Leftrightarrow & \left[ \begin{aligned} n &= %s \text{ (nhận)} \\ n &= -%s \text{ (loại)} \end{aligned} \right.
                \end{align*}
                Vậy $n = %s$.'''
                % (A, B, A, B, A, B, 
                   A, B, k1, k2, A, B,
                   k1, k2,
                   k1, k2,
                   k1, k2,
                   2*k1*k2,
                   kq, kq+1,
                   kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

