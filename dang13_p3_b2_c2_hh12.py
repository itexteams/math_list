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


def bt_dang13_p3_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- Randomization of the problem parameters ---

                # Randomize coordinates of A and B
                def rand_coord(min_val=5, max_val=20):
                    return random.randint(min_val, max_val)

                ax, ay, az = rand_coord(), rand_coord(), rand_coord()
                bx, by, bz = rand_coord(), rand_coord(), rand_coord()

                # Choose simple fraction for t: t_num / t_den
                fractions = [Rational(n, d) for n, d in [(1,2), (1,3), (2,3), (1,4), (3,4), (1,5), (2,5), (3,5), (4,5)]]
                t = random.choice(fractions)
                t_num = t.p
                t_den = t.q

                # To ensure (bz - az) is a multiple of t_den, let bz - az = k * t_den
                k = random.randint(2, 5) # Scale factor for z difference
                delta_z_new = k * t_den

                # Randomly decide which point is higher, set coordinates
                while True:
                    if random.choice([True, False]):
                        az_temp = rand_coord(15, 25)
                        bz_temp = az_temp - delta_z_new
                    else:
                        az_temp = rand_coord(5, 15)
                        bz_temp = az_temp + delta_z_new

                    delta_z = bz_temp - az_temp
                    c_temp = az_temp + t * delta_z
                    c_temp = int(c_temp)

                    # Ensure c is a simple integer altitude (e.g., between 8 and 20)
                    if 8 <= c_temp <= 20 and c_temp != az_temp and c_temp != bz_temp:
                        az, bz, c = az_temp, bz_temp, c_temp
                        break

                # Re-randomize ax, ay, bx, by after fixing az, bz
                ax, ay = rand_coord(), rand_coord()
                bx, by = rand_coord(), rand_coord()

                # 1. vectơ AB
                AB_x, AB_y, AB_z = bx - ax, by - ay, bz - az # AB_z is delta_z

                # 2. Coordinates of C(a, b, c)
                a = ax + t * AB_x
                b = ay + t * AB_y
                # c is already calculated

                # 3. Calculation of P
                P = 10 * a - b + 3 * c

                # Final result (P should be an integer)
                kq = int(P)

                # --- Helper function (Định nghĩa trước khi sử dụng!) ---
                def latex_to_text(l):
                    # Hàm này nhận latex number string và trả về giá trị số nguyên
                    l_str = str(l).replace('\\circ', '').replace('$', '').replace('{', '').replace('}', '').replace(' ', '').replace('latex(', '').replace(')', '').replace('\\frac', '').replace('\\left', '').replace('\\right', '').strip()
                    try:
                         # Đối với các đáp án là số nguyên
                         return int(l_str)
                    except ValueError:
                         # Trả về một giá trị lớn để loại trừ nó khỏi danh sách đáp án
                         return kq + 1000 


                da = '$%s$'%(latex(kq))

                # Incorrect answers (raw integer values)
                s_raw = []
                seen_values = {kq}

                # Generate 3 incorrect answers with small offsets
                offsets = [random.choice([1, 2, 3, 4, -1, -2, -3, -4]), 
                           random.choice([5, 6, -5, -6]), 
                           random.choice([7, 8, -7, -8])]

                for offset in offsets:
                    val = kq + offset
                    if val not in seen_values:
                        s_raw.append(val)
                        seen_values.add(val)

                # Ensure three distinct wrong answers
                while len(s_raw) < 3:
                    new_wrong = kq + random.choice([10, 11, -10, -11])
                    if new_wrong not in seen_values:
                        s_raw.append(new_wrong)
                        seen_values.add(new_wrong)

                # s contains raw latex number strings
                s = [latex(val) for val in s_raw]

                # Convert all options to the final LaTeX format
                da_d = ('\\True ' + str(da))


                s_final = ['$%s$'%(val) for val in s]

                das1 = random.choice(s_final)
                s_final.remove(das1)
                das2 = random.choice(s_final) 
                s_final.remove(das2)
                das3 = random.choice(s_final) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # --- Question Content ---
                def format_coord(x, y, z):
                    return f'{latex(x)};{latex(y)};{latex(z)}'

                noidungcauhoi = ('''Trong một khu du lịch, người ta cho du khách trải nghiệm thiên nhiên bằng cách đu theo đường trượt zipline từ vị trí $A$ cao $%s$ mét sang vị trí $B$ cao $%s$ mét. Với hệ trục tọa độ $Oxyz$ cho trước (đơn vị: mét), tọa độ của $A(%s;%s;%s)$ và $B(%s;%s;%s)$. Biết tọa độ du khách khi ở độ cao $%s$ mét là $(a;b;c)$. Giá trị $P = 10a - b + 3c$ bằng bao nhiêu?'''
                                 %(latex(az), latex(bz), latex(ax), latex(ay), latex(az), latex(bx), latex(by), latex(bz), latex(c)
                                 ))

                # --- Solution Content ---

                loigiai=('''Ta có $\\overrightarrow{AB} = B - A = (%s - %s; %s - %s; %s - %s) = (%s; %s; %s)$.\\\\
            Phương trình tham số của đường zipline là $d: \\begin{cases} x = %s + %st \\\\ y = %s + %st \\\\ z = %s + %st \\end{cases}$.\\\\
            Gọi $C(a;b;c)$ là tọa độ của du khách đang ở độ cao $%s$ mét. Ta có $c=%s$, nên khi đó: \\\\
            $%s + %st = %s \\Rightarrow %st = %s \\Rightarrow t = %s$.\\\\
            Thay $t = %s$ vào phương trình của $x$ và $y$, ta có: \\\\
            $a = x_C = %s + %s \\cdot \\left(%s\\right) = %s + %s = %s$. \\\\
            $b = y_C = %s + %s \\cdot \\left(%s\\right) = %s + %s = %s$. \\\\
            Vậy tọa độ của du khách là $C\\left(%s; %s; %s\\right)$, suy ra $a=%s, b=%s, c=%s$. \\\\
            Khi đó $P = 10a - b + 3c = 10 \\cdot \\left(%s\\right) - %s + 3 \\cdot (%s) = %s - %s + %s = %s$.'''

                         # AB vectơ
                         %(latex(bx), latex(ax), latex(by), latex(ay), latex(bz), latex(az), latex(AB_x), latex(AB_y), latex(AB_z),

                           # Parametric equation
                           latex(ax), latex(AB_x), latex(ay), latex(AB_y), latex(az), latex(AB_z),

                           # Find t
                           latex(c), latex(c),
                           latex(az), latex(AB_z), latex(c), latex(-AB_z), latex(c - az), latex(t),

                           # Calculate a, b
                           latex(t),
                           latex(ax), latex(AB_x), latex(t), latex(ax), latex(t * AB_x), latex(a),
                           latex(ay), latex(AB_y), latex(t), latex(ay), latex(t * AB_y), latex(b),

                           # Final P calculation
                           latex(a), latex(b), latex(c), latex(a), latex(b), latex(c),
                           latex(a), latex(b), latex(c), latex(10*a), latex(b), latex(3*c), latex(kq)
                           ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')
            return content   

