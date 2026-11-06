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


def bt_dang47_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo danh sách các bộ tên đỉnh để random
            danh_sach_ten = [
                ('S', 'A', 'B', 'C'),
            ]

            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn ngẫu nhiên bộ tên đỉnh
                d, d1, d2, d3 = random.choice(danh_sach_ten)

                # Đáp án đúng luôn là 60 độ cho cấu hình này
                kq = 60
                da_dung = '$%s^\\circ$' % kq

                # Các đáp án nhiễu
                s = ['$30^\\circ$', '$45^\\circ$', '$90^\\circ$', '$120^\\circ$', '$150^\\circ$']
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Cho hình chóp $%s.%s%s%s$ có $%s%s, %s%s, %s%s$ vuông góc với nhau từng đôi một và $%s%s = %s%s = %s%s$. '
                    'Gọi $M$ là trung điểm của $%s%s$. Tính góc giữa $%sM$ và $%s%s$.'
                    % (d, d1, d2, d3, d, d1, d, d2, d, d3, d, d1, d, d2, d, d3, d1, d3, d, d1, d2)
                )

                # Các đáp án
                da_d = '\\True ' + da_dung
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Vẽ hình bằng TikZ
                tikz_code = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]\n'
                    '\\coordinate (S) at (0,0); \n'
                    '\\coordinate (A) at (0,3); \n'
                    '\\coordinate (C) at (1.5,-1); \n'
                    '\\coordinate (B) at (4,0); \n'
                    '\\coordinate (M) at ($(A)!0.5!(C)$);\n'
                    '\\draw[dashed] (S)--(B);\n'
                    '\\draw (S)--(A)--(C)--(S) (C)--(B) (S)--(M) (A)--(B);\n'
                    '\\tkzDrawPoints(S,A,B,C,M)\n'
                    '\\tkzLabelPoints[left](S,A)\n'
                    '\\tkzLabelPoints[right](B)\n'
                    '\\tkzLabelPoints[below](C)\n'
                    '\\tkzLabelPoints[above right](M)\n'
                    '\\tkzMarkRightAngle(A,S,B)\n'
                    '\\tkzMarkRightAngle(A,S,C)\n'
                    '\\tkzMarkRightAngle(B,S,C)\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}'
                ).replace('S', d).replace('A', d1).replace('B', d2).replace('C', d3)

                # Lời giải chi tiết
                loigiai = (
                    'Đặt $%s%s = %s%s = %s%s = a$. \\\\\n'
                    'Ta sử dụng phương pháp vectơ: \\\\\n'
                    'Vì $M$ là trung điểm của $%s%s$ nên $\\vec{%sM} = \\frac{1}{2}(\\vec{%s%s} + \\vec{%s%s})$. \\\\\n'
                    'Ta có $\\vec{%s%s} = \\vec{%s%s} - \\vec{%s%s}$. \\\\\n'
                    'Xét tích vô hướng: \\\\\n'
                    '$\\vec{%sM} \\cdot \\vec{%s%s} = \\frac{1}{2}(\\vec{%s%s} + \\vec{%s%s})(\\vec{%s%s} - \\vec{%s%s})$ \\\\\n'
                    '$= \\frac{1}{2}(\\vec{%s%s} \\cdot \\vec{%s%s} - \\vec{%s%s}^2 + \\vec{%s%s} \\cdot \\vec{%s%s} - \\vec{%s%s} \\cdot \\vec{%s%s})$. \\\\\n'
                    'Do $%s%s, %s%s, %s%s$ đôi một vuông góc nên $\\vec{%s%s} \\cdot \\vec{%s%s} = \\vec{%s%s} \\cdot \\vec{%s%s} = \\vec{%s%s} \\cdot \\vec{%s%s} = 0$. \\\\\n'
                    'Suy ra $\\vec{%sM} \\cdot \\vec{%s%s} = \\frac{1}{2}(0 - a^2 + 0 - 0) = -\\frac{a^2}{2}$. \\\\\n'
                    'Độ dài các đoạn thẳng: \\\\\n'
                    '$%sM = \\sqrt{\\vec{%sM}^2} = \\sqrt{\\frac{1}{4}(\\vec{%s%s} + \\vec{%s%s})^2} = \\sqrt{\\frac{1}{4}(a^2 + a^2)} = \\frac{a\\sqrt{2}}{2} = \\frac{a}{\\sqrt{2}}$. \\\\\n'
                    '$%s%s = \\sqrt{(a^2 + a^2)} = a\\sqrt{2}$. \\\\\n'
                    'Gọi $\\alpha$ là góc giữa hai vectơ $\\vec{%sM}$ và $\\vec{%s%s}$, ta có: \\\\\n'
                    '$\\cos \\alpha = \\frac{\\vec{%sM} \\cdot \\vec{%s%s}}{%sM \\cdot %s%s} = \\frac{-\\frac{a^2}{2}}{\\frac{a}{\\sqrt{2}} \\cdot a\\sqrt{2}} = \\frac{-\\frac{a^2}{2}}{a^2} = -\\frac{1}{2}$. \\\\\n'
                    'Suy ra $\\alpha = 120^\\circ$. \\\\\n'
                    'Vậy góc giữa đường thẳng $%sM$ và $%s%s$ bằng $180^\\circ - 120^\\circ = 60^\\circ$.'
                    % (d, d1, d, d2, d, d3, d1, d3, d, d, d1, d, d3, d1, d2, d, d2, d, d1, d, d1, d2, d, d1, d, d3, d, d2, d, d1, 
                       d, d1, d, d2, d, d1, d, d3, d, d2, d, d3, d, d1, d, d1, d, d2, d, d3, d, d1, d, d2, d, d1, d, d3, d, d2, d, d3,
                       d, d1, d2, d, d, d, d1, d, d3, d1, d2, d, d1, d2, d, d1, d2, d, d1, d2, d, d1, d2)
                )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(tikz_code)+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

