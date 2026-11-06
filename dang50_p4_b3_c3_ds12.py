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


def bt_dang50_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tỉ số k sao cho S2 = k*S1. 
                # Mặc định trong đề gốc là S1 = S2 (k=1)
                k_ratio = random.choice([1, 2, 3]) 
                val_inside = (k_ratio + 1)**2

                # Đáp án đúng dựa trên biến đổi: b = căn_bậc_3((k+1)^2) * a
                kq = 'b = \\sqrt[3]{%s}a' % (val_inside)

                # Các đáp án trắc nghiệm nhiễu
                s_options = [
                    '$b = \\sqrt[3]{%s}a$' % (k_ratio + 1),
                    '$b = \\sqrt{%s}a$' % (val_inside),
                    '$b = %sa$' % (val_inside),
                    '$b = \\sqrt[3]{%s}a$' % (val_inside + 2),
                    '$b = %sa$' % (k_ratio + 1),
                ]
                # Loại bỏ phương án trùng với đáp án đúng
                s_options = [opt for opt in s_options if opt != '$%s$' % kq]
                random.shuffle(s_options)

                da_d = '\\True $%s$' % kq
                das1, das2, das3 = s_options[:3]

                # Câu hỏi với TikZ đã sửa phần tô màu S1
                text_s2 = "S_2 = %s S_1" % k_ratio if k_ratio > 1 else "S_1 = S_2"

                tikz_code = r'''\begin{tikzpicture}[scale=0.8, >=stealth]
                \draw[->] (-3,0) -- (3,0) node[below] {$x$};
                \draw[->] (0,-0.5) -- (0,4.5) node[left] {$y$};
                \draw (0,0) node[below left] {$O$};
                \draw[thick, domain=-2.1:2.1, samples=100] plot (\x, {\x*\x});
                \node at (2.2, 4.2) {$y=x^2$};
                \draw[dashed] (-2.5, 1.2) -- (2.5, 1.2) node[right] {$y=a$};
                \draw[dashed] (-2.5, 3) -- (2.5, 3) node[right] {$y=b$};
                \fill[black] plot[domain=-1.095:1.095, samples=100] (\x, {\x*\x}) -- (1.095, 1.2) -- (-1.095, 1.2) -- cycle;
                \begin{scope}
                    \clip plot[domain=-1.73:1.73, samples=100] (\x, {\x*\x}) -- (1.73, 3) -- (-1.73, 3) -- cycle;
                    \fill[pattern=north west lines, pattern color=gray] (-2, 1.2) rectangle (2, 3);
                \end{scope}
                \node at (0, 0.6) [white] {$S_1$};
                \node at (0, 2.1) {$S_2$};
            \end{tikzpicture}'''

                noidungcauhoi = ('''\\immini{Trong hệ trục tọa độ $Oxy$, cho parabol $(P): y = x^2$ và hai đường thẳng $y = a, y = b$ ($0 < a < b$) như hình vẽ. Gọi $S_1$ là diện tích hình phẳng giới hạn bởi parabol $(P)$ và đường thẳng $y = a$ (phần tô đen); $S_2$ là diện tích hình phẳng giới hạn bởi parabol $(P)$ và đường thẳng $y = b$ (phần gạch chéo).
                Tìm điều kiện của $a$ và $b$ để $%s$.}{%s}''' % (text_s2,tikz_code))

                # Đưa các đáp án vào danh sách shuffle
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải với \text{d}x
                loigiai = ('''Phương trình hoành độ giao điểm của $(P)$ với $y=b$ là $x^2=b \\Leftrightarrow x=\\pm\\sqrt{b}$.\\\\
                             Phương trình hoành độ giao điểm của $(P)$ với $y=a$ là $x^2=a \\Leftrightarrow x=\\pm\\sqrt{a}$.\\\\
                             Gọi $S$ là diện tích hình phẳng giới hạn bởi $(P)$ và đường thẳng $y=b$. Khi đó $S = S_1 + S_2$.\\\\
                             Ta có: $S = 2\\int_{0}^{\\sqrt{b}} (b - x^2) \\text{d}x = 2\\left( bx - \\frac{x^3}{3} \\right) \\bigg|_{0}^{\\sqrt{b}} = \\frac{4b\\sqrt{b}}{3}$.\\\\
                             Tương tự, diện tích hình phẳng $S_1$ là: $S_1 = 2\\int_{0}^{\\sqrt{a}} (a - x^2) \\text{d}x = \\frac{4a\\sqrt{a}}{3}$.\\\\
                             Theo giả thiết $%s \\Rightarrow S = S_1 + %s S_1 = %s S_1$.\\\\
                             Do đó: $\\frac{4b\\sqrt{b}}{3} = %s \\cdot \\frac{4a\\sqrt{a}}{3} \\Leftrightarrow (\\sqrt{b})^3 = %s(\\sqrt{a})^3 \\Leftrightarrow b\\sqrt{b} = %s a\\sqrt{a}$.\\\\
                             Bình phương hai vế ta được: $b^3 = (%s)^2 a^3 \\Leftrightarrow b = \\sqrt[3]{%s} a$.'''
                           % (text_s2, k_ratio if k_ratio > 1 else "", k_ratio + 1, k_ratio + 1, k_ratio + 1, k_ratio + 1, k_ratio + 1, val_inside))

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

