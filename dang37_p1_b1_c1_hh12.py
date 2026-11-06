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


def bt_dang37_p1_b1_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Danh sách các bộ đỉnh tứ diện
        list_vertices = [
            ('A', 'B', 'C', 'D'),
            ('S', 'A', 'B', 'C'),
            ('P', 'Q', 'R', 'S'),
            ('E', 'F', 'G', 'H')
        ]
        vertices = random.choice(list_vertices)

        # Chọn cặp cạnh đối diện lấy trung điểm (0, 1, hoặc 2)
        pair_choice = random.randint(0, 2)
        if pair_choice == 0:
            X1, X2, Y1, Y2 = vertices[0], vertices[1], vertices[2], vertices[3]
        elif pair_choice == 1:
            X1, X2, Y1, Y2 = vertices[0], vertices[2], vertices[1], vertices[3]
        else:
            X1, X2, Y1, Y2 = vertices[0], vertices[3], vertices[1], vertices[2]

        # Chọn tên hai điểm trung điểm M, N không trùng với tên các đỉnh
        possible_midpoints = [('M', 'N'), ('I', 'J'), ('E', 'F'), ('P', 'Q'), ('K', 'L')]
        valid_midpoints = [p for p in possible_midpoints if p[0] not in vertices and p[1] not in vertices]
        M_pt, N_pt = random.choice(valid_midpoints)

        # Đẳng thức sai (Đáp án đúng của bài toán)
        du = ['$\\overrightarrow{%s%s} = \\frac{1}{2}(\\overrightarrow{%s%s} + \\overrightarrow{%s%s})$' % (M_pt, N_pt, X1, X2, Y1, Y2)]
        da = random.choice(du)

        # Các đẳng thức đúng (Các phương án sai của bài toán)
        s = [
            '$\\overrightarrow{%s%s} = \\frac{1}{2}(\\overrightarrow{%s%s} + \\overrightarrow{%s%s})$' % (M_pt, N_pt, X1, Y2, X2, Y1),
            '$\\overrightarrow{%s%s} = \\frac{1}{2}(\\overrightarrow{%s%s} + \\overrightarrow{%s%s})$' % (M_pt, N_pt, X1, Y1, X2, Y2),
            '$2\\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s}$' % (M_pt, N_pt, X1, Y2, X2, Y1),
            '$2\\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s}$' % (M_pt, N_pt, X1, Y1, X2, Y2)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tứ diện $%s%s%s%s$. Gọi $%s$ và $%s$ lần lượt là trung điểm của $%s%s$ và $%s%s$. Đẳng thức nào sau đây sai?'''
                         % (vertices[0], vertices[1], vertices[2], vertices[3], M_pt, N_pt, X1, X2, Y1, Y2))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Theo quy tắc cộng vectơ và tính chất trung điểm:\\\\
    Giả sử $%s$ là trung điểm của $%s%s$ và $%s$ là trung điểm của $%s%s$.\\\\
    Ta có:\\\\
    $\\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s}$\\\\
    $\\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s}$\\\\
    Cộng vế theo vế hai đẳng thức trên, ta được:\\\\
    $2\\overrightarrow{%s%s} = (\\overrightarrow{%s%s} + \\overrightarrow{%s%s}) + \\overrightarrow{%s%s} + \\overrightarrow{%s%s} + (\\overrightarrow{%s%s} + \\overrightarrow{%s%s})$\\\\
    Vì $%s$ là trung điểm của $%s%s$ nên $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\vec{0}$.\\\\
    Vì $%s$ là trung điểm của $%s%s$ nên $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\vec{0}$.\\\\
    Do đó $2\\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} \\implies \\overrightarrow{%s%s} = \\frac{1}{2}(\\overrightarrow{%s%s} + \\overrightarrow{%s%s})$.\\\\
    Tương tự, ta cũng có $2\\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} \\implies \\overrightarrow{%s%s} = \\frac{1}{2}(\\overrightarrow{%s%s} + \\overrightarrow{%s%s})$.\\\\
    Do đó các khẳng định $\\overrightarrow{%s%s} = \\frac{1}{2}(\\overrightarrow{%s%s} + \\overrightarrow{%s%s})$, $\\overrightarrow{%s%s} = \\frac{1}{2}(\\overrightarrow{%s%s} + \\overrightarrow{%s%s})$ và $2\\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s}$ đều là đẳng thức đúng.\\\\
    Vậy đẳng thức sai là $\\overrightarrow{%s%s} = \\frac{1}{2}(\\overrightarrow{%s%s} + \\overrightarrow{%s%s})$.'''
                   % (M_pt, X1, X2, N_pt, Y1, Y2,
                      M_pt, N_pt, M_pt, X1, X1, Y2, Y2, N_pt,
                      M_pt, N_pt, M_pt, X2, X2, Y1, Y1, N_pt,
                      M_pt, N_pt, M_pt, X1, M_pt, X2, X1, Y2, X2, Y1, Y2, N_pt, Y1, N_pt,
                      M_pt, X1, X2, M_pt, X1, M_pt, X2,
                      N_pt, Y1, Y2, Y1, N_pt, Y2, N_pt,
                      M_pt, N_pt, X1, Y2, X2, Y1, M_pt, N_pt, X1, Y2, X2, Y1,
                      M_pt, N_pt, X1, Y1, X2, Y2, M_pt, N_pt, X1, Y1, X2, Y2,
                      M_pt, N_pt, X1, Y2, X2, Y1, M_pt, N_pt, X1, Y1, X2, Y2, M_pt, N_pt, X1, Y2, X2, Y1,
                      M_pt, N_pt, X1, X2, Y1, Y2))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

