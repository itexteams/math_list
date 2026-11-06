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


def bt_dang61_p3_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Chọn ngẫu nhiên 3 chữ số khác nhau từ 1 đến 9
                digits = sample(range(1, 10), 3)
                d1, d2, d3 = digits[0], digits[1], digits[2]

                # Chọn số lần xuất hiện cho mỗi chữ số
                a = randint(2, 3)
                b = randint(2, 3)
                c = randint(3, 4)
                n = a + b + c # Tổng số chữ số

                # Tính toán kết quả theo công thức hoán vị lặp
                # kq = n! / (a! * b! * c!)
                tu = math.factorial(n)
                mau = math.factorial(a) * math.factorial(b) * math.factorial(c)
                kq_val = tu // mau

                # Các bước trung gian cho lời giải (Tổ hợp)
                c1 = n
                c2 = n - a
                c3 = n - a - b

                val_c1 = math.comb(c1, a)
                val_c2 = math.comb(c2, b)
                val_c3 = math.comb(c3, c)

                # Các đáp án trắc nghiệm
                kq = str(kq_val)

                # Tạo các phương án sai
                s = set()
                while len(s) < 3:
                    # Một số lỗi sai thường gặp: n!, hoặc tích các số, hoặc sai số ngẫu nhiên
                    wrong1 = math.factorial(n) // (a * b * c)
                    wrong2 = a * b * c * n * 10
                    wrong3 = kq_val + randint(10, 100)
                    wrong4 = kq_val - randint(10, 50)

                    candidates = [wrong1, wrong2, wrong3, wrong4]
                    pick = random.choice(candidates)
                    if pick != kq_val and pick > 0:
                        s.add('$%s$'%(latex(pick)))

                list_wrong = list(s)
                das1 = list_wrong[0]
                das2 = list_wrong[1]
                das3 = list_wrong[2]

                # Câu hỏi
                noidungcauhoi = ('''Từ các chữ số $%s, %s, %s$ lập được bao nhiêu số tự nhiên có $%s$ chữ số, trong đó chữ số $%s$ có mặt $%s$ lần, chữ số $%s$ có mặt $%s$ lần, chữ số $%s$ có mặt $%s$ lần?'''
                                 %(latex(d1), latex(d2), latex(d3), latex(n), 
                                   latex(d1), latex(a), latex(d2), latex(b), latex(d3), latex(c)
                                  ))

                # Các đáp án
                da_d = ('\\True $%s$' %(kq))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Cách 1: dùng tổ hợp\\\\
                         Chọn vị trí cho $%s$ chữ số $%s$ có $C_{%s}^{%s}$ cách.\\\\
                         Chọn vị trí cho $%s$ chữ số $%s$ có $C_{%s}^{%s}$ cách.\\\\
                         Chọn vị trí cho $%s$ chữ số $%s$ có $C_{%s}^{%s}$ cách.\\\\
                         Vậy số các số tự nhiên thỏa yêu cầu bài toán là $C_{%s}^{%s} \\cdot C_{%s}^{%s} \\cdot C_{%s}^{%s} = %s$ số.\\\\
                         Cách 2: dùng hoán vị lặp\\\\
                         Số các số tự nhiên thỏa yêu cầu bài toán là $\\frac{%s!}{%s! \\cdot %s! \\cdot %s!} = %s$ số.'''

                         %(latex(a), latex(d1), latex(c1), latex(a),
                           latex(b), latex(d2), latex(c2), latex(b),
                           latex(c), latex(d3), latex(c3), latex(c),
                           latex(c1), latex(a), latex(c2), latex(b), latex(c3), latex(c), latex(kq),
                           latex(n), latex(a), latex(b), latex(c), latex(kq)
                          ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

