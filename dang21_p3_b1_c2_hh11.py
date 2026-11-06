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


def bt_dang21_p3_b1_c2_hh11(self):
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập bộ thông số: (Hệ số AB, SC_latex, Giá trị góc số)
                cases = [
                    (2, 'a\\sqrt{2}', 45),
                    (2, '2a', 60),
                    (2, '\\frac{2a}{\\sqrt{3}}', 30),
                ]

                selected_case = random.choice(cases)
                ab_coeff = selected_case[0]
                sc_str = selected_case[1]
                angle_num = selected_case[2] # Giá trị số để tính toán
                kq_dung_str = f"{angle_num}^\\circ"

                # Các đáp án nhiễu (dùng số để dễ quản lý)
                all_angles = [30, 45, 60, 90]
                if angle_num in all_angles:
                    all_angles.remove(angle_num)

                random.shuffle(all_angles)
                da_s1 = f'${all_angles[0]}^\\circ$'
                da_s2 = f'${all_angles[1]}^\\circ$'
                da_s3 = f'${all_angles[2]}^\\circ$'
                da_d = f'\\True ${kq_dung_str}$'

                # Trộn đáp án trắc nghiệm
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB = %sa, BC = a$. Các cạnh bên của hình chóp cùng bằng $%s$. Góc giữa hai đường thẳng $AB$ và $SC$ bằng'
                    % (latex(ab_coeff), sc_str)
                )

                # TikZ vẽ hình
                hinh_ve = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                    '\\coordinate (A) at (0,0);\n'
                    '\\coordinate (B) at (-1.5,-1.2);\n'
                    '\\coordinate (C) at (2.5,-1.2);\n'
                    '\\coordinate (D) at (4,0);\n'
                    '\\coordinate (O) at (1.25,-0.6);\n'
                    '\\coordinate (S) at (1.25,3);\n'
                    '\\coordinate (M) at (3.25,-0.6);\n'
                    '\\draw [dashed] (S)--(A) (A)--(B) (A)--(D) (B)--(D) (A)--(C) (S)--(O) (O)--(M);\n'
                    '\\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D) (S)--(M);\n'
                    '\\foreach \\p/\\pos in {S/above, A/left, B/below left, C/below right, D/right, M/below right} \\fill (\\p) circle (1pt) node[\\pos]{\\p};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}'
                )

                # Lời giải chi tiết
                # Sử dụng angle_num cho Decimal để không bị lỗi float
                number = Decimal(angle_num)
                kqz = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                loigiai = (
                    'Ta có $AB \\parallel CD$ nên $(AB; SC) = (CD; SC) = \\widehat{SCD}$. \\\\'
                    'Vì các cạnh bên của hình chóp bằng nhau nên hình chiếu của $S$ xuống mặt đáy trùng với tâm $O$ của hình chữ nhật. \\\\'
                    'Gọi $M$ là trung điểm của $CD$. Vì $ABCD$ là hình chữ nhật nên $OM \\perp CD$. \\\\'
                    'Mà $SO \\perp (ABCD) \\Rightarrow SO \\perp CD$. Suy ra $CD \\perp (SOM) \\Rightarrow CD \\perp SM$. \\\\'
                    'Do đó tam giác $SCM$ vuông tại $M$. \\\\'
                    'Ta có $CM = \\frac{CD}{2} = \\frac{AB}{2} = \\frac{%sa}{2} = a$. \\\\'
                    'Xét tam giác vuông $SCM$ có $SC = %s, CM = a$. \\\\'
                    '$\\cos \\widehat{SCD} = \\frac{CM}{SC} = \\frac{a}{%s}$. \\\\'
                    'Từ đó suy ra $\\widehat{SCD} = %s$. Vậy $(AB, SC) = %s$.'
                    % (latex(ab_coeff), sc_str, sc_str, kq_dung_str, kq_dung_str)
                )

                # Đáp án ngắn
                dapan = '\\shortans[0]{$%s$}\n' % (kqz)

            # Xuất nội dung theo cấu trúc \choice
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
                hinh_ve + str(dapan) +
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

