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


def bt_dang37_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random tên các đỉnh của tứ diện (4 đỉnh)
        vertices = random.sample(['A', 'B', 'C', 'D', 'S', 'P', 'Q', 'R', 'K', 'H'], 4)
        v1, v2, v3, v4 = vertices

        # Random tên các điểm trên cạnh (3 điểm)
        points_pool = [p for p in ['M', 'N', 'E', 'F', 'I', 'J', 'G', 'L'] if p not in vertices]
        points = random.sample(points_pool, 3)
        p1, p2, pe = points

        # Câu hỏi
        noidungcauhoi = ('''Cho bốn điểm $%s, %s, %s, %s$ không cùng nằm trong một mặt phẳng. Trên $%s%s, %s%s$ lần lượt lấy các điểm $%s$ và $%s$ sao cho $%s%s$ cắt $%s%s$ tại $%s$. Điểm $%s$ không thuộc mặt phẳng nào sau đây?'''
                         % (v1, v2, v3, v4, v1, v2, v1, v4, p1, p2, p1, p2, v2, v4, pe, pe))

        # Các đáp án
        da_d = ('\\True $(%s%s%s)$' % (v1, v3, v4))
        das1 = ('$(%s%s%s)$' % (v2, v3, v4))
        das2 = ('$(%s%s%s)$' % (v1, v2, v4))
        das3 = ('$(%s%s%s)$' % (v3, p1, p2))

        list_1 = [da_d, das1, das2, das3]
        random.shuffle(list_1)

        # Vẽ hình TikZ cho lời giải
        tikz_code = ('''\\begin{center}
           \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (3,3.5);
            \\coordinate (B) at (0,0);
            \\coordinate (C) at (2,-1.5);
            \\coordinate (D) at (5,0);
            \\coordinate (M) at ($(A)!0.4!(B)$);
            \\coordinate (N) at ($(A)!0.6!(D)$);
            \\coordinate (E) at (intersection of M--N and B--D);
            \\draw[line width=1pt] (A)--(B) (A)--(C) (A)--(D) (B)--(C)--(D) (N)--(E) (D)--(E);
            \\draw[line width=1pt, dashed] (B)--(D) (M)--(N);
            \\fill (A) circle (1pt) node[above] {$%s$};
            \\fill (B) circle (1pt) node[left] {$%s$};
            \\fill (C) circle (1pt) node[below] {$%s$};
            \\fill (D) circle (1pt) node[below right] {$%s$};
            \\fill (M) circle (1pt) node[above left] {$%s$};
            \\fill (N) circle (1pt) node[above right] {$%s$};
            \\fill (E) circle (1pt) node[above] {$%s$};
           \\end{tikzpicture}
           \\end{center}''' % (v1, v2, v3, v4, p1, p2, pe))

        # Nội dung lời giải
        loigiai = ('''%s
            Ta có: \\\\
            $%s \\in %s%s \\Rightarrow %s \\in (%s%s%s)$ và $(%s%s%s)$. \\\\
            $%s \\in %s%s \\Rightarrow %s \\in (%s%s%s)$. \\\\
            Vậy $%s$ không thuộc mặt phẳng $(%s%s%s)$.'''
                % (tikz_code, 
                   pe, v2, v4, pe, v2, v3, v4, v1, v2, v4,
                   pe, p1, p2, pe, v3, p1, p2,
                   pe, v1, v3, v4))

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

