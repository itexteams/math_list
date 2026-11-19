
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


def bt_dang12_p4_b5_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        pt = random.choice(['I', 'M', 'N', 'E'])
        pt_p = f"{pt}'"
        th = random.choice(['1', '2'])
        if th == '1':
            v1, v2, v1p, v2p = 'A', 'B', "A'", "B'"
            n1, n2, n1p, n2p = 'A', 'B', 'Ap', 'Bp'
        else:
            v1, v2, v1p, v2p = 'B', 'A', "B'", "A'"
            n1, n2, n1p, n2p = 'B', 'A', 'Bp', 'Ap'
        tiso_choice = random.choice([
            ("\\frac{S'}{S}", "\\frac{S'}{S} = \\frac{1}{2} = 0,5"),
            ("\\frac{S}{S'}", "\\frac{S}{S'} = 2")
        ])
        tiso_hoi, ketluan_tiso = tiso_choice
        tikz_code = f"""\\begin{{center}}
    \\begin{{tikzpicture}}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=0.85]
    \\coordinate (Ap) at (0,0);
    \\coordinate (Bp) at (4.5,0);
    \\coordinate (Cp) at (1.5,-1.5);
    \\coordinate (A) at (0.5,3.2);
    \\coordinate (B) at (5,3.2);
    \\coordinate (C) at (2,1.7);
    \\coordinate (I) at ($(A)!0.5!(B)$);
    \\coordinate (Ip) at ($(Ap)!0.5!(Bp)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(A) (Ap)--(Cp)--(Bp) (A)--(Ap) (B)--(Bp) (C)--(Cp) ({n1})--(Cp);
    \\draw[line width=1pt, dashed] (Ap)--(Bp) (I)--({n2p}) ({n1})--(Ip) (Cp)--(Ip);
    \\fill (A) circle (1.5pt) node[above left] {{$A$}};
    \\fill (B) circle (1.5pt) node[above right] {{$B$}};
    \\fill (C) circle (1.5pt) node[above] {{$C$}};
    \\fill (Ap) circle (1.5pt) node[left] {{$A'$}};
    \\fill (Bp) circle (1.5pt) node[right] {{$B'$}};
    \\fill (Cp) circle (1.5pt) node[below] {{$C'$}};
    \\fill (I) circle (1.5pt) node[above] {{${pt}$}};
    \\fill (Ip) circle (1.5pt) node[above right] {{${pt_p}$}};
    \\end{{tikzpicture}}
    \\end{{center}}"""
        noidungcauhoi = f"Cho hình lăng trụ $ABC.A'B'C'$, gọi ${pt}$ là trung điểm $AB$. Gọi $S, S'$ lần lượt là diện tích của tam giác $\\Delta ABC$ và hình chiếu của tam giác ${v1}{v1p}C'$ lên mặt phẳng $(A'B'C')$ theo phương ${pt}{v2p}$. Khi đó tỉ số ${tiso_hoi}$ bằng bao nhiêu?"
        loigiai = f"""Lấy ${pt_p}$ là trung điểm $A'B'$. \\\\
    Ta có $\\begin{{cases}} {v1}{pt} \\parallel {pt_p}{v2p} \\\\ {v1}{pt} = {pt_p}{v2p} = \\frac{{1}}{{2}}AB \\end{{cases}} \\Rightarrow {v1}{pt}{v2p}{pt_p}$ là hình bình hành. \\\\
    $\\Rightarrow {v1}{pt_p} \\parallel {pt}{v2p} \\Rightarrow$ hình chiếu song song của ${v1}$ lên $(A'B'C')$ theo phương ${pt}{v2p}$ là ${pt_p}$. \\\\
    $\\Rightarrow$ hình chiếu của $\\Delta {v1}{v1p}C'$ lên $(A'B'C')$ theo phương ${pt}{v2p}$ là $\\Delta {pt_p}{v1p}C'$. \\\\
    Vì ${pt_p}$ là trung điểm $A'B'$ nên $S' = S_{{\\Delta {pt_p}{v1p}C'}} = \\frac{{1}}{{2}}S_{{\\Delta A'B'C'}} = \\frac{{1}}{{2}}S_{{\\Delta ABC}} = \\frac{{1}}{{2}}S$. \\\\
    $\\Rightarrow {ketluan_tiso}$.
    {tikz_code}"""
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
