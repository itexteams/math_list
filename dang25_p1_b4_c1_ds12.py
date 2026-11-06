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


def bt_dang25_p1_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ số (a, b, số nghiệm) tương ứng với phương trình af(x) - b = 0
                # Dựa vào đồ thị: min tại (2, 1), max tại (0, 2), hai đầu mút là (-2, -3) và (4, 6)
                cases = [
                    (3, 4, 3), (3, 5, 3), (4, 5, 3), (4, 7, 3), (5, 6, 3), (5, 9, 3), # 3 nghiệm (1 < b/a < 2)
                    (2, 2, 2), (3, 3, 2), (4, 4, 2), # 2 nghiệm (b/a = 1)
                    (2, 4, 2), (3, 6, 2), (4, 8, 2), # 2 nghiệm (b/a = 2)
                    (2, 1, 1), (3, -1, 1), (2, 5, 1), (3, 8, 1), (2, -4, 1), # 1 nghiệm (-3 <= b/a < 1 hoặc 2 < b/a <= 6)
                    (2, -8, 0), (3, -10, 0), (2, 14, 0), (3, 20, 0) # 0 nghiệm (b/a < -3 hoặc b/a > 6)
                ]
                a, b, kq = random.choice(cases)

                # Xử lý chuỗi phương trình
                if b > 0:
                    eq_str = "%sf(x) - %s = 0" % (a, b)
                elif b < 0:
                    eq_str = "%sf(x) + %s = 0" % (a, -b)
                else:
                    eq_str = "%sf(x) = 0" % (a)

                # Hàm định dạng phân số LaTeX
                def format_frac(tu, mau):
                    if tu % mau == 0:
                        return str(tu // mau)
                    if tu < 0:
                        return "-\\frac{%s}{%s}" % (-tu, mau)
                    return "\\frac{%s}{%s}" % (tu, mau)

                frac_str = format_frac(b, a)

                # Các đáp án trắc nghiệm
                da = kq
                pool = [0, 1, 2, 3, 4]
                pool.remove(da)
                random.shuffle(pool)

                das1 = pool[0]
                das2 = pool[1]
                das3 = pool[2]

                # Vẽ hình bằng TikZ (Dùng hàm đa thức bậc 3 đã phục dựng: y = 0.25x^3 - 0.75x^2 + 2)
                hinhve = '''\\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.8]
            \\draw[->] (-3, 0) -- (5.5, 0) node[below] {$x$};
            \\draw[->] (0, -4) -- (0, 7) node[left] {$y$};
            \\node[below left] at (0,0) {$O$};
            \\draw[dashed] (-2,0) node[above left] {$-2$} -- (-2,-3) -- (0,-3) node[right] {$-3$};
            \\draw[dashed] (2,0) node[below] {$2$} -- (2,1) -- (0,1) node[left] {$1$};
            \\draw[dashed] (4,0) node[below] {$4$} -- (4,6) -- (0,6) node[left] {$6$};
            \\node[above left] at (0,2) {$2$};
            \\draw[smooth, line width=1pt, domain=-2:4, samples=100] plot (\\x, {0.25*(\\x)^3 - 0.75*(\\x)^2 + 2});
            \\end{tikzpicture}
            \\end{center}'''

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = f(x)$ liên tục trên đoạn $[-2;4]$ và có đồ thị như hình vẽ:
            %s
            Số nghiệm thực của phương trình $%s$ trên đoạn $[-2;4]$ là''' % (hinhve, eq_str))

                # Các đáp án
                da_d = ('\\True $%s$' % str(da))
                da_s1 = '$%s$' % str(das1)
                da_s2 = '$%s$' % str(das2)
                da_s3 = '$%s$' % str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $%s \\Leftrightarrow f(x) = %s$.\\\\
            Số nghiệm của phương trình là số giao điểm của đồ thị hàm số $y = f(x)$ và đường thẳng $y = %s$.\\\\
            Quan sát đồ thị, ta thấy đường thẳng $y = %s$ cắt đồ thị tại $%s$ điểm phân biệt trên đoạn $[-2;4]$.\\\\
            Vậy phương trình đã cho có $%s$ nghiệm thực.''' % (eq_str, frac_str, frac_str, frac_str, kq, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

