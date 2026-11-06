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


def bt_dang10_p3_b2_c2_hh12(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # === Tham số cố định theo đề bài mẫu ===
                # Đường thẳng d: x/2 = y/-1 = (z+1)/1 => A(2t, -t, t-1)
                # Mặt phẳng (alpha): x - 2y - 2z + 5 = 0
                a, b, c, D_mp = randint(1,4), randint(-4,-1), randint(-4,-1), randint(1,5)
                khoang_cach_cho_truoc = 3

                # Khai báo t là biến thực để giải Abs (Khắc phục lỗi NotImplementedError)
                t = symbols('t', real=True)

                # === Tính toán theo lời giải ===

                # Mẫu số: |vec(n)|
                mau_so = sqrt(a**2 + b**2 + c**2)
                # Tử số: |ax_A + by_A + cz_A + D|
                tu_so = Abs(a*(2*t) + b*(-t) + c*(t-1) + D_mp)

                # Phương trình khoảng cách
                # pt = tu_so / mau_so - khoang_cach_cho_truoc
                # |2t + 2t - 2t + 2 + 5| / 3 = 3 => |2t + 7| = 9
                pt_goc = Abs(2*t + 7) - 9

                # Giải phương trình |2t + 7| = 9
                giai_t = solve(pt_goc, t) # Kết quả: [1, -8]

                # Chọn t > 0 (Hoành độ x_A = 2t > 0 => t > 0)
                t_chon = None
                for val in giai_t:
                    if val > 0:
                        t_chon = val
                        break

                # Tọa độ điểm A và Độ dài OA
                if t_chon is not None:
                    # A(2t, -t, t-1)
                    xA = 2 * t_chon
                    yA = -t_chon
                    zA = t_chon - 1

                    # OA = sqrt(x_A^2 + y_A^2 + z_A^2)
                    OA_sq = xA**2 + yA**2 + zA**2
                    OA_exact = sqrt(OA_sq) # sqrt(5)

                    # Kết quả làm tròn đến hàng phần mười
                    kq2 = float(OA_exact)
                    kq3 = Decimal(kq2).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    kq = str(kq3).replace('.', ',') # '2,2'
                else:
                    # Trường hợp dự phòng (nên không xảy ra với tham số mẫu)
                    kq, kq2 = '2,2', 2.2
                    OA_exact = sqrt(5)


                # Các đáp án trắc nghiệm
                da = '$%s$' % (kq)
                kq4 = round(kq2, 1) # Giá trị dùng để tạo đáp án sai: 2.2

                s = ['$%s$' % (latex(round(kq4 + 0.1, 1))).replace('.', ','), # 2,3
                     '$%s$' % (latex(round(kq4 + 0.2, 1))).replace('.', ','), # 2,4
                     '$%s$' % (latex(round(kq4 - 0.1, 1))).replace('.', ','), # 2,1
                     '$%s$' % (latex(round(kq4 - 0.2, 1))).replace('.', ','), # 2,0
                    ]

                random.shuffle(s)

                # Lấy 3 đáp án sai duy nhất
                das_list = list(set(s))
                while len(das_list) < 3: # Đảm bảo có 3 đáp án sai
                    das_list.append('$%s$' % (latex(round(kq4 + 0.3, 1))).replace('.', ','))

                das1, das2, das3 = das_list[0], das_list[1], das_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong không gian $Oxyz$, cho đường thẳng $d: \\frac{x}{2} = \\frac{y}{-1} = \\frac{z+1}{1}$ và mặt phẳng $(\\alpha): x - 2y - 2z + 5 = 0$. Điểm $A$ có hoành độ dương thuộc đường thẳng $d$ sao cho khoảng cách từ $A$ đến $(\\alpha)$ bằng $%s$. Độ dài $OA$ bằng bao nhiêu (kết quả làm tròn đến hàng phần mười).'''
                                 % (latex(khoang_cach_cho_truoc)
                                 ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''$A \\in d \\Rightarrow  A(2t; -t; t-1)$, với $t$ là tham số.
                Điều kiện hoành độ $x_A = 2t > 0 \\Rightarrow  t > 0$. \\\\
                Khoảng cách từ $A$ đến $(\\alpha): x - 2y - 2z + 5 = 0$ là:
                $$d(A, (\\alpha)) = \\frac{|(2t) - 2(-t) - 2(t-1) + 5|}{\\sqrt{1^2 + (-2)^2 + (-2)^2}} = \\frac{|2t + 2t - 2t + 2 + 5|}{3} = \\frac{|2t + 7|}{3}$$
                Theo đề bài, $d(A, (\\alpha)) = %s$, ta có
                $$\\frac{|2t + 7|}{3} = %s \\iff |2t + 7| = %s \\iff \\begin{cases} 2t + 7 = %s \\Rightarrow  t = 1 \\text{ (thỏa mãn } t>0 \\text{)} \\\\ 2t + 7 = -%s \\Rightarrow  t = -8 \\text{ (loại)} \\end{cases}$$
                Với $t=1$, ta có $A(2; -1; 0)$. \\\\
                Độ dài $OA$ là
                $$OA = \\sqrt{2^2 + (-1)^2 + 0^2} = \\sqrt{5} \\approx %s.$$'''
                         % (latex(khoang_cach_cho_truoc), latex(khoang_cach_cho_truoc), latex(khoang_cach_cho_truoc * 3), latex(khoang_cach_cho_truoc * 3), latex(khoang_cach_cho_truoc * 3), kq
                         ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))                                                                                                 

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

