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


def bt_dang30_p1_b1_c2_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random cạnh a từ 1 đến 10 và góc A từ các góc tiêu biểu
                a = random.randint(1, 10)
                angles = [60, 90, 120]
                alpha = random.choice(angles)

                # Tính toán độ dài và biểu thức chính xác dựa theo góc alpha
                if alpha == 60:
                    val = (a * math.sqrt(3)) / 2
                    if a % 2 == 0:
                        exact_ao = "\\sqrt{3}" if a == 2 else "%s\\sqrt{3}" % (a // 2)
                    else:
                        exact_ao = "\\frac{\\sqrt{3}}{2}" if a == 1 else "\\frac{%s\\sqrt{3}}{2}" % a

                elif alpha == 90:
                    val = (a * math.sqrt(2)) / 2
                    if a % 2 == 0:
                        exact_ao = "\\sqrt{2}" if a == 2 else "%s\\sqrt{2}" % (a // 2)
                    else:
                        exact_ao = "\\frac{\\sqrt{2}}{2}" if a == 1 else "\\frac{%s\\sqrt{2}}{2}" % a

                elif alpha == 120:
                    val = a / 2
                    if a % 2 == 0:
                        exact_ao = str(a // 2)
                    else:
                        exact_ao = "\\frac{1}{2}" if a == 1 else "\\frac{%s}{2}" % a

                # Làm tròn đến hàng phần chục
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
                noidungcauhoi = ('''Cho hình thoi tâm $O$, cạnh bằng $%s$ và $\\widehat{A} = %s^\\circ$. Độ dài của vectơ $\\overrightarrow{AO}$ bằng bao nhiêu? \\textit{Kết quả làm tròn đến hàng phần chục.}''' % (str_a, alpha))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính toán tọa độ động cho hình vẽ TikZ dựa vào góc A
                half_alpha = alpha / 2
                len_draw = 2.0  # Chiều dài cạnh vẽ trên giấy (phóng to để dễ nhìn)
                x_B = len_draw * math.cos(math.radians(half_alpha))
                y_B = len_draw * math.sin(math.radians(half_alpha))
                x_C = 2 * x_B
                x_O = x_B

                # Tọa độ cung tròn cho góc A
                arc_start_x = 0.4 * math.cos(math.radians(-half_alpha))
                arc_start_y = 0.4 * math.sin(math.radians(-half_alpha))

                # Tọa độ ký hiệu góc vuông
                sq_x1 = x_O - 0.15
                sq_y1 = 0.15

                # Mã TikZ vẽ hình thoi động
                code_hinh = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, >=stealth]
            \\coordinate (A) at (0,0);
            \\coordinate (C) at (%.3f,0);
            \\coordinate (B) at (%.3f,%.3f);
            \\coordinate (D) at (%.3f,-%.3f);
            \\coordinate (O) at (%.3f,0);
            \\draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
            \\draw (A) -- (C);
            \\draw (B) -- (D);
            \\draw (%.3f,0) -- (%.3f,%.3f) -- (%.3f,%.3f);
            \\draw (%.3f,%.3f) arc (-%.1f:%.1f:0.4);
            \\node[left] at (A) {$A$};
            \\node[above] at (B) {$B$};
            \\node[right] at (C) {$C$};
            \\node[below] at (D) {$D$};
            \\node[below right] at (O) {$O$};
            \\node[above left] at (%.3f,%.3f) {$%s$};
            \\end{tikzpicture}
            \\end{center}''' % (x_C, x_B, y_B, x_B, y_B, x_O, sq_x1, sq_x1, sq_y1, x_O, sq_y1, arc_start_x, arc_start_y, half_alpha, half_alpha, x_B/2, y_B/2, str_a))

                # Nội dung lời giải dạng tổng quát đúng cho mọi góc
                loigiai = ('''%s
            Trong hình thoi $ABCD$, hai đường chéo $AC$ và $BD$ vuông góc với nhau tại trung điểm $O$ của mỗi đường và $AO$ là tia phân giác của góc $\\widehat{A}$.\\\\
            Suy ra $\\widehat{OAB} = \\frac{\\widehat{A}}{2} = \\frac{%s^\\circ}{2} = %s^\\circ$.\\\\
            Xét $\\triangle OAB$ vuông tại $O$, ta có:
            $$AO = AB \\cdot \\cos{\\widehat{OAB}} = %s \\cdot \\cos{%s^\\circ} = %s$$
            Vậy $\\left| \\overrightarrow{AO} \\right| = AO \\approx %s$.''' % (code_hinh, alpha, int(half_alpha), str_a, int(half_alpha), exact_ao, kq))

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

