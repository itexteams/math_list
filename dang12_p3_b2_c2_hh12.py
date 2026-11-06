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


def bt_dang12_p3_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random initial coordinates A(a1; a2; a3) and final coordinates B(b1; b2; b3)
                # Ensure a3 is not 0 for the plane intersection to be meaningful
                # and a3 != b3 so the vectơ is not parallel to the Oxy plane.

                # Coordinates of A
                a1 = random.randint(1, 5) * 5 # A value like 5, 10, 15, 20, 25
                a2 = random.randint(-5, 5) * 2 # A value like -10, -8, ..., 8, 10
                a3 = random.randint(3, 8) # Must be > 0 and different from b3

                # Coordinates of B
                b1 = random.randint(1, 5) * 5 
                b2 = random.randint(-5, 5) * 2
                b3 = random.randint(-8, -3) # Must be < 0 and different from a3

                # Example from image: A(5; 0; 5), B(10; 10; 3)
                # The image uses a simpler case where the z-coordinates are both positive, which is mathematically fine, 
                # but I'm making it so the plane is always crossed (one z positive, one negative) or the plane is $z=0$ (meaning the landing is from above, which is typical).
                # Let's stick to the image style for a more direct analogy, but ensure a3 != b3 and a3 > 0.

                a1 = random.randint(2, 8) # 2 to 8
                a2 = random.randint(-4, 4) # -4 to 4
                a3 = random.randint(5, 12) # 5 to 12 (initial height)

                b1 = a1 + random.choice([-1, 1]) * random.randint(3, 8)
                b2 = a2 + random.choice([-1, 1]) * random.randint(3, 8)
                b3 = random.randint(1, a3 - 1) # Must be between 1 and a3-1

                # vectơ AB
                u1 = b1 - a1
                u2 = b2 - a2
                u3 = b3 - a3

                # Parametric equation of the line AB:
                # x = a1 + u1*t
                # y = a2 + u2*t
                # z = a3 + u3*t

                # Landing point M(a; b; 0) is the intersection with Oxy plane (z=0)
                # z = a3 + u3*t = 0
                # t = -a3 / u3 

                t_num = -a3
                t_den = u3
                t_val = Rational(t_num, t_den)

                # Coordinates of M(a; b; 0)
                # a = a1 + u1 * t
                # b = a2 + u2 * t

                a_val = Rational(a1) + Rational(u1) * t_val
                b_val = Rational(a2) + Rational(u2) * t_val

                # Result: a + b
                kq_exact = a_val + b_val

                # Convert to decimal for rounding (làm tròn đến hàng phần chục - round to one decimal place)
                # Use float for intermediate calculation and Decimal for controlled rounding
                kq_float = float(kq_exact)
                kq_dec = Decimal(str(kq_float))

                # Rounding to the nearest tenth (0.1)
                kq_rounded = kq_dec.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Format the final answer for display
                kq = str(kq_rounded).replace('.', ',') # Replace '.' with ',' for Vietnamese format

                # Create the correct answer string for the quiz
                da = '$$%s$$'%(kq)

                # Generate incorrect answers for multiple choice
                # Use the rounded float value (kq_float) for the base of distractors
                kq_base = float(kq_rounded)

                s = [
                    '$$%s$$'%(latex(round(kq_base + 1.1, 1))).replace('.',','),
                    '$$%s$$'%(latex(round(kq_base + 0.9, 1))).replace('.',','),
                    '$$%s$$'%(latex(round(kq_base - 1.2, 1))).replace('.',','),
                    '$$%s$$'%(latex(round(kq_base - 0.7, 1))).replace('.',','),
                    '$$%s$$'%(latex(round(kq_base + 2.0, 1))).replace('.',','),
                    '$$%s$$'%(latex(round(kq_base - 1.5, 1))).replace('.',','),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Khi gắn hệ tọa độ $Oxyz$ (đơn vị trên mỗi trục tính theo kilômét) vào một sân bay, mặt phẳng $(Oxy)$ trùng với mặt sân bay. Một máy bay bay theo đường thẳng từ vị trí $A(%s; %s; %s)$ đến vị trí $B(%s; %s; %s)$ và hạ cánh tại vị trí $M(a; b; 0)$. Giá trị của $a+b$ bằng bao nhiêu? (làm tròn đến hàng phần chục).'''
                                 %(latex(a1), latex(a2), latex(a3),
                                   latex(b1), latex(b2), latex(b3)
                                  ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Ta có $\\overrightarrow{AB} = (%s - %s; %s - %s; %s - %s) = (%s; %s; %s)$.\\\\
                         Đường thẳng $AB$ có vectơ chỉ phương $\\vec{u} = (%s; %s; %s)$ nên có phương trình tham số là
                         $$\\begin{cases} x = %s + %st \\\\ y = %s + %st \\\\ z = %s + %st \\end{cases}$$
                         Vị trí máy bay hạ cánh là giao điểm $M(a; b; 0)$ của đường thẳng $AB$ và mặt phẳng $(Oxy)$, nên ta có $z=0$.
                         $$%s + %st = 0 \\Rightarrow t = \\frac{-%s}{%s} = %s.$$
                         Thay giá trị $t=%s$ vào phương trình tham số của $x$ và $y$, ta được tọa độ điểm $M(a; b; 0)$ với
                         $$a = %s + %s \\cdot %s = %s \\quad \\text{và} \\quad b = %s + %s \\cdot %s = %s.$$
                         Vậy $a+b = %s + %s = %s$.\\\\
                         Làm tròn đến hàng phần chục, ta được kết quả là $%s$.'''
                         %(latex(b1), latex(a1), latex(b2), latex(a2), latex(b3), latex(a3), latex(u1), latex(u2), latex(u3),
                           latex(u1), latex(u2), latex(u3),
                           latex(a1), latex(u1), latex(a2), latex(u2), latex(a3), latex(u3),
                           latex(a3), latex(u3), latex(a3), latex(u3), latex(t_val),
                           latex(t_val),
                           latex(a1), latex(u1), latex(t_val), latex(a_val),
                           latex(a2), latex(u2), latex(t_val), latex(b_val),
                           latex(a_val), latex(b_val), latex(kq_exact),
                           kq
                         ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+').replace('+ -', '-')
            return content   

