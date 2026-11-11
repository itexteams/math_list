# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 15:27:24 2026

@author: Lenovo
"""

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


def bt_dang4_p4_b2_c1_hh11(self):
    # Khai báo biến
    lisdang=['1', '2']
    dang=random.choice(lisdang)
    if dang=='1':
        # Dạng 1: Giữ nguyên tên điểm
        p1, p2 = 'M', 'N'
    else:
        # Dạng 2: Đổi tên điểm
        p1, p2 = 'E', 'F'
    # Nội dung câu hỏi
    noidungcauhoi = ('Cho hình chóp $S.ABCD$ đáy là hình bình hành.\\\\ \n'
                     'a) Tìm giao tuyến của các cặp mặt phẳng $(SAD)$ và $(SBC)$; $(SAB)$ và $(SCD)$. \\\\ \n'
                     'b) Lấy $%s$ thuộc $SC$. Tìm giao điểm $%s$ của $SD$ và $(AB%s)$. Tứ giác $AB%s%s$ là hình gì? \n'
                     %(p1, p2, p1, p1, p2))
    # Nội dung lời giải
    loigiai = (    '\\begin{center}\n'
                   '\\begin{tikzpicture}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=1]\n'
                   '    \\coordinate (A) at (0,0);\n'
                   '    \\coordinate (B) at (-1.5,-1.5);\n'
                   '    \\coordinate (C) at (2.5,-1.5);\n'
                   '    \\coordinate (D) at (4,0);\n'
                   '    \\coordinate (S) at (0.5,3);\n'
                   '    \\coordinate (M) at (1.5,0.75);\n'
                   '    \\coordinate (N) at (2.25,1.5);\n'
                   '    \\draw[dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(N) ;\n'
                   '    \\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D) (B)--(M) (N)--(D) (M)--(N);\n'
                   '    \\draw (S) + (-3,0) -- ($(S)+(4,0)$);\n'
                   '    \\fill (A) circle (1pt) node[left] {$A$};\n'
                   '    \\fill (B) circle (1pt) node[below left] {$B$};\n'
                   '    \\fill (C) circle (1pt) node[below right] {$C$};\n'
                   '    \\fill (D) circle (1pt) node[right] {$D$};\n'
                   '    \\fill (S) circle (1pt) node[above] {$S$};\n'
                   '    \\fill (M) circle (1pt) node[below right] {$%s$};\n'
                   '    \\fill (N) circle (1pt) node[above right] {$%s$};\n'
                   '\\end{tikzpicture}\n'
                   '\\end{center}\n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item Trong $(SAD)$ dựng đường thẳng $d$ đi qua $S$ và song song với $AD$. \\\\ \n'
                   'Ta có: $d // AD$, $AD // BC \\Rightarrow d // BC$. \\\\ \n'
                   'Suy ra $d$ thuộc $(SBC)$. \\\\ \n'
                   'Nên $d$ là giao tuyến của $(SAD)$ và $(SBC)$. \\\\ \n'
                   'Tương tự, trong $(SAB)$ dựng đường thẳng $d_1$ đi qua $S$, song song với $AB$ thì $d_1$ là giao tuyến của $(SAB)$ với $(SCD)$. \n'
                   '\\item Giả sử $SD \\cap (AB%s) = %s$ \\\\ \n'
                   '$\\Rightarrow (AB%s) \\cap (SCD) = %s%s$. \\\\ \n'
                   'Xét ba mặt phẳng $(AB%s); (ABCD); (SCD)$ lần lượt cắt nhau theo $3$ giao tuyến là $AB, %s%s, CD$ nên chúng song song hoặc đồng quy. \\\\ \n'
                   'Mà $AB // CD \\Rightarrow AB // CD // %s%s \\Rightarrow AB%s%s$ là hình thang. \n'
                   '\\end{enumEX} \n'
                   %(p1, p2, p1, p2, p1, p1, p2, p1, p1, p2, p1, p2, p1, p2))
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
