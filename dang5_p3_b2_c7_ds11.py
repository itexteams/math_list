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


def bt_dang5_p3_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang=='1':
                # Random các thông số: T(t) = -at^2 + bt + c
                # a thường nhỏ (0.1 đến 0.3), b (1.0 đến 2.0), c (98.0 đến 100.0)
                a_val = Rational(randint(1, 3), 10)
                b_val = Rational(randint(10, 20), 10)
                c_val = Rational(randint(980, 1000), 10)
                t0 = randint(1, 4)

                # Biểu thức hàm số và đạo hàm
                f = -a_val*t**2 + b_val*t + c_val
                f_prime = diff(f, t)

                # Tính toán giá trị tại t0
                kq_val = f_prime.subs(t, t0)

                # Làm tròn và định dạng số thập phân dùng dấu phẩy
                kq_float = float(kq_val)
                kq_rounded = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                da_str = str(kq_rounded).replace('.', ',')

                # Đáp án đúng
                da = '$%s$' % (da_str)

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                while len(s) < 6:
                    sai_val = kq_rounded + Decimal(str(random.choice([-1.5, -1.2, -0.5, 0.5, 1.2, 1.5, 2.1, -2.1])))
                    sai_str = '$%s$' % (str(sai_val).replace('.', ','))
                    if sai_str != da and sai_str not in s:
                        s.append(sai_str)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung câu hỏi
                # Lưu ý: Giữ nguyên lỗi diễn đạt "t là nhiệt độ" từ ảnh nếu muốn y hệt, 
                # nhưng ở đây tôi dùng t là thời gian để bài toán logic hơn, hoặc bám sát mặt chữ.
                noidungcauhoi = ('''Nhiệt độ cơ thể của một người trong thời gian bị bệnh được cho bởi công thức $T \\left( t \\right) = -%s t^2 + %s t + %s$ trong đó $t$ là nhiệt độ (tính theo đơn vị đo nhiệt độ Fahrenheit) tại thời điểm $t$ (tính theo ngày). Tốc độ thay đổi của nhiệt độ (đơn vị: $^\\circ F$/ngày) ở thời điểm $t = %s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 %(latex(a_val).replace('.', ','), 
                                   latex(b_val).replace('.', ','), 
                                   latex(c_val).replace('.', ','), 
                                   latex(t0)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # f_prime_val là biểu thức đạo hàm để thay vào %s
                f_p_tex = latex(f_prime).replace('.', ',')
                # Tính toán chi tiết cho bước thế số
                buoc_the_so = latex(f_prime.subs(t, t0)).replace('.', ',')

                loigiai = ('''Ta có: $T \\left( t \\right) = -%s t^2 + %s t + %s$ nên $T' \\left( t \\right) = %s$. \\\\
                             Ở thời điểm $t = %s$ thì $T' \\left( %s \\right) = %s \\left( ^\\circ F/\\text{ngày} \\right)$'''
                           %(latex(a_val).replace('.', ','), 
                             latex(b_val).replace('.', ','), 
                             latex(c_val).replace('.', ','), 
                             f_p_tex, 
                             latex(t0), 
                             latex(t0), 
                             da_str))
                dapan='\\shortans[0]{$%s$}\n'%(da_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

