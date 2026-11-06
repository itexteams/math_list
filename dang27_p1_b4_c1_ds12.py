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


def bt_dang27_p1_b4_c1_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        k_val = random.choice([1, 2, 3, 4, 6, 7])
        target_val = -k_val

        # Nghiệm t in (0, 1) cho đúng 2 nghiệm x phân biệt
        da = '$2$'

        s = ['$0$', '$4$', '$1$', '$3$']
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # TikZ bảng biến thiên (không để dấu % chú thích bên trong chuỗi)
        bbt_tikz = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) rectangle (9,3);
        \\draw[line width=1pt] (0,2.3) -- (9,2.3);
        \\draw[line width=1pt] (0,1.6) -- (9,1.6);
        \\draw[line width=1pt] (1.2,0) -- (1.2,3);
        \\node at (0.6, 2.65) {$x$};
        \\node at (1.6, 2.65) {$-\\infty$};
        \\node at (3.3, 2.65) {$0$};
        \\node at (5.0, 2.65) {$1$};
        \\node at (6.8, 2.65) {$4$};
        \\node at (8.5, 2.65) {$+\\infty$};
        \\node at (0.6, 1.95) {$f'(x)$};
        \\node at (2.45, 1.95) {$-$};
        \\node at (3.3, 1.95) {$0$};
        \\node at (4.15, 1.95) {$+$};
        \\node at (5.0, 1.95) {$0$};
        \\node at (5.9, 1.95) {$-$};
        \\draw[line width=1pt, dotted] (5.0, 1.5) -- (5.0, 0.9);
        \\node at (0.6, 0.8) {$f(x)$};
        \\node (A) at (1.6, 1.3) {$+\\infty$};
        \\node (B) at (3.3, 0.3) {$-8$};
        \\node (C) at (5.0, 0.8) {$5$};
        \\node (D) at (6.8, 1.3) {$13$};
        \\node (E) at (8.5, 0.3) {$-\\infty$};
        \\draw[line width=1pt, ->] (A) -- (B);
        \\draw[line width=1pt, ->] (B) -- (C);
        \\draw[line width=1pt, ->] (C) -- (D);
        \\draw[line width=1pt, ->] (D) -- (E);
    \\end{tikzpicture}
    \\end{center}'''

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hàm số $y = f(x)$ liên tục trên $\\mathbb{R}$ và có bảng biến thiên sau:
    %s
    Phương trình $f(\\cos x) + %s = 0$ có bao nhiêu nghiệm thuộc khoảng $\\left(-\\frac{\\pi}{2}; \\frac{\\pi}{2}\\right)$?'''
                         % (bbt_tikz, k_val))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Phương trình đã cho tương đương với:
    $$f(\\cos x) = %s$$
    Đặt $t = \\cos x$. Với $x \\in \\left(-\\frac{\\pi}{2}; \\frac{\\pi}{2}\\right)$, ta có $t \\in (0; 1]$.\\\\
    Khi đó phương trình trở thành $f(t) = %s$ với $t \\in (0; 1]$.\\\\
    Dựa vào bảng biến thiên của hàm số $y = f(x)$:\\\\
    Trên nửa khoảng $(0; 1]$, hàm số $y = f(t)$ đồng biến từ $f(0) = -8$ lên $f(1) = 5$.\\\\
    Vì $-8 < %s < 5$ nên đường thẳng $y = %s$ cắt đồ thị hàm số $y = f(t)$ tại đúng $1$ điểm duy nhất $t_0 \\in (0; 1)$.\\\\
    Với mỗi giá trị $t_0 \\in (0; 1)$, phương trình $\\cos x = t_0$ có đúng $2$ nghiệm phân biệt thuộc khoảng $\\left(-\\frac{\\pi}{2}; \\frac{\\pi}{2}\\right)$ là $x = \\arccos(t_0)$ và $x = -\\arccos(t_0)$.\\\\
    Vậy phương trình đã cho có đúng $2$ nghiệm thuộc khoảng $\\left(-\\frac{\\pi}{2}; \\frac{\\pi}{2}\\right)$.'''
                   % (target_val, target_val, target_val, target_val))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[0]) + '}\n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

