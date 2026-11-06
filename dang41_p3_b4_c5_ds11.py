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


def bt_dang41_p3_b4_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random dữ liệu
                # c0: nồng độ ban đầu (mg/lít)
                c0 = randint(15, 25)
                # t1: thời điểm đo lần 2 (giờ)
                t1 = randint(3, 5)
                # c1: nồng độ tại thời điểm t1 (c1 < c0)
                c1 = randint(10, c0 - 2)
                # c_min: nồng độ tối thiểu để tiêm liều mới (c_min < c1)
                c_min = randint(5, c1 - 2)

                # Bước 2: Tính toán
                # Công thức: C(t) = C0 * e^(-rt)
                # Tại t1: c1 = c0 * e^(-r*t1) => e^(-r*t1) = c1/c0 => -r*t1 = ln(c1/c0) => r = ln(c0/c1) / t1
                r_val = math.log(c0 / c1) / t1

                # Tìm t sao cho C(t) = c_min
                # c_min = c0 * e^(-rt) => e^(-rt) = c_min/c0 => -rt = ln(c_min/c0) => t = ln(c0/c_min) / r
                t_res = math.log(c0 / c_min) / r_val

                # Làm tròn đến hàng đơn vị theo quy tắc ROUND_HALF_UP
                kq_num = int(Decimal(str(t_res)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                # Bước 3: Tạo đáp án
                da = '$%s$' % (kq_num)

                # Tạo danh sách đáp án sai không trùng với đáp án đúng
                s = []
                while len(s) < 3:
                    sai = kq_num + random.choice([-3, -2, -1, 1, 2, 3])
                    if sai > 0 and str(sai) not in s and sai != kq_num:
                        s.append(str(sai))

                das1 = '$%s$' % (s[0])
                das2 = '$%s$' % (s[1])
                das3 = '$%s$' % (s[2])

                # Bước 4: Nội dung câu hỏi (không dùng tiền tố r)
                noidungcauhoi = ('''Sau khi một loại thuốc kháng sinh được tiêm vào cơ thể thì nồng độ của thuốc trong máu sẽ giảm dần theo thời gian do quá trình chuyển hóa. Nồng độ thuốc trong máu sau $t$ giờ kể từ khi tiêm được mô hình hóa bởi công thức $C\\left( t \\right) = C_0 \\cdot e^{-rt}$ (mg/lít). Trong đó:
            \\\\+ $C_0$ là nồng độ thuốc trong máu ngay sau khi tiêm.
            \\\\+ $r$ là hằng số dương đo tốc độ phân hủy của thuốc.
            \\\\+ $e \\approx 2,718$.
            \\\\Biết rằng ngay sau khi tiêm, nồng độ thuốc trong máu là $%s$ mg/lít và sau đó $%s$ giờ nồng độ thuốc giảm còn $%s$ mg/lít. Để đạt hiệu quả điều trị, bác sĩ sẽ tiêm lại một liều mới khi nồng độ thuốc trong máu của bệnh nhân giảm xuống và còn ít nhất $%s$ mg/lít. Theo mô hình trên, để đạt hiệu quả điều trị thì khoảng thời gian nhiều nhất giữa hai lần tiêm thuốc là bao nhiêu giờ (kết quả làm tròn đến hàng đơn vị)?'''
                                 % (latex(c0), latex(t1), latex(c1), latex(c_min)))

                # Bước 5: Nội dung lời giải chi tiết
                # Chuyển đổi số thập phân sang dấu phẩy cho hiển thị
                t_res_str = ('%.2f' % t_res).replace('.', ',')

                loigiai = ('''Theo giả thiết, ta có $C_0 = %s$ mg/lít. \\\\
            Nồng độ thuốc tại thời điểm $t = %s$ là $C\\left( %s \\right) = %s \\cdot e^{-r \\cdot %s} = %s$. \\\\
            $\\Rightarrow e^{-%sr} = \\frac{%s}{%s} \\Rightarrow -%sr = \\ln \\left( \\frac{%s}{%s} \\right) \\Rightarrow r = -\\frac{1}{%s} \\ln \\left( \\frac{%s}{%s} \\right) = \\frac{1}{%s} \\ln \\left( \\frac{%s}{%s} \\right)$. \\\\
            Để đạt hiệu quả điều trị, ta cần nồng độ thuốc $C\\left( t \\right) \\ge %s$. \\\\
            $\\Rightarrow %s \\cdot e^{-rt} \\ge %s \\Rightarrow e^{-rt} \\ge \\frac{%s}{%s}$. \\\\
            $\\Rightarrow -rt \\ge \\ln \\left( \\frac{%s}{%s} \\right) \\Rightarrow t \\le -\\frac{1}{r} \\ln \\left( \\frac{%s}{%s} \\right) = \\frac{\\ln \\left( \\frac{%s}{%s} \\right)}{r}$. \\\\
            Thay số ta được: $t \\le \\frac{\\ln \\left( \\frac{%s}{%s} \\right)}{\\frac{1}{%s} \\ln \\left( \\frac{%s}{%s} \\right)} = %s \\cdot \\frac{\\ln \\left( %s \\right)}{\\ln \\left( %s \\right)} \\approx %s$ (giờ). \\\\
            Làm tròn đến hàng đơn vị, ta được kết quả là $%s$ giờ.'''
                           % (latex(c0), latex(t1), latex(t1), latex(c0), latex(t1), latex(c1),
                              latex(t1), latex(c1), latex(c0), latex(t1), latex(c1), latex(c0), latex(t1), latex(c1), latex(c0), latex(t1), latex(c0), latex(c1),
                              latex(c_min), latex(c0), latex(c_min), latex(c_min), latex(c0),
                              latex(c_min), latex(c0), latex(c_min), latex(c0), latex(c0), latex(c_min),
                              latex(c0), latex(c_min), latex(t1), latex(c0), latex(c1), latex(t1), ('%.2f' % (c0/c_min)).replace('.',','), ('%.2f' % (c0/c1)).replace('.',','), t_res_str,
                              latex(kq_num)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
                # Bước 6: Xuất câu trắc nghiệm
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content 

