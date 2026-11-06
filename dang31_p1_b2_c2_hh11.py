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


def bt_dang31_p1_b2_c2_hh11(self):
            # Khai báo biến
            # - Cách 2: Trộn thứ tự các phương án đúng/sai.

            vertices = ['B', 'C']
            random.shuffle(vertices)
            V1 = vertices[0] # Giả sử là B
            V2 = vertices[1] # Giả sử là C

            # M là trung điểm của AV1 (ví dụ AB)
            # N là trung điểm của SV1 (ví dụ SB)

            # Bước 4: Điều chỉnh phương án sai không trùng đáp án đúng
            # Các mệnh đề ĐÚNG:
            # 1. CV2 \perp SV1 (Ví dụ CM \perp SB)
            # 2. CV2 \perp AN  (Ví dụ CM \perp AN)
            # 3. MN \perp CV2  (Ví dụ MN \perp MC)
            # Mệnh đề SAI: 
            # 4. AN \perp V1V2 (Ví dụ AN \perp BC)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.A''' + V1 + V2 + '''$ có đáy $A''' + V1 + V2 + '''$ là tam giác đều, cạnh bên $SA$ vuông góc với đáy. Gọi $M, N$ lần lượt là trung điểm của $A''' + V1 + '''$ và $S''' + V1 + '''$. Trong các mệnh đề sau, mệnh đề nào là mệnh đề sai?''')

            # Hình vẽ TikZ
            hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, line join=round, line cap=round, line width=1pt]
                \\coordinate (A) at (0,0);
                \\coordinate (V1) at (1,-1.5);
                \\coordinate (V2) at (4,0);
                \\coordinate (S) at (0,3.5);
                \\coordinate (M) at ($(A)!0.5!(V1)$);
                \\coordinate (N) at ($(S)!0.5!(V1)$);
                \\draw [dashed] (A)--(V2) (V2)--(M);
                \\draw (S)--(A)--(V1)--(V2)--(S) (S)--(V1) (A)--(N);
                \\draw (M)--(N);
                \\node [left] at (A) {$A$};
                \\node [below] at (V1) {$''' + V1 + '''$};
                \\node [right] at (V2) {$''' + V2 + '''$};
                \\node [above] at (S) {$S$};
                \\node [below left] at (M) {$M$};
                \\node [right] at (N) {$N$};
                \\fill (A); \\fill (V1); \\fill (V2) ;
                \\fill (S) ; \\fill (M) ; \\fill (N) ;
            \\end{tikzpicture}
            \\end{center}''')

            # Các đáp án
            da_dung_1 = '''$''' + V2 + '''M \\perp S''' + V1 + '''$'''
            da_dung_2 = '''$''' + V2 + '''M \\perp AN$'''
            da_dung_3 = '''$MN \\perp M''' + V2 + '''$'''
            da_sai    = '''\\True $AN \\perp ''' + V1 + V2 + '''$'''

            list_ans = [da_dung_1, da_dung_2, da_dung_3, da_sai]
            random.shuffle(list_ans)

            # Nội dung lời giải chi tiết
            loigiai = ('''Ta có: 
            $\\begin{cases} ''' + V2 + '''M \\perp A''' + V1 + ''' \\\\ ''' + V2 + '''M \\perp SA \\end{cases} \\Rightarrow  ''' + V2 + '''M \\perp \\left( SA''' + V1 + ''' \\right) \\Rightarrow  ''' + V2 + '''M \\perp S''' + V1 + '''.$ \\\\
            Mà $AN \\subset \\left( SA''' + V1 + ''' \\right) \\Rightarrow  ''' + V2 + '''M \\perp AN$. \\\\
            Mặt khác:
            $\\begin{cases} MN // SA \\\\ SA \\perp \\left( A''' + V1 + V2 + ''' \\right) \\end{cases} \\Rightarrow  MN \\perp \\left( A''' + V1 + V2 + ''' \\right)$. \\\\
            Vì $\\begin{cases} MN \\perp \\left( A''' + V1 + V2 + ''' \\right) \\\\ ''' + V2 + '''M \\subset \\left( A''' + V1 + V2 + ''' \\right) \\end{cases} \\Rightarrow  MN \\perp M''' + V2 + '''.$''')

            # Xuất câu trắc nghiệm theo đúng cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' 
                '\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + hinh_ve + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

