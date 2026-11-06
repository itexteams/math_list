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


def bt_dang41_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số k sao cho SA = k * (a*sqrt(3)/2)
                # Trong đề bài gốc SA = a*sqrt(3) tương ứng k = 2
                # Kết quả tan alpha = AH/SA = (a*sqrt(3)/2) / (k * a*sqrt(3)/2) = 1/k
                k_val = random.choice([2, 3, 4, 5])

                # Tính toán các giá trị cho lời giải
                # AH = a*sqrt(3)/2
                # SA = k_val * AH
                sa_factor = Rational(k_val, 2)
                if sa_factor == 1:
                    sa_tex = "a\\sqrt{3}"
                elif sa_factor.denominator == 1:
                    sa_tex = "%sa\\sqrt{3}" % (sa_factor.numerator)
                else:
                    sa_tex = "\\frac{%sa\\sqrt{3}}{%s}" % (sa_factor.numerator, sa_factor.denominator)

                # Đáp án đúng
                kq_frac = Rational(1, k_val)
                da = "$%s$" % (latex(kq_frac))

                # Các đáp án nhiễu
                s_list = []
                potential_denominators = [2, 3, 4, 5, 6]
                for d in potential_denominators:
                    if d != k_val:
                        s_list.append("$%s$" % (latex(Rational(1, d))))

                random.shuffle(s_list)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Nội dung câu hỏi
                noidungcauhoi = ("Cho hình chóp $S.ABCD$ có đáy là hình thoi cạnh $a$, góc $\\widehat{ABC} = 60^\\circ$, $SA \\perp \\left(ABCD\\right)$, $SA = %s$. Gọi $\\alpha$ là góc giữa $SA$ và mặt phẳng $\\left(SCD\\right)$. Giá trị của $\\tan \\alpha$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)."
                                 % (sa_tex))

                # Các đáp án
                da_d = ("\\True " + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Hình vẽ TikZ
                hinh_ve = ("\\begin{center}\n"
                           "\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round, line width=1pt]\n"
                           "\\coordinate (A) at (0,3);\n"
                           "\\coordinate (B) at (-1.5,1);\n"
                           "\\coordinate (C) at (2.5,1);\n"
                           "\\coordinate (D) at (4,3);\n"
                           "\\coordinate (S) at (0,7);\n"
                           "\\coordinate (H) at (3.25,2);\n"
                           "\\coordinate (K) at (1.625,4.5);\n"
                           "\\draw [dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (A)--(H) (A)--(K);\n"
                           "\\draw (S)--(B)--(C)--(D)--(S)--(C) (S)--(H);\n"
                           "\\node [left] at (A) {$A$};\n"
                           "\\node [left] at (B) {$B$};\n"
                           "\\node [below] at (C) {$C$};\n"
                           "\\node [right] at (D) {$D$};\n"
                           "\\node [above] at (S) {$S$};\n"
                           "\\node [below right] at (H) {$H$};\n"
                           "\\node [right] at (K) {$K$};\n"
                           "\\end{tikzpicture}\n"
                           "\\end{center}")
                h1=kq_frac
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')
                # Nội dung lời giải
                loigiai = (hinh_ve + 
                           "Trong mặt phẳng $\\left(ABCD\\right)$, kẻ $AH \\perp CD$ tại $H$. \\\\\n"
                           "Vì hình thoi $ABCD$ có cạnh $a$ và $\\widehat{ABC} = 60^\\circ$ nên tam giác $ADC$ là tam giác đều cạnh $a$. \\\\\n"
                           "Khi đó $H$ là trung điểm của $CD$ và $AH = \\frac{a\\sqrt{3}}{2}$. \\\\\n"
                           "Ta có $CD \\perp AH$ và $CD \\perp SA$ (do $SA \\perp \\left(ABCD\\right)$), suy ra $CD \\perp \\left(SAH\\right)$. \\\\\n"
                           "Trong mặt phẳng $\\left(SAH\\right)$, kẻ $AK \\perp SH$ tại $K$. \\\\\n"
                           "Vì $AK \\perp SH$ và $AK \\perp CD$ (do $CD \\perp \\left(SAH\\right)$), suy ra $AK \\perp \\left(SCD\\right)$. \\\\\n"
                           "Do đó, góc giữa đường thẳng $SA$ và mặt phẳng $\\left(SCD\\right)$ là góc giữa $SA$ và hình chiếu $SK$ của nó trên $\\left(SCD\\right)$, chính là góc $\\widehat{ASK}$ hay $\\widehat{ASH} = \\alpha$. \\\\\n"
                           "Trong tam giác $SAH$ vuông tại $A$, ta có: \\\\\n"
                           "$\\tan \\alpha = \\tan \\widehat{ASH} = \\frac{AH}{AS} = \\frac{\\frac{a\\sqrt{3}}{2}}{%s} = %s \\approx %s$."
                           % (sa_tex, latex(kq_frac),kqz))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

