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


def bt_dang34_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Lựa chọn ngẫu nhiên tên các đỉnh và trung điểm để tạo sự đa dạng
        V = random.sample(['A', 'B', 'C', 'D', 'E', 'F', 'S', 'P'], 4)
        P = random.sample(['M', 'N', 'I', 'J', 'K', 'H'], 2)

        v1, v2, v3, v4 = V 
        m, n = P           

        # Câu hỏi
        noidungcauhoi = ('''Cho tứ diện $%s%s%s%s$. Gọi $%s, %s$ lần lượt là trung điểm của $%s%s$ và $%s%s$. Khẳng định nào dưới đây sai?'''
                         %(v1, v2, v3, v4, m, n, v3, v4, v1, v2))

        # Các đáp án trắc nghiệm
        # Khẳng định A
        das1 = '$({%s%s%s}) \\cap ({%s%s%s}) = {%s%s}$' % (v1, v2, m, v1, v3, v4, v1, m)
        # Khẳng định B
        das2 = '$({%s%s%s}) \\cap ({%s%s%s}) = {%s%s}$' % (v1, v2, m, v4, v3, n, m, n)
        # Khẳng định C (Khẳng định sai - là đáp án cần chọn)
        da_false = '$({%s%s%s}) \\cap ({%s%s%s}) = {%s%s}$' % (v1, m, n, v1, v3, v4, v1, v2)
        # Khẳng định D
        das3 = '$({%s%s%s}) \\cap ({%s%s%s}) = {%s%s}$' % (v1, v3, v4, v2, v4, v3, v3, v4)

        # Đưa đáp án đúng (chọn câu sai) và các phương án nhiễu vào
        da_d = ('\\True ' + str(da_false))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Mã TikZ để vẽ hình
        tikz_code = ('''\\begin{center}
           \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (-2,0);
            \\coordinate (C) at (3,0);
            \\coordinate (B) at (0.5,-2);
            \\coordinate (D) at (0,4);
            \\coordinate (N) at ($(A)!0.5!(B)$);
            \\coordinate (M) at ($(C)!0.5!(D)$);
            \\draw[line width=1pt] (A)--(B) (B)--(C) (C)--(D) (D)--(A) (D)--(B);
            \\draw[line width=1pt, dashed] (A)--(C) (A)--(M) (M)--(N) (N)--(C);
            \\fill (A) circle (1pt) node[left] {$%s$};
            \\fill (B) circle (1pt) node[below] {$%s$};
            \\fill (C) circle (1pt) node[right] {$%s$};
            \\fill (D) circle (1pt) node[above] {$%s$};
            \\fill (N) circle (1pt) node[left] {$%s$};
            \\fill (M) circle (1pt) node[right] {$%s$};
           \\end{tikzpicture}
           \\end{center}''' % (v1, v2, v3, v4, n, m))

        # Nội dung lời giải
        loigiai = ('''%s 
            Ta có: $%s \\in ({%s%s%s}) \\cap ({%s%s%s})$ (1) \\\\
            $\\begin{cases} %s \\in ({%s%s%s}) \\\\ %s \\in {%s%s} \\subset ({%s%s%s}) \\end{cases} \\Rightarrow %s \\in ({%s%s%s}) \\cap ({%s%s%s})$ (2) \\\\
            Từ (1) và (2) suy ra $({%s%s%s}) \\cap ({%s%s%s}) = {%s%s}$. \\\\
            Vậy khẳng định $({%s%s%s}) \\cap ({%s%s%s}) = {%s%s}$ là khẳng định sai.'''
            %(tikz_code,
              v1, v1, m, n, v1, v3, v4,
              m, v1, m, n, m, v3, v4, v1, v3, v4, m, v1, m, n, v1, v3, v4,
              v1, m, n, v1, v3, v4, v1, m,
              v1, m, n, v1, v3, v4, v1, v2))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\n\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content

