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


def bt_dang20_p1_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2', '3']
    dang = random.choice(lisdang)

    # Thông tin chung của bài toán
    td = 'ABCD'
    d1, d2, d3 = 'I', 'J', 'K'
    e1, e2, e3 = 'AB', 'BC', 'BD'

    if dang == '1':
        # Tìm giao tuyến của (ABC) và (IJK)
        mp = 'ABC'
        gt = 'IJ'
        s1 = 'KI'
        s2 = '$AB$'
        s3 = 'KJ'
        p1, p2 = 'I', 'J'
        canh1, canh2 = 'AB', 'BC'
    elif dang == '2':
        # Tìm giao tuyến của (ABD) và (IJK)
        mp = 'ABD'
        gt = 'IK'
        s1 = 'IJ'
        s2 = '$AB$'
        s3 = 'KJ'
        p1, p2 = 'I', 'K'
        canh1, canh2 = 'AB', 'BD'
    elif dang == '3':
        # Tìm giao tuyến của (BCD) và (IJK)
        mp = 'BCD'
        gt = 'JK'
        s1 = 'IJ'
        s2 = '$BC$'
        s3 = 'KI'
        p1, p2 = 'J', 'K'
        canh1, canh2 = 'BC', 'BD'

    # Câu hỏi
    noidungcauhoi = ('''Cho tứ diện $%s$, gọi $%s, %s, %s$ lần lượt là trung điểm của $%s, %s, %s$. Giao tuyến của hai mặt phẳng $(%s)$ và $(IJK)$ là'''
                     % (td, d1, d2, d3, e1, e2, e3, mp))

    # Các đáp án trắc nghiệm
    da_d = ('\\True $%s$' % gt)
    da_s1 = '$%s$' % s1
    da_s2 = s2
    da_s3 = '$%s$' % s3

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Nội dung lời giải
    loigiai = ('''Ta có $%s \\in %s \\subset (%s)$ và $%s \\in (IJK)$ nên $%s$ là điểm chung thứ nhất của hai mặt phẳng $(%s)$ và $(IJK)$. \\\\
    Tương tự $%s$ là điểm chung thứ hai của hai mặt phẳng đó. \\\\
    Vậy giao tuyến của hai mặt phẳng $(%s)$ và $(IJK)$ là $%s$.
    \\\\
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (2,4);
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (2.5,-1.5);
    \\coordinate (D) at (6,0);
    \\coordinate (I) at ($(A)!0.5!(B)$);
    \\coordinate (J) at ($(B)!0.5!(C)$);
    \\coordinate (K) at ($(B)!0.5!(D)$);
    \\draw[line width=1pt] (A)--(B) (B)--(C) (C)--(D) (D)--(A) (A)--(C) (I)--(J);
    \\draw[line width=1pt, dashed] (B)--(D) (I)--(K) (J)--(K);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (I) circle (1pt) node[left] {$I$};
    \\fill (J) circle (1pt) node[below left] {$J$};
    \\fill (K) circle (1pt) node[above right] {$K$};
    \\end{tikzpicture}
    \\end{center}'''
               % (p1, canh1, mp, p1, p1, mp, p2, mp, gt))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\choice \n'
               '{'+str(list_1[1])+'}\n'
               '{'+str(list_1[2])+'}\n'
               '{'+str(list_1[3])+'}\n'
               '{'+str(list_1[0])+'}\n'
               '\\loigiai{'+str(loigiai)+'}\n'
               '\\end{ex}\n\\end{minipage} \n\n')
    return content

