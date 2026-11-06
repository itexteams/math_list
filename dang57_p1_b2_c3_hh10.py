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


def bt_dang57_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # B1 & B3: Phân tích và Thiết lập Random
            # ==========================================
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Để đảm bảo tọa độ nguyên đẹp, ta chọn đường thẳng d: x - y + c = 0 (vectơ pháp tuyến (1; -1))
                # Hoặc d: x + y + c = 0 (vectơ pháp tuyến (1; 1))
                # Điều này giúp phép đối xứng qua d luôn ra số nguyên.

                loai_duong = random.choice(['hieu', 'tong'])
                xM = randint(-3, 3)
                yM = randint(-3, 3)

                if loai_duong == 'hieu':
                    a, b = 1, -1
                    c = -(a*xM + b*yM) # Đảm bảo M thuộc d
                else:
                    a, b = 1, 1
                    c = -(a*xM + b*yM)

                # Chọn điểm A không nằm trên d
                xA = xM + randint(1, 3)
                yA = yM + randint(2, 4)
                if a*xA + b*yA + c == 0: xA += 1 # Tránh A thuộc d

                # Tính tọa độ A' đối xứng với A qua d
                # Với d: ax + by + c = 0, A' = (xA - 2aH, yA - 2bH) với H = (axA + byA + c)/(a^2 + b^2)
                fA = a*xA + b*yA + c
                mau = a**2 + b**2
                xA_p = int(xA - 2*a*fA/mau)
                yA_p = int(yA - 2*b*fA/mau)

                # Chọn điểm B sao cho M nằm giữa A' và B (để MA+MB nhỏ nhất)
                # Vectơ A'M = (xM - xA_p, yM - yA_p). Chọn B sao cho vectơ A'B = k * vectơ A'M (k > 1)
                k = randint(2, 3)
                xB = xA_p + k*(xM - xA_p)
                yB = yA_p + k*(yM - yA_p)
                fB = a*xB + b*yB + c

                # Phương trình đường thẳng A'B (đi qua A' và M)
                # (yM - yA_p)x - (xM - xA_p)y + xM*yA_p - yM*xA_p = 0
                m_ab = yM - yA_p
                n_ab = -(xM - xA_p)
                p_ab = xM*yA_p - yM*xA_p

                # Rút gọn phương trình A'B
                u_gcd = math.gcd(math.gcd(m_ab, n_ab), p_ab)
                m_ab //= u_gcd
                n_ab //= u_gcd
                p_ab //= u_gcd
                if m_ab < 0: 
                    m_ab, n_ab, p_ab = -m_ab, -n_ab, -p_ab

                # ==========================================
                # B4: Tạo các phương án sai (không trùng đáp án đúng)
                # ==========================================
                da = 'M(%s;%s)' % (xM, yM)

                s = [
                    'M(%s;%s)' % (xM + 1, yM),
                    'M(%s;%s)' % (xM, yM - 1),
                    'M(%s;%s)' % (xM - 2, yM + 1),
                    'M(%s;%s)' % (yM, xM),
                    'M(%s;%s)' % (xM + 2, yM + 2),
                    'M(%s;%s)' % (xA_p, yA_p)
                ]

                random.shuffle(s)
                list_wrong = []
                for item in s:
                    if item != da and len(list_wrong) < 3:
                        list_wrong.append(item)

                da_d = '\\True $' + da + '$'
                da_s1 = '$' + list_wrong[0] + '$'
                da_s2 = '$' + list_wrong[1] + '$'
                da_s3 = '$' + list_wrong[2] + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # ==========================================
                # B2: Viết lại đề bài và lời giải (theo mẫu)
                # ==========================================
                # Biểu thức đường thẳng d để in
                pt_d = latex(a*symbols('x') + b*symbols('y') + c) + " = 0"
                pt_ab = latex(m_ab*symbols('x') + n_ab*symbols('y') + p_ab) + " = 0"

                noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho đường thẳng $d: %s$ và hai điểm $A(%s;%s)$, $B(%s;%s)$. Tọa độ điểm $M$ thuộc đường thẳng $d$ sao cho $MA + MB$ nhỏ nhất là'''
                                 %(pt_d, latex(xA), latex(yA), latex(xB), latex(yB)))

                loigiai = ('''Xét vị trí tương đối của $A, B$ so với $d$: \\\\
                             $(%s \\cdot (%s) %+d \\cdot %s (%s)+d)(%s \\cdot (%s) %+d \\cdot (%s) %+d) = %s \\cdot (%s) = %s > 0$. \\\\
                             Suy ra $A, B$ nằm cùng phía so với $d$. \\\\
                             Gọi $A'(%s; %s)$ là điểm đối xứng của $A$ qua $d$. \\\\
                             Khi đó với mọi $M \\in d$, ta có $MA + MB = MA' + MB \\ge A'B$. \\\\
                             Dấu "$=$" xảy ra khi $M = A'B \\cap d$. \\\\
                             Đường thẳng $A'B$ có phương trình: $%s$. \\\\
                             Tọa độ $M$ là nghiệm của hệ: $\\begin{cases} %s \\\\ %s \\end{cases} \\Rightarrow M(%s; %s)$.'''
                           %(latex(a), latex(xA), b, latex(yA), c, 
                             latex(a), latex(xB), b, latex(yB), c,
                             latex(fA), latex(fB), latex(fA*fB),
                             latex(xA_p), latex(yA_p),
                             pt_ab, pt_d, pt_ab, latex(xM), latex(yM)))

            # ==========================================
            # Xuất nội dung theo định dạng mẫu
            # ==========================================
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

