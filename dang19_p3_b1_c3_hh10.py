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


def bt_dang19_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tạo các hệ số ngẫu nhiên để đảm bảo nghiệm t là số nguyên
                # Đường thẳng Delta: x = x0 + u1*t, y = y0 + u2*t
                # Điểm A(xA, yA)
                # Để AM ngắn nhất tại t_min nguyên, ta chọn M_min trước

                u1 = randint(1, 3) * random.choice([-1, 1])
                u2 = randint(1, 3) * random.choice([-1, 1])
                while u1 == 0 and u2 == 0:
                    u2 = randint(1, 3)

                t_min = randint(-3, 3)
                x0 = randint(-5, 5)
                y0 = randint(-5, 5)

                # Điểm M tại vị trí AM ngắn nhất
                a_val = x0 + u1 * t_min
                b_val = y0 + u2 * t_min

                # Vector pháp tuyến của Delta là (u1, u2). Vector AM phải cùng phương với vector pháp tuyến n(-u2, u1)
                # Chọn k để điểm A có tọa độ nguyên
                k = randint(1, 4) * random.choice([-1, 1])
                xa = a_val + k * u2
                ya = b_val - k * u1

                # Tính S = 2a + b
                S_val = 2 * a_val + b_val

                # Tính toán các hệ số cho lời giải
                c1 = x0 - xa
                c2 = y0 - ya

                # AM^2 = (u1*t + c1)^2 + (u2*t + c2)^2 = (u1^2+u2^2)t^2 + 2(u1*c1 + u2*c2)t + (c1^2+c2^2)
                A_quad = u1**2 + u2**2
                B_quad = 2 * (u1 * c1 + u2 * c2)
                C_quad = c1**2 + c2**2

                # Biến đổi hằng đẳng thức: A(t + B/2A)^2 + Remainder
                hdt_t = Rational(-B_quad, 2 * A_quad) # t_min = -B/2A
                remainder = C_quad - Rational(B_quad**2, 4 * A_quad)

                # Các đáp án trắc nghiệm
                da = '$%s$' % (latex(S_val))

                # Tạo danh sách đáp án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = S_val + randint(-5, 5)
                    if sai != S_val:
                        s.add('$%s$' % (latex(sai)))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                # Delta: x = x0 + u1*t, y = y0 + u2*t
                # Lưu ý cách viết hệ phương trình tham số
                noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho đường thẳng $\\Delta : \\begin{cases} x = %s %s %st \\\\ y = %s %s %st \\end{cases}$ và điểm $A(%s;%s)$. Điểm $M(a;b)$ thuộc đường thẳng $\\Delta$ sao cho đoạn thẳng $AM$ ngắn nhất. Giá trị $S = 2a + b$ bằng bao nhiêu?'''
                                 % (latex(x0), '+' if u1 >= 0 else '', latex(u1),
                                    latex(y0), '+' if u2 >= 0 else '', latex(u2),
                                    latex(xa), latex(ya)
                                    ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo mẫu ảnh
                # Vector AM = (xM - xA; yM - yA)
                vec_am_x = '%s %s %st' % (latex(c1), '+' if u1 >= 0 else '', latex(u1))
                vec_am_y = '%s %s %st' % (latex(c2), '+' if u2 >= 0 else '', latex(u2))

                loigiai = ('''$M \\in \\Delta \\Rightarrow M(%s %s %st; %s %s %st) \\Rightarrow \\overrightarrow{AM} = (%s; %s)$ \\\\
                             $\\Rightarrow AM = \\sqrt{(%s)^2 + (%s)^2} = \\sqrt{%st^2 %s %st + %s} = \\sqrt{%s(t %s %s)^2 + %s} \\ge \\sqrt{%s} = %s$. \\\\
                             $\\Rightarrow AM$ ngắn nhất là $%s$ khi $t = %s \\Rightarrow M(%s; %s) \\Rightarrow a = %s; b = %s$. \\\\
                             Vậy $S = 2a + b = 2 \\cdot (%s) + %s = %s$.'''
                           % (latex(x0), '+' if u1 >= 0 else '', latex(u1), latex(y0), '+' if u2 >= 0 else '', latex(u2), vec_am_x, vec_am_y,
                              vec_am_x, vec_am_y, latex(A_quad), '+' if B_quad >= 0 else '', latex(B_quad), latex(C_quad),
                              latex(A_quad), '+' if -hdt_t >= 0 else '', latex(-hdt_t), latex(remainder), latex(remainder), latex(sqrt(remainder)),
                              latex(sqrt(remainder)), latex(t_min), latex(a_val), latex(b_val), latex(a_val), latex(b_val),
                              latex(a_val), latex(b_val), latex(S_val)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content 

