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


def bt_dang37_p3_b1_c3_ds12(self):
            # Khai báo biến
            # --- KHỞI TẠO BIẾN NGẪU NHIÊN ---

            k = random.randint(1, 3)
            a = 6 * k
            b = random.randint(2, 6)
            c = random.randint(2, 6)

            # Giá trị f(0) và F(0)
            val_f0 = random.randint(1, 5)
            val_F0 = random.randint(1, 5)

            # --- GIẢI BÀI TOÁN BẰNG SYMPY ---
            # 1. Tìm f(x)
            f_prime = a*x + b*sin(x) - c*cos(x)
            f_int = integrate(f_prime, x) 
            # f_int sẽ là (a/2)x^2 - b*cos(x) - c*sin(x)
            C1 = val_f0 - f_int.subs(x, 0)
            f_x = f_int + C1

            # 2. Tìm F(x)
            F_int = integrate(f_x, x)
            # F_int sẽ là (a/6)x^3 - b*sin(x) + c*cos(x) + C1*x
            C2 = val_F0 - F_int.subs(x, 0)
            F_x = F_int + C2

            # 3. Tính F(pi/2) và làm tròn đến hàng đơn vị
            res_val = F_x.subs(x, pi/2).evalf()
            kq_final = int(Decimal(float(res_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

            # --- TẠO CÁC PHƯƠNG ÁN SAI ---
            da = str(kq_final)
            s = set()
            while len(s) < 3:
                sai = kq_final + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                if sai != kq_final and sai > 0:
                    s.add(str(sai))
            list_sai = list(s)

            # --- NỘI DUNG CÂU HỎI (LATEX) ---
            noidungcauhoi = (r'''Cho hàm số $F(x)$ là một nguyên hàm của hàm số $f(x)$ trên $\mathbb{R}$. Biết rằng $f'(x) = %s$, $f(0) = %s, F(0) = %s$. Giá trị $F\left(\frac{\pi}{2}\right)$ bằng bao nhiêu? Viết kết quả làm tròn đến hàng đơn vị.'''
                            %(latex(f_prime), latex(val_f0), latex(val_F0)))

            # --- NỘI DUNG LỜI GIẢI (LATEX) ---
            # Bước 1: Tính f(x)
            f_x_step = latex(f_int).replace('cos(x)', r'\cos x').replace('sin(x)', r'\sin x')
            # Bước 2: Tính F(x)
            F_x_step = latex(F_int).replace('cos(x)', r'\cos x').replace('sin(x)', r'\sin x')

            loigiai = (r'''$f(x) = \int f'(x) \text{d} x = \int (%s) \text{d}x = %s + C$. \\
                          Có $f(0) = %s \Rightarrow %s + C = %s \Rightarrow C = %s$. \\
                          $\Rightarrow f(x) = %s$. \\
                          Ta có $F(x) = \int f(x) \text{d}x = \int (%s) \text{d}x$ \\
                          $= %s + C$. \\
                          Mà $F(0) = %s \Rightarrow %s + C = %s \Rightarrow C = %s$. \\
                          $\Rightarrow F(x) = %s$. \\
                          Suy ra $F\left(\frac{\pi}{2}\right) \approx %s$.'''
                       %(latex(f_prime), f_x_step, 
                         val_f0, latex(f_int.subs(x,0)), val_f0, latex(C1),
                         latex(f_x), 
                         latex(f_x), F_x_step,
                         val_F0, latex(F_int.subs(x,0)), val_F0, latex(C2),
                         latex(F_x),
                         str(kq_final)))
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(str(kq_final))

            # --- XUẤT KẾT QUẢ THEO MẪU ---
            da_d = r'\True ' + da
            list_ans = [da_d, list_sai[0], list_sai[1], list_sai[2]]
            random.shuffle(list_ans)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')

            return content  

