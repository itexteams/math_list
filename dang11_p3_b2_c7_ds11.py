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


def bt_dang11_p3_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo các hệ số để v'(t) có nghiệm nguyên đẹp
                # v(t) = t^2 - 2kt + m -> x(t) = 1/3*t^3 - k*t^2 + m*t + c
                k = randint(2, 4)
                m = randint(5, 8)
                c = randint(1, 10)

                # Khoảng thời gian [t1, t2] sao cho k nằm trong khoảng này
                t1 = random.choice([0.5, 1.5])
                t2 = randint(5, 7)

                # Hàm tọa độ và vận tốc
                xt = Rational(1, 3)*t**3 - k*t**2 + m*t + c
                vt = diff(xt, t)

                # Tính giá trị tại các biên và điểm cực trị
                v_t1 = vt.subs(t, t1)
                v_k = vt.subs(t, k)
                v_t2 = vt.subs(t, t2)

                # Tìm vận tốc lớn nhất
                v_max_val = max(v_t1, v_k, v_t2)

                # Định dạng số thập phân dùng dấu phẩy
                def format_vn(val):
                    num = Decimal(float(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP).normalize()
                    return str(num).replace('.', ',')

                kq_chinh_xac = format_vn(v_max_val)

                # Các đáp án trắc nghiệm
                da = '$%s$' % kq_chinh_xac

                # Tạo các phương án nhiễu không trùng đáp án đúng
                s = []
                while len(s) < 6:
                    sai = float(v_max_val) + random.choice([-2, -1, 1, 2, 3, 5])
                    if sai > 0 and format_vn(sai) != kq_chinh_xac:
                        val_str = '$%s$' % format_vn(sai)
                        if val_str not in s:
                            s.append(val_str)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một chất điểm chuyển động thẳng trên trục với biểu thức tọa độ $x=%s$ (cm), $t$ tính theo giây (s). Hỏi từ thời điểm $t=%s$ s đến thời điểm $t=%s$ s thì vận tốc lớn nhất của chất điểm là bao nhiêu cm/s?'''
                                 % (latex(xt), format_vn(t1), format_vn(t2)))

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải bao gồm bảng biến thiên mô phỏng bằng TikZ
                loigiai = ('''Vận tốc của vật tại thời điểm $t$ là: $v\\left(t\\right)=x'\\left(t\\right)=%s$. \\\\
            Lập bảng biến thiên của hàm số $v\\left(t\\right)$ trên đoạn $\\left[%s;%s\\right]$ ta được: \\\\
            \\begin{tikzpicture}[line width=1pt]
            \\draw (0,0) rectangle (12,2.5);
            \\draw (0,1.5) -- (12,1.5);
            \\draw (2,0) -- (2,2.5);
            \\node at (1,2) {$t$};
            \\node at (3,2) {$%s$};
            \\node at (7,2) {$%s$};
            \\node at (11,2) {$%s$};
            \\node at (1,0.75) {$v\\left(t\\right)$};
            \\node (A) at (3,1.2) {$%s$};
            \\node (B) at (7,0.3) {$%s$};
            \\node (C) at (11,1.2) {$%s$};
            \\draw[->] (A) -- (B);
            \\draw[->] (B) -- (C);
            \\end{tikzpicture} \\\\
            Vậy vận tốc lớn nhất của chất điểm là $v_{\\max}=%s$ (cm/s).'''
                           % (latex(vt), format_vn(t1), format_vn(t2),
                              format_vn(t1), format_vn(k), format_vn(t2),
                              format_vn(v_t1), format_vn(v_k), format_vn(v_t2),
                              kq_chinh_xac))
                dapan='\\shortans[0]{$%s$}\n'%(kq_chinh_xac)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

