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


def bt_dang45_p3_b3_c5_ds10(self):
            while True:
                # Bước 1: Chọn n và p sao cho kết quả C(n, k) < 9999
                # k = 3n / (3 + 2p). Ta chọn các cặp (n, p) đẹp:
                # (n=10, p=1) -> k=6, C(10,6)=210
                # (n=15, p=1) -> k=9, C(15,9)=5005
                # (n=12, p=3) -> k=4, C(12,4)=495
                # (n=5, p=1)  -> k=3, C(5,3)=10
                config = random.choice([
                    {'n': 5, 'p': 1}, 
                    {'n': 10, 'p': 1}, 
                    {'n': 15, 'p': 1},
                    {'n': 12, 'p': 3},
                    {'n': 9, 'p': 3}
                ])
                n_val = config['n']
                p = config['p']

                # Tính k_val
                k_val = (3 * n_val) // (3 + 2 * p)
                kq_val = math.comb(n_val, k_val)

                if 0 < kq_val < 9999:
                    break

            # Tính hằng số A trong phương trình C_n^2 - C_n^1 = A
            A_val = (n_val * (n_val - 1) // 2) - n_val

            # Nghiệm âm phục vụ trình bày lời giải: n^2 - 3n - 2A = 0
            # n1*n2 = -2A => n_neg = -2A / n_val
            n_negative = int(-(2 * A_val) / n_val)

            # Định dạng mẫu thức
            mau_thuc = "x" if p == 1 else "x^{%s}" % p

            # Câu hỏi
            noidungcauhoi = (r'''Số hạng không chứa $x$ trong khai triển của $\left(x\sqrt{x} + \dfrac{1}{%s}\right)^n$ với $x > 0$, biết $n$ là số nguyên dương thỏa mãn $C_n^2 - C_n^1 = %s$ bằng bao nhiêu?'''
                             % (mau_thuc, A_val))

            # Các phương án nhiễu (Số nguyên)
            da_d = '\\True $%s$' % kq_val
            s_set = set()
            while len(s_set) < 3:
                # Nhiễu dựa trên k-1 hoặc các số gần đó
                offset = random.choice([-1, 1, 10, 50, 100])
                cand = kq_val + offset
                if cand > 0 and cand != kq_val:
                    s_set.add('$%s$' % cand)

            list_ans = [da_d] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải
            tu_so_mu = 3 * n_val
            mau_so_mu = 3 + 2 * p
            loigiai = (r'''Điều kiện: $n \in \mathbb{N}, n \ge 2$. \\
                         $C_n^2 - C_n^1 = %s \Leftrightarrow \dfrac{n(n-1)}{2} - n = %s \Leftrightarrow n^2 - 3n - %s = 0 \Leftrightarrow \left[ \begin{aligned} & n = %s \text{ (tm)} \\ & n = %s \text{ (loại)} \end{aligned} \right.$ \\
                         Ta có $\left(x\sqrt{x} + \dfrac{1}{%s}\right)^{%s} = \sum_{k=0}^{%s} C_{%s}^k \left(x^{\frac{3}{2}}\right)^{%s-k} \left(x^{-%s}\right)^k = \sum_{k=0}^{%s} C_{%s}^k x^{\frac{3(%s-k) - 2 \cdot %s \cdot k}{2}}$. \\
                         Số hạng không chứa $x$ ứng với: $\dfrac{%s - 3k - %sk}{2} = 0 \Leftrightarrow %s - %sk = 0 \Leftrightarrow k = %s$. \\
                         Vậy số hạng cần tìm là $C_{%s}^{%s} = %s$.'''
                       % (A_val, A_val, 2 * A_val, n_val, n_negative,
                          mau_thuc, n_val, n_val, n_val, n_val, p,
                          n_val, n_val, n_val, p,
                          tu_so_mu, 2 * p, tu_so_mu, mau_so_mu, k_val,
                          n_val, k_val, kq_val))

            # Đáp án ngắn (Ghi đúng kết quả số nguyên vào ô dapan)
            dapan = '\\shortans[0]{$%d$}\n' % kq_val

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth}' + '\n'
                       '\\begin{ex}' + '\n' + noidungcauhoi + dapan +
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}' + '\n' + '\\end{minipage}' + '\n\n')

            return content

