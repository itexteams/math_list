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


def bt_dang21_p4_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số cho đồ thị
                v_max = random.randint(2, 6) # Vận tốc tối đa (m/s)
                t1 = random.randint(1, 3)    # Thời điểm bắt đầu đi đều (s)
                t2 = t1 + random.randint(1, 3) # Tổng thời gian xét (s)

                # Tính quãng đường S = diện tích hình thang
                # S = (đáy lớn + đáy bé) * chiều cao / 2
                # Đáy lớn = t2, đáy bé = t2 - t1, chiều cao = v_max
                day_lon = t2
                day_be = t2 - t1
                S_rational = Rational((day_lon + day_be) * v_max, 2)

                # Đáp án đúng
                kq = latex(S_rational)
                da = '$%s$' % kq

                # Tạo các đáp án sai (đảm bảo không trùng và không âm)
                s = set()
                while len(s) < 3:
                    # Các phương án nhiễu: tính sai công thức hoặc cộng trừ ngẫu nhiên
                    wrong = random.choice([
                        Rational(t2 * v_max, 2), # Diện tích tam giác (quên đoạn đi đều)
                        S_rational + random.randint(1, 3),
                        S_rational - Rational(1, 2) if S_rational > 1 else S_rational + 4,
                        Rational((t1 + t2) * v_max, 2),
                        v_max * t2 # Chuyển động đều hoàn toàn
                    ])
                    if wrong != S_rational and wrong > 0:
                        s.add('$%s$' % latex(wrong))

                list_wrong = list(s)
                das1, das2, das3 = list_wrong[0], list_wrong[1], list_wrong[2]

                # Vẽ hình bằng TikZ
                tikz_code = r"""\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \draw[->] (-0.5,0) -- (%s+0.8,0) node[below] {$t$ (s)};
                \draw[->] (0,-0.5) -- (0,%s+0.8) node[left] {$v$ (m/s)};
                \draw[thick, blue] (0,0) -- (%s,%s) -- (%s,%s);
                \draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s) -- (0,%s) node[left] {$%s$};
                \draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s);
                \node[below left] at (0,0) {$O$};
            \end{tikzpicture}""" % (t2, v_max, t1, v_max, t2, v_max, t1, t1, t1, v_max, v_max, v_max, t2, t2, t2, v_max)

                # Câu hỏi
                noidungcauhoi = ('''Một vật chuyển động với vận tốc được cho bởi đồ thị ở hình bên. Tính quãng đường (đơn vị: m) mà vật di chuyển được trong $%s$ giây đầu tiên.
            \\begin{center}
            %s
            \\end{center}''' % (latex(t2), tikz_code))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Dựa vào đồ thị, quãng đường vật đi được từ thời điểm $t=0$ đến $t=%s$ giây chính là diện tích hình thang tạo bởi đồ thị và trục hoành. \\\\
                Quãng đường vật đi được là:
                $$S = \\int_0^{%s} |v(t)| dt = \\frac{(%s + %s) \\cdot %s}{2} = %s \\text{ (m)}.$$''' 
                % (latex(t2), latex(t2), latex(t2), latex(day_be), latex(v_max), kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

