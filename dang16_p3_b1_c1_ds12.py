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


def bt_dang16_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                while True:
                    # Chọn p sao cho diện tích S = p^2 / 4 không bằng 0
                    p = random.choice([-7, -5, -3, 3, 5, 7])
                    x0 = random.choice([-2, -1, 1, 2, 3])
                    q = randint(-10, 10)

                    # Kiểm tra điều kiện có cực trị: q + x0^2 + p*x0 phải cùng dấu với hệ số của phần phân thức
                    # Để hàm bậc hai trên bậc nhất có cực trị thì phần dư tử số phải khác 0
                    rem_val = q + x0**2 + p * x0
                    if rem_val != 0:
                        break

                # Phương trình đường thẳng cực trị là y = 2x + p
                # Giao điểm với Ox: A(-p/2; 0) -> OA = |p| / 2
                # Giao điểm với Oy: B(0; p) -> OB = |p|
                # Diện tích S = p^2 / 4
                S_val = (p**2) / 4.0

                # Làm tròn đến hàng phần mười
                kq_dec = Decimal(str(S_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec).replace('.', ',')

                # Tạo các phương án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Các đáp án nhiễu
                s_candidates = [
                    round(S_val + 1.25, 1),
                    round(S_val + 2.5, 1),
                    round(S_val - 1.25, 1) if S_val > 2.0 else round(S_val + 3.75, 1),
                    round(S_val - 0.5, 1) if S_val > 1.0 else round(S_val + 4.5, 1),
                    round((p**2) / 2.0, 1),
                    round(abs(p) / 2.0, 1)
                ]

                s = []
                for val in s_candidates:
                    val_str = str(val).replace('.', ',')
                    s.append('$%s$' % (val_str))

                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Định dạng các hệ số để hiển thị đề bài đẹp mắt
                sign_p = '+' if p > 0 else ''
                sign_q = '+' if q > 0 else ''

                term_p = '%s%s x' % (sign_p, p) if p != 0 else ''
                term_q = '%s%s' % (sign_q, q) if q != 0 else ''

                tu_so = 'x^2 %s %s' % (term_p, term_q)
                tu_so = ' '.join(tu_so.split())

                sign_x0 = '+' if -x0 > 0 else ''
                mau_so = 'x %s %s' % (sign_x0, -x0)
                mau_so = ' '.join(mau_so.split())

                # Câu hỏi
                noidungcauhoi = ('''Biết đồ thị $(C)$ của hàm số $y = \\frac{%s}{%s}$ có hai điểm cực trị. Đường thẳng đi qua hai điểm cực trị của đồ thị hàm số $(C)$ tạo với hai trục tọa độ một tam giác có diện tích $S$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % (tu_so, mau_so))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết từng bước
                p_abs = abs(p)
                p_abs_half = abs(p) / 2.0
                p_abs_half_str = str(p_abs_half).replace('.', ',')
                p_str = str(p_abs).replace('.', ',')

                loigiai = ('''Tập xác định của hàm số là $D = \\mathbb{R} \\setminus \\{%s\\}$.\\\\
                           Đối với hàm số dạng phân thức $y = \\frac{u(x)}{v(x)}$, đường thẳng đi qua hai điểm cực trị của đồ thị hàm số có phương trình là:\\\\
                           $$y = \\frac{u\'(x)}{v\'(x)} = \\frac{2x %s}{1} \\Rightarrow y = 2x %s \\quad (d).$$ \\\\
                           Gọi $A, B$ lần lượt là giao điểm của đường thẳng $(d)$ với các trục tọa độ $Ox, Oy$.\\\\
                           Với $y = 0 \\Rightarrow 2x %s = 0 \\Leftrightarrow x = %s \\Rightarrow A\\left(%s; 0\\right) \\Rightarrow OA = %s$.\\\\
                           Với $x = 0 \\Rightarrow y = %s \\Rightarrow B(0; %s) \\Rightarrow OB = %s$.\\\\
                           Diện tích tam giác vuông $OAB$ là:\\\\
                           $$S = \\frac{1}{2} \\cdot OA \\cdot OB = \\frac{1}{2} \\cdot %s \\cdot %s = %s.$$ \\\\
                           Vậy diện tích tam giác $S$ bằng $%s$.'''
                           % (latex(x0),
                              '+' + str(p) if p >= 0 else str(p),
                              '+' + str(p) if p >= 0 else str(p),
                              '+' + str(p) if p >= 0 else str(p),
                              str(-p/2.0).replace('.', ','),
                              str(-p/2.0).replace('.', ','),
                              p_abs_half_str,
                              latex(p), latex(p), p_str,
                              p_abs_half_str, p_str, kq, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

