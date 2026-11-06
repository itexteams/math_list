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


def bt_dang39_p3_b2_c4_ds12(self):
            # Khai báo biến
            n = 5 # Tổng số quà mỗi hộp
            choices = [2, 3, 4]
            random.shuffle(choices)

            i1, i2, i3 = choices # Số điện thoại iPhone trong mỗi hộp
            h1, h2, h3 = n - i1, n - i2, n - i3 # Số tai nghe tương ứng

            # 3. Tính toán xác suất
            # P(Ak) = 1/3
            # P(B|Ak) = (ik/n) * ((ik-1)/(n-1))
            pb_a1 = Rational(i1 * (i1 - 1), n * (n - 1))
            pb_a2 = Rational(i2 * (i2 - 1), n * (n - 1))
            pb_a3 = Rational(i3 * (i3 - 1), n * (n - 1))

            # P(B) = P(B|A1)P(A1) + P(B|A2)P(A2) + P(B|A3)P(A3)
            pb = Rational(1, 3) * (pb_a1 + pb_a2 + pb_a3)

            # P(A2|B) = (P(B|A2) * P(A2)) / P(B)
            pa2_b = (pb_a2 * Rational(1, 3)) / pb

            # Làm tròn đến hàng phần mười
            val_final = float(pa2_b)
            kq_dec = Decimal(str(val_final)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq_str = str(kq_dec).replace('.', ',')

            # 4. Điều chỉnh các phương án sai
            da = '$%s$' % kq_str
            s = []
            for offset in [-0.2, -0.1, 0.1, 0.2, 0.3]:
                wrong_val = float(kq_dec) + offset
                if 0 < wrong_val < 1:
                    w_str = '$%s$' % (str(round(wrong_val, 1)).replace('.', ','))
                    if w_str != da and w_str not in s:
                        s.append(w_str)

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một người tham gia trò chơi với ba hộp quà đặc biệt: Hộp màu vàng có $%s$ điện thoại iPhone và $%s$ tai nghe, hộp màu bạc có $%s$ điện thoại iPhone và $%s$ tai nghe và hộp màu đồng có $%s$ điện thoại iPhone và $%s$ tai nghe. Luật chơi được thực hiện qua 2 bước sau:\\\\
            Bước 1: Người chơi chọn ngẫu nhiên một hộp.\\\\
            Bước 2: Từ hộp đã chọn, người chơi lấy ngẫu nhiên 1 món quà:\\\\
            - Nếu quà là điện thoại iPhone, người chơi được giữ nó và lấy thêm 1 quà nữa từ cùng hộp.\\\\
            - Nếu quà là tai nghe, trò chơi kết thúc.\\\\
            Biết rằng người chơi lấy được hai điện thoại iPhone, tính xác suất để người đó lấy từ hộp màu bạc (làm tròn kết quả đến hàng phần mười)''' 
            %(latex(i1), latex(h1), latex(i2), latex(h2), latex(i3), latex(h3)))

            # Nội dung lời giải chi tiết
            loigiai = ('''Gọi $A_1$ là biến cố: Hộp được chọn màu vàng. \\\\
            $A_2$ là biến cố: Hộp được chọn màu bạc. \\\\
            $A_3$ là biến cố: Hộp được chọn màu đồng. \\\\
            $B$ là biến cố: Người chơi lấy được hai điện thoại iPhone. \\\\
            Ta có: $P(A_1) = P(A_2) = P(A_3) = \\frac{1}{3}$. \\\\
            Ta cần tính: $P(A_2 | B)$. Ta có: $P(A_2 | B) = \\frac{P(A_2 B)}{P(B)}$. \\\\
            Ta có: $P(A_2 B) = P(B | A_2) \\cdot P(A_2) = \\frac{%s}{5} \\cdot \\frac{%s}{4} \\cdot \\frac{1}{3} = %s$. \\\\
            Ta có: $P(B) = P(B | A_1) \\cdot P(A_1) + P(B | A_2) \\cdot P(A_2) + P(B | A_3) \\cdot P(A_3)$ \\\\
            $= \\frac{1}{3} \\cdot \\left( \\frac{%s}{5} \\cdot \\frac{%s}{4} + \\frac{%s}{5} \\cdot \\frac{%s}{4} + \\frac{%s}{5} \\cdot \\frac{%s}{4} \\right) = %s$. \\\\
            Vậy: $P(A_2 | B) = \\frac{P(A_2 B)}{P(B)} = \\frac{%s}{%s} \\approx %s$.''' 
            %(latex(i2), latex(i2-1), latex(pb_a2 * Rational(1,3)),
              latex(i1), latex(i1-1), latex(i2), latex(i2-1), latex(i3), latex(i3-1), latex(pb),
              latex(pb_a2 * Rational(1,3)), latex(pb), kq_str))
            dapan=' \\shortans[0]{$%s$} '%(kq_str)

            # Đưa các đáp án vào danh sách
            da_d = '\\True ' + str(da)
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

