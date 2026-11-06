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


def bt_dang31_p3_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random hệ số để hàm số lồi (f'' > 0)
                # f(x) = ax^4 + bx^2 + cx + d
                a = random.randint(2, 5)
                b = random.randint(1, 4)
                c = random.randint(-3, 3)
                # d quyết định số nghiệm (nếu d âm và a,b dương thì thường có 2 nghiệm)
                d = random.randint(-6, 2)

                f = a*x**4 + b*x**2 + c*x + d
                f_prime = diff(f, x)
                f_double_prime = diff(f_prime, x)

                # Bước 2: Tính toán các giá trị tại điểm mút
                f_m1 = f.subs(x, -1)
                f_0 = f.subs(x, 0)
                f_1 = f.subs(x, 1)

                fp_m1 = f_prime.subs(x, -1)
                fp_1 = f_prime.subs(x, 1)

                # Bước 3: Đếm số nghiệm thực trong khoảng (-1, 1)
                roots = real_roots(f)
                m_count = 0
                for r in roots:
                    if -1 < r < 1:
                        m_count += 1

                # Gán kết quả m theo biến kq như mẫu
                kq = m_count

                # Các đáp án trắc nghiệm
                du = ['$m = %s$' % (kq)]
                da = random.choice(du)

                # Tạo danh sách các đáp án sai (loại trừ đáp án đúng)
                s_pool = ['$m = 0$', '$m = 1$', '$m = 2$', '$m = 3$', '$m = 4$']
                if da in s_pool:
                    s_pool.remove(da)
                random.shuffle(s_pool)

                das1 = s_pool[0]
                das2 = s_pool[1]
                das3 = s_pool[2]

                # Câu hỏi
                noidungcauhoi = (r'''Cho phương trình $%s = 0$. Phương trình có đúng $m$ nghiệm trên khoảng $(-1;1)$. giá trị $m$ bằng bao nhiêu?'''
                                %(latex(f)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết y hệt logic trong ảnh mẫu)
                # Sử dụng dấu chứng minh f'' > 0 để khẳng định tính đơn điệu của đạo hàm
                loigiai=(r'''Xét $f(x) = %s$ trên khoảng $[-1;1]$. \\
                          Ta có $f(x)$ liên tục trên đoạn $[-1;1]$. \\
                          $f(-1)=%s, f(0)=%s, f(1)=%s$. \\'''
                          %(latex(f), latex(f_m1), latex(f_0), latex(f_1)))

                if f_m1 * f_0 < 0 and f_1 * f_0 < 0:
                    loigiai += r'''Vì $f(-1).f(0)<0$ và $f(1).f(0)<0$ nên phương trình có ít nhất hai nghiệm trong $(-1;1)$. \\'''

                loigiai += (r'''Mặt khác $f'(x)=%s$. Ta có $f''(x)=%s$. \\
                              Vì $f''(x) > 0$ với mọi $x \in (-1;1)$ nên $f'(x)$ là hàm số đồng biến. \\
                              Do đó phương trình $f'(x)=0$ có tối đa một nghiệm, dẫn tới $f(x)=0$ có tối đa hai nghiệm. \\
                              Kết hợp các điều kiện trên, phương trình có đúng $%s$ nghiệm trên khoảng $(-1;1)$."'''
                              %(latex(f_prime), latex(f_double_prime), kq))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm đúng mẫu content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

