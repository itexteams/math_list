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


def bt_dang3_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tìm bộ số (m, n) sao cho n^2 - m^2 không phải số chính phương để giữ nguyên căn thức giống mẫu
                while True:
                    m = randint(1, 3)
                    n = randint(4, 7)
                    if math.gcd(m, n) == 1 and not math.isqrt(n**2 - m**2)**2 == (n**2 - m**2):
                        break

                # Tính các đại lượng toán học
                sin_x = Rational(m, n)
                cos2x = 1 - 2*sin_x**2

                # n^2 - m^2 = k_val -> rút gọn căn thức ra k_trong_can và hệ số ngoài
                k_val = n**2 - m**2
                cos_x_tuyetdoi = sqrt(k_val)/n

                sin2x = -2 * sin_x * cos_x_tuyetdoi
                cot2x = cos2x / sin2x

                # Biến đổi cot2x về dạng (a * sqrt(d)) / b
                # cot2x = (n^2 - 2m^2) / (-2m * sqrt(k_val)) = (2m^2 - n^2) * sqrt(k_val) / (2m * k_val)
                tu_so_so_hoc = 2*m**2 - n**2
                mau_so_so_hoc = 2*m*k_val

                # Rút gọn phân số tu_so_so_hoc / mau_so_so_hoc
                phan_so_rut_gon = Rational(tu_so_so_hoc, mau_so_so_hoc)
                a_heso = phan_so_rut_gon.p
                b = phan_so_rut_gon.q

                # Đưa phần thừa từ căn ra ngoài nếu có để đưa về dạng a * sqrt(k_trong_can) / b
                # Phân tích k_val thành nhân tử chính phương lớn nhất
                ngoai_can = 1
                k_trong_can = k_val
                for i in range(2, int(math.sqrt(k_val)) + 1):
                    while k_trong_can % (i**2) == 0:
                        ngoai_can *= i
                        k_trong_can //= i**2

                # Nhân hệ số ngoài căn vào tử số và rút gọn lại với mẫu số b
                tu_moi = a_heso * ngoai_can
                phan_so_cuoi = Rational(tu_moi, b)
                a = phan_so_cuoi.p
                b = phan_so_cuoi.q

                # Đáp án đúng
                kq_dung = a + b

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(latex(kq_dung))]
                da = random.choice(du)

                # Tạo các phương án nhiễu không trùng đáp án đúng
                s = []
                for sai in [a - b, b - a, a + b + 2, a + b - 2, a + b + 5, a + b - 5]:
                    val_sai = '$%s$'%(latex(sai))
                    if val_sai != da and val_sai not in s:
                        s.append(val_sai)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\sin x = \\frac{%s}{%s}, \\frac{\\pi}{2} < x < \\pi$. Biết $\\cot 2x = \\frac{a\\sqrt{%s}}{b}$ với $\\frac{a}{b}$ là phân số tối giản và $b>0$. Tổng $a+b$ bằng bao nhiêu?'''
                                 %(latex(m), latex(n), latex(k_trong_can)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Vì $\\frac{\\pi}{2} < x < \\pi$ nên $\\cos x < 0$. \\\\
                           Ta có $\\cos x = -\\sqrt{1 - \\sin^2 x} = -\\sqrt{1 - \\left(\\frac{%s}{%s}\\right)^2} = -\\frac{\\sqrt{%s}}{%s}$. \\\\
                           Khi đó: \\\\
                           $\\sin 2x = 2\\sin x \\cdot \\cos x = 2 \\cdot \\frac{%s}{%s} \\cdot \\left(-\\frac{\\sqrt{%s}}{%s}\\right) = -\\frac{%s\\sqrt{%s}}{%s}$. \\\\
                           $\\cos 2x = 1 - 2\\sin^2 x = 1 - 2 \\cdot \\left(\\frac{%s}{%s}\\right)^2 = \\frac{%s}{%s}$. \\\\
                           Suy ra: \\\\
                           $\\cot 2x = \\frac{\\cos 2x}{\\sin 2x} = \\frac{\\frac{%s}{%s}}{-\\frac{%s\\sqrt{%s}}{%s}} = \\frac{%s\\sqrt{%s}}{%s}$. \\\\
                           Do $\\frac{a}{b}$ là phân số tối giản và $b>0$ nên $a = %s$ và $b = %s$. \\\\
                           Vậy $a+b = %s + %s = %s$.'''
                           %(latex(m), latex(n), latex(k_val), latex(n),
                             latex(m), latex(n), latex(k_val), latex(n), latex(2*m), latex(k_val), latex(n**2),
                             latex(m), latex(n), latex(n**2 - 2*m**2), latex(n**2),
                             latex(n**2 - 2*m**2), latex(n**2), latex(2*m), latex(k_val), latex(n**2), latex(a), latex(k_trong_can), latex(b),
                             latex(a), latex(b), latex(a), latex(b), latex(kq_dung)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

