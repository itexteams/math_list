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


def bt_dang14_p1_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (Dạng 1: Tính P(B|A) dựa trên công thức Bayes)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tạo các giá trị ngẫu nhiên để bài toán đa dạng
                # P(B) = n1/10
                n1 = randint(3, 8) 
                pb = Rational(n1, 10)
                p_notb = 1 - pb

                # P(A|B) = n2/10
                n2 = randint(4, 9)
                pa_cond_b = Rational(n2, 10)

                # P(A|not B) = n3/100 (thường chọn số có đuôi 5 hoặc 0 để giống đề mẫu)
                n3 = randint(2, 8) * 5 + randint(0, 4) * 10
                pa_cond_notb = Rational(n3, 100)

                # Tính toán theo công thức xác suất toàn phần
                # P(A) = P(B)P(A|B) + P(not B)P(A|not B)
                pa = pb * pa_cond_b + p_notb * pa_cond_notb

                # Tính P(B|A) theo công thức Bayes
                res = (pb * pa_cond_b) / pa

                # Đáp án đúng
                kq = latex(res)
                da = '$%s$' % kq

                # Tạo các phương án nhiễu (sai)
                s = set()
                while len(s) < 3:
                    # Nhiễu 1: Đảo tử số và mẫu số hoặc thay đổi nhẹ
                    sai1 = latex(Rational(res.p + randint(1, 5), res.q))
                    # Nhiễu 2: Tính nhầm P(not B|A)
                    sai2 = latex(1 - res)
                    # Nhiễu 3: Quên không chia cho P(A) hoặc chia sai
                    sai3 = latex(Rational(res.p, res.q + randint(1, 10)))

                    candidates = ['$%s$' % sai1, '$%s$' % sai2, '$%s$' % sai3]
                    for c in candidates:
                        if c != da:
                            s.add(c)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hai biến cố $A$ và $B$, với $P(B)=%s$, $P(A|B)=%s$, $P(A|\\overline{B})=%s$. Giá trị $P(B|A)$ bằng'''
                                 %(latex(float(pb)).replace('.',','), 
                                   latex(float(pa_cond_b)).replace('.',','), 
                                   latex(float(pa_cond_notb)).replace('.',',')))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo mẫu ảnh
                # Chuyển đổi các giá trị sang số thực để hiển thị giống định dạng thập phân trong lời giải mẫu
                pb_val = float(pb)
                p_notb_val = float(p_notb)
                pa_b_val = float(pa_cond_b)
                pa_notb_val = float(pa_cond_notb)
                pa_val = float(pa)
                tu_so_val = float(pb * pa_cond_b)

                loigiai = ('''Theo công thức xác suất toàn phần: \\\\
                             $P(A) = P(B).P(A|B) + P(\\overline{B}).P(A|\\overline{B}) = %s.%s + %s.%s = %s$. \\\\
                             Theo công thức Bayes: \\\\
                             $P(B|A) = \\frac{P(B).P(A|B)}{P(A)} = \\frac{%s.%s}{%s} = %s$.'''
                           %(str(pb_val).replace('.',','), str(pa_b_val).replace('.',','),
                             str(p_notb_val).replace('.',','), str(pa_notb_val).replace('.',','),
                             str(pa_val).replace('.',','),
                             str(pb_val).replace('.',','), str(pa_b_val).replace('.',','),
                             str(pa_val).replace('.',','),
                             latex(res)
                            ))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
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

