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


def bt_dang28_p1_b1_c2_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random theo các bộ số Pytago để kết quả chẵn đẹp
                triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)]
                ab, ad, bd = random.choice(triples)
                str_ab = str(ab)
                str_ad = str(ad)

                val_ab2 = ab**2
                val_ad2 = ad**2
                val_bd2 = bd**2
                val_bd = bd
                val = bd / 2

            elif dang == '2':
                # Random theo dạng chứa căn bậc hai (như đề gốc)
                a = random.randint(1, 5)
                if a == 1:
                    str_ab = "\\sqrt{3}"
                    str_ad = "1"
                else:
                    str_ab = "%s\\sqrt{3}" % a
                    str_ad = str(a)

                val_ab2 = 3 * (a**2)
                val_ad2 = a**2
                val_bd2 = 4 * (a**2)
                val_bd = 2 * a
                val = a

            # Định dạng kết quả (bỏ số .0 nếu là số nguyên)
            if val == int(val):
                kq = str(int(val))
                kq_float = float(val)
            else:
                kq_dec = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec).replace('.', ',')
                kq_float = float(kq_dec)

            # Các đáp án trắc nghiệm
            du = ['$%s$' % (kq)]
            da = random.choice(du)

            # Tạo các phương án nhiễu
            s_vals = [
                kq_float + 1, kq_float + 2, kq_float + 3,
                kq_float + 1.5, kq_float + 2.5, kq_float + 0.5
            ]
            if kq_float - 1 > 0: s_vals.append(kq_float - 1)
            if kq_float - 2 > 0: s_vals.append(kq_float - 2)

            s = []
            for v in s_vals:
                if v == int(v):
                    s.append('$%s$' % str(int(v)))
                else:
                    s.append('$%s$' % str(v).replace('.', ','))

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Câu hỏi
            noidungcauhoi = ('''Cho hình chữ nhật $ABCD$ tâm $O$ có cạnh $AB = %s, AD = %s$. Tìm vectơ $\\vec{u}$ có điểm đầu và điểm cuối từ các vectơ đó, khác vectơ không và cùng hướng với vectơ $\\overrightarrow{BD}$ (khác $\\overrightarrow{BD}$), tính độ dài vectơ $\\vec{u}$ đó?''' % (str_ab, str_ad))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Mã TikZ vẽ hình chữ nhật
            code_hinh = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.9, >=stealth]
            \\coordinate (A) at (0,2);
            \\coordinate (B) at (4,2);
            \\coordinate (C) at (4,0);
            \\coordinate (D) at (0,0);
            \\coordinate (O) at (2,1);
            \\draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
            \\draw (A) -- (C);
            \\draw (B) -- (D);
            \\node[above left] at (A) {$A$};
            \\node[above right] at (B) {$B$};
            \\node[below right] at (C) {$C$};
            \\node[below left] at (D) {$D$};
            \\node[above] at (O) {$O$};
            \\end{tikzpicture}
            \\end{center}''')

            # Nội dung lời giải (đã nhúng hình ảnh)
            loigiai = ('''%s
            Ta có $\\vec{u}$ khác vectơ không và cùng hướng với vectơ $\\overrightarrow{BD}$ nên $\\vec{u}$ là một trong hai vectơ $\\overrightarrow{BO}, \\overrightarrow{OD}$.\\\\
            Áp dụng định lí Py-ta-go cho tam giác $ABD$: $BD^2 = AB^2 + AD^2 = %s + %s = %s \\Rightarrow BD = %s$.\\\\
            Vì vậy: $|\\vec{u}| = |\\overrightarrow{BO}| = |\\overrightarrow{OD}| = \\frac{BD}{2} = %s$.''' % (code_hinh, val_ab2, val_ad2, val_bd2, val_bd, kq))

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

