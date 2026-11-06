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


def bt_dang35_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo các biến ký hiệu cho việc tính toán
            b_sym, c_sym = symbols('b c')

            # Bước 1 & 3: Thiết lập các giá trị ngẫu nhiên và tính toán logic bài toán
            # Để bài toán đẹp (tọa độ nguyên), ta sẽ chọn A và các đường thẳng sao cho kết quả nguyên
            def generate_data():
                while True:
                    # Ngẫu nhiên tọa độ điểm A
                    xa = random.randint(-5, 5)
                    ya = random.randint(-5, 5)

                    # Đường trung tuyến CC' có dạng y - k = 0 (giống mẫu trong ảnh)
                    k = random.randint(-5, 5)

                    # Đường trung tuyến BB' có dạng x - my + n = 0
                    m = random.randint(1, 3)
                    # Để B có tọa độ nguyên, ta chọn yB trước, sau đó tính xB qua phương trình BB'
                    # Mà C' (trung điểm AB) nằm trên CC' (y=k) nên (ya + yb)/2 = k => yb = 2k - ya
                    yb = 2 * k - ya
                    xb = random.randint(-5, 5)
                    # Tính n dựa trên B(xb, yb) thuộc BB': xb - m*yb + n = 0 => n = m*yb - xb
                    n = m * yb - xb

                    # Tính tọa độ C(xc, yc): C thuộc CC' nên yc = k
                    # B' (trung điểm AC) thuộc BB': (xa + xc)/2 - m*(ya + yc)/2 + n = 0
                    # => xc/2 = m*(ya + k)/2 - n - xa/2 => xc = m*(ya + k) - 2n - xa
                    yc = k
                    xc = m * (ya + yc) - 2 * n - xa

                    # Kiểm tra điều kiện tam giác (A, B, C không thẳng hàng) và các điểm phân biệt
                    if (xa*(yb-yc) + xb*(yc-ya) + xc*(ya-yb)) != 0 and (xb != xc or yb != yc):
                        return xa, ya, m, n, k, xb, yb, xc, yc

            xa, ya, m, n, k, xb, yb, xc, yc = generate_data()

            # Biểu diễn phương trình đường thẳng để in
            eq_BB = 'x - %sy + %s = 0' % (latex(m) if m != 1 else '', latex(n))
            if m == 1: eq_BB = 'x - y + %s = 0' % latex(n) # Case m=1
            # Tinh chỉnh hiển thị dấu cho n
            if n > 0: eq_BB = eq_BB.replace('+ %s'%n, '+ %s'%n)
            elif n < 0: eq_BB = eq_BB.replace('+ %s'%n, '- %s'%abs(n))
            else: eq_BB = eq_BB.replace('+ 0', '')

            eq_CC = 'y - %s = 0' % latex(k) if k != 0 else 'y = 0'

            # Bước 2: Viết nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có $A(%s;%s)$ và hai đường trung tuyến là $BB': %s$, $CC': %s$. Tìm tọa độ đỉnh $B$ và $C$.'''
                            % (latex(xa), latex(ya), eq_BB, eq_CC))

            # Bước 4: Tạo các phương án và lời giải chi tiết
            da_dung = '$B(%s;%s)$ và $C(%s;%s)$' % (latex(xb), latex(yb), latex(xc), latex(yc))

            # Tạo phương án sai (tránh trùng đáp án đúng)
            s = []
            while len(s) < 3:
                offset = random.choice([-2, -1, 1, 2])
                wrong_b = (xb + offset, yb - offset)
                wrong_c = (xc - offset, yc + offset)
                candidate = '$B(%s;%s)$ và $C(%s;%s)$' % (latex(wrong_b[0]), latex(wrong_b[1]), latex(wrong_c[0]), latex(wrong_c[1]))
                if candidate != da_dung and candidate not in s:
                    s.append(candidate)

            da_s1, da_s2, da_s3 = s
            list_1 = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết theo đúng logic trong ảnh
            # B thuộc BB' nên xB = m*b - n (với b là tung độ yB)
            # Trong ảnh x - 2y + 1 = 0 => x = 2y - 1. Dạng (2b-1; b)
            expr_xb = '%sb %s' % (latex(m) if m != 1 else '', latex(-n) if -n < 0 else '+ ' + latex(-n))
            if m == 1: expr_xb = 'b %s' % (latex(-n) if -n < 0 else '+ ' + latex(-n))
            expr_xb = expr_xb.replace('+ -', '- ').replace('  ', ' ')

            yc_val = k
            # Trung điểm C' của AB: ((m*b - n + xa)/2 ; (b + ya)/2)
            mid_c_y = ' \\frac{b + %s}{2} ' % latex(ya)

            loigiai = ('''Do $B \\in BB'$ nên tọa độ của $B$ có dạng $(%s; b)$. \\\\
            Vì $C'$ là trung điểm của $AB$ nên $C' \\left( \\frac{%s + %s}{2}; %s \\right)$. \\\\
            Mặt khác, $C' \\in CC'$ nên ta được: $%s - %s = 0 \\Leftrightarrow b = %s$. \\\\
            Suy ra $B(%s; %s)$. \\\\
            Tương tự, vì $C \\in CC'$ nên tọa độ $C$ có dạng $(c; %s)$. \\\\
            $B'$ là trung điểm của $AC$ nên $B' \\left( \\frac{c + %s}{2}; \\frac{%s + %s}{2} \\right) = B' \\left( \\frac{c + %s}{2}; %s \\right)$. \\\\
            Mặt khác $B' \\in BB'$ nên ta có phương trình: \\\\
            $\\frac{c + %s}{2} - %s(%s) + %s = 0 \\Leftrightarrow c = %s$. \\\\
            Vậy $B(%s; %s)$ và $C(%s; %s)$.'''
                % (expr_xb, expr_xb, latex(xa), mid_c_y, 
                   mid_c_y, latex(k), latex(yb),
                   latex(xb), latex(yb),
                   latex(yc), latex(xa), latex(ya), latex(yc), latex(xa), latex(Rational(ya+yc, 2)),
                   latex(xa), latex(m), latex(Rational(ya+yc, 2)), latex(n), latex(xc),
                   latex(xb), latex(yb), latex(xc), latex(yc)
                  ))

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content 

