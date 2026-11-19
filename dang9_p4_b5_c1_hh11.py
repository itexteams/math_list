
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


def bt_dang9_p4_b5_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        p1, p2 = random.choice([('M', 'N'), ('E', 'F'), ('P', 'Q'), ('I', 'J')])
        kp = random.choice(['K', 'H', 'T'])
        tiso_choice = random.choice([
            (f"\\frac{{{p1}A}}{{{p1}C'}}", f"\\frac{{{p1}A}}{{{p1}C'}} = \\frac{{{p2}{kp}}}{{{p2}C'}} = \\frac{{{kp}B'}}{{C'D'}} = 2"),
            (f"\\frac{{{p1}C'}}{{{p1}A}}", f"\\frac{{{p1}A}}{{{p1}C'}} = \\frac{{{p2}{kp}}}{{{p2}C'}} = \\frac{{{kp}B'}}{{C'D'}} = 2 \\Rightarrow \\frac{{{p1}C'}}{{{p1}A}} = \\frac{{1}}{{2}}"),
            (f"\\frac{{{p1}A}}{{AC'}}", f"\\frac{{{p1}A}}{{{p1}C'}} = \\frac{{{p2}{kp}}}{{{p2}C'}} = \\frac{{{kp}B'}}{{C'D'}} = 2 \\Rightarrow \\frac{{{p1}A}}{{AC'}} = \\frac{{2}}{{3}}"),
            (f"\\frac{{{p1}C'}}{{AC'}}", f"\\frac{{{p1}A}}{{{p1}C'}} = \\frac{{{p2}{kp}}}{{{p2}C'}} = \\frac{{{kp}B'}}{{C'D'}} = 2 \\Rightarrow \\frac{{{p1}C'}}{{AC'}} = \\frac{{1}}{{3}}")
        ])
        tiso_hoi, ketluan_tiso = tiso_choice
        tikz_code = f"""\\begin{{center}}
    \\begin{{tikzpicture}}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=0.85]
    \\coordinate (A) at (0,0);
    \\coordinate (D) at (4,0);
    \\coordinate (B) at (1,1.3);
    \\coordinate (C) at (5,1.3);
    \\coordinate (Ap) at (0,3);
    \\coordinate (Dp) at (4,3);
    \\coordinate (Bp) at (1,4.3);
    \\coordinate (Cp) at (5,4.3);
    \\coordinate (K) at ($(Bp)!2!(Ap)$);
    \\coordinate (N) at ($(K)!2/3!(Cp)$);
    \\coordinate (M) at ($(A)!2/3!(Cp)$);
    \\draw[line width=1pt] (A)--(D)--(C)--(Cp)--(Dp)--(Ap)--(A) (D)--(Dp) (Ap)--(Bp)--(Cp) (Bp)--(Dp) (K)--(Ap) (K)--(A) (K)--(Cp);
    \\draw[line width=1pt, dashed] (A)--(B)--(C) (B)--(Bp) (Ap)--(B) (A)--(Cp) (M)--(N);
    \\fill (A) circle (1.5pt) node[below left] {{$A$}};
    \\fill (B) circle (1.5pt) node[left] {{$B$}};
    \\fill (C) circle (1.5pt) node[right] {{$C$}};
    \\fill (D) circle (1.5pt) node[below] {{$D$}};
    \\fill (Ap) circle (1.5pt) node[left] {{$A'$}};
    \\fill (Bp) circle (1.5pt) node[above] {{$B'$}};
    \\fill (Cp) circle (1.5pt) node[above right] {{$C'$}};
    \\fill (Dp) circle (1.5pt) node[right] {{$D'$}};
    \\fill (K) circle (1.5pt) node[left] {{${kp}$}};
    \\fill (N) circle (1.5pt) node[above] {{${p2}$}};
    \\fill (M) circle (1.5pt) node[below right] {{${p1}$}};
    \\end{{tikzpicture}}
    \\end{{center}}"""
        noidungcauhoi = f"Cho hình hộp $ABCD.A'B'C'D'$. Xác định các điểm ${p1}, {p2}$ tương ứng trên các đoạn $AC', B'D'$ sao cho ${p1}{p2}$ song song với $BA'$ và tính tỉ số ${tiso_hoi}$."
        loigiai = f"""Xét phép chiếu song song lên $(A'B'C'D')$ theo phương chiếu $BA'$. \\\\
    Ta có ${p2}$ là ảnh của ${p1}$ hay ${p2}$ chính là giao điểm của $B'D'$ và ảnh của $AC'$ qua phép chiếu này. \\\\
    Do đó ta xác định ${p1}, {p2}$ như sau: \\\\
    Trên $A'B'$ kéo dài lấy điểm ${kp}$ sao cho $A'{kp} = B'A'$ thì $ABA'{kp}$ là hình bình hành nên $A{kp} \\parallel BA'$ suy ra ${kp}$ là ảnh của $A$ qua phép chiếu song song trên. \\\\
    Gọi ${p2} = B'D' \\cap {kp}C'$. \\\\
    Đường thẳng qua ${p2}$ và song song với $A{kp}$ cắt $AC'$ tại ${p1}$. Ta có ${p1}, {p2}$ là các điểm cần xác định. \\\\
    Theo định lí Thales, ta có ${ketluan_tiso}$.
    {tikz_code}"""
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
