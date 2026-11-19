
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


def bt_dang11_p4_b5_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        p1, p2 = random.choice([('M', 'N'), ('P', 'Q'), ('E', 'F'), ('H', 'K')])
        cap_canh = random.choice([('AB', 'CD', 'A', 'B', 'C', 'D', 'left', 'right'), ('AD', 'BC', 'A', 'D', 'B', 'C', 'above', 'below')])
        c1, c2, v1, v2, v3, v4, pos1, pos2 = cap_canh
        huong = random.choice([('A', "C'", 'A', 'Cp'), ('B', "D'", 'B', 'Dp'), ('C', "A'", 'C', 'Ap'), ('D', "B'", 'D', 'Bp')])
        dinh_day, dinh_tren, node_day, node_tren = huong
        tikz_code = f"""\\begin{{center}}
    \\begin{{tikzpicture}}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=0.8]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (4,0);
    \\coordinate (A) at (1.5,1.5);
    \\coordinate (D) at (5.5,1.5);
    \\coordinate (Bp) at (0,3.5);
    \\coordinate (Cp) at (4,3.5);
    \\coordinate (Ap) at (1.5,5);
    \\coordinate (Dp) at (5.5,5);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (Op) at ($(Ap)!0.5!(Cp)$);
    \\coordinate (P1) at ($({v1})!0.5!({v2})$);
    \\coordinate (P2) at ($({v3})!0.5!({v4})$);
    \\draw[line width=1pt] (B)--(C)--(D)--(Dp)--(Cp)--(Bp)--(B) (C)--(Cp) (Ap)--(Bp) (Ap)--(Dp) (Ap)--(Cp) (Bp)--(Dp);
    \\draw[line width=1pt, dashed] (A)--(B) (A)--(D) (A)--(Ap) (A)--(C) (B)--(D) (O)--(Op) (P1)--(P2) ({node_day})--(Op) ({node_tren})--(O) ({node_tren})--(P1) ({node_tren})--(P2);
    \\fill (A) circle (1.5pt) node[left] {{$A$}};
    \\fill (B) circle (1.5pt) node[below left] {{$B$}};
    \\fill (C) circle (1.5pt) node[below] {{$C$}};
    \\fill (D) circle (1.5pt) node[right] {{$D$}};
    \\fill (Ap) circle (1.5pt) node[above] {{$A'$}};
    \\fill (Bp) circle (1.5pt) node[left] {{$B'$}};
    \\fill (Cp) circle (1.5pt) node[above] {{$C'$}};
    \\fill (Dp) circle (1.5pt) node[above right] {{$D'$}};
    \\fill (O) circle (1.5pt) node[below] {{$O$}};
    \\fill (Op) circle (1.5pt) node[above] {{$O'$}};
    \\fill (P1) circle (1.5pt) node[{pos1}] {{${p1}$}};
    \\fill (P2) circle (1.5pt) node[{pos2}] {{${p2}$}};
    \\end{{tikzpicture}}
    \\end{{center}}"""
        noidungcauhoi = f"Cho hình hộp chữ nhật $ABCD.A'B'C'D'$. Gọi $O = AC \\cap BD$ và $O' = A'C' \\cap B'D'$. Điểm ${p1}, {p2}$ lần lượt là trung điểm của ${c1}$ và ${c2}$. Qua phép chiếu song song theo phương ${dinh_day}O'$ lên mặt phẳng $(ABCD)$. Xác định hình chiếu của tam giác ${dinh_tren}{p1}{p2}$."
        loigiai = f"""Ta có: $O'{dinh_tren} = {dinh_day}O$ và $O'{dinh_tren} \\parallel {dinh_day}O$ nên tứ giác $O'{dinh_tren}O{dinh_day}$ là hình bình hành $\\Rightarrow O'{dinh_day} \\parallel {dinh_tren}O$. \\\\
    Do đó hình chiếu của điểm ${dinh_tren}$ qua phép chiếu song song theo phương $O'{dinh_day}$ lên $(ABCD)$ là điểm $O$. \\\\
    Mặt khác điểm ${p1}$ và ${p2}$ thuộc $(ABCD)$ nên hình chiếu của ${p1}$ và ${p2}$ qua phép chiếu song song theo phương $O'{dinh_day}$ lên mặt phẳng $(ABCD)$ lần lượt là điểm ${p1}$ và ${p2}$. \\\\
    Mà $O$ là trung điểm của ${p1}{p2}$ nên $O \\in {p1}{p2}$. \\\\
    Vậy qua phép chiếu song song theo phương ${dinh_day}O'$ lên $(ABCD)$ thì hình chiếu của $\\Delta {dinh_tren}{p1}{p2}$ là đoạn thẳng ${p1}{p2}$.
    {tikz_code}"""
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
