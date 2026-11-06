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


def bt_dang27_p1_b1_c2_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random cạnh a của tam giác đều từ 1 đến 10
                a = random.randint(1, 10)

                # Tính toán độ dài BI = a * sqrt(21) / 6
                val = (a * math.sqrt(21)) / 6

                # Làm tròn đến hàng phần chục theo chuẩn toán học
                kq_dec = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Thay dấu chấm thành dấu phẩy
                kq = str(kq_dec).replace('.', ',')
                kq_float = float(kq_dec)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu bằng cách cộng/trừ 0.1, 0.2, 0.3
                s = [
                    '$%s$' % str(Decimal(str(kq_float + 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(str(kq_float + 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(str(kq_float + 0.3)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(str(kq_float - 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(str(kq_float - 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(str(kq_float - 0.3)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                str_a = "1" if a == 1 else str(a)
                noidungcauhoi = ('''Cho tam giác $ABC$ đều cạnh $%s$ và $G$ là trọng tâm. Gọi $I$ là trung điểm của $AG$. Tính độ dài của vectơ $\\overrightarrow{BI}$. \\textit{Kết quả làm tròn đến hàng phần chục.}''' % str_a)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Định dạng chuỗi toán học theo a
                if a == 1:
                    str_ab_bm = "1^2 - \\frac{1}{4}"
                    str_ag = "\\frac{\\sqrt{3}}{3}"
                    str_bm2_mi2 = "\\frac{1}{4} + \\frac{1}{3}"
                    str_bi = "\\frac{\\sqrt{21}}{6}"
                else:
                    str_ab_bm = "%s^2 - \\frac{%s}{4}" % (a, a**2)
                    str_bm2_mi2 = "\\frac{%s}{4} + \\frac{%s}{3}" % (a**2, a**2)

                    # Rút gọn phân số chứa căn cho AG
                    if a % 3 == 0:
                        str_ag = "\\sqrt{3}" if a == 3 else "%s\\sqrt{3}" % (a // 3)
                    else:
                        str_ag = "\\frac{%s\\sqrt{3}}{3}" % a

                    # Rút gọn phân số chứa căn cho BI
                    if a % 6 == 0:
                        str_bi = "\\sqrt{21}" if a == 6 else "%s\\sqrt{21}" % (a // 6)
                    elif a % 2 == 0:
                        str_bi = "\\frac{%s\\sqrt{21}}{3}" % (a // 2)
                    elif a % 3 == 0:
                        str_bi = "\\frac{%s\\sqrt{21}}{2}" % (a // 3)
                    else:
                        str_bi = "\\frac{%s\\sqrt{21}}{6}" % a

                # Mã TikZ vẽ hình tam giác đều
                code_hinh = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1.5, >=stealth]
            \\coordinate (B) at (0,0);
            \\coordinate (C) at (2,0);
            \\coordinate (M) at (1,0);
            \\coordinate (A) at (1, 1.732);
            \\coordinate (G) at (1, 0.577);
            \\coordinate (I) at (1, 1.155);
            \\draw[thick] (A) -- (B) -- (C) -- cycle;
            \\draw (A) -- (M);
            \\fill (A) circle (1pt) node[above] {$A$};
            \\fill (B) circle (1pt) node[left] {$B$};
            \\fill (C) circle (1pt) node[right] {$C$};
            \\fill (M) circle (1pt) node[below] {$M$};
            \\fill (G) circle (1pt) node[below right] {$G$};
            \\fill (I) circle (1pt) node[left] {$I$};
            \\end{tikzpicture}
            \\end{center}''')

                # Nội dung lời giải
                loigiai = ('''%s
            Ta có $\\left| \\overrightarrow{AB} \\right| = AB = %s$. Gọi $M$ là trung điểm của $BC$,\\\\
            Ta có $AG = \\frac{2}{3}AM = \\frac{2}{3}\\sqrt{AB^2 - BM^2} = \\frac{2}{3}\\sqrt{%s} = %s$.\\\\
            Lại có $I$ là trung điểm $AG$ và $G$ là trọng tâm nên ta dễ dàng suy ra \\\\ $MI = MG + GI = \\frac{1}{3}AM + \\frac{1}{3}AM = \\frac{2}{3}AM = AG = %s$.\\\\
            Áp dụng định lý Py-ta-go trong tam giác vuông $BMI$, ta có:\\\\
            $|\\overrightarrow{BI}| = BI = \\sqrt{BM^2 + MI^2} = \\sqrt{%s} = %s \\approx %s$.''' % (code_hinh, str_a, str_ab_bm, str_ag, str_ag, str_bm2_mi2, str_bi, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

