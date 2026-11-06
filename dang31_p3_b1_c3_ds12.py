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


def bt_dang31_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Hàm vận tốc v(t) = a*t - t^2. 
                # Để kết quả nguyên đẹp, chọn a là số chẵn và t1 là bội của 3.
                a = random.choice([2, 4, 6, 8])
                t1 = random.choice([3, 6, 9])
                x0 = randint(1, 10) # Tọa độ ban đầu

                # Tính toán các hệ số cho lời giải
                hiso_t2 = a // 2
                hiso_t3_mau = 3

                # Tính tọa độ tại thời điểm t1: x(t1) = (a/2)*t1^2 - (1/3)*t1^3 + x0
                xt1_tu = (hiso_t2 * (t1**2)) - Rational(t1**3, 3) + x0

                # Khoảng cách so với vị trí ban đầu: |x(t1) - x0| = |(a/2)*t1^2 - (1/3)*t1^3|
                kq_val = abs(int((hiso_t2 * (t1**2)) - (t1**3 / 3)))

                # Đáp án đúng
                da = '$%s$ m' % kq_val

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    # Các phương án nhiễu: tính nhầm dấu, quên trị tuyệt đối, hoặc tính nhầm t1^2 thành t1
                    nhieu = random.choice([
                        abs(kq_val + randint(5, 15)),
                        abs(kq_val - randint(5, 10)),
                        abs(int(a * t1 - t1**2)), # v(t1)
                        abs(int(hiso_t2 * t1 - (t1**2 / 3))), # tính sai bậc
                        20, 25, 40, 50
                    ])
                    if nhieu != kq_val and nhieu > 0:
                        s.add('$%s$ m' % int(nhieu))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # B2: Viết lại bài toán theo mẫu code python
                # Câu hỏi
                noidungcauhoi = (r'''Một vật chuyển động dọc theo một đường thẳng (có gắn trục tọa độ $Ox$ với độ dài đơn vị bằng $1$ m). Biết rằng vật chuyển động với vận tốc (tính theo m/s) là $v(t) = %st - t^2$ ($0 \le t \le 10$, tính theo giây) và lúc đầu vật ở vị trí có tọa độ $x_0 = %s$. Tại thời điểm $t = %s$ giây, vật cách vị trí ban đầu bao xa?'''
                                 % (latex(a), latex(x0), latex(t1)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Tính các giá trị trung gian để trình bày lời giải
                t1_2 = t1**2
                t1_3 = t1**3
                v_t1_int = int(hiso_t2 * t1_2 - t1_3 / 3 + x0)
                khoang_cach_tinh = int(v_t1_int - x0)

                loigiai = (r'''Ta có $x(t) = \int v(t) \text{d}t = \int (%st - t^2) \text{d}t = %st^2 - \frac{t^3}{3} + C$. \\
                             Theo giả thiết, $x(0) = x_0 = %s$, suy ra $C = %s$. \\
                             Vậy $x(t) = %st^2 - \frac{t^3}{3} + %s, 0 \le t \le 10$. \\
                             Ta có $|x(%s) - x(0)| = \left| %s \cdot %s^2 - \frac{%s^3}{3} + %s - %s \right| = |%s| = %s$. \\
                             Vậy tại thời điểm $t = %s$, vật cách vị trí ban đầu %s m.'''
                           % (latex(a), latex(hiso_t2), latex(x0), latex(x0),
                              latex(hiso_t2), latex(x0),
                              latex(t1), latex(hiso_t2), latex(t1), latex(t1), latex(x0), latex(x0),
                              latex(khoang_cach_tinh), latex(kq_val),
                              latex(t1), latex(kq_val)))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

