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


def bt_dang22_p3_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số cho bài toán thực tế và đa dạng
                C_setup = random.choice([20000, 25000, 30000, 35000, 40000, 45000, 50000, 60000, 80000, 100000]) # Chi phí thiết lập ban đầu (USD)
                c = random.choice([4, 5, 6, 7, 8, 9, 10, 12, 15, 20]) # Chi phí trên mỗi sản phẩm (USD)

                # Đáp án đúng là giới hạn của F(x) khi x tiến tới vô cùng (bằng chi phí biến đổi trên mỗi sản phẩm)
                kq = c

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                # Tạo danh sách các đáp án nhiễu logic
                s = [
                    '$%s$' % (latex(kq + 2)),
                    '$%s$' % (latex(kq + 4)),
                    '$%s$' % (latex(kq + 5)),
                    '$%s$' % (latex(kq * 2)),
                    '$%s$' % (latex(kq - 2 if kq > 2 else kq + 8)),
                    '$%s$' % (latex(kq + 10))
                ]

                # Xóa trùng và xóa đáp án đúng ra khỏi danh sách nhiễu
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Định dạng chuỗi hiển thị số tiền thiết lập ban đầu (có dấu cách hàng nghìn)
                C_setup_str = str(C_setup)[:-3] + ' 000'

                # Câu hỏi
                noidungcauhoi = ('''Tại một công ty sản xuất đồ chơi an toàn cho trẻ em, công ty phải chi $%s$ USD để thiết lập dây chuyền sản xuất ban đầu. Sau đó, cứ sản xuất được một sản phẩm đồ chơi $A$, công ty phải trả $%s$ USD cho nguyên liệu ban đầu và nhân công. Gọi $x$ ($x \\ge 1$) là số đồ chơi $A$ mà công ty đã sản xuất và $P(x)$ (đơn vị USD) là tổng số tiền bao gồm cả chi phí ban đầu mà công ty phải chi trả khi sản xuất $x$ đồ chơi $A$. Người ta xác định chi phí trung bình cho mỗi sản phẩm đồ chơi $A$ là $F(x) = \\frac{P(x)}{x}$. Xem $F(x)$ là hàm số theo $x$ xác định trên nửa khoảng $[1; +\\infty)$. Khi đó, chi phí trung bình của mỗi đồ chơi $A$ thấp nhất càng gần nhưng không thể nhỏ hơn bao nhiêu (USD)?'''
                                 % (C_setup_str, latex(c)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Tổng chi phí bao gồm chi phí ban đầu và chi phí sản xuất để làm ra $x$ đồ chơi $A$ là:\\\\
            $P(x) = %s + %sx$ (USD).\\\\
            Chi phí trung bình cho mỗi sản phẩm đồ chơi $A$ là:\\\\
            $F(x) = \\frac{P(x)}{x} = \\frac{%s + %sx}{x} = \\frac{%s}{x} + %s$ (USD).\\\\
            Với $x \\ge 1$, ta luôn có $\\frac{%s}{x} > 0$ nên $F(x) > %s$.\\\\
            Khi số lượng sản phẩm sản xuất ra ngày càng lớn (tức là khi thời gian và sản lượng tiến ra vô cùng, $x \\to +\\infty$), ta có:\\\\
            $$\\lim_{x \\to +\\infty} F(x) = \\lim_{x \\to +\\infty} \\left(\\frac{%s}{x} + %s\\right) = 0 + %s = %s.$$\\\\
            Do đó, chi phí trung bình của mỗi đồ chơi $A$ thấp nhất sẽ càng ngày càng gần nhưng không thể nhỏ hơn $%s$ USD.'''
                           % (C_setup_str, latex(c), C_setup_str, latex(c), C_setup_str, latex(c),
                              C_setup_str, latex(c), C_setup_str, latex(c), latex(c), latex(c), latex(c)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(c))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

