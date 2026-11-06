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


def bt_dang48_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            a = symbols('a')

            # B1 & B3: Thiết lập thông số và logic random
            n = random.randint(1, 3)
            m = random.randint(1, 3)
            if n == m: m += 1 

            list_goc = [30, 45, 60]
            goc_val = random.choice(list_goc)
            goc_rad = goc_val * pi / 180

            # B2: Tính toán lời giải chi tiết
            S_day_val = n * m
            S_day = S_day_val * a**2

            tu_AE = n * m
            mau_AE_sq = n**2 + m**2
            AE = (Rational(tu_AE, 1) * a) / sqrt(mau_AE_sq)

            val_tan = simplify(tan(goc_rad))
            SA = simplify(AE * val_tan)

            V_correct = simplify(Rational(1, 3) * SA * S_day)

            # B4: Tạo các phương án sai
            def generate_distractors(correct_val):
                options = set()
                da_str = '$%s$' % latex(correct_val).replace('.', ',')
                options.add(da_str)

                # Các sai lầm logic
                wrong1 = simplify(SA * S_day) 
                wrong2 = simplify(Rational(1, 6) * SA * S_day)
                wrong3 = simplify(Rational(1, 3) * (AE / val_tan) * S_day)

                candidates = [wrong1, wrong2, wrong3]
                for cand in candidates:
                    cand_str = '$%s$' % latex(cand).replace('.', ',')
                    if cand_str not in options:
                        options.add(cand_str)

                while len(options) < 4:
                    extra = simplify(correct_val * Rational(random.randint(2, 5), random.randint(1, 4)))
                    options.add('$%s$' % latex(extra).replace('.', ','))

                res = list(options)
                random.shuffle(res)
                return res, da_str

            options_list, da_dung = generate_distractors(V_correct)

            # Chuẩn bị nội dung TikZ
            tikz_code = '''\\begin{center} \\begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1.0cm,y=1.0cm, scale=0.7, line width=1pt]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (-1.5,-1.5);
                \\coordinate (D) at (4,0);
                \\coordinate (C) at (2.5,-1.5);
                \\coordinate (S) at (0,4);
                \\coordinate (E) at (0.6,-0.4); 
                \\draw [dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D) (A)--(E) (S)--(E);
                \\draw (S)--(B)--(C)--(D)--cycle (S)--(C) ;
                \\draw (A) node[left] {$A$} (B) node[left] {$B$} (C) node[right] {$C$} (D) node[right] {$D$} (S) node[above] {$S$} (E) node[left] {$E$};
            \\end{tikzpicture} \\end{center}'''

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật $AB = %s$, $AD = %s$, cạnh bên $SA$ vuông góc với đáy. Thể tích $V$ của khối chóp $S.ABCD$ biết góc giữa hai mặt phẳng $\\left(SBD\\right)$ và $\\left(ABCD\\right)$ bằng $%s^\\circ$ bằng'''
                             %(latex(n*a), latex(m*a), goc_val))

            # Nội dung lời giải chi tiết
            loigiai = ('''Kẻ $AE \\perp BD$. Vì $SA \\perp \\left(ABCD\\right)$ nên theo định lý ba đường vuông góc, ta có $SE \\perp BD$. \\\\
                             Khi đó $\\left(\\left(SBD\\right),\\left(ABCD\\right)\\right) = \\widehat{SEA} = %s^\\circ$. \\\\
                             Xét $\\triangle ABD$ vuông tại $A$: \\\\
                             $AE = \\frac{AB \\cdot AD}{\\sqrt{AB^2 + AB^2}} = \\frac{%s \\cdot %s}{\\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2}} = %s$. \\\\
                             Xét $\\triangle SAE$ vuông tại $A$: \\\\
                             $SA = AE \\cdot \\tan %s^\\circ = %s \\cdot %s = %s$. \\\\
                             Khi đó thể tích $S.ABCD$ là: \\\\
                             $V = \\frac{1}{3} SA \\cdot S_{ABCD} = \\frac{1}{3} \\cdot %s \\cdot %s = %s$.'''
                       %(goc_val, latex(n*a), latex(m*a), latex(n*a), latex(m*a), latex(AE), 
                         goc_val, latex(AE), latex(val_tan), latex(SA),
                         latex(SA), latex(S_day), latex(V_correct)
                        ))

            # Xử lý các đáp án để đưa vào list_1
            list_1 = []
            for opt in options_list:
                if opt == da_dung:
                    list_1.append('\\True ' + str(opt))
                else:
                    list_1.append(str(opt))

            # Xuất câu trắc nghiệm đúng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n' 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+ str(tikz_code)+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

