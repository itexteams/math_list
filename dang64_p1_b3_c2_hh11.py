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


def bt_dang64_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các hệ số cho AB=a*k1, BC=a*k2, SA=a*k3
                # Để kết quả đẹp, ta chọn các bộ số phù hợp
                options = [
                    (1, sqrt(3), 1), # Gốc trong ảnh
                    (1, 1, 1),
                    (2, 1, 2),
                    (1, sqrt(7), 3),
                    (2, sqrt(5), 1)
                ]
                k1, k2, k3 = random.choice(options)

                a = symbols('a')
                AB = k1 * a
                BC = k2 * a
                AD = BC
                SA = k3 * a

                # Bước 2: Tính toán các giá trị
                # AH = (SA * AB) / sqrt(SA^2 + AB^2)
                tu_AH = k3 * k1
                mau_AH_sq = k3**2 + k1**2
                AH_val = (tu_AH / sqrt(mau_AH_sq))

                # BD = sqrt(AB^2 + AD^2)
                BD_val = sqrt(k1**2 + k2**2)

                # sin_alpha = AH / BD
                sin_val = simplify(AH_val / BD_val)

                # Đáp án đúng
                da = '$%s$' % latex(sin_val).replace('.', ',')

                # Tạo các đáp án sai
                s = []
                while len(s) < 3:
                    # Tạo các giá trị sai bằng cách thay đổi các căn thức hoặc hệ số
                    wrong_val = simplify(sin_val * random.choice([Rational(1,2), Rational(2,1), sqrt(2), sqrt(3)/2, Rational(3,4)]))
                    wrong_str = '$%s$' % latex(wrong_val).replace('.', ',')
                    if wrong_str != da and wrong_str not in s:
                        s.append(wrong_str)

                das1, das2, das3 = s

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, $AB = %s$, $BC = %s$, $SA = %s$ và $SA$ vuông góc với mặt phẳng $\\left( ABCD \\right)$. Đặt $\\alpha$ là góc giữa đường thẳng $BD$ và $\\left( SBC \\right)$. Giá trị của $\\sin \\alpha$ bằng'''
                                 % (latex(AB), latex(BC), latex(SA)))

                # Hình vẽ TikZ
                # Tọa độ: A(0,0,0), B(0,-2,0), D(4,0,0), C(4,-2,0), S(0,0,4)
                tikz_code = r'''\begin{center}
            \begin{tikzpicture}[scale=0.8, line width=1pt, line join=round, line cap=round]
                \tkzDefPoints{0/0/A, -1.5/-1.5/B, 3/0/D, 0/3.5/S}
                \tkzDefPointBy[translation=from A to D](B) \tkzGetPoint{C}
                \tkzInterLL(A,C)(B,D) \tkzGetPoint{O}
                \tkzDefPointBy[projection=onto S--B](A) \tkzGetPoint{H}
                \tkzDrawSegments(S,B B,C C,D S,C S,D)
                \tkzDrawSegments[dashed](S,A A,B A,D A,C B,D A,H)
                \tkzLabelPoints[left](A, H)
                \tkzLabelPoints[below left](B)
                \tkzLabelPoints[below right](C, O)
                \tkzLabelPoints[right](D)
                \tkzLabelPoints[above](S)
                \tkzMarkRightAngle(S,A,D)
                \tkzMarkRightAngle(S,A,B)
                \tkzMarkRightAngle(A,H,B)
                \fill[red] (O) circle (0pt);
            \end{tikzpicture}
            \end{center}'''

                # Lời giải chi tiết
                loigiai = ('''Ta có $AD // BC \\Rightarrow AD // \\left( SBC \\right) \\Rightarrow d\\left( D, \\left( SBC \\right) \\right) = d\\left( A, \\left( SBC \\right) \\right)$.\\\\
                             Vì $\\alpha$ là góc giữa $BD$ và $\\left( SBC \\right)$ nên $\\sin \\alpha = \\frac{d\\left( D, \\left( SBC \\right) \\right)}{BD} = \\frac{d\\left( A, \\left( SBC \\right) \\right)}{BD}$.\\\\
                             Ta có $\\begin{cases} BC \\perp AB \\\\ BC \\perp SA \\end{cases} \\Rightarrow BC \\perp \\left( SAB \\right)$.\\\\
                             Kẻ $AH \\perp SB$ tại $H$. Vì $BC \\perp \\left( SAB \\right) \\Rightarrow BC \\perp AH$.\\\\
                             Từ đó $AH \\perp \\left( SBC \\right) \\Rightarrow d\\left( A, \\left( SBC \\right) \\right) = AH$.\\\\
                             Xét tam giác $SAB$ vuông tại $A$ có $AH$ là đường cao:\\\\
                             $\\frac{1}{AH^2} = \\frac{1}{AB^2} + \\frac{1}{AS^2} = \\frac{1}{\\left( %s \\right)^2} + \\frac{1}{\\left( %s \\right)^2} \\Rightarrow AH = %s$.\\\\
                             Xét tam giác $ABD$ vuông tại $A$: $BD = \\sqrt{AB^2 + AD^2} = \\sqrt{\\left( %s \\right)^2 + \\left( %s \\right)^2} = %s$.\\\\
                             Vậy $\\sin \\alpha = \\frac{AH}{BD} = \\frac{%s}{%s} = %s$.'''
                           % (latex(AB), latex(SA), latex(AH_val*a), latex(AB), latex(AD), latex(BD_val*a),
                              latex(AH_val*a), latex(BD_val*a), latex(sin_val)))

            # Xuất câu trắc nghiệm
            list_1 = ['\\True ' + str(da), str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + tikz_code+ str(loigiai).replace('.', ',') + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

