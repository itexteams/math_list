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


def bt_dang9_p3_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp để đảm bảo vectơ chỉ phương và góc đẹp
                while True:
                    # 1. Ngẫu nhiên hóa vectơ Chỉ phương u1 (AB) và u2 (CD)
                    # Chọn vectơ u1, u2 với tọa độ nhỏ
                    u1_x, u1_y, u1_z = choice([-2, -1, 1, 2]), choice([-2, -1, 1, 2]), choice([-2, -1, 1, 2])
                    u2_x, u2_y, u2_z = choice([-2, -1, 1, 2]), choice([-2, -1, 1, 2]), choice([-2, -1, 1, 2])

                    # Đảm bảo u1 và u2 không phải vectơ 0
                    if u1_x == 0 and u1_y == 0 and u1_z == 0: continue
                    if u2_x == 0 and u2_y == 0 and u2_z == 0: continue

                    # 2. Tính cos(alpha)
                    # Tử số: |u1 . u2|
                    tu_so_val = abs(u1_x * u2_x + u1_y * u2_y + u1_z * u2_z)
                    # Mẫu số: |u1| * |u2|
                    u1_mag_sq = u1_x**2 + u1_y**2 + u1_z**2
                    u2_mag_sq = u2_x**2 + u2_y**2 + u2_z**2
                    mau_so_val = sqrt(u1_mag_sq * u2_mag_sq)

                    # 3. Kiểm tra góc alpha là góc đẹp (90, 60, 45, 30)
                    if mau_so_val != 0:
                        cos_alpha = tu_so_val / mau_so_val

                        # Kiểm tra xem cos(alpha) có gần 0, 1/2, sqrt(2)/2, sqrt(3)/2 hay không
                        if abs(cos_alpha - 0) < 1e-6: # cos(alpha) = 0 => alpha = 90
                            kq = 90
                            break
                        elif abs(cos_alpha**2 - 0.25) < 1e-6: # cos^2(alpha) = 1/4 => cos(alpha) = 1/2 => alpha = 60
                            kq = 60
                            break
                        elif abs(cos_alpha**2 - 0.5) < 1e-6: # cos^2(alpha) = 1/2 => cos(alpha) = sqrt(2)/2 => alpha = 45
                            kq = 45
                            break
                        elif abs(cos_alpha**2 - 0.75) < 1e-6: # cos^2(alpha) = 3/4 => cos(alpha) = sqrt(3)/2 => alpha = 30
                            kq = 30
                            break

                # 4. Ngẫu nhiên hóa Tọa độ A, B, C, D
                # Để đảm bảo AB = u1 và CD = u2, ta chọn A, C ngẫu nhiên và tính B, D

                xA, yA, zA = randint(-2, 2), randint(-2, 2), randint(-2, 2)
                xC, yC, zC = randint(-2, 2), randint(-2, 2), randint(-2, 2)

                # B = A + u1
                xB, yB, zB = xA + u1_x, yA + u1_y, zA + u1_z
                # D = C + u2
                xD, yD, zD = xC + u2_x, yC + u2_y, zC + u2_z

                # 5. Tạo đáp án

                # Đáp án đúng
                du = ['$%s^\\circ$'%(latex(kq))]
                da= random.choice(du) 

                # Đáp án sai (chọn các góc đẹp khác)
                s = [f'${g}^\\circ$' for g in [30, 45, 60, 90] if g != kq]
                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # 6. Câu hỏi

                noidungcauhoi = ('''Trong không gian $Oxyz$, cho bốn điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$, $D(%s;%s;%s)$. Góc giữa hai đường thẳng $AB$ và $CD$ bằng bao nhiêu độ?'''
                                  %(latex(xA),latex(yA),latex(zA),
                                    latex(xB),latex(yB),latex(zB),
                                    latex(xC),latex(yC),latex(zC),
                                    latex(xD),latex(yD),latex(zD)
                                  ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # 7. Nội dung lời giải

                cos_alpha_sym = tu_so_val / mau_so_val

                loigiai=('''Đường thẳng $AB$ có vectơ chỉ phương là $\\vec{u}_1 = \\vec{AB} = (%s-%s; %s-%s; %s-%s) = (%s;%s;%s)$.\\\\
                            Đường thẳng $CD$ có vectơ chỉ phương là $\\vec{u}_2 = \\vec{CD} = (%s-%s; %s-%s; %s-%s) = (%s;%s;%s)$.\\\\
                            Gọi $\\alpha$ là góc giữa hai đường thẳng $AB$ và $CD$. Ta có công thức:
                            $$\\cos\\alpha = \\frac{|\\vec{u}_1 \\cdot \\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|}$$
                            Với $|\\vec{u}_1 \\cdot \\vec{u}_2| = |%s(%s) + %s(%s) + %s(%s)| = |%s| = %s.$ \\\\
                            $|\\vec{u}_1| = \\sqrt{%s^2 + %s^2 + %s^2} = \\sqrt{%s}$ \\\\
                            $|\\vec{u}_2| = \\sqrt{%s^2 + %s^2 + %s^2} = \\sqrt{%s}$\\\\
                            $|\\vec{u}_1| \\cdot |\\vec{u}_2| = \\sqrt{%s} \\cdot \\sqrt{%s} = \\sqrt{%s}.$\\\\
                            Suy ra \\\\
                            $$\\cos\\alpha = \\frac{%s}{\\sqrt{%s}} = %s.$$\\\\
                            Vậy góc $\\alpha = %s^\\circ$.'''
                        %(latex(xB),latex(xA),latex(yB),latex(yA),latex(zB),latex(zA), latex(u1_x),latex(u1_y),latex(u1_z),
                          latex(xD),latex(xC),latex(yD),latex(yC),latex(zD),latex(zC), latex(u2_x),latex(u2_y),latex(u2_z),
                          latex(u1_x),latex(u2_x),latex(u1_y),latex(u2_y),latex(u1_z),latex(u2_z), latex(u1_x*u2_x + u1_y*u2_y + u1_z*u2_z), latex(tu_so_val),
                          latex(u1_x),latex(u1_y),latex(u1_z),latex(u1_mag_sq),
                          latex(u2_x),latex(u2_y),latex(u2_z),latex(u2_mag_sq),
                          latex(u1_mag_sq),latex(u2_mag_sq),latex(u1_mag_sq * u2_mag_sq),
                          latex(tu_so_val),latex(u1_mag_sq * u2_mag_sq),latex(cos_alpha_sym),
                          latex(kq)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--', '+')
            return content   


