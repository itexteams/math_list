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


def bt_dang69_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random cơ số A để tính giá trị A^4 * P
                A = random.choice([6, 7, 8, 9, 10, 11, 12])

                # Tính toán chính xác giá trị xác suất P và kết quả
                # P = 8100 / 30260340 = 45 / 168113
                ans_val_dec = Decimal(A**4) * Decimal(45) / Decimal(168113)

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq3 = ans_val_dec.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')

                # Các đáp án trắc nghiệm (Tạo các phương án sai lệch đi 1 chút so với đáp án đúng)
                kq_float = float(kq3)
                s_floats = [
                    round(kq_float + 0.05, 2),
                    round(kq_float - 0.05, 2),
                    round(kq_float + 0.12, 2),
                    round(kq_float - 0.12, 2),
                    round(kq_float + 0.24, 2),
                    round(kq_float - 0.24, 2)
                ]
                # Đổi các đáp án sai sang định dạng chuỗi có dấu phẩy
                s_strs = [str(Decimal(str(f)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',') for f in s_floats]

                du = ['$%s$' % (kq)]
                da = du[0]

                s = ['$%s$' % val for val in s_strs]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''\\immini{Cho bảng $6 \\times 6$ gồm $36$ ô vuông đơn vị và cho $8$ quân cờ đôi một khác nhau. Người ta xếp ngẫu nhiên $8$ quân cờ đó vào $36$ ô trong bảng sao cho mỗi ô xếp nhiều nhất một quân cờ. Hai cách xếp được gọi là như nhau nếu vị trí của $8$ quân cờ tương ứng trên bảng là giống nhau sau khi xếp xong (không tính đến thứ tự xếp các quân cờ vào bảng). Chọn ngẫu nhiên một cách xếp như trên. Gọi $P$ là xác suất của biến cố: “Cách xếp được chọn thỏa mãn đồng thời ba điều kiện sau: \\\\
                - Trên mỗi hàng có ít nhất một quân cờ; \\\\
                - Trên mỗi cột có ít nhất một quân cờ; \\\\
                - Mỗi quân cờ phải cùng hàng với đúng một quân cờ khác hoặc cùng cột với đúng một quân cờ khác.” \\\\
                Giá trị của $%s^4 P$ bằng bao nhiêu (không làm tròn kết quả các phép tính trung gian, chỉ làm tròn kết quả phép tính cuối cùng đến hàng phần trăm)?}
                                 {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                                 	\\draw  [line width=1.5]  (36.2,31) -- (66,31) -- (66,60.8) -- (36.2,60.8) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=0.5 ][line width=1.5]  (66,31) -- (95.8,31) -- (95.8,60.8) -- (66,60.8) -- cycle ;
                                 	\\draw  [line width=1.5]  (95.8,31) -- (125.6,31) -- (125.6,60.8) -- (95.8,60.8) -- cycle ;
                                 	\\draw  [line width=1.5]  (125.6,31) -- (155.4,31) -- (155.4,60.8) -- (125.6,60.8) -- cycle ;
                                 	\\draw  [line width=1.5]  (155.4,31) -- (185.2,31) -- (185.2,60.8) -- (155.4,60.8) -- cycle ;
                                 	\\draw  [line width=1.5]  (185.2,31) -- (215,31) -- (215,60.8) -- (185.2,60.8) -- cycle ;
                                 	\\draw  [line width=1.5]  (36.2,60.8) -- (66,60.8) -- (66,90.6) -- (36.2,90.6) -- cycle ;
                                 	\\draw  [line width=1.5]  (66,60.8) -- (95.8,60.8) -- (95.8,90.6) -- (66,90.6) -- cycle ;
                                 	\\draw  [line width=1.5]  (95.8,60.8) -- (125.6,60.8) -- (125.6,90.6) -- (95.8,90.6) -- cycle ;
                                 	\\draw  [line width=1.5]  (125.6,60.8) -- (155.4,60.8) -- (155.4,90.6) -- (125.6,90.6) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.5 ][line width=1.5]  (155.4,60.8) -- (185.2,60.8) -- (185.2,90.6) -- (155.4,90.6) -- cycle ;
                                 	\\draw  [line width=1.5]  (185.2,60.8) -- (215,60.8) -- (215,90.6) -- (185.2,90.6) -- cycle ;
                                 	\\draw  [line width=1.5]  (36.2,90.6) -- (66,90.6) -- (66,120.4) -- (36.2,120.4) -- cycle ;
                                 	\\draw  [line width=1.5]  (66,90.6) -- (95.8,90.6) -- (95.8,120.4) -- (66,120.4) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.5 ][line width=1.5]  (95.8,90.6) -- (125.6,90.6) -- (125.6,120.4) -- (95.8,120.4) -- cycle ;
                                 	\\draw  [line width=1.5]  (125.6,90.6) -- (155.4,90.6) -- (155.4,120.4) -- (125.6,120.4) -- cycle ;
                                 	\\draw  [line width=1.5]  (155.4,90.6) -- (185.2,90.6) -- (185.2,120.4) -- (155.4,120.4) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=0.5 ][line width=1.5]  (185.2,90.6) -- (215,90.6) -- (215,120.4) -- (185.2,120.4) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=0.5 ][line width=1.5]  (36.2,120.4) -- (66,120.4) -- (66,150.2) -- (36.2,150.2) -- cycle ;
                                 	\\draw  [line width=1.5]  (66,120.4) -- (95.8,120.4) -- (95.8,150.2) -- (66,150.2) -- cycle ;
                                 	\\draw  [line width=1.5]  (95.8,120.4) -- (125.6,120.4) -- (125.6,150.2) -- (95.8,150.2) -- cycle ;
                                 	\\draw  [line width=1.5]  (125.6,120.4) -- (155.4,120.4) -- (155.4,150.2) -- (125.6,150.2) -- cycle ;
                                 	\\draw  [line width=1.5]  (155.4,120.4) -- (185.2,120.4) -- (185.2,150.2) -- (155.4,150.2) -- cycle ;
                                 	\\draw  [line width=1.5]  (185.2,120.4) -- (215,120.4) -- (215,150.2) -- (185.2,150.2) -- cycle ;
                                 	\\draw  [line width=1.5]  (36.2,150.2) -- (66,150.2) -- (66,180) -- (36.2,180) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1.5]  (66,150.2) -- (95.8,150.2) -- (95.8,180) -- (66,180) -- cycle ;
                                 	\\draw  [line width=1.5]  (95.8,150.2) -- (125.6,150.2) -- (125.6,180) -- (95.8,180) -- cycle ;
                                 	\\draw  [line width=1.5]  (125.6,150.2) -- (155.4,150.2) -- (155.4,180) -- (125.6,180) -- cycle ;
                                 	\\draw  [line width=1.5]  (155.4,150.2) -- (185.2,150.2) -- (185.2,180) -- (155.4,180) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 189; green, 16; blue, 224 }  ,fill opacity=0.5 ][line width=1.5]  (185.2,150.2) -- (215,150.2) -- (215,180) -- (185.2,180) -- cycle ;
                                 	\\draw  [line width=1.5]  (36.2,180) -- (66,180) -- (66,209.8) -- (36.2,209.8) -- cycle ;
                                 	\\draw  [line width=1.5]  (66,180) -- (95.8,180) -- (95.8,209.8) -- (66,209.8) -- cycle ;
                                 	\\draw  [line width=1.5]  (95.8,180) -- (125.6,180) -- (125.6,209.8) -- (95.8,209.8) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 144; green, 19; blue, 254 }  ,fill opacity=0.5 ][line width=1.5]  (125.6,180) -- (155.4,180) -- (155.4,209.8) -- (125.6,209.8) -- cycle ;
                                 	\\draw  [line width=1.5]  (155.4,180) -- (185.2,180) -- (185.2,209.8) -- (155.4,209.8) -- cycle ;
                                 	\\draw  [line width=1.5]  (185.2,180) -- (215,180) -- (215,209.8) -- (185.2,209.8) -- cycle ;
                                 	\\draw (72,37) node [anchor=north west][inner sep=0.75pt]    {$A$};
                                 	\\draw (160,69) node [anchor=north west][inner sep=0.75pt]    {$B$};
                                 	\\draw (101.33,98) node [anchor=north west][inner sep=0.75pt]    {$C$};
                                 	\\draw (189.33,98) node [anchor=north west][inner sep=0.75pt]    {$D$};
                                 	\\draw (40.67,128) node [anchor=north west][inner sep=0.75pt]    {$E$};
                                 	\\draw (72.67,158) node [anchor=north west][inner sep=0.75pt]    {$F$};
                                 	\\draw (130,188) node [anchor=north west][inner sep=0.75pt]    {$H$};
                                 	\\draw (189.33,158) node [anchor=north west][inner sep=0.75pt]    {$G$};
                                 	\\draw (45,9) node [anchor=north west][inner sep=0.75pt]    {$1$};
                                 	\\draw (75,9) node [anchor=north west][inner sep=0.75pt]    {$2$};
                                 	\\draw (105.67,9) node [anchor=north west][inner sep=0.75pt]    {$3$};
                                 	\\draw (135,9) node [anchor=north west][inner sep=0.75pt]    {$4$};
                                 	\\draw (165,9) node [anchor=north west][inner sep=0.75pt]    {$5$};
                                 	\\draw (195,9) node [anchor=north west][inner sep=0.75pt]    {$6$};
                                 	\\draw (19,38) node [anchor=north west][inner sep=0.75pt]    {$1$};
                                 	\\draw (19,68) node [anchor=north west][inner sep=0.75pt]    {$2$};
                                 	\\draw (19,99) node [anchor=north west][inner sep=0.75pt]    {$3$};
                                 	\\draw (19,128) node [anchor=north west][inner sep=0.75pt]    {$4$};
                                 	\\draw (19,158) node [anchor=north west][inner sep=0.75pt]    {$5$};
                                 	\\draw (19,188) node [anchor=north west][inner sep=0.75pt]    {$6$};
                                 \\end{tikzpicture}}''' 
                                 % (A))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Số phần tử của không gian mẫu là số cách chọn $8$ ô từ $36$ ô: $\\Omega = C_{36}^8 = 30260340$. \\\\
                Gọi biến cố đề bài là $X$. Ta đếm số kết quả thuận lợi cho $X$. \\\\
                Theo điều kiện đề bài, mỗi hàng và mỗi cột có ít nhất $1$ quân cờ, tổng số quân cờ là $8$. Lại có điều kiện thứ 3: “Mỗi quân cờ phải cùng hàng với đúng một quân cờ khác hoặc cùng cột với đúng một quân cờ khác”. Điều này có nghĩa là mỗi quân cờ phải nằm trên một hàng có đúng $2$ quân cờ, hoặc một cột có đúng $2$ quân cờ. \\\\
                Để thỏa mãn điều kiện này, số quân cờ trên $6$ hàng phải là một hoán vị của $(2, 2, 1, 1, 1, 1)$, và trên $6$ cột cũng là một hoán vị của $(2, 2, 1, 1, 1, 1)$. \\\\
                Gọi $R$ là tập gồm $2$ hàng có $2$ quân cờ, có $C_6^2 = 15$ cách chọn. \\\\
                Gọi $C$ là tập gồm $2$ cột có $2$ quân cờ, có $C_6^2 = 15$ cách chọn. \\\\
                Vì mỗi quân cờ phải nằm trong $R$ hoặc $C$, mà tổng số quân cờ là $8$ bằng tổng sức chứa của $R$ và $C$ ($4+4=8$), nên không có quân cờ nào nằm ở ô giao của $R$ và $C$. Do đó, $4$ quân cờ của $R$ phải nằm ở $4$ cột không thuộc $C$. \\\\
                Số cách xếp $4$ quân cờ này vào $2$ hàng thuộc $R$ và $4$ cột không thuộc $C$ (mỗi hàng $2$ quân, mỗi cột $1$ quân) là $C_4^2 = 6$ cách. \\\\
                Tương tự, số cách xếp $4$ quân cờ của $C$ vào $4$ hàng không thuộc $R$ là $C_4^2 = 6$ cách. \\\\
                Số kết quả thuận lợi là $|X| = 15 \\cdot 15 \\cdot 6 \\cdot 6 = 8100$. \\\\
                Xác suất $P = \\frac{8100}{30260340} = \\frac{45}{168113}$. \\\\
                Vậy giá trị cần tìm là $%s^4 \\cdot P = %s \\cdot \\frac{45}{168113} \\approx %s$.'''
                           % (A, A**4, kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

