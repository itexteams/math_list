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


def bt_dang31_p3_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp để tìm bộ số đẹp (M là số nguyên và A, B cùng phía)
                while True:
                    # Tọa độ điểm A, B ngẫu nhiên
                    xa, ya = random.randint(-5, 5), random.randint(-5, 5)
                    xb, yb = random.randint(-5, 5), random.randint(-5, 5)

                    if (xa, ya) == (xb, yb): continue

                    # Đường thẳng d: ax + by + c = 0
                    a_d, b_d = random.randint(-3, 3), random.randint(-3, 3)
                    if a_d == 0 and b_d == 0: continue
                    c_d = random.randint(-10, 10)

                    # Kiểm tra A, B có cùng phía với d không
                    fa = a_d * xa + b_d * ya + c_d
                    fb = a_d * xb + b_d * yb + c_d

                    if fa * fb > 0:
                        # Phương trình đường thẳng AB: (ya-yb)x + (xb-xa)y + xa*yb - xb*ya = 0
                        a_ab = ya - yb
                        b_ab = xb - xa
                        c_ab = xa * yb - xb * ya

                        # Tìm giao điểm M của d và AB
                        # Hệ: a_d*x + b_d*y = -c_d
                        #     a_ab*x + b_ab*y = -c_ab
                        det = a_d * b_ab - a_ab * b_d
                        if det == 0: continue # Song song thì bỏ qua

                        xm_num = b_d * c_ab - b_ab * c_d
                        ym_num = a_ab * c_d - a_d * c_ab

                        if xm_num % det == 0 and ym_num % det == 0:
                            xm, ym = xm_num // det, ym_num // det
                            # Tính AB để dùng trong lời giải
                            ab_val = math.sqrt((xb-xa)**2 + (yb-ya)**2)
                            ab_sq = (xb-xa)**2 + (yb-ya)**2
                            break

                # Đáp án đúng
                kq = 'M(%s; %s)' % (xm, ym)
                da_d = ('\\True $' + kq + '$')

                # Tạo các phương án sai bằng cách nhiễu tọa độ
                s_list = [
                    'M(%s; %s)' % (xm + 1, ym),
                    'M(%s; %s)' % (xm, ym + 1),
                    'M(%s; %s)' % (xm - 2, ym + 1),
                    'M(%s; %s)' % (xm + 2, ym - 1),
                    'M(%s; %s)' % (ya, xa), # Đảo tọa độ
                    'M(%s; %s)' % (xm + 1, ym - 1)
                ]
                random.shuffle(s_list)
                da_s1 = '$' + s_list[0] + '$'
                da_s2 = '$' + s_list[1] + '$'
                da_s3 = '$' + s_list[2] + '$'

                # Câu hỏi
                str_d = ''
                if a_d != 0: 
                    str_d += f'{a_d if a_d != 1 else ""}x'
                if b_d > 0: 
                    str_d += f'+{b_d if b_d != 1 else ""}y'
                elif b_d < 0:
                    str_d += f'{b_d if b_d != -1 else "-"}y'
                if c_d > 0: str_d += f'+{c_d}'
                elif c_d < 0: str_d += f'{c_d}'
                str_d = str_d.replace('1x', 'x').replace('-1x', '-x').replace('1y', 'y').replace('-1y', '-y') + '=0'

                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường thẳng $d: %s$ và hai điểm $A(%s;%s)$, $B(%s;%s)$. Điểm $M$ thuộc $d$ sao cho $|MA - MB|$ lớn nhất là $(a;b)$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 %(str_d, xa, ya, xb, yb))

                # Lời giải chi tiết
                # Phương trình AB dạng Latex
                str_ab = ''
                if a_ab != 0: str_ab += f'{a_ab if a_ab != 1 else ""}x'
                if b_ab > 0: str_ab += f'+{b_ab if b_ab != 1 else ""}y'
                elif b_ab < 0: str_ab += f'{b_ab if b_ab != -1 else "-"}y'
                if c_ab > 0: str_ab += f'+{c_ab}'
                elif c_ab < 0: str_ab += f'{c_ab}'
                str_ab = str_ab.replace('1x', 'x').replace('-1x', '-x').replace('1y', 'y').replace('-1y', '-y') + '=0'

                h1=xm+ym
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.',',')

                loigiai = ('''Ta có $P(A, d) \\cdot P(B, d) = (%s \\cdot (%s) + %s \\cdot (%s) + %s)(%s \\cdot (%s) + %s \\cdot (%s) + %s) = %s \\cdot (%s) = %s > 0$. \\\\
                           Suy ra hai điểm $A$ và $B$ cùng phía so với đường thẳng $d$. \\\\
                           Theo bất đẳng thức tam giác mở rộng, ta có $|MA - MB| \\le AB = \\sqrt{%s}$. \\\\
                           Dấu "$=$" xảy ra khi và chỉ khi $A, M, B$ thẳng hàng hay $M$ thuộc đường thẳng $AB$. \\\\
                           Đường thẳng $AB$ đi qua $A(%s;%s)$ và $B(%s;%s)$ nên có phương trình $AB: %s$. \\\\
                           Mặt khác, theo giả thiết $M$ thuộc $d$ nên tọa độ điểm $M$ thỏa mãn hệ \\\\
                           $\\begin{cases} %s \\\\ %s \\end{cases} \\Rightarrow M(%s; %s)$. Vậy $a+b=%s$.'''
                           %(a_d, xa, b_d, ya, c_d, a_d, xb, b_d, yb, c_d, fa, fb, fa*fb, ab_sq, xa, ya, xb, yb, str_ab, str_d, str_ab, xm, ym, latex(xm+ym)))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kqz)
                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\ +', '\\')
            return content 

