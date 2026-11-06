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


def bt_dang39_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random tên các điểm để tạo ra nhiều bài toán khác nhau
        pool = ['A', 'B', 'C', 'D', 'S', 'M', 'N', 'E', 'F', 'I', 'P', 'Q', 'R', 'K', 'H']
        selected_points = random.sample(pool, 10)
        p_A, p_B, p_C, p_D, p_S, p_M, p_N, p_E, p_I, p_F = selected_points

        # Mã TikZ vẽ hình theo phong cách mẫu
        tikz_code = ('\\begin{center}\n'
                     '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                     ' \\coordinate (B) at (2,0);\n'
                     ' \\coordinate (C) at (5,0);\n'
                     ' \\coordinate (A) at (3.5,1.5);\n'
                     ' \\coordinate (D) at (6.5,1.5);\n'
                     ' \\coordinate (S) at (4,5);\n'
                     ' \\coordinate (M) at ($(S)!0.5!(A)$);\n'
                     ' \\coordinate (N) at ($(B)!0.5!(C)$);\n'
                     ' \\coordinate (E) at ($(A)!2!(B)$);\n'
                     ' \\coordinate (I) at (intersection of E--M and S--B);\n'
                     ' \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D) (B)--(E)--(N) (E)--(I);\n'
                     ' \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (D)--(N) (M)--(N) (M)--(D) (I)--(M);\n'
                     ' \\fill (A) circle (1pt) node[above right] {$%s$};\n'
                     ' \\fill (B) circle (1pt) node[above left] {$%s$};\n'
                     ' \\fill (C) circle (1pt) node[below right] {$%s$};\n'
                     ' \\fill (D) circle (1pt) node[right] {$%s$};\n'
                     ' \\fill (S) circle (1pt) node[above] {$%s$};\n'
                     ' \\fill (M) circle (1pt) node[above] {$%s$};\n'
                     ' \\fill (N) circle (1pt) node[below] {$%s$};\n'
                     ' \\fill (E) circle (1pt) node[below] {$%s$};\n'
                     ' \\fill (I) circle (1pt) node[above left] {$%s$};\n'
                     '\\end{tikzpicture}\n'
                     '\\end{center}' % (p_A, p_B, p_C, p_D, p_S, p_M, p_N, p_E, p_I))

        # Câu hỏi
        noidungcauhoi = ('Cho hình chóp $%s.%s%s%s%s$ có đáy $%s%s%s%s$ là hình bình hành. Gọi $%s, %s$ lần lượt là trung điểm của cạnh $%s%s, %s%s$. Giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ là' 
                         % (p_S, p_A, p_B, p_C, p_D, p_A, p_B, p_C, p_D, p_M, p_N, p_S, p_A, p_B, p_C, p_M, p_N, p_D, p_S, p_B, p_C))

        # Các đáp án
        da_d = ('\\True $%s%s$ (với $%s$ là điểm trên cạnh $%s%s$ và $%s%s = \\frac{2}{3}%s%s$)' % (p_N, p_I, p_I, p_S, p_B, p_S, p_I, p_S, p_B))
        das1 = ('$%s%s$' % (p_M, p_N))
        das2 = ('$%s%s$ (với $%s$ là trung điểm cạnh $%s%s$)' % (p_N, p_F, p_F, p_S, p_B))
        das3 = ('$%s%s$ (với $%s$ là giao điểm của $%s%s$ và $%s%s$)' % (p_N, p_E, p_E, p_M, p_D, p_S, p_B))

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, das1, das2, das3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('%s\n'
                   'Trong mặt phẳng $(%s%s%s%s)$, gọi $%s%s \\cap %s%s = \\{%s\\}$. \\\\\n'
                   'Trong mặt phẳng $(%s%s%s)$, gọi $%s%s \\cap %s%s = \\{%s\\}$. \\\\\n'
                   'Ta có $%s \\in (%s%s%s) \\cap (%s%s%s)$. \\\\\n'
                   'Mặt khác $\\begin{cases} %s \\in %s%s \\\\ %s \\in %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s \\in (%s%s%s) \\cap %s%s$. \\\\\n'
                   'Vậy $%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$. \\\\\n'
                   'Lại có trong tam giác $%s%s%s$ có $%s%s$ và $%s%s$ là đường trung tuyến. Vậy $%s$ là trọng tâm của tam giác $%s%s%s$ nên $%s%s = \\frac{2}{3}%s%s$.' % 
                   (tikz_code, 
                    p_A, p_B, p_C, p_D, p_D, p_N, p_A, p_B, p_E, 
                    p_S, p_A, p_B, p_E, p_M, p_S, p_B, p_I, 
                    p_N, p_M, p_N, p_D, p_S, p_B, p_C, 
                    p_I, p_S, p_B, p_I, p_M, p_E, p_M, p_N, p_D, p_I, p_M, p_N, p_D, p_S, p_B, 
                    p_N, p_I, p_M, p_N, p_D, p_S, p_B, p_C, 
                    p_S, p_A, p_E, p_E, p_M, p_S, p_B, p_I, p_S, p_A, p_E, p_S, p_I, p_S, p_B))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content

