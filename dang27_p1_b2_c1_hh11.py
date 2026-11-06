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


def bt_dang27_p1_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    # Random tên các đỉnh để tạo ra các bài toán khác nhau
    if dang == '1':
        A, B, C, D = 'A', 'B', 'C', 'D'
        M, N = 'M', 'N'
        H, G, O = 'H', 'G', 'O'

    # Khai báo các mặt phẳng và đường thẳng
    mp_day1 = B + C + D
    mp_day2 = A + C + D
    mp_cheo = A + B + D

    # Câu hỏi
    noidungcauhoi = ('''Cho tứ diện $%s%s%s%s$. Các điểm $%s, %s$ lần lượt là trung điểm $%s%s, %s%s$. Các điểm $%s, %s$ lần lượt là trọng tâm các tam giác $%s; %s$. Đường thẳng $%s%s$ chéo với đường thẳng nào sau đây?'''
                     % (A, B, C, D, M, N, B, D, A, D, H, G, mp_day1, mp_day2, H, G))

    # Các đáp án
    da_d = ('\\True $%s%s$' % (C, D))
    da_s1 = ('$%s%s$' % (M, N))
    da_s2 = ('$%s%s$' % (C, N))
    da_s3 = ('$%s%s$' % (A, B))

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Nội dung lời giải
    loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D) at (0,1);
    \\coordinate (C) at (1.5,-1.5);
    \\coordinate (B) at (5.5,1);
    \\coordinate (A) at (2,4);
    \\coordinate (M) at ($(D)!0.5!(B)$);
    \\coordinate (N) at ($(D)!0.5!(A)$);
    \\coordinate (O) at ($(D)!0.5!(C)$);
    \\coordinate (H) at ($(O)!1/3!(B)$);
    \\coordinate (G) at ($(O)!1/3!(A)$);
    \\draw[line width=1pt] (A)--(C) (A)--(D) (C)--(B) (A)--(B) (D)--(C) (A)--(O) (C)--(N);
    \\draw[line width=1pt, dashed] (D)--(B) (O)--(B) (G)--(H) (M)--(N) ;
    \\fill (A) circle (1pt) node[above] {$%s$};
    \\fill (B) circle (1pt) node[right] {$%s$};
    \\fill (C) circle (1pt) node[below] {$%s$};
    \\fill (D) circle (1pt) node[left] {$%s$};
    \\fill (M) circle (1pt) node[above right] {$%s$};
    \\fill (N) circle (1pt) node[left] {$%s$};
    \\fill (O) circle (1pt) node[below left] {$%s$};
    \\fill (H) circle (1pt) node[below] {$%s$};
    \\fill (G) circle (1pt) node[left] {$%s$};
    \\end{tikzpicture}
    \\end{center}
    Do $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s} = \\frac{1}{3} \\Rightarrow %s%s // %s%s$ (Định lý Talet)\\\\
    Xét tam giác $%s$ có: $%s%s // %s%s$ (do $%s%s$ là đường trung bình của tam giác) $\\Rightarrow %s%s // %s%s$ \\\\
    Lại có: $%s%s \\cap %s%s = %s$ \\\\
    Vậy $%s%s$ và $%s%s$ chéo nhau.'''
               % (A, B, C, D, M, N, O, H, G,  # Các điểm trong hình vẽ
                  O, G, O, A, O, H, O, B, H, G, A, B, # Phần tỷ lệ
                  mp_cheo, M, N, A, B, M, N, H, G, M, N, # Phần xét tam giác
                  H, G, C, N, G, # Phần giao điểm
                  H, G, C, D)) # Phần kết luận

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\choice \n'
               '{'+str(list_1[1])+'}\n'
               '{'+str(list_1[2])+'}\n'
               '{'+str(list_1[3])+'}\n'
               '{'+str(list_1[0])+'}\n'
               '\\loigiai{'+str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

