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


def bt_dang43_p3_b3_c5_ds10(self):
            # Bước 1: Chọn n cụ thể là bội của 3 để k = 2n/3 nguyên
            # Giới hạn n trong [3, 6, 9, 12, 15] để kết quả < 9999
            n_val = random.choice([3, 6, 9, 12, 15])

            # Bước 2: Tính hằng số K trong phương trình A_n^2 - C_n^2 = K
            # K = n(n-1) - n(n-1)/2 = n(n-1)/2
            k_const = n_val * (n_val - 1) // 2

            # Bước 3: Tính số hạng không chứa x
            # k = 2n/3. Vì n chia hết cho 3 nên k luôn là số chẵn -> (-1)^k = 1
            k_val = (2 * n_val) // 3
            kq_val = math.comb(n_val, k_val)

            # Câu hỏi
            noidungcauhoi = (r'''Số hạng không chứa $x$ trong khai triển $\left(x^2 - \dfrac{1}{x}\right)^{n}$ biết $A_{n}^2 - C_{n}^2 = %s$ bằng bao nhiêu?'''
                             % (latex(k_const)))

            # Các đáp án trắc nghiệm
            da_d = '\\True $%d$' % kq_val

            # Tạo các phương án nhiễu
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, 100, 2, 5])
                nhieu = kq_val + offset
                if nhieu != kq_val and nhieu > 0:
                    s_set.add('$%d$' % nhieu)

            list_ans = [da_d] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải
            n_neg = (1 - int(math.sqrt(1 + 8 * k_const))) // 2
            loigiai = (r'''Ta có: $A_{n}^2 - C_{n}^2 = %s \Leftrightarrow n(n-1) - \dfrac{n(n-1)}{2} = %s$ \\
                         $\Leftrightarrow \dfrac{1}{2}n(n-1) = %s \Leftrightarrow n^2 - n - %s = 0$ \\
                         $\Leftrightarrow \left[ \begin{aligned} & n = %d \\ & n = %d \text{ (loại)} \end{aligned} \right.$ \\
                         Số hạng tổng quát trong khai triển là: $T_{k+1} = C_{%d}^k \cdot (x^2)^{%d-k} \cdot \left(-\dfrac{1}{x}\right)^k = C_{%d}^k \cdot (-1)^k \cdot x^{%d-3k}$. \\
                         Số hạng không chứa $x$ ứng với: $%d - 3k = 0 \Leftrightarrow k = %d$. \\
                         Vậy số hạng cần tìm là: $C_{%d}^{%d} \cdot (-1)^{%d} = %d$.'''
                       % (latex(k_const), latex(k_const), latex(k_const), latex(2 * k_const),
                          n_val, n_neg, n_val, n_val, n_val, 2 * n_val, 
                          2 * n_val, k_val, n_val, k_val, k_val, kq_val))

            # Đáp án ngắn (Kết quả số nguyên cụ thể)
            dapan = '\\shortans[0]{$%d$}\n' % kq_val

            # Xuất nội dung
            content = (r'\begin{minipage}{\textwidth}' + '\n'
                       r'\begin{ex}' + '\n' + noidungcauhoi + dapan +
                       r'\loigiai{' + loigiai + '}\n'
                       r'\end{ex}' + '\n' + r'\end{minipage}' + '\n\n').replace('\\frac', '\\dfrac')

            return content

