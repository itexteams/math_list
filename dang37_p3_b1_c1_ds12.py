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


def bt_dang37_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Hàm số dạng v(x) = k*(x0 - x)*x^n
                # Ta random bậc n của x để tạo ra phân số a/b khác nhau
                n = random.choice([2, 3, 4, 5])

                # Giải bài toán tổng quát v(x) = k*x0*x^n - k*x^(n+1)
                # Đạo hàm: v'(x) = k*n*x0*x^(n-1) - k*(n+1)*x^n = k*x^(n-1) * (n*x0 - (n+1)*x)
                # v'(x) = 0 <=> x = n/(n+1) * x0

                a = n
                b = n + 1

                # Yêu cầu tính giá trị biểu thức M = p*a + q*b
                p = random.choice([1, 2, 3])
                q = random.choice([1, 2, 3])

                # Đáp án đúng
                kq = p * a + q * b

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)

                # Các phương án nhiễu
                s = ['$%s$'%(kq + 1),
                     '$%s$'%(kq + 2),
                     '$%s$'%(kq + 3),
                     '$%s$'%(kq - 1),
                     '$%s$'%(kq - 2),
                     '$%s$'%(kq - 3),
                     '$%s$'%(kq + 4),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                if n == 2:
                    fx = 'x^2'
                    dfx1 = '2x'
                    dfx2 = '3x^2'
                else:
                    fx = f'x^{n}'
                    dfx1 = f'{n}x^{n-1}'
                    dfx2 = f'{n+1}x^{n}'

                bieuthuc_x = ''
                if p == 1 and q == 1:
                    bieuthuc = 'a+b'
                elif p == 1:
                    bieuthuc = f'a+{q}b'
                elif q == 1:
                    bieuthuc = f'{p}a+b'
                else:
                    bieuthuc = f'{p}a+{q}b'

                noidungcauhoi = ('''Khi một vật lạ mắc kẹt trong khí quản khiến ta phải ho, cơ hoành đẩy lên trên gây ra tăng áp lực trong phổi, theo đó cuống họng co thắt làm hẹp khí quản khiến không khí đi qua mạnh hơn. Đối với một lượng không khí bị đẩy ra trong một khoảng thời gian cố định, khí quản càng nhỏ thì luồng không khí càng đẩy ra nhanh hơn. Vận tốc luồng khí thoát ra càng cao, lực tác động lên vật lạ càng lớn. Qua nghiên cứu một số trường hợp, người ta nhận thấy vận tốc $v$ của luồng khí liên hệ với bán kính $x$ của khí quản theo công thức: $v(x) = k(x_0 - x) \\cdot %s$ với $\\frac{1}{2}x_0 \\le x \\le x_0$, trong đó $k$ là hằng số $(k > 0)$ và $x_0$ là bán kính khí quản ở trạng thái bình thường. Khi đó $x = \\frac{a}{b}x_0$ (với $\\frac{a}{b}$ là phân số tối giản, $a, b \\in \\mathbb{Z}$) thì vận tốc luồng khí của một cơn ho trong trường hợp này là lớn nhất. Giá trị $%s$ bằng bao nhiêu?'''
                                 %(fx, bieuthuc
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
                loigiai=('''Ta có $v(x) = k(x_0 - x) \\cdot %s = k \\cdot x_0 \\cdot %s - k \\cdot x^{%s}$, với $x \\in \\left[ \\frac{1}{2}x_0; x_0 \\right]$. \\\\
                         Đạo hàm $v'(x) = k \\cdot x_0 \\cdot %s - k \\cdot %s = k \\cdot x^{%s} \\left( %sx_0 - %sx \\right)$. \\\\
                         Cho $v'(x) = 0 \\Leftrightarrow x = \\frac{%s}{%s}x_0$ (do $x \\ge \\frac{1}{2}x_0 > 0$). \\\\
                         Ta thấy $v'(x)$ đổi dấu từ dương sang âm khi qua điểm $x = \\frac{%s}{%s}x_0$ nên hàm số đạt giá trị lớn nhất tại $x = \\frac{%s}{%s}x_0$. \\\\
                         Vậy để vận tốc luồng khí là lớn nhất thì $x = \\frac{%s}{%s}x_0$. \\\\
                         Đồng nhất với giả thiết ta có $a = %s$, $b = %s$ (do $\\frac{%s}{%s}$ là phân số tối giản). \\\\
                         Vậy $%s = %s \\cdot %s + %s \\cdot %s = %s$.'''
                         %(fx, fx, latex(n+1),
                           dfx1, dfx2, latex(n-1), latex(n), latex(n+1),
                           latex(n), latex(n+1),
                           latex(n), latex(n+1), latex(n), latex(n+1),
                           latex(n), latex(n+1),
                           latex(a), latex(b), latex(a), latex(b),
                           bieuthuc, latex(p), latex(a), latex(q), latex(b), latex(kq)
                         ))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content  

