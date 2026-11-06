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


def bt_dang28_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1 & 3: Khởi tạo các giá trị ngẫu nhiên và tính toán
                # Giả sử đường thẳng Delta: ax + by + c = 0
                # Trong ảnh: x - 2y + 3 = 0 => a=1, b=-2, c=3
                a = randint(1, 4) * random.choice([-1, 1])
                b = randint(1, 4) * random.choice([-1, 1])
                if a == 1 and b == -2: # Tránh trùng khít hoàn toàn nếu muốn đa dạng, hoặc giữ nguyên
                    c = 3
                else:
                    c = randint(-10, 10)

                # Vectơ pháp tuyến n = (a, b)
                # Vectơ chỉ phương cơ sở u_base = (-b, a)
                u1_base, u2_base = -b, a

                # Tạo đáp án ĐÚNG (là vectơ KHÔNG phải vectơ chỉ phương)
                # Ta chọn một vectơ tỉ lệ với vectơ pháp tuyến (a, b) vì nó vuông góc với chỉ phương
                k_true = random.choice([1, 2, -1, -2])
                ans_x, ans_y = k_true * a, k_true * b

                # Bước 4: Tạo các phương án SAI (thực tế là các vectơ chỉ phương)
                # Đảm bảo không trùng với đáp án đúng
                k_vals = [1, 2, -1, -2, 3, -3]
                random.shuffle(k_vals)

                # Lấy 3 hệ số k cho 3 phương án sai
                s_factors = k_vals[:3]

                da = '$\\vec{u}=(%s; %s)$'%(latex(ans_x), latex(ans_y))

                das1 = '$\\vec{v}=(%s; %s)$'%(latex(s_factors[0] * u1_base), latex(s_factors[0] * u2_base))
                das2 = '$\\vec{m}=(%s; %s)$'%(latex(s_factors[1] * u1_base), latex(s_factors[1] * u2_base))
                das3 = '$\\vec{q}=(%s; %s)$'%(latex(s_factors[2] * u1_base), latex(s_factors[2] * u2_base))

                # Câu hỏi
                # Viết lại phương trình đường thẳng Delta
                sign_b = '+' if b > 0 else ''
                sign_c = '+' if c > 0 else ''
                # Format phương trình đơn giản (chưa tối ưu hóa triệt để 1x, -1x nhưng đủ dùng cho random)
                pt = '%sx %s %sy %s %s = 0'%(latex(a), sign_b, latex(b), sign_c, latex(c))
                pt = pt.replace(' 1x', ' x').replace('-1x', '-x').replace(' 1y', ' y').replace('-1y', '-y')

                noidungcauhoi = ('''Cho đường thẳng $\\Delta : %s$. Vectơ nào sau đây \\textbf{không là} vectơ chỉ phương của $\\Delta$?'''
                                 %(pt))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Nội dung lời giải chi tiết như trong ảnh
                loigiai=('''Nếu $\\vec{u}$ là một vectơ chỉ phương của đường thẳng $\\Delta$ thì $k\\vec{u}, \\forall k \\neq 0$ cũng là vectơ chỉ phương của đường thẳng $\\Delta$. \\\\
                          Từ phương trình đường thẳng $\\Delta$ ta thấy đường thẳng $\\Delta$ có một vectơ chỉ phương có tọa độ là $(%s; %s)$. \\\\
                          Do đó vectơ %s không phải là vectơ chỉ phương của $\\Delta$ (vì không cùng phương với $(%s; %s)$).'''
                         %(latex(u1_base), latex(u2_base), 
                           str(da),
                           latex(u1_base), latex(u2_base)
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

