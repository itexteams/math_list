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


def bt_dang38_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random tên các đỉnh của tứ diện và các điểm
        pool = ['A', 'B', 'C', 'D', 'S', 'M', 'N', 'E', 'O', 'F', 'K', 'H', 'P', 'Q', 'R']
        vertices = random.sample(pool, 4)
        V1, V2, V3, V4 = vertices

        pool = [x for x in pool if x not in vertices]
        P1, P2 = random.sample(pool, 2)

        pool = [x for x in pool if x not in [P1, P2]]
        P3 = random.choice(pool)
        pool.remove(P3)
        P4 = random.choice(pool)
        pool.remove(P4)
        P5 = random.choice(pool)
        pool.remove(P5)
        P6 = random.choice(pool)

        # Câu hỏi
        noidungcauhoi = ('''Cho tứ diện $%s%s%s%s$. Gọi $%s, %s$ là hai điểm lần lượt nằm trên các cạnh $%s%s, %s%s$ và $%s%s$ không song song với $%s%s$. Đường thẳng $%s%s$ cắt $%s%s$ tại $%s$. Gọi $%s$ là điểm nằm trong tam giác $%s%s%s$. Giao điểm của đường thẳng $%s%s$ và mặt phẳng $(%s%s%s)$ là'''
                         %(V1, V2, V3, V4, P1, P2, V1, V2, V1, V4, P1, P2, V2, V4, P1, P2, V2, V4, P3, P4, V2, V3, V4, V3, V4, P4, P1, P2))

        # Các đáp án
        da_d = ('\\True $%s$ ($%s$ là giao điểm của $%s%s$ và $%s%s$)' % (P5, P5, P4, P3, V3, V4))
        das1 = 'Điểm $%s$' % (P3)
        das2 = 'Điểm $%s$' % (V4)
        das3 = '$%s$ ($%s$ là giao điểm của $%s%s$ và $%s%s$)' % (P6, P6, P4, V2, V3, V4)

        list_1 = [da_d, das1, das2, das3]
        random.shuffle(list_1)

        # Mã TikZ
        tikz_code = ('''\\begin{center}
           \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (V2) at (0,0);
            \\coordinate (V4) at (4,0);
            \\coordinate (V1) at (1.2,3.5);
            \\coordinate (V3) at (1.4,-1.8);
            \\coordinate (P1) at ($(V1)!0.3!(V2)$);
            \\coordinate (P3) at (7,0); 
            \\coordinate (P2) at (intersection of P1--P3 and V1--V4); 
            \\coordinate (P4) at (2,-0.5); 
            \\coordinate (P5) at (intersection of P4--P3 and V3--V4); 
            \\draw[line width=1pt] (V1)--(V2) (V1)--(V3) (V1)--(V4) (V2)--(V3)--(V4) (P2)--(P3) (V4)--(P3) (P5)--(P3);
            \\draw[line width=1pt, dashed] (V2)--(V4) (P1)--(P2) (P1)--(P4)--(P2) (P4)--(P5);
            \\fill (V1) circle (1pt) node[above] {$%s$};
            \\fill (V2) circle (1pt) node[left] {$%s$};
            \\fill (V3) circle (1pt) node[below] {$%s$};
            \\fill (V4) circle (1pt) node[above right] {$%s$};
            \\fill (P1) circle (1pt) node[left] {$%s$};
            \\fill (P2) circle (1pt) node[above right] {$%s$};
            \\fill (P3) circle (1pt) node[above] {$%s$};
            \\fill (P4) circle (1pt) node[left] {$%s$};
            \\fill (P5) circle (1pt) node[below right] {$%s$};
           \\end{tikzpicture}
           \\end{center}''' % (V1, V2, V3, V4, P1, P2, P3, P4, P5))

        # Nội dung lời giải
        loigiai = ('''%s
            Trong mặt phẳng $(%s%s%s)$, gọi $%s$ là giao điểm của $%s%s$ và $%s%s$. \\\\
            Ta có: $\\begin{cases} %s \\in %s%s \\\\ %s \\in %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow (%s%s%s) \\cap %s%s = \\{%s\\}$.'''
            % (tikz_code, V2, V3, V4, P5, V3, V4, P4, P3, P5, V3, V4, P5, P4, P3, P4, P1, P2, P4, P1, P2, V3, V4, P5))

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

