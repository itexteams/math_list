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


def bt_dang12_p3_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Để bài toán có nghiệm đẹp và giống cấu trúc đề bài:
                # t^2 - 2t - 3 = 0 có nghiệm t = 3.
                # Ta cần (a+b) = t^2 = 9 và c = 3.
                # Chọn ngẫu nhiên cặp (a, b) sao cho a + b = 9
                pairs = [(1, 8), (2, 7), (3, 6), (4, 5)]
                a, b = random.choice(pairs)
                c = 3

                # Tính toán nghiệm
                # Với t = 3, ta có sqrt((a+x)(b-x)) = (3^2 - 9)/2 = 0
                # => x = -a hoặc x = b
                x1 = -a
                x2 = b

                # Tổng bình phương các nghiệm
                kq_val = x1**2 + x2**2
                kq = str(kq_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai
                s = [
                    '$%s$' % (kq_val + 5),
                    '$%s$' % (kq_val - 5),
                    '$%s$' % (kq_val + 10),
                    '$%s$' % (kq_val + 13),
                    '$%s$' % (kq_val - 7),
                    '$%s$' % (kq_val + 2)
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Phương trình: sqrt(a+x) + sqrt(b-x) = sqrt((a+x)(b-x)) + c
                noidungcauhoi = ('''Cho phương trình sau: $\\sqrt{%s+x} + \\sqrt{%s-x} = \\sqrt{(%s+x)(%s-x)} + %s$. Tổng bình phương các nghiệm của phương trình bằng bao nhiêu?'''
                                 % (latex(a), latex(b), latex(a), latex(b), latex(c)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                sum_ab = a + b
                loigiai = ('''Đặt $t = \\sqrt{%s+x} + \\sqrt{%s-x}$ ($t \\ge 0$). \\\\
                             $\\Rightarrow t^2 = (%s+x) + (%s-x) + 2\\sqrt{(%s+x)(%s-x)} \\Rightarrow \\frac{t^2 - %s}{2} = \\sqrt{(%s+x)(%s-x)}$. \\\\
                             Phương trình đã cho trở thành: $t = \\frac{t^2 - %s}{2} + %s \\Leftrightarrow t^2 - 2t - 3 = 0 \\Leftrightarrow \\left[\\begin{aligned} & t = -1 \\text{ (loại)} \\\\ & t = 3 \\text{ (nhận)} \\end{aligned}\\right.$. \\\\
                             Với $t = 3$ thì $\\frac{3^2 - %s}{2} = \\sqrt{(%s+x)(%s-x)} \\Leftrightarrow (%s+x)(%s-x) = 0 \\Leftrightarrow \\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right.$. \\\\
                             Tập nghiệm của phương trình là: $S = \\{%s; %s\\}$. \\\\
                             Vậy tổng bình phương các nghiệm của phương trình bằng: $(%s)^2 + %s^2 = %s$.'''
                           % (latex(a), latex(b), 
                              latex(a), latex(b), latex(a), latex(b), latex(sum_ab), latex(a), latex(b),
                              latex(sum_ab), latex(c),
                              latex(sum_ab), latex(a), latex(b), latex(a), latex(b), latex(x1), latex(x2),
                              latex(x1), latex(x2),
                              latex(x1), latex(x2), latex(kq)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))              

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

