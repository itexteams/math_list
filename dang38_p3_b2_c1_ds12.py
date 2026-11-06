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


def bt_dang38_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Random độ dài cạnh hình vuông a (trong đề gốc a = 1)
                a_val = random.choice([1, 2, 3, 4, 5])
                a = sp.Integer(a_val)

                # Giá trị cực đại đạt được khi y = a*(sqrt(2) - 1)
                # S_max = a^2 * (3 - 2*sqrt(2))
                s_max_expr = a**2 * (3 - 2*sp.sqrt(2))
                kq_float = float(s_max_expr.evalf())

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_chinh_xac = str(kq_decimal).replace('.', ',')

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                da_dung = '$%s$' % kq_chinh_xac

                s_distractors = set()
                while len(s_distractors) < 3:
                    # Tạo sai số ngẫu nhiên
                    sai_so = random.choice([-0.05, -0.03, 0.02, 0.04, 0.08, 0.12])
                    val_sai = round(kq_float + sai_so, 2)
                    if val_sai > 0 and val_sai != round(kq_float, 2):
                        s_distractors.add('$%s$' % str(val_sai).replace('.', ','))

                list_sai = list(s_distractors)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # B2: Viết lại nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Cho hình vuông $ABCD$ có độ dài cạnh bằng $%s$. Cung $AC$ là một phần tư đường tròn tâm $D$, bán kính $DA$ (tham khảo hình vẽ). Giả sử $P$ là điểm thay đổi trên cung $AC$ ($P$ khác $A$ và $C$). Tiếp tuyến tại điểm $P$ của cung $AC$ cắt các đoạn thẳng $AB, BC$ theo thứ tự tại các điểm $M, N$. Diện tích lớn nhất của tam giác $BMN$ bằng bao nhiêu (kết quả làm tròn đến hàng phần trăm)?}
                                 { \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
            	\\draw  [line width=1]  (93,26) -- (242.47,26) -- (242.47,175.47) -- (93,175.47) -- cycle ;
            	\\draw  [draw opacity=0][line width=1]  (93.47,27) .. controls (175.09,27.25) and (241.21,93.37) .. (241.47,175) -- (93,175.47) -- cycle ; \\draw  [line width=1]  (93.47,27) .. controls (175.09,27.25) and (241.21,93.37) .. (241.47,175) ;  
            	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.63 ][line width=1]  (242.05,98.29) -- (139.67,26.24) -- (242.46,26.83) -- cycle ;
            	\\draw (74,7.33) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\\draw (244.67,11) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\\draw (242.47,175.47) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\\draw (76.67,174) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\\draw (130.67,4.67) node [anchor=north west][inner sep=0.75pt]    {$M$};
            	\\draw (244,89) node [anchor=north west][inner sep=0.75pt]    {$N$};
            	\\draw (162.67,52.67) node [anchor=north west][inner sep=0.75pt]    {$P$};
            \\end{tikzpicture}}'''
                                 % (latex(a)))

                # Nội dung lời giải chi tiết (B1)
                # MB = a - x, NB = a - y. Thế x = a(a-y)/(a+y) vào S = 1/2(a-x)(a-y)
                # Ta có a-x = a - a(a-y)/(a+y) = 2ay/(a+y)
                # Vậy S = 1/2 * [2ay/(a+y)] * (a-y) = ay(a-y)/(a+y)

                loigiai = ('''Ta có các tiếp tuyến $AM, MP$ cắt nhau tại $M$ và $CN, NP$ cắt nhau tại $N$.\\\\
                             $\\rightarrow AM = MP = x; CN = NP = y \\left( 0 \\le x, y \\le %s \\right) \\rightarrow MN = x + y; MB = %s - x; NB = %s - y$.\\\\
                             Ta có: $MN^2 = MB^2 + NB^2 \\rightarrow \\left( x + y \\right)^2 = \\left( %s - x \\right)^2 + \\left( %s - y \\right)^2 \\rightarrow x = \\frac{%s \\left( %s - y \\right)}{%s + y}$.\\\\
                             $S_{BMN} = \\frac{1}{2} \\left( %s - x \\right) \\left( %s - y \\right) = \\frac{1}{2} \\left( %s - \\frac{%s \\left( %s - y \\right)}{%s + y} \\right) \\left( %s - y \\right) = \\frac{%s y \\left( %s - y \\right)}{%s + y} = f\\left( y \\right)$.\\\\
                             Xét hàm số $f\\left( y \\right)$ trên đoạn $\\left[ 0; %s \\right]$, ta tìm được: \\\\
                             $\\max_{\\left[ 0; %s \\right]} f\\left( y \\right) = f\\left( %s \\left( \\sqrt{2} - 1 \\right) \\right) = %s \\left( 3 - 2\\sqrt{2} \\right) \\approx %s$.'''
                           % (latex(a), latex(a), latex(a), latex(a), latex(a), latex(a), latex(a), latex(a),
                              latex(a), latex(a), latex(a), latex(a), latex(a), latex(a), latex(a),
                              latex(a), latex(a), latex(a), latex(a), latex(a), latex(a), latex(a**2), kq_chinh_xac))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq_chinh_xac)
                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm (B2)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

