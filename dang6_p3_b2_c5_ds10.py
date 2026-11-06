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


def bt_dang6_p3_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo các đối tượng trang trí ngẫu nhiên
                list_obj = [
                    ('ngôi sao', 'hình tròn', '\\star', '\\circ'),
                    ('viên bi đỏ', 'viên bi xanh', '\\bullet', '\\circ'),
                    ('dấu tích', 'dấu nhân', '\\checkmark', '\\times'),
                    ('hình vuông', 'hình tròn', '\\square', '\\circ')
                ]
                obj1_name, obj2_name, sym1, sym2 = random.choice(list_obj)

                # Các giá trị cố định của bài toán 4x4
                n_h = 1296 
                n_c = 1296 
                n_hc = 90 
                n_h_union_c = 2502 

                # Random kiểu hỏi: "và" (kết quả 90) hoặc "hoặc" (kết quả 2502)
                kieu_hoi = random.choice(['và', 'hoặc'])

                if kieu_hoi == 'và':
                    da_dung = n_hc
                    s = [str(n_h_union_c), str(n_h), '84', '96', '120']
                else:
                    da_dung = n_h_union_c
                    s = [str(n_hc), str(n_h), '2412', '2592', '2600']

                # Trộn và chọn đáp án
                da = '$%s$' % latex(da_dung)
                s = list(set(s))
                if str(da_dung) in s: s.remove(str(da_dung))
                random.shuffle(s)
                das1 = '$%s$' % s[0]
                das2 = '$%s$' % s[1]
                das3 = '$%s$' % s[2]

                # Mã TikZ cho hai hình vẽ (Dùng %% để thoát dấu % và \\ để in ra \)
                tikz_code = ('''\\begin{center}
                \\begin{tikzpicture}[scale=0.6, font=\\footnotesize, baseline=(current bounding box.center)]
                    \\draw (0,0) grid (4,4);
                    \\node at (2,-0.6) {Hình 1};
                \\end{tikzpicture}
                \\hspace{1.5cm}
                \\begin{tikzpicture}[scale=0.6, font=\\footnotesize, baseline=(current bounding box.center)]
                    \\draw (0,0) grid (4,4);
                    \\foreach \\x/\\y in {0.5/3.5, 1.5/3.5, 0.5/2.5, 1.5/2.5, 2.5/1.5, 3.5/1.5, 2.5/0.5, 3.5/0.5}
                        \\node at (\\x,\\y) {$%s$};
                    \\foreach \\x/\\y in {2.5/3.5, 3.5/3.5, 2.5/2.5, 3.5/2.5, 0.5/1.5, 1.5/1.5, 0.5/0.5, 1.5/0.5}
                        \\node at (\\x,\\y) {$%s$};
                    \\node at (2,-0.6) {Hình 2};
                \\end{tikzpicture}
            \\end{center}''' % (sym1, sym2))

                # Câu hỏi
                noidungcauhoi = ('''Người ta trang trí một bảng ô vuông $4 \\times 4$ (như hình 1) bởi các %s và các %s giống nhau. Mỗi ô vuông nhỏ được dán một %s hoặc một %s, sao cho trong mỗi hàng %s mỗi cột của bảng ô vuông đều có $2$ %s và $2$ %s (tham khảo một cách dán trong hình 2).
            %s
            Có tất cả bao nhiêu cách trang trí bảng ô vuông thỏa mãn yêu cầu trên?'''
                                 %(obj1_name, obj2_name, obj1_name, obj2_name, kieu_hoi, obj1_name, obj2_name, tikz_code))

                # Lời giải chi tiết (\\\\ để in ra xuống dòng LaTeX \\)
                loigiai = ('''Trong một hàng, số cách chọn $2$ ô để đặt %s ($2$ ô còn lại tự động đặt %s) là: $C_4^2 = 6$ cách. \\\\
            Vì bảng có $4$ hàng và việc sắp xếp ở mỗi hàng là độc lập với nhau, nên tổng số cách để cả $4$ hàng đều thỏa mãn điều kiện là: $N\\left(H\\right) = 6^4 = 1296$ cách. \\\\
            Tương tự như hàng, mỗi cột có $4$ ô và ta chọn $2$ ô để đặt %s, có $C_4^2 = 6$ cách cho mỗi cột. Với $4$ cột, tổng số cách để cả $4$ cột đều thỏa mãn điều kiện là: $N\\left(C\\right) = 6^4 = 1296$ cách. \\\\
            Xét số cách trang trí thỏa mãn đồng thời "mỗi hàng và mỗi cột" (cách hiểu 1): \\\\
            - Khả năng 1: Hàng 1 và Hàng 2 giống hệt nhau (có $6$ cách chọn Hàng 1, Hàng 2 cố định theo). Khi đó Hàng 3 và Hàng 4 phải giống nhau và là phần bù của Hàng 1. $\\Rightarrow 6 \\times 1 = 6$ cách. \\\\
            - Khả năng 2: Hàng 1 và Hàng 2 là phần bù của nhau (không chung vị trí %s nào). Khi đó Hàng 3 và Hàng 4 cũng phải là phần bù của nhau. $\\Rightarrow 6 \\times 1 \\times 6 = 36$ cách. \\\\
            - Khả năng 3: Hàng 1 và Hàng 2 chung nhau đúng $1$ vị trí %s. Có $6 \\times 4 \\times 2 = 48$ cách. \\\\
            Số cách trang trí thỏa mãn đồng thời cả hàng và cột là: $N\\left(HC\\right) = 6 + 36 + 48 = 90$ cách. \\\\'''
                           %(obj1_name, obj2_name, obj1_name, obj1_name, obj1_name))

                if kieu_hoi == 'hoặc':
                    loigiai += ('''\\\\ Theo yêu cầu đề bài "mỗi hàng hoặc mỗi cột" (cách hiểu 2), ta áp dụng công thức hợp của hai tập hợp: \\\\
                                $N\\left(H \\cup C\\right) = N\\left(H\\right) + N\\left(C\\right) - N\\left(HC\\right) = 1296 + 1296 - 90 = 2502$ cách.''')
                else:
                    loigiai += ('''Theo yêu cầu đề bài "mỗi hàng và mỗi cột", số cách trang trí thỏa mãn là: $N\\left(HC\\right) = 90$ cách.''')

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(da_dung))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

