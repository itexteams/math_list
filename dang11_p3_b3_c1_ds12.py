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


def bt_dang11_p3_b3_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                K = random.choice([120, 150, 160, 200])

                # P0: Initial population at t=0 (Must be < K)
                P0 = random.choice([10, 15, 20])

                # Choose r (growth rate coefficient)
                r = random.choice([Rational(1, 2), Rational(3, 4)])
                r_float = float(r)

                b_val = Rational(P0, K - P0)
                a_val = K * b_val

                # Simplify a and b for cleaner presentation
                # If the denominator of b is 1, a and b are integers.
                if b_val.q == 1:
                    a = int(a_val)
                    b = int(b_val)
                else:
                    # Use fractional form or round them (fractional is better for accuracy)
                    a = a_val
                    b = b_val


                P_prime_0_val = a_val * r * Rational(1, (b_val + 1)**2)

                # Round P'(0) to a clean integer or simple fraction
                P_prime_0 = round(float(P_prime_0_val)) if P_prime_0_val.q == 1 or P_prime_0_val.q == 2 else P_prime_0_val

                # The final answer is K
                kq_value = K
                kq = latex(kq_value) 

                # Set up the distractors for the multiple-choice question

                du = ['$%s$'%(kq), # Correct answer (K)
                      ]
                da = random.choice(du)

                # Distractors
                s = ['$%s$'%(latex(kq_value + 10)), # K + 10
                     '$%s$'%(latex(kq_value - 10)) if kq_value > 10 else '$%s$'%(latex(kq_value + 20)), # K - 10
                     '$%s$'%(latex(P0)), # Distractor: Initial Population (P0)
                     '$%s$'%(latex(kq_value/2)), # Distractor: K/2
                     '$%s$'%(latex(a)), # Distractor: a
                    ]

                # Select three unique incorrect answers
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Format the problem statement

                # Naming the exponent term
                r_exp_latex = latex(r)

                # Câu hỏi
                noidungcauhoi = ('''Giả sử số lượng của một quần thể nấm men tại môi trường nuôi cấy trong phòng thí nghiệm được mô hình hoá bằng hàm số $$P(t) = \\frac{%s}{%s + e^{-%s t}}$$ (tế bào). 
                                  Tại thời điểm ban đầu $t=0$, quần thể có $%s$ tế bào và tăng với tốc độ $%s$ tế bào/giờ. 
                                  Theo mô hình này số lượng nấm men không vượt quá bao nhiêu tế bào?'''
                                  %(latex(a), latex(b), r_exp_latex,
                                    latex(P0), latex(P_prime_0)
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
                loigiai=('''Số lượng nấm men không vượt quá giới hạn là giới hạn tại vô cùng (tiệm cận ngang) của hàm số $P(t)$.\\\\
                         $$\\lim_{t \\to +\\infty} P(t) = \\lim_{t \\to +\\infty} \\frac{%s}{%s + e^{-%s t}}$$
                         Vì hệ số $r=%s > 0$, ta có $\\lim_{t \\to +\\infty} e^{-%s t} = 0$. \\\\
                         Do đó: $$\\lim_{t \\to +\\infty} P(t) = \\frac{%s}{%s + 0} = \\frac{%s}{%s} = %s.$$
                         Vậy số lượng nấm men không vượt quá $%s$ tế bào (đây chính là sức chứa của môi trường).'''
                         # Đảm bảo đủ đối số: 3 + 2 + 5 + 1 = 11 đối số
                         %(latex(a), latex(b), r_exp_latex, # 1, 2, 3
                           r_exp_latex, r_exp_latex, # 4, 5
                           latex(a), latex(b), # 6, 7
                           latex(a), latex(b), latex(kq_value), # 8, 9, 10
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

