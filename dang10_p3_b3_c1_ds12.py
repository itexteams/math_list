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


def bt_dang10_p3_b3_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Randomize the constants A and B for the cost function C(t) = A*1000 + B*t (A is in million VND, B is in thousand VND)
                # A: Fixed Cost (in million VND)
                A_million = random.choice([5, 8, 10, 12])
                # A_thousand: Fixed Cost (in thousand VND)
                A_thousand = A_million * 1000

                # B: Marginal Cost (in thousand VND/unit) - the limit value (answer)
                B = random.choice([40, 60, 75, 80])

                # The Total Cost Function C(t) = A_thousand + B*t (using x as variable t for SymPy)
                Ct = A_thousand + B*x

                # The Average Cost Function f(t) = C(t) / t
                ft = Ct/x

                # The limit as x approaches infinity (The correct answer: B)
                limit_ft = limit(ft, x, oo)

                # The final answer
                kq_value = limit_ft
                kq = latex(kq_value) # B

                # Set up the distractors for the multiple-choice question

                du = ['$%s$'%(kq), # Correct answer (B)
                      ]
                da = random.choice(du)

                # Distractors
                s = ['$%s$'%(latex(kq_value + 5)), # B + 5
                     '$%s$'%(latex(kq_value - 5)) if kq_value > 5 else '$%s$'%(latex(kq_value + 10)), # B - 5
                     '$%s$'%(latex(A_million)), # Distractor: Fixed Cost (in million)
                     '$%s$'%(latex(A_thousand / 100)), # Distractor: A/1000*10 = A/100 (e.g., 70)
                     '$%s$'%(latex(kq_value*2)), # Distractor: 2*B
                    ]

                # Select three unique incorrect answers
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một tác giả muốn xuất bản một cuốn sách Toán học. Biết chi phí xuất bản là $%s$ triệu đồng và giá tiền in mỗi cuốn sách là $%s$ nghìn đồng. Gọi $t$ ($t \\geq 1$) là số cuốn sách sẽ in và $f(t)$ (Đơn vị nghìn đồng) là chi phí trung bình của mỗi cuốn sách. Khi đó, chi phí tối đa (chi phí in cho mỗi cuốn khi $t \\to +\\infty$) là bao nhiêu (nghìn đồng)?'''
                                  %(latex(A_million), latex(B)
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
                loigiai=('''Tổng số tiền cần bỏ ra để in $t$ cuốn sách là (đơn vị nghìn đồng): \\\\
                         $$C(t) = %s + %s t.$$
                         Chi phí trung bình của mỗi cuốn sách là: $$f(t)=\\frac{C(t)}{t}=\\frac{%s + %s t}{t} = %s + \\frac{%s}{t}.$$
                         Chi phí tối đa (hay chi phí biên) là giới hạn của chi phí trung bình khi số cuốn sách $t \\to +\\infty$:\\\\
                         $$\\lim_{t \\to +\\infty} f(t) = \\lim_{t \\to +\\infty} \\left(%s + \\frac{%s}{t}\\right) = %s + 0 = %s.$$
                         Vậy chi phí tối đa (tối thiểu mà chi phí trung bình có thể đạt được) là $%s$ nghìn đồng.'''
                         # Đảm bảo đủ đối số: 2 + 4 + 4 + 1 = 11 đối số
                         %(latex(A_thousand), latex(B), # 1, 2
                           latex(A_thousand), latex(B), latex(B), latex(A_thousand), # 3, 4, 5, 6
                           latex(B), latex(A_thousand), latex(B), latex(kq_value), # 7, 8, 9, 10
                           latex(kq_value) # 11
                         )) 

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content       

