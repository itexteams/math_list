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


def bt_dang50_p1_b1_c1_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random 4 giá trị hoành độ tăng dần: x1 < x2 < x3 < x4
        x1 = random.randint(-4, -1)
        x2 = x1 + random.randint(1, 2)
        x3 = x2 + random.randint(1, 2)
        x4 = x3 + random.randint(1, 2)

        # Xây dựng bảng xét dấu f'(x) bằng TikZ có đóng khung viền ngoài
        bang_xet_dau = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) rectangle (10.5,1.6);
        \\draw[line width=1pt] (0,0.8) -- (10.5,0.8);
        \\draw[line width=1pt] (1.6,0) -- (1.6,1.6);
        \\draw[line width=1pt] (5.15,0) -- (5.15,0.8);
        \\draw[line width=1pt] (5.25,0) -- (5.25,0.8);
        \\draw[line width=1pt] (6.95,0) -- (6.95,0.8);
        \\draw[line width=1pt] (7.05,0) -- (7.05,0.8);
        \\node at (0.8,1.2) {$x$};
        \\node at (0.8,0.4) {$f'(x)$};
        \\node at (2.1,1.2) {$-\\infty$};
        \\node at (3.6,1.2) {$%s$};
        \\node at (5.2,1.2) {$%s$};
        \\node at (7.0,1.2) {$%s$};
        \\node at (8.6,1.2) {$%s$};
        \\node at (9.9,1.2) {$+\\infty$};
        \\node at (2.85,0.4) {$-$};
        \\node at (3.6,0.4) {$0$};
        \\node at (4.4,0.4) {$+$};
        \\node at (6.1,0.4) {$+$};
        \\node at (7.8,0.4) {$-$};
        \\node at (8.6,0.4) {$0$};
        \\node at (9.3,0.4) {$+$};
    \\end{tikzpicture}
    \\end{center}''' % (latex(x1), latex(x2), latex(x3), latex(x4)))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{R}$ và có bảng xét dấu $f'(x)$ như sau:
    %s
    Kết luận nào sau đây đúng?''' % bang_xet_dau)

        # Đáp án đúng: Hàm số có 2 điểm cực tiểu (tại x1 và x4)
        da = 'Hàm số có $2$ điểm cực tiểu'
        da_d = ('\\True ' + str(da))

        # Các phương án sai
        s = [
            'Hàm số có $4$ điểm cực trị',
            'Hàm số có $2$ điểm cực đại',
            'Hàm số có $2$ điểm cực trị',
            'Hàm số có $1$ điểm cực trị',
            'Hàm số có $3$ điểm cực tiểu',
            'Hàm số không có cực trị'
        ]
        random.shuffle(s)
        da_s1 = str(s[0])
        da_s2 = str(s[1])
        da_s3 = str(s[2])

        # Đưa các đáp án vào danh sách và xáo trộn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải chi tiết
        loigiai = ('''Hàm số $y=f(x)$ liên tục trên $\\mathbb{R}$.\\\\
    Dựa vào bảng xét dấu của $f'(x)$, ta thấy:\\\\
    - Khi qua điểm $x=%s$, đạo hàm $f'(x)$ đổi dấu từ âm sang dương nên $x=%s$ là một điểm cực tiểu của hàm số.\\\\
    - Khi qua điểm $x=%s$, đạo hàm $f'(x)$ không đổi dấu (cùng mang dấu dương) nên $x=%s$ không là điểm cực trị của hàm số.\\\\
    - Khi qua điểm $x=%s$, đạo hàm $f'(x)$ đổi dấu từ dương sang âm và hàm số liên tục tại điểm này nên $x=%s$ là điểm cực đại của hàm số.\\\\
    - Khi qua điểm $x=%s$, đạo hàm $f'(x)$ đổi dấu từ âm sang dương nên $x=%s$ là một điểm cực tiểu của hàm số.\\\\
    Như vậy, hàm số có $1$ điểm cực đại (tại $x=%s$) và có $2$ điểm cực tiểu (tại $x=%s$ và $x=%s$).\\\\
    Do đó, kết luận đúng là: Hàm số có $2$ điểm cực tiểu.'''
                   % (latex(x1), latex(x1),
                      latex(x2), latex(x2),
                      latex(x3), latex(x3),
                      latex(x4), latex(x4),
                      latex(x3), latex(x1), latex(x4)))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\choice \n'
               '{' + str(list_1[1]) + '}\n'
               '{' + str(list_1[2]) + '}\n'
               '{' + str(list_1[3]) + '}\n'
               '{' + str(list_1[0]) + '}\n'
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

