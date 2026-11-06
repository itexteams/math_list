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


def bt_dang34_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến - Mở rộng thêm các dạng câu hỏi
            lisdang=['1', '2', '3', '4']
            dang=random.choice(lisdang)

            # Tạo độ lệch ngẫu nhiên cho nhiệt độ (giữ nguyên hình dạng đồ thị)
            shift = random.randint(-3, 3)

            t0 = 25 + shift
            t4 = 20 + shift   # Giá trị nhỏ nhất
            t8 = 31 + shift
            t12 = 28 + shift
            t16 = 34 + shift  # Giá trị lớn nhất
            t20 = 27 + shift
            t24 = 24 + shift

            # Chuẩn hóa tọa độ y để vẽ hình trong TikZ (chia cho 8 để hình vừa vặn)
            y0 = t0 / 8.0
            y4 = t4 / 8.0
            y8 = t8 / 8.0
            y12 = t12 / 8.0
            y16 = t16 / 8.0
            y20 = t20 / 8.0
            y24 = t24 / 8.0

            # Vẽ lại hình dạng đồ thị bằng TikZ với độ dày nét 1pt
            tikz_code = (
                "\\begin{center}\n"
                "\\begin{tikzpicture}[>=stealth, scale=1]\n"
                "\\draw[->, line width=1pt] (-0.5,0) -- (7,0) node[below] {$x$ (giờ)};\n"
                "\\draw[->, line width=1pt] (0,-0.5) -- (0,5.5) node[left] {$t$ ($^\\circ$C)};\n"
                "\\node[below left] at (0,0) {$O$};\n"
                "\\draw[line width=1pt] (1,0.05) -- (1,-0.05) node[below] {$4$};\n"
                "\\draw[line width=1pt] (2,0.05) -- (2,-0.05) node[below] {$8$};\n"
                "\\draw[line width=1pt] (3,0.05) -- (3,-0.05) node[below] {$12$};\n"
                "\\draw[line width=1pt] (4,0.05) -- (4,-0.05) node[below] {$16$};\n"
                "\\draw[line width=1pt] (5,0.05) -- (5,-0.05) node[below] {$20$};\n"
                "\\draw[line width=1pt] (6,0.05) -- (6,-0.05) node[below] {$24$};\n"
                "\\node[left] at (0, %s) {$%s$};\n"
                "\\draw[dashed, line width=1pt] (1,0) -- (1,%s);\n"
                "\\draw[dashed, line width=1pt] (2,0) -- (2,%s);\n"
                "\\draw[dashed, line width=1pt] (3,0) -- (3,%s);\n"
                "\\draw[dashed, line width=1pt] (4,0) -- (4,%s);\n"
                "\\draw[dashed, line width=1pt] (5,0) -- (5,%s);\n"
                "\\draw[dashed, line width=1pt] (6,0) -- (6,%s);\n"
                "\\draw[line width=1pt] plot[smooth, tension=0.6] coordinates {(0,%s) (1,%s) (2,%s) (3,%s) (4,%s) (5,%s) (6,%s)};\n"
                "\\node[above] at (1,%s) {$%s$};\n"
                "\\node[above] at (2,%s) {$%s$};\n"
                "\\node[above] at (3,%s) {$%s$};\n"
                "\\node[above] at (4,%s) {$%s$};\n"
                "\\node[above] at (5,%s) {$%s$};\n"
                "\\node[above] at (6,%s) {$%s$};\n"
                "\\end{tikzpicture}\n"
                "\\end{center}"
                % (y0, t0, y4, y8, y12, y16, y20, y24, y0, y4, y8, y12, y16, y20, y24, y4, t4, y8, t8, y12, t12, y16, t16, y20, t20, y24, t24)
            )

            if dang=='1':
                # DẠNG 1: Hỏi nhiệt độ thấp nhất
                da = "$%s^\\circ C$" % (t4)
                s = [
                    "$%s^\\circ C$" % (t24),
                    "$%s^\\circ C$" % (t0),
                    "$%s^\\circ C$" % (t16),
                    "$%s^\\circ C$" % (t8),
                    "$%s^\\circ C$" % (t12)
                ]

                s = list(set(s))
                if da in s: s.remove(da)
                das1 = random.choice(s); s.remove(das1)
                das2 = random.choice(s); s.remove(das2)
                das3 = random.choice(s)

                noidungcauhoi = ('''Hình bên cho biết sự thay đổi của nhiệt độ ở thành phố Nha Trang trong một ngày ($24$ giờ).\\\\
                                 %s
                                 Nhiệt độ thấp nhất trong ngày là bao nhiêu độ $C$?''' % (tikz_code))

                loigiai = ('''Dựa vào đồ thị biểu diễn sự thay đổi của nhiệt độ trong ngày, ta quan sát trục tung để tìm giá trị nhiệt độ thấp nhất.\\\\
                           Mức nhiệt độ thấp nhất trên đồ thị tương ứng với điểm thấp nhất của đường cong biểu diễn.\\\\
                           Điểm thấp nhất của đồ thị đạt được tại thời điểm $x = 4$ giờ với mức nhiệt độ là $%s^\\circ C$.\\\\
                           Vậy nhiệt độ thấp nhất trong ngày là $%s^\\circ C$.''' % (t4, t4))

            elif dang=='2':
                # DẠNG 2: Hỏi nhiệt độ cao nhất
                da = "$%s^\\circ C$" % (t16)
                s = [
                    "$%s^\\circ C$" % (t4),
                    "$%s^\\circ C$" % (t0),
                    "$%s^\\circ C$" % (t24),
                    "$%s^\\circ C$" % (t8),
                    "$%s^\\circ C$" % (t12)
                ]

                s = list(set(s))
                if da in s: s.remove(da)
                das1 = random.choice(s); s.remove(das1)
                das2 = random.choice(s); s.remove(das2)
                das3 = random.choice(s)

                noidungcauhoi = ('''Hình bên cho biết sự thay đổi của nhiệt độ ở thành phố Nha Trang trong một ngày ($24$ giờ).\\\\
                                 %s
                                 Nhiệt độ cao nhất trong ngày là bao nhiêu độ $C$?''' % (tikz_code))

                loigiai = ('''Dựa vào đồ thị biểu diễn sự thay đổi của nhiệt độ trong ngày, ta quan sát trục tung để tìm giá trị nhiệt độ cao nhất.\\\\
                           Mức nhiệt độ cao nhất trên đồ thị tương ứng với điểm cao nhất của đường cong biểu diễn.\\\\
                           Điểm cao nhất của đồ thị đạt được tại thời điểm $x = 16$ giờ với mức nhiệt độ là $%s^\\circ C$.\\\\
                           Vậy nhiệt độ cao nhất trong ngày là $%s^\\circ C$.''' % (t16, t16))

            elif dang=='3':
                # DẠNG 3: Hỏi thời điểm nhiệt độ cao nhất
                da = "$16$ giờ"
                s = ["$4$ giờ", "$8$ giờ", "$12$ giờ", "$20$ giờ", "$24$ giờ"]

                s = list(set(s))
                if da in s: s.remove(da)
                das1 = random.choice(s); s.remove(das1)
                das2 = random.choice(s); s.remove(das2)
                das3 = random.choice(s)

                noidungcauhoi = ('''Hình bên cho biết sự thay đổi của nhiệt độ ở thành phố Nha Trang trong một ngày ($24$ giờ).\\\\
                                 %s
                                 Nhiệt độ trong ngày cao nhất vào lúc mấy giờ?''' % (tikz_code))

                loigiai = ('''Dựa vào đồ thị biểu diễn sự thay đổi của nhiệt độ trong ngày, ta tìm điểm cao nhất của đường cong biểu diễn.\\\\
                           Điểm cao nhất của đồ thị có tung độ tương ứng với mức nhiệt độ là $%s^\\circ C$.\\\\
                           Từ điểm này, gióng vuông góc xuống trục hoành (trục thời gian), ta nhận được giá trị $x = 16$.\\\\
                           Vậy nhiệt độ trong ngày cao nhất vào lúc $16$ giờ.''' % (t16))

            elif dang=='4':
                # DẠNG 4: Hỏi thời điểm nhiệt độ thấp nhất
                da = "$4$ giờ"
                s = ["$16$ giờ", "$8$ giờ", "$12$ giờ", "$20$ giờ", "$24$ giờ"]

                s = list(set(s))
                if da in s: s.remove(da)
                das1 = random.choice(s); s.remove(das1)
                das2 = random.choice(s); s.remove(das2)
                das3 = random.choice(s)

                noidungcauhoi = ('''Hình bên cho biết sự thay đổi của nhiệt độ ở thành phố Nha Trang trong một ngày ($24$ giờ).\\\\
                                 %s
                                 Nhiệt độ trong ngày thấp nhất vào lúc mấy giờ?''' % (tikz_code))

                loigiai = ('''Dựa vào đồ thị biểu diễn sự thay đổi của nhiệt độ trong ngày, ta tìm điểm thấp nhất của đường cong biểu diễn.\\\\
                           Điểm thấp nhất của đồ thị có tung độ tương ứng với mức nhiệt độ là $%s^\\circ C$.\\\\
                           Từ điểm này, gióng vuông góc xuống trục hoành (trục thời gian), ta nhận được giá trị $x = 4$.\\\\
                           Vậy nhiệt độ trong ngày thấp nhất vào lúc $4$ giờ.''' % (t4))

            # Định dạng các phương án trả lời (không có dấu chấm ở cuối)
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Trộn thứ tự các phương án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm đúng định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

