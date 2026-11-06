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


def bt_dang25_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Thiết lập các hệ số cho AB = w*a, AD = l*a, SA = h*a
                # Mặc định trong hình là w=1, l=2, h=3
                w = random.randint(1, 3)
                l = random.randint(1, 4)
                if w == l: l += 1 # Đảm bảo là hình chữ nhật chứ không phải hình vuông
                h = random.randint(2, 5)

                a = symbols('a')
                side_AB = w * a
                side_AD = l * a
                side_SA = h * a

                # Bước 1 & 2: Nghiên cứu và tính toán lời giải
                # AC = sqrt(AB^2 + AD^2)
                ac_sq = w**2 + l**2
                ac_val = simplify(sqrt(ac_sq))

                # tan(phi) = SA / AC = h / sqrt(w^2 + l^2)
                tan_phi = simplify(Rational(h, 1) / sqrt(ac_sq))

                # Đáp án đúng
                da = '$%s$' % (latex(tan_phi))

                # Bước 4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = []
                # Các trường hợp sai phổ biến: nghịch đảo, quên căn, hoặc nhầm cạnh
                wrong_1 = simplify(sqrt(ac_sq) / Rational(h, 1)) # Nghịch đảo
                wrong_2 = simplify(Rational(h, w)) # Nhầm tan = SA/AB
                wrong_3 = simplify(Rational(w, h)) # Nhầm tan = AB/SA
                wrong_4 = simplify(Rational(h, l)) # Nhầm tan = SA/AD

                potential_wrongs = [wrong_1, wrong_2, wrong_3, wrong_4]
                for p in potential_wrongs:
                    val = '$%s$' % (latex(p))
                    if val != da and val not in s:
                        s.append(val)

                # Nếu chưa đủ 3 đáp án sai thì tạo thêm ngẫu nhiên
                while len(s) < 3:
                    fake_val = simplify(Rational(random.randint(1, 5), random.randint(2, 5)))
                    val = '$%s$' % (latex(fake_val))
                    if val != da and val not in s:
                        s.append(val)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                # Sử dụng \left( \right) và không dùng tiền tố r
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật có $AB = %s, AD = %s, SA$ vuông góc với mặt phẳng $\\left( ABCD \\right), SA = %s$. Gọi $\\varphi$ là góc giữa $SC$ và $\\left( ABCD \\right)$. Khi đó $\\tan \\varphi$ bằng'
                                 % (latex(side_AB), latex(side_AD), latex(side_SA)))

                # Hình vẽ bằng TikZ
                hinh_ve = ('\\begin{center}\n'
                           '\\begin{tikzpicture}[scale=1, line width=1pt]\n'
                           '\\coordinate (A) at (0,2);\n'
                           '\\coordinate (B) at (-1.5,0.5);\n'
                           '\\coordinate (C) at (2.5,0.5);\n'
                           '\\coordinate (D) at (4,2);\n'
                           '\\coordinate (S) at (0,5);\n'
                           '\\draw [dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C);\n'
                           '\\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D);\n'
                           '\\node at (A) [above left] {$A$};\n'
                           '\\node at (B) [below left] {$B$};\n'
                           '\\node at (C) [below right] {$C$};\n'
                           '\\node at (D) [right] {$D$};\n'
                           '\\node at (S) [above] {$S$};\n'
                           '\\draw [green!50!black] (2.1,0.5) arc (180:145:0.5);\n'
                           '\\end{tikzpicture}\n'
                           '\\end{center}')

                # Nội dung lời giải chi tiết
                loigiai = ('$AC$ là hình chiếu của $SC$ trên $\\left( ABCD \\right)$ nên $\\left( SC, \\left( ABCD \\right) \\right) = \\left( SC, AC \\right) = \\angle SCA = \\varphi$. \\\\\n'
                           'Ta có: $AC = \\sqrt{AD^{2} + DC^{2}} = \\sqrt{\\left( %s \\right)^{2} + \\left( %s \\right)^{2}} = %s$. \\\\\n'
                           'Tam giác $SAC$ vuông tại $A$ nên $\\tan \\varphi = \\frac{SA}{AC} = \\frac{%s}{%s} = %s$.'
                           % (latex(side_AD), latex(side_AB), latex(ac_val * a),
                              latex(side_SA), latex(ac_val * a), latex(tan_phi)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' 
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + hinh_ve + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

