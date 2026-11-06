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


def bt_dang61_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo bài toán dựa trên bộ ba số Pythagore để M, m luôn nguyên
                # b^2 + (c-1)^2 = k^2
                u = randint(2, 4)
                v = randint(1, u - 1)

                b_val = 2 * u * v
                c_minus_1 = u**2 - v**2
                c_val = c_minus_1 + 1
                k = u**2 + v**2

                # Tính M và m dựa trên công thức nghiệm của Delta_y >= 0
                # Nghiệm là y = ((c+1) +/- k) / 2
                M_val = (c_val + 1 + k) // 2
                m_val = (c_val + 1 - k) // 2
                ans_val = M_val - m_val

                # Tính x tại các điểm cực trị để đưa vào lời giải
                # Phương trình: (y-1)x^2 - bx + y - c = 0
                x_m = Rational(b_val, 2 * (m_val - 1))
                x_M = Rational(b_val, 2 * (M_val - 1))
                x_1 = Rational(c_val - 1, -b_val)

                # Các đáp án trắc nghiệm
                kq = str(ans_val)
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo danh sách đáp án nhiễu
                s = [
                    '$%s$' % (ans_val + 1),
                    '$%s$' % (ans_val + 2),
                    '$%s$' % (ans_val + 5),
                    '$%s$' % (ans_val - 1),
                    '$%s$' % (ans_val - 2),
                    '$%s$' % (ans_val + 10),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                # Hiển thị dấu cho b và c
                b_str = "- %sx" % (b_val) # Để giống mẫu ảnh (x^2 - 8x + 7)
                c_str = "+ %s" % (c_val)

                noidungcauhoi = ('''Gọi $M, m$ lần lượt là giá trị lớn nhất, giá trị nhỏ nhất của hàm số $y = \\frac{x^2 %s %s}{x^2 + 1}$. Tính tổng $M - m$.'''
                                 % (b_str, c_str))

                # Nội dung lời giải (Sử dụng cấu trúc y hệt ảnh mẫu)
                loigiai = ('''Gọi $y_0$ là một giá trị bất kì thuộc tập giá trị của hàm số đã cho. \\\\
            Khi đó phải tồn tại một giá trị $x$ sao cho \\\\
            $y_0 = \\frac{x^2 %s %s}{x^2 + 1}$ \\\\
            $\\Leftrightarrow (y_0 - 1)x^2 + %sx + y_0 - %s = 0 \\quad (*)$. \\\\
            + Nếu $y_0 = 1$ thì $x_0 = %s$. \\\\
            + Nếu $y_0 \\neq 1$ thì $(*)$ có nghiệm khi và chỉ khi: \\\\
            $\\Delta' = -y_0^2 + %sy_0 - %s \\geq 0 \\Leftrightarrow %s \\leq y_0 \\leq %s$. \\\\
            Kết hợp hai trường hợp ta có: $%s \\leq y_0 \\leq %s$. \\\\
            Ta thấy $y_0 = %s \\Rightarrow x = %s$; \\\\
            $y_0 = %s \\Rightarrow x = %s$. \\\\
            Vậy $m = \\min_{\\mathbb{R}} y = %s; M = \\max_{\\mathbb{R}} y = %s$ \\\\
            $\\Rightarrow M - m = %s$.'''
                           % (b_str, c_str, 
                              b_val, c_val, 
                              latex(x_1), 
                              (M_val + m_val), (M_val * m_val), m_val, M_val,
                              m_val, M_val,
                              m_val, latex(x_m),
                              M_val, latex(x_M),
                              m_val, M_val,
                              ans_val))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

