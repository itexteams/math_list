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


def bt_dang18_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Biên độ dao động ngẫu nhiên (A1 = A2 = A)
                A = random.choice([2, 3, 4, 5])

                # Tần số góc omega ngẫu nhiên dưới dạng phân số nhân với pi
                tuso_w = random.choice([1, 2, 4])
                mauso_w = random.choice([3, 5])
                omega_latex = "\\frac{%s\\pi}{%s}" % (tuso_w if tuso_w != 1 else "", mauso_w)

                # Chọn cặp pha ban đầu phi1 và phi2 sao cho có thể tổng hợp đơn giản bằng công thức cộng cos
                # Mẫu số chung của pha ban đầu thường là 3, 4, 6
                # Chọn bộ pha ban đầu mẫu: phi1 = pi/6, phi2 = -pi/3 -> trung bình cộng là -pi/12, hiệu chia đôi là pi/4
                # Để đa dạng bài toán, ta có thể ngẫu nhiên hóa dựa trên bộ số có sẵn
                bo_pha = random.choice([
                    {"phi1_rad": pi/6, "phi1_str": "\\frac{\\pi}{6}", "phi2_rad": -pi/3, "phi2_str": "-\\frac{\\pi}{3}"},
                    {"phi1_rad": pi/4, "phi1_str": "\\frac{\\pi}{4}", "phi2_rad": -pi/12, "phi2_str": "-\\frac{\\pi}{12}"},
                    {"phi1_rad": pi/3, "phi1_str": "\\frac{\\pi}{3}", "phi2_rad": -pi/6, "phi2_str": "-\\frac{\\pi}{6}"}
                ])

                phi1_rad = bo_pha["phi1_rad"]
                phi1_str = bo_pha["phi1_str"]
                phi2_rad = bo_pha["phi2_rad"]
                phi2_str = bo_pha["phi2_str"]

                # Tính pha ban đầu tổng hợp: phi = (phi1 + phi2) / 2
                phi_tonghop = (phi1_rad + phi2_rad) / 2
                # Tính hiệu chia đôi: (phi1 - phi2) / 2
                phi_hieu = (phi1_rad - phi2_rad) / 2

                # Biên độ tổng hợp mới: 2 * A * cos(phi_hieu)
                A_tonghop = 2 * A * cos(phi_hieu)
                A_tonghop_latex = latex(A_tonghop)

                # Chuẩn hóa giá trị số thập phân của pha ban đầu tổng hợp
                val_phi = float(phi_tonghop)
                kq3 = Decimal(str(val_phi)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai
                s = []
                val_phi_4 = round(val_phi, 1)
                for sai_val in [val_phi_4 + 0.5, val_phi_4 + 0.8, val_phi_4 - 0.4, val_phi_4 - 0.7]:
                    sai_str = str(Decimal(str(sai_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    if ('$%s$' % sai_str) not in s and ('$%s$' % sai_str) != da:
                        s.append('$%s$' % sai_str)

                while len(s) < 3:
                    sai_val = round(random.uniform(-3.1, 3.1), 1)
                    sai_str = str(Decimal(str(sai_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    if ('$%s$' % sai_str) not in s and ('$%s$' % sai_str) != da:
                        s.append('$%s$' % sai_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong Vật lí, phương trình tổng quát của một vật dao động điều hòa cho bởi công thức $x(t) = A \\cos(\\omega t + \\varphi)$, trong đó $t$ là thời điểm (tính bằng giây), $x(t)$ là li độ của vật tại thời điểm $t$, $A$ là biên độ dao động ($A > 0$) và $\\varphi \\in [-\\pi;\\pi]$ là pha ban đầu của dao động. Xét hai dao động điều hòa có phương trình: \\\\
                                 $x_1(t) = %s \\cos\\left(%s t + %s\\right)$ (cm), $x_2(t) = %s \\cos\\left(%s t %s\\right)$ (cm). \\\\
                                 Pha ban đầu của dao động tổng hợp này bằng bao nhiêu? (Kết quả làm tròn đến chữ số thập phân thứ nhất).'''
                                 % (latex(A), omega_latex, phi1_str, latex(A), omega_latex, phi2_str if phi2_str.startswith('-') else ('+ ' + phi2_str)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $x(t) = x_1(t) + x_2(t) = %s \\cos\\left(%s t + %s\\right) + %s \\cos\\left(%s t %s\\right)$ \\\\
                             $= 2 \\cdot %s \\cos\\left(%s t %s\\right) \\cdot \\cos %s = %s \\cos\\left(%s t %s\\right)$. \\\\
                             Vậy pha ban đầu bằng $%s \\approx %s$.'''
                           % (latex(A), omega_latex, phi1_str, latex(A), omega_latex, phi2_str if phi2_str.startswith('-') else ('+ ' + phi2_str),
                              latex(A), omega_latex, latex(phi_tonghop) if float(phi_tonghop) < 0 else ('+ ' + latex(phi_tonghop)), latex(phi_hieu), A_tonghop_latex, omega_latex, latex(phi_tonghop) if float(phi_tonghop) < 0 else ('+ ' + latex(phi_tonghop)),
                              latex(phi_tonghop), kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

