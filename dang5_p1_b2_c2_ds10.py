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


def bt_dang5_p1_b2_c2_ds10(self):
            # Khai báo biến
            x0 = randint(2, 4) 
            y0 = randint(3, 4) 
            a = randint(1, 2) 
            b = randint(5, 7)
            c = randint(-9, 9) 
            d = randint(-9, 9)
            e = Rational((-b*x0), (y0-b))
            f = randint(-19, 19)
            while c == 0 or d == 0 or f == 0:
                c = randint(-9, 9) 
                d = randint(-9, 9)
                f = randint(-19, 19)

            gt0 = 0 + f
            gta = c*0 + d*a + f
            gtb = c*x0 + d*y0 + f
            gtc = Rational((c*(-b*x0)), (y0-b)) + d*0 + f

            list2 = [gt0, gta, gtb, gtc]
            ln = max(list2)
            nn = min(list2)

            list4 = [2, -2]
            list3 = ['dang3']
            rd = random.choice(list3)
            rd4 = random.choice(list4)

            # Nội dung câu hỏi
            if rd == 'dang3':
                noidungcauhoi = ('''Cho cặp số $(x;y)$ là nghiệm của hệ bất phương trình $\\heva{& %sx-%sy+%s\\ge0\\\\& %sx-%sy+%s\\ge0\\\\& x\\ge0\\\\& y\\ge0\\\\}$. Gọi $M$ là giá trị lớn nhất của biểu thức $F(x;y)=%sx+%sy+%s$. Khi đó $M$ bằng\\\\'''
                            % (latex(y0-a), latex(x0), latex(x0*a), latex(y0-b), latex(x0), latex(x0*b), latex(c), latex(d), latex(f)))

            # Các đáp án
            da_d = '\\True $%s$' % (latex(ln))
            da_s1 = '$%s$' % (latex(ln+rd4))
            da_s2 = '$%s$' % (latex(ln-1))
            da_s3 = '$%s$' % (latex(ln+1))

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('Vẽ các đường thẳng:\\\\\n'
                        '$d_1: %sx-%sy+%s=0;\\\\\n' 
                        'd_2: %sx-%sy+%s=0;\\\\\n' 
                        'd_3: x=0;\\\\\n' 
                        'd_4: y=0$ trên cùng một hệ trục tọa độ $(Oxy)$.\\\\\n'
                        'Miền nghiệm của hệ là miền tứ giác $OABC$ với tọa độ các đỉnh $O(0;0);A(0;%s);B(%s;%s);C(%s;0)$ (hình vẽ).\\\\\n' 
                        'Giá trị lớn nhất của $F(x;y)$ đạt được tại một trong các đỉnh của tứ giác $OABC$.\\\\\n'
                        'Ta có: \\\\\n'
                        '$F(0;0) = (%s)0+(%s)0+%s= %s$. \\\\\n'
                        '$F(0;%s) = (%s)0+(%s)%s+%s = %s$. \\\\\n'
                        '$F(%s;%s) = (%s)%s+(%s)%s+%s= %s$. \\\\\n'
                        '$F(%s;0) = (%s)%s+(%s)0+%s= %s$. \\\\\n'
                        'Vậy giá trị lớn nhất của $F(x;y)$ là $M=%s$.'
                        % (latex(y0-a), latex(x0), latex(x0*a), latex(y0-b), latex(x0), latex(x0*b),
                            latex(a), latex(x0), latex(y0), latex(e),
                            latex(c), latex(d), latex(f), latex(gt0),
                            latex(a), latex(c), latex(d), latex(a), latex(f), latex(gta),
                            latex(x0), latex(y0), latex(c), latex(x0), latex(d), latex(y0), latex(f), latex(gtb),
                            latex(e), latex(c), latex(e), latex(d), latex(f), latex(gtc), latex(ln)))

            # --- PHẦN TẠO HÌNH VẼ MỚI (THEO PHONG CÁCH YÊU CẦU) ---
            e_float = float(-b * x0) / (y0 - b)

            # Tính toán giới hạn của trục tọa độ để hình vẽ bao quát được đa giác
            xmax_val = int(max(x0, e_float)) + 3
            ymax_val = int(max(y0, a)) + 3

            # Tính tọa độ 2 đầu mút của d1 và d2 để vẽ đường thẳng cắt ngang hệ trục
            # Phương trình d1: y = ((y0-a)x + x0*a)/x0
            y1_start = ((y0 - a) * (-2) + x0 * a) / x0
            y1_end = ((y0 - a) * (xmax_val + 1) + x0 * a) / x0

            # Phương trình d2: y = ((y0-b)x + x0*b)/x0
            y2_start = ((y0 - b) * (-2) + x0 * b) / x0
            y2_end = ((y0 - b) * (xmax_val + 1) + x0 * b) / x0

            hinhve = (f'\\begin{{center}}\n'
                      f'\\begin{{tikzpicture}}[>=stealth, scale=0.7, line width=1pt]\n'
                      f'\\clip (-2, -2) rectangle ({xmax_val}, {ymax_val});\n'
                      f'\\fill[pattern=north east lines, pattern color=black] (-2, -2) rectangle ({xmax_val}, {ymax_val});\n'
                      f'\\fill[white] (0,0) -- ({e_float},0) -- ({x0},{y0}) -- (0,{a}) -- cycle;\n'
                      f'\\draw[black] (-2, {y1_start}) -- ({xmax_val + 1}, {y1_end});\n'
                      f'\\draw[black] (-2, {y2_start}) -- ({xmax_val + 1}, {y2_end});\n'
                      f'\\coordinate (A) at (0, {a});\n'
                      f'\\coordinate (B) at ({x0}, {y0});\n'
                      f'\\coordinate (C) at ({e_float}, 0);\n'
                      f'\\fill (0,0) circle (1pt);\n'
                      f'\\fill (A) circle (1pt) node[above right] {{$A$}};\n'
                      f'\\fill (B) circle (1pt) node[above right] {{$B$}};\n'
                      f'\\fill (C) circle (1pt) node[above right] {{$C$}};\n'
                      f'\\node at (-1, {((y0 - a) * (-1) + x0 * a) / x0}) [below left] {{$d_1$}};\n'
                      f'\\node at (-1, {((y0 - b) * (-1) + x0 * b) / x0}) [below left] {{$d_2$}};\n'
                      f'\\draw[->] (-2, 0) -- ({xmax_val}, 0) node[below] {{$x$}};\n'
                      f'\\draw[->] (0, -2) -- (0, {ymax_val}) node[left] {{$y$}};\n'
                      f'\\node at (0,0) [below left] {{$O$}};\n'                          
                      f'\\end{{tikzpicture}} '
                      f'\\end{{center}}')
            # -------------------------------------------------------------

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'
                + hinhve + '\n'
                + str(loigiai) + '\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('1x', 'x').replace('-1x', '-x').replace('1y', 'y').replace('.0', '').replace('+-', '-')

            return content

