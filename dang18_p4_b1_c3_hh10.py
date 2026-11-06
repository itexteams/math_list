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


def bt_dang18_p4_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Random điểm M(xM, yM)
                xM = randint(-5, 5)
                yM = randint(-5, 5)

                # Để trung điểm I của PQ có tọa độ nguyên, tổng hoành độ và tung độ của P, Q phải chẵn
                xP = randint(-5, 5)
                yP = randint(-5, 5)

                # Đảm bảo xQ, yQ khác xP, yP và I nguyên
                xQ = xP + 2 * randint(-3, 3)
                if xQ == xP: xQ = xP + 2
                yQ = yP + 2 * randint(-2, 2)
                if yQ == yP: yQ = yP + 2

                # Tính toán các thành phần lời giải
                # 1. Trường hợp song song PQ
                u1 = xQ - xP
                u2 = yQ - yP
                # Rút gọn vecto chỉ phương
                g1 = math.gcd(u1, u2)
                a1, b1 = u1 // g1, u2 // g1

                # 2. Trường hợp đi qua trung điểm I
                xI = (xP + xQ) // 2
                yI = (yP + yQ) // 2
                v1 = xI - xM
                v2 = yI - yM

                # Rút gọn vecto chỉ phương MI
                if v1 == 0 and v2 == 0: # Tránh trường hợp M trùng I
                    xM += 1
                    v1 = xI - xM

                g2 = math.gcd(v1, v2)
                a2, b2 = v1 // g2, v2 // g2

                # Hàm tạo chuỗi phương trình tham số
                def pt_ts(x0, y0, a, b):
                    res = '\\begin{cases} x = ' + str(x0)
                    if a > 0: res += ' + ' + (str(a) if a != 1 else '') + 't'
                    elif a < 0: res += ' - ' + (str(abs(a)) if abs(a) != 1 else '') + 't'

                    res += ' \\\\ y = ' + str(y0)
                    if b > 0: res += ' + ' + (str(b) if b != 1 else '') + 't'
                    elif b < 0: res += ' - ' + (str(abs(b)) if abs(b) != 1 else '') + 't'
                    res += ' \\end{cases}'
                    return res

                # Đáp án đúng
                d1_true = pt_ts(xM, yM, a1, b1)
                d2_true = pt_ts(xM, yM, a2, b2)
                da_dung = d1_true + ' \\text{và} ' + d2_true

                # B4: Điều chỉnh các phương án sai
                s1 = pt_ts(xM, yM, a1+1, b1) + ' \\text{và} ' + pt_ts(xM, yM, a2, b2-1)
                s2 = pt_ts(xP, yP, a1, b1) + ' \\text{và} ' + pt_ts(xQ, yQ, a2, b2)
                s3 = pt_ts(xM, yM, b1, a1) + ' \\text{và} ' + pt_ts(xM, yM, b2, a2)

                # Câu hỏi
                noidungcauhoi = ('Lập phương trình đường thẳng đi qua điểm $M(%s;%s)$ và cách đều hai điểm $P(%s;%s)$, $Q(%s;%s)$.'
                                 %(latex(xM), latex(yM), latex(xP), latex(yP), latex(xQ), latex(yQ)))

                # Các đáp án
                da_d = ('\\True $' + str(da_dung))+'$'
                da_s1 = '$'+str(s1)+'$'
                da_s2 = '$'+str(s2) +'$'
                da_s3 = '$'+str(s3) +'$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B2: Viết lại y hệt nội dung ảnh)
                loigiai = ('Xét đường thẳng $d$ song song với $PQ$ ($d // PQ$) thì thỏa mãn điều kiện cách đều $P$ và $Q$. \\\\'
                           'Vectơ chỉ phương $\\vec{PQ} = (%s; %s)$. Do $d$ đi qua $M(%s; %s)$ và có cùng VTCP với $PQ$ nên '
                           '$d: %s$. \\\\'
                           'Xét đường thẳng $d\'$ không song song với $PQ$. Để $d\'$ cách đều $P, Q$ thì $d\'$ phải đi qua trung điểm $I$ của đoạn thẳng $PQ$. \\\\'
                           'Tọa độ trung điểm $I$ của $PQ$ là: $I\\left(\\frac{%s + (%s)}{2}; \\frac{%s + %s}{2}\\right) = (%s; %s)$. \\\\'
                           'Khi đó $d\'$ đi qua hai điểm $M(%s; %s)$ và $I(%s; %s)$. \\\\'
                           'Vectơ chỉ phương $\\vec{MI} = (%s; %s)$. \\\\'
                           'Vậy phương trình đường thẳng $d\'$ là: $d\': %s$.'
                           %(latex(u1), latex(u2), latex(xM), latex(yM), d1_true,
                             latex(xP), latex(xQ), latex(yP), latex(yQ), latex(xI), latex(yI),
                             latex(xM), latex(yM), latex(xI), latex(yI), latex(v1), latex(v2), d2_true))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

