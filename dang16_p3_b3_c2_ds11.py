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


def bt_dang16_p3_b3_c2_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài cạnh hình vuông đầu tiên a1: 3 đến 8
                a1 = random.randint(3, 8) 

                # Số hạng cần tìm (n): Hình vuông C4 đến C7
                n = random.randint(4, 7)

                # CÔNG BỘI (không đổi theo hình học)
                q_value = sqrt(10) / 4

                # Tính toán giá trị cần tìm
                # Công thức: a_n = a1 * q**(n-1)
                an_value = a1 * (q_value**(n-1))

                # SỬA LỖI: Chuyển kết quả tính toán (sympy.Float/float) thành chuỗi (str)
                # trước khi truyền vào Decimal() để tránh TypeError.
                kq = Decimal(str(an_value.evalf())).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Định dạng kết quả (chuyển dấu . thành ,)
                kq_str = str(kq).replace('.',',')

                # --- Tạo các đáp án nhiễu ---
                kq_float = float(kq)

                s_options_float = [
                    round(kq_float + random.uniform(0.5, 1.5), 2),
                    round(kq_float - random.uniform(0.5, 1.5), 2),
                    round(kq_float * random.uniform(0.8, 0.95), 2), 
                    round(kq_float * random.uniform(1.05, 1.2), 2),
                ]

                # Chuyển dấu . thành , cho các đáp án nhiễu
                s_options = []
                for i in s_options_float:
                    kq_float_ans = Decimal(i).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    kq_str_ans = str(kq_float_ans).replace('.',',')
                    s_options.append(kq_str_ans)

                s_options = list(set(s_options))
                # --- Nội dung Câu hỏi ---
                a1_latex = latex(a1).replace('.',',')
                n_latex = latex(n).replace('.',',')
                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                    '''Cho hình vuông $C_1$ có cạnh bằng $%s$. Người ta chia mỗi cạnh hình vuông thành bốn phần bằng nhau và nối các điểm chia một cách thích hợp để có hình vuông $C_2$. Cứ tiếp tục quá trình như trên, ta nhận được dãy các hình vuông $C_1, C_2, C_3, \\dots$. Gọi $a_n$ là độ dài cạnh hình vuông $C_n$. Độ dài cạnh của hình vuông $C_{%s}$ bằng bao nhiêu? (làm tròn đến hai chữ số thập phân).}'''
                    '{'
                    '''\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1cm,y=1cm]
            	\\clip(-0.5,-0.5) rectangle (5,4.1);
            	\\draw [line width=1.2pt] (0,4)-- (4,4);
            	\\draw [line width=1.2pt] (4,4)-- (4,0);
            	\\draw [line width=1.2pt] (0,0)-- (4,0);
            	\\draw [line width=1.2pt] (0,0)-- (0,4);
            	\\draw [line width=1.2pt] (0,3)-- (3,4);
            	\\draw [line width=1.2pt] (3,4)-- (4,1);
            	\\draw [line width=1.2pt] (4,1)-- (1,0);
            	\\draw [line width=1.2pt] (1,0)-- (0,3);
            	\\draw [line width=1.2pt] (0.25,2.25)-- (2.25,3.75);
            	\\draw [line width=1.2pt] (2.25,3.75)-- (3.75,1.75);
            	\\draw [line width=1.2pt] (3.75,1.75)-- (1.75,0.25);
            	\\draw [line width=1.2pt] (1.75,0.25)-- (0.25,2.25);
            	\\draw [line width=1.2pt] (0.625,1.75)-- (1.75,3.375);
            	\\draw [line width=1.2pt] (1.75,3.375)-- (3.375,2.25);
            	\\draw [line width=1.2pt] (3.375,2.25)-- (2.25,0.625);
            	\\draw [line width=1.2pt] (2.25,0.625)-- (0.625,1.75);
            	\\draw [line width=1.2pt] (1.46875,2.96875)-- (2.96875,2.53125);
            	\\draw [line width=1.2pt] (2.96875,2.53125)-- (2.53125,1.03125);
            	\\draw [line width=1.2pt] (2.53125,1.03125)-- (1.03125,1.46875);
            	\\draw [line width=1.2pt] (1.03125,1.46875)-- (1.46875,2.96875);
            	\\draw [line width=1.2pt] (1.359375,2.59375)-- (2.59375,2.640625);
            	\\draw [line width=1.2pt] (2.59375,2.640625)-- (2.640625,1.40625);
            	\\draw [line width=1.2pt] (1.359375,2.59375)-- (1.40625,1.359375);
            	\\draw [line width=1.2pt] (1.37109375,2.28515625)-- (2.28515625,2.62890625);
            	\\draw [line width=1.2pt] (2.28515625,2.62890625)-- (2.62890625,1.71484375);
            	\\draw [line width=1.2pt] (2.62890625,1.71484375)-- (1.71484375,1.37109375);
            	\\draw [line width=1.2pt] (1.71484375,1.37109375)-- (1.37109375,2.28515625);
            	\\draw [line width=1.2pt] (1.40625,1.359375)-- (2.640625,1.40625);
            \\end{tikzpicture}}'''
                                 %(a1_latex, n_latex)
                                 )

                # Nội dung lời giải
                loigiai = ('''Độ dài cạnh của hình vuông đầu tiên là: $a_1 = %s$. \\\\
                Theo cách dựng hình vuông $C_{n+1}$ từ hình vuông $C_n$, cạnh $a_{n+1}$ là cạnh huyền của một tam giác vuông có hai cạnh góc vuông lần lượt là $\\frac{a_n}{4}$ và $3\\frac{a_n}{4}$. \\\\
                Áp dụng định lý Pythagoras: \\\\
                $$a_{n+1}^2 = \\left(\\frac{a_n}{4}\\right)^2 + \\left(3\\frac{a_n}{4}\\right)^2 = \\frac{a_n^2}{16} + \\frac{9a_n^2}{16} = \\frac{10a_n^2}{16}$$
                Suy ra: $$a_{n+1} = \\sqrt{\\frac{10a_n^2}{16}} = \\frac{\\sqrt{10}}{4} a_n$$
                Vậy, dãy số $(a_n)$ là một cấp số nhân với số hạng đầu $a_1 = %s$ và công bội $$q = \\frac{a_{n+1}}{a_n} = \\frac{\\sqrt{10}}{4}$$
                Độ dài cạnh của hình vuông $C_{%s}$ là $a_{%s}$:
                $$a_{%s} = a_1 \\cdot q^{%s-1} = %s \\cdot \\left(\\frac{\\sqrt{10}}{4}\\right)^{%s} \\approx %s.$$'''

                         %(a1_latex, 
                           a1_latex, 
                           n_latex, n_latex,
                           n_latex, n_latex, a1_latex, latex(n-1), kq_str
                         ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_str))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')       
            return content 

