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


def bt_dang36_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random tên các đỉnh của hình chóp (1 đỉnh chóp, 4 đỉnh đáy, 1 tâm)
        pool = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'M', 'N', 'P', 'Q', 'S', 'V', 'X', 'Y', 'Z']
        points = random.sample(pool, 6)

        Top = points[0] # Đỉnh S
        V1 = points[1]  # Đỉnh A
        V2 = points[2]  # Đỉnh B
        V3 = points[3]  # Đỉnh C
        V4 = points[4]  # Đỉnh D
        O = points[5]   # Tâm O

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $%s.%s%s%s%s$ có đáy $%s%s%s%s$ là hình bình hành tâm $%s$. Đường thẳng $%s%s$ không phải là giao tuyến của hai mặt phẳng nào sau đây?'''
                         %(Top, V1, V2, V3, V4, V1, V2, V3, V4, O, Top, V1))

        # Các đáp án trắc nghiệm
        da_d = ('\\True $({%s%s%s})$ và $({%s%s%s})$' % (Top, V1, V3, Top, V3, V4))
        das1 = '$({%s%s%s})$ và $({%s%s%s})$' % (Top, V1, V2, Top, V1, V3)
        das2 = '$({%s%s%s})$ và $({%s%s%s})$' % (Top, O, V3, Top, V1, V2)
        das3 = '$({%s%s%s}) \\cap ({%s%s%s})$' % (Top, V1, V3, Top, V1, V4)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, das1, das2, das3]
        random.shuffle(list_1)

        # Mã TikZ vẽ hình
        tikz_code = ('''\\begin{center}
           \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (1.5,1.5);
            \\coordinate (B) at (0,0);
            \\coordinate (C) at (4,0);
            \\coordinate (D) at (5.5,1.5);
            \\coordinate (S) at (2.5,5);
            \\coordinate (O) at ($(A)!0.5!(C)$);
            \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D);
            \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O);
            \\fill (A) circle (1pt) node[left] {$%s$};
            \\fill (B) circle (1pt) node[below left] {$%s$};
            \\fill (C) circle (1pt) node[below right] {$%s$};
            \\fill (D) circle (1pt) node[right] {$%s$};
            \\fill (S) circle (1pt) node[above] {$%s$};
            \\fill (O) circle (1pt) node[above right] {$%s$};
           \\end{tikzpicture}
           \\end{center}''' % (V1, V2, V3, V4, Top, O))

        # Nội dung lời giải
        loigiai = ('''%s 
            Ta có: \\\\
            $\\begin{cases} %s \\in ({%s%s%s}) \\cap ({%s%s%s}) \\\\ %s \\in ({%s%s%s}) \\cap ({%s%s%s}) \\end{cases} \\Rightarrow ({%s%s%s}) \\cap ({%s%s%s}) = %s%s$. \\\\
            Vậy $%s%s$ không phải là giao tuyến của hai mặt phẳng $({%s%s%s})$ và $({%s%s%s})$.'''
            %(tikz_code, 
              Top, Top, V1, V3, Top, V3, V4, 
              V3, Top, V1, V3, Top, V3, V4, 
              Top, V1, V3, Top, V3, V4, Top, V3, 
              Top, V1, Top, V1, V3, Top, V3, V4))

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

