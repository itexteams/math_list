
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


def bt_dang6_p4_b5_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_diem = random.choice([('M', 'N', 'E'), ('M', 'N', 'P'), ('D', 'E', 'F'), ('H', 'K', 'P')])
        p1, p2, p3 = bo_diem
        phuong = random.choice(['SC', 'SA', 'SB'])
        if phuong == 'SC':
            q1, q2 = f"{p1}'", f"{p2}'"
            canh1, canh2 = "CA", "CB"
            tamgiac_anh = f"{q1}{q2}C"
            tikz_them = f"""\\coordinate (Q1) at ($(C)!0.5!(A)$);
    \\coordinate (Q2) at ($(C)!0.5!(B)$);
    \\draw[line width=1pt] (P2)--(Q2);
    \\draw[line width=1pt, dashed] (P1)--(Q1)--(Q2);
    \\fill (Q1) circle (1.5pt) node[below] {{${q1}$}};
    \\fill (Q2) circle (1.5pt) node[below right] {{${q2}$}};"""
        elif phuong == 'SA':
            q1, q2 = f"{p2}'", f"{p3}'"
            canh1, canh2 = "AB", "AC"
            tamgiac_anh = f"A{q1}{q2}"
            tikz_them = f"""\\coordinate (Q1) at ($(A)!0.5!(B)$);
    \\coordinate (Q2) at ($(A)!0.5!(C)$);
    \\draw[line width=1pt] (P2)--(Q1);
    \\draw[line width=1pt, dashed] (P3)--(Q2)--(Q1);
    \\fill (Q1) circle (1.5pt) node[below left] {{${q1}$}};
    \\fill (Q2) circle (1.5pt) node[below] {{${q2}$}};"""
        else:
            q1, q2 = f"{p1}'", f"{p3}'"
            canh1, canh2 = "BA", "BC"
            tamgiac_anh = f"{q1}B{q2}"
            tikz_them = f"""\\coordinate (Q1) at ($(B)!0.5!(A)$);
    \\coordinate (Q2) at ($(B)!0.5!(C)$);
    \\draw[line width=1pt] (P1)--(Q1) (P3)--(Q2);
    \\draw[line width=1pt, dashed] (Q1)--(Q2);
    \\fill (Q1) circle (1.5pt) node[below left] {{${q1}$}};
    \\fill (Q2) circle (1.5pt) node[below right] {{${q2}$}};"""
        tikz_code = f"""\\begin{{center}}
    \\begin{{tikzpicture}}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=0.8]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (3,-1.2);
    \\coordinate (C) at (5,0);
    \\coordinate (S) at (2.6,3.6);
    \\coordinate (P1) at ($(S)!0.5!(A)$);
    \\coordinate (P2) at ($(S)!0.5!(B)$);
    \\coordinate (P3) at ($(S)!0.5!(C)$);
    \\draw[line width=1pt] (S)--(A)--(B)--(C)--(S)--(B) (P1)--(P2)--(P3);
    \\draw[line width=1pt, dashed] (A)--(C) (P1)--(P3);
    {tikz_them}
    \\fill (A) circle (1.5pt) node[left] {{$A$}};
    \\fill (B) circle (1.5pt) node[below] {{$B$}};
    \\fill (C) circle (1.5pt) node[right] {{$C$}};
    \\fill (S) circle (1.5pt) node[above] {{$S$}};
    \\fill (P1) circle (1.5pt) node[left] {{${p1}$}};
    \\fill (P2) circle (1.5pt) node[above right] {{${p2}$}};
    \\fill (P3) circle (1.5pt) node[right] {{${p3}$}};
    \\end{{tikzpicture}}
    \\end{{center}}"""
        noidungcauhoi = f"Cho hình chóp $S.ABC$. Gọi ${p1}, {p2}, {p3}$ lần lượt là trung điểm của $SA, SB, SC$. Tìm ảnh của $\\triangle {p1}{p2}{p3}$ trong phép chiếu song song trên $(ABC)$ theo phương ${phuong}$."
        loigiai = f"""Gọi ${q1}; {q2}$ lần lượt là trung điểm của ${canh1}$ và ${canh2}$. \\\\
    $\\Rightarrow$ Ảnh của $\\triangle {p1}{p2}{p3}$ trong phép chiếu song song trên $(ABC)$ theo phương ${phuong}$ là $\\triangle {tamgiac_anh}$.
    {tikz_code}"""
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
