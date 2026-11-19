
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


def bt_dang10_p4_b5_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        p1, p2 = random.choice([('M', 'N'), ('E', 'F'), ('P', 'Q')])
        q1, q2 = random.choice([('I', 'J'), ('H', 'K'), ('U', 'V')])
        duong_thang = random.choice(['\\Delta', 'd'])
        tiso_choice = random.choice([
            (f"\\frac{{{q1}{p1}}}{{{q1}{q2}}}", "1", f"{q1}{p1} = {q1}{q2} \\Rightarrow \\frac{{{q1}{p1}}}{{{q1}{q2}}} = 1"),
            (f"\\frac{{{q1}{p1}}}{{{q2}{p1}}}", "\\frac{1}{2}", f"{q1}{p1} = {q1}{q2} \\Rightarrow \\frac{{{q1}{p1}}}{{{q2}{p1}}} = \\frac{1}{2}"),
            (f"\\frac{{{q1}{q2}}}{{{q2}{p1}}}", "\\frac{1}{2}", f"{q1}{p1} = {q1}{q2} \\Rightarrow \\frac{{{q1}{q2}}}{{{q2}{p1}}} = \\frac{1}{2}"),
            (f"\\frac{{{q2}{p1}}}{{{q1}{p1}}}", "2", f"{q1}{p1} = {q1}{q2} \\Rightarrow \\frac{{{q2}{p1}}}{{{q1}{p1}}} = 2")
        ])
        tiso_hoi, kq, ketluan_tiso = tiso_choice
        tikz_code = f"""\\begin{{center}}
    \\begin{{tikzpicture}}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=0.85]
    \\coordinate (A) at (0,0);
    \\coordinate (D) at (4,0);
    \\coordinate (B) at (1.3,1.2);
    \\coordinate (C) at (5.3,1.2);
    \\coordinate (Ap) at (0,3);
    \\coordinate (Dp) at (4,3);
    \\coordinate (Bp) at (1.3,4.2);
    \\coordinate (Cp) at (5.3,4.2);
    \\coordinate (M) at ($(C)!0.5!(D)$);
    \\coordinate (N) at ($(C)!0.5!(Cp)$);
    \\coordinate (Np) at ($(C)!-0.5!(D)$);
    \\coordinate (Ip) at ($(B)!0.5!(M)$);
    \\coordinate (I) at ($(A)!0.5!(N)$);
    \\coordinate (J) at ($(Ap)!0.5!(B)$);
    \\coordinate (Delta1) at ($(M)!-0.25!(J)$);
    \\coordinate (Delta2) at ($(J)!-0.25!(M)$);
    \\draw[line width=1pt] (A)--(D)--(C)--(Cp)--(Dp)--(Ap)--(A) (D)--(Dp) (Ap)--(Bp)--(Cp) (Dp)--(C) (N)--(Np)--(C) (M)--(Delta1) (J)--(Delta2);
    \\draw[line width=1pt, dashed] (A)--(B)--(C) (B)--(Bp) (Ap)--(B) (A)--(N) (A)--(Np) (B)--(M) (I)--(Ip) (M)--(J);
    \\fill (A) circle (1.5pt) node[below left] {{$A$}};
    \\fill (B) circle (1.5pt) node[left] {{$B$}};
    \\fill (C) circle (1.5pt) node[below right] {{$C$}};
    \\fill (D) circle (1.5pt) node[below] {{$D$}};
    \\fill (Ap) circle (1.5pt) node[left] {{$A'$}};
    \\fill (Bp) circle (1.5pt) node[above] {{$B'$}};
    \\fill (Cp) circle (1.5pt) node[above right] {{$C'$}};
    \\fill (Dp) circle (1.5pt) node[above] {{$D'$}};
    \\fill (M) circle (1.5pt) node[below] {{${p1}$}};
    \\fill (N) circle (1.5pt) node[right] {{${p2}$}};
    \\fill (Np) circle (1.5pt) node[right] {{${p2}'$}};
    \\fill (I) circle (1.5pt) node[above] {{${q1}$}};
    \\fill (Ip) circle (1.5pt) node[below] {{${q1}'$}};
    \\fill (J) circle (1.5pt) node[above right] {{${q2}$}};
    \\node[above] at (Delta1) {{${duong_thang}$}};
    \\end{{tikzpicture}}
    \\end{{center}}"""
        noidungcauhoi = f"Cho hình hộp $ABCD.A'B'C'D'$. Gọi ${p1}, {p2}$ lần lượt là trung điểm của $CD$ và $CC'$. Gọi ${duong_thang}$ là đường thẳng đi qua ${p1}$ đồng thời cắt $A{p2}$ và $A'B$. Gọi ${q1}, {q2}$ lần lượt là giao điểm của ${duong_thang}$ với $A{p2}$ và $A'B$. Hãy tính tỉ số ${tiso_hoi}$."
        loigiai = f"""Xét phép chiếu song song lên $(ABCD)$ theo phương chiếu $A'B$. \\\\
    Khi đó ${q2}, {q1}, {p1}$ lần lượt có hình chiếu là $B, {q1}', {p1}$. \\\\
    Do ${q2}, {q1}, {p1}$ thẳng hàng nên $B, {q1}', {p1}$ cũng thẳng hàng. \\\\
    Gọi ${p2}'$ là hình chiếu của ${p2}$ thì $A{p2}'$ là hình chiếu của $A{p2}$. \\\\
    Vì ${q1} \\in A{p2} \\Rightarrow {q1}' \\in A{p2}' \\Rightarrow {q1}' = B{p1} \\cap A{p2}'$. \\\\
    Ta có ${p1}C = C{p2}'$ suy ra ${p1}{p2}' = CD = AB$. \\\\
    Do đó ${q1}'$ là trung điểm của $B{p1}$. \\\\
    Mặt khác ${q1}{q1}' \\parallel {q2}B$ nên ${q1}{q1}'$ là đường trung bình của $\\Delta {p1}B{q2} \\Rightarrow {ketluan_tiso}$.
    {tikz_code}"""
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
