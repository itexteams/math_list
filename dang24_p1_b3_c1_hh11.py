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


def bt_dang24_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2', '3']
    dang = random.choice(lisdang)

    # Random tên đường thẳng và mặt phẳng
    cap_duong = random.choice([('a', 'b', 'c'), ('d_1', 'd_2', 'd_3'), ('d', '\\Delta', 'd\''), ('p', 'q', 'r')])
    d1, d2, d3 = cap_duong[0], cap_duong[1], cap_duong[2]

    cap_mp = random.choice([('\\alpha', '\\beta'), ('P', 'Q'), ('\\alpha', 'P')])
    mp1, mp2 = cap_mp[0], cap_mp[1]

    # TikZ vẽ hình minh họa giống 100% hình gốc trong đề bài
    hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (0.5,2.4) -- (4,2.4) node[above, midway] {$%s$};
    \\coordinate (M1) at (0,0);
    \\coordinate (M2) at (3.5,0);
    \\coordinate (M3) at (4.4,1.8);
    \\coordinate (M4) at (0.9,1.8);
    \\draw[line width=1pt] (M1) -- (M2) -- (M3) -- (M4) -- cycle;
    \\draw[line width=1pt] (0.45,0) arc (0:63:0.45);
    \\node at (0.3,0.2) {$%s$};
    \\draw[line width=1pt] (0.85,0.9) -- (3.5,0.9) node[above right] {$%s$};
    \\draw[line width=1pt] (1.3,0.3) -- (3.3,1.5);
    \\fill (2.3,0.9) circle (1pt);
    \\node[below right] at (1.3,0.3) {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (d1, mp1, d3, d2))

    if dang == '1':
        # Dạng 1: Giống hệt câu 10 gốc trong ảnh
        noidungcauhoi = ('''Có bao nhiêu mặt phẳng song song với cả hai đường thẳng chéo nhau $%s$ và $%s$?'''
                         % (d1, d2))

        da = 'Vô số'

        s = [
            '$1$',
            '$2$',
            '$3$',
            '$0$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        loigiai = ('''%s
    Gọi $%s$ và $%s$ là hai đường thẳng chéo nhau, $%s$ là đường thẳng song song với $%s$ và cắt $%s$. \\\\
    Gọi $(%s) = \\text{mp}(%s, %s)$. Do $%s // %s$ nên ta có $%s // (%s)$. \\\\
    Giả sử $(%s) // (%s)$. Mà $%s \\subset (%s)$. Suy ra $%s // (%s)$. \\\\
    Mặt khác $%s // (%s) \\Rightarrow %s // (%s)$. \\\\
    Ta có vô số mặt phẳng $(%s) // (%s)$. \\\\
    Vậy có vô số mặt phẳng song song với cả hai đường thẳng chéo nhau.'''
                   % (hinh_tikz, d1, d2, d3, d1, d2, mp1, d2, d3, d1, d3, d1, mp1, mp1, mp2, d2, mp1, d2, mp2, d1, mp1, d1, mp2, mp2, mp1))

    elif dang == '2':
        # Dạng 2: Có bao nhiêu mặt phẳng chứa đường thẳng này và song song với đường thẳng kia?
        noidungcauhoi = ('''Cho hai đường thẳng chéo nhau $%s$ và $%s$. Có bao nhiêu mặt phẳng chứa đường thẳng $%s$ và song song với đường thẳng $%s$?'''
                         % (d1, d2, d1, d2))

        da = '$1$'

        s = [
            '$2$',
            '$3$',
            'Vô số',
            '$0$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        loigiai = ('''%s
    Lấy một điểm $M$ tùy ý trên đường thẳng $%s$. Qua $M$ dựng đường thẳng $%s\' // %s$. \\\\
    Hai đường thẳng cắt nhau $%s$ và $%s\'$ xác định duy nhất một mặt phẳng $(%s)$. \\\\
    Mặt phẳng $(%s)$ này chứa đường thẳng $%s$ và song song với đường thẳng $%s$. \\\\
    Vậy có duy nhất $1$ mặt phẳng chứa đường thẳng $%s$ và song song với đường thẳng $%s$.'''
                   % (hinh_tikz, d1, d2, d2, d1, d2, mp1, mp1, d1, d2, d1, d2))

    elif dang == '3':
        # Dạng 3: Có bao nhiêu cặp mặt phẳng song song lần lượt chứa hai đường thẳng chéo nhau?
        noidungcauhoi = ('''Cho hai đường thẳng chéo nhau $%s$ và $%s$. Có bao nhiêu cặp mặt phẳng song song với nhau lần lượt chứa hai đường thẳng $%s$ và $%s$?'''
                         % (d1, d2, d1, d2))

        da = '$1$'

        s = [
            '$2$',
            '$3$',
            'Vô số',
            '$0$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        loigiai = ('''%s
    Theo tính chất hình học không gian: \\\\
    Qua đường thẳng $%s$ có duy nhất một mặt phẳng $(%s)$ song song với $%s$. \\\\
    Qua đường thẳng $%s$ có duy nhất một mặt phẳng $(%s)$ song song với $%s$. \\\\
    Khi đó hai mặt phẳng $(%s)$ và $(%s)$ song song với nhau. \\\\
    Vậy có duy nhất $1$ cặp mặt phẳng song song với nhau lần lượt chứa hai đường thẳng chéo nhau $%s$ và $%s$.'''
                   % (hinh_tikz, d1, mp1, d2, d2, mp2, d1, mp1, mp2, d1, d2))

    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choice \n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '{' + str(list_1[0]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

