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


def bt_dang60_p1_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random bài toán
                # Thiết lập tọa độ để đảm bảo hình dáng đồ thị như mẫu
                x1 = random.randint(-4, -3)
                x2 = -1
                x3 = 1
                x4 = random.randint(3, 4)

                y1 = random.randint(-3, -2)
                y2 = random.randint(1, 2)
                y3 = 0 
                y4 = random.randint(3, 4)

                # TikZ code: Sử dụng %% để tránh lỗi format character của Python %
                # Cấu trúc: (x,y) -- (0,y) đảm bảo vuông góc với Oy
                # Cấu trúc: (x,y) -- (x,0) đảm bảo vuông góc với Ox
                tikz_graph = r"""\begin{tikzpicture}[scale=0.7, font=\footnotesize, line join=round, line cap=round, >=stealth]
                %% Ve he truc toa do
                \draw[->] (%d-0.8,0) -- (%d+1,0) node[below] {$x$};
                \draw[->] (0,%d-0.8) -- (0,%d+1) node[left] {$y$};
                \node[below left] at (0,0) {$O$};
                \draw[dashed] (%d,0) node[above] {$%d$} -- (%d,%d) -- (0,%d) node[right] {$%d$};
                \draw[dashed] (%d,0) node[below] {$%d$} -- (%d,%d) -- (0,%d) node[right] {$%d$};
                \node[below] at (%d,0) {$%d$};
                \draw[dashed] (%d,0) node[below] {$%d$} -- (%d,%d) -- (0,%d) node[left] {$%d$};
                \draw[thick, blue] (%d,%d) -- (%d,%d) -- (%d,%d) -- (%d,%d);
            \end{tikzpicture}""" % (x1, x4, y1, y4, 
                   x1, x1, x1, y1, y1, y1, # P1: duong tu x1 -> point -> y1
                   x2, x2, x2, y2, y2, y2, # P2: duong tu x2 -> point -> y2
                   x3, x3,               # P3: chi hien thi label x3
                   x4, x4, x4, y4, y4, y4, # P4: duong tu x4 -> point -> y4
                   x1, y1, x2, y2, x3, y3, x4, y4, # Do thi
                   ) # Cham tron

                # Bước 4: Đáp án và các phương án nhiễu
                da = 'Hàm số đồng biến trên các khoảng $(%s; %s)$ và $(%s; %s)$' % (latex(x1), latex(x2), latex(x3), latex(x4))

                s = [
                    'Hàm số nghịch biến trên các khoảng $(%s; %s)$ và $(%s; %s)$' % (latex(x1), latex(x2), latex(x3), latex(x4)),
                    'Hàm số đồng biến trên khoảng $(%s; %s)$' % (latex(x2), latex(x3)),
                    'Hàm số nghịch biến trên khoảng $(%s; %s)$' % (latex(x1), latex(x4)),
                    'Hàm số đồng biến trên khoảng $(%s; %s)$' % (latex(x1), latex(x3)),
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                noidungcauhoi = ('''Cho hàm số $y = f(x)$ có tập xác định là $[%s; %s]$ và có đồ thị như hình vẽ sau. Khẳng định nào sau đây là đúng?
            \\begin{center}
            %s
            \\end{center}''' % (latex(x1), latex(x4), tikz_graph))

                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                loigiai = ('''Dựa vào đồ thị ta thấy: \\\\
                             - Trên các khoảng $(%s; %s)$ và $(%s; %s)$, đồ thị hàm số có hướng đi lên từ trái sang phải, do đó hàm số đồng biến. \\\\
                             - Trên khoảng $(%s; %s)$, đồ thị hàm số có hướng đi xuống từ trái sang phải, do đó hàm số nghịch biến. \\\\
                             Vậy khẳng định đúng là: Hàm số đồng biến trên các khoảng $(%s; %s)$ và $(%s; %s)$.''' 
                           % (latex(x1), latex(x2), latex(x3), latex(x4), latex(x2), latex(x3), latex(x1), latex(x2), latex(x3), latex(x4)))

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

