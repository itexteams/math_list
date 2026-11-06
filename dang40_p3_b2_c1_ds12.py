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


def bt_dang40_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tập dữ liệu cấu hình sẵn để đảm bảo nghiệm x_val luôn nguyên và đẹp
                # Cấu trúc: a, b, C_1, M (sản lượng tối đa), C_0 (chi phí cố định), tax_rate (thuế %), T (1 - tax), Ta, Tb, c3, c4, x2, x_val, P_max
                data_list = [
                    {'a': 80, 'b': 0.015, 'C_1': 7.2, 'M': 68, 'C_0': 100, 'tax_rate': 10, 'T': 0.9, 'Ta': 72, 'Tb': 0.0135, 'c3': 64.8, 'c4': 0.0405, 'x2': 1600, 'x_val': 40, 'P_max': 1628},
                    {'a': 120, 'b': 0.015, 'C_1': 6.75, 'M': 80, 'C_0': 150, 'tax_rate': 10, 'T': 0.9, 'Ta': 108, 'Tb': 0.0135, 'c3': 101.25, 'c4': 0.0405, 'x2': 2500, 'x_val': 50, 'P_max': 3225},
                    {'a': 50, 'b': 0.015, 'C_1': 8.55, 'M': 55, 'C_0': 80, 'tax_rate': 10, 'T': 0.9, 'Ta': 45, 'Tb': 0.0135, 'c3': 36.45, 'c4': 0.0405, 'x2': 900, 'x_val': 30, 'P_max': 649}
                ]

                # Chọn ngẫu nhiên một bộ số
                d = random.choice(data_list)

                # Định dạng lại các số có dấu thập phân bằng dấu phẩy
                a = str(d['a']).replace('.', ',')
                b = str(d['b']).replace('.', ',')
                C_1 = str(d['C_1']).replace('.', ',')
                M = str(d['M'])
                C_0 = str(d['C_0'])
                tax_rate = str(d['tax_rate'])
                T = str(d['T']).replace('.', ',')
                Ta = str(d['Ta']).replace('.', ',')
                Tb = str(d['Tb']).replace('.', ',')
                c3 = str(d['c3']).replace('.', ',')
                c4 = str(d['c4']).replace('.', ',')
                x2 = str(d['x2'])
                x_val = str(d['x_val'])
                P_max = str(d['P_max']).replace('.', ',')
                P_max_val = d['P_max']

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (P_max)]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên không trùng với đáp án đúng
                s = [
                    '$%s$' % (str(P_max_val + 120).replace('.', ',')),
                    '$%s$' % (str(P_max_val - 100).replace('.', ',')),
                    '$%s$' % (str(P_max_val + 240).replace('.', ',')),
                    '$%s$' % (str(P_max_val - 200).replace('.', ',')),
                    '$%s$' % (str(P_max_val + 310).replace('.', ',')),
                    '$%s$' % (str(P_max_val - 50).replace('.', ','))
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Nhà máy A chuyên sản xuất một loại sản phẩm cho nhà máy B. Hai nhà máy thỏa thuận rằng, hàng tháng nhà máy A cung cấp cho nhà máy B số lượng sản phẩm theo đơn đặt hàng của nhà máy B (tối đa $%s$ tấn sản phẩm). Nếu số lượng đặt hàng là $x$ tấn sản phẩm thì giá bán cho mỗi tấn sản phẩm là $p\\left(x\\right)=%s-%sx^2$ (đơn vị triệu đồng). Chi phí để nhà máy A sản xuất $x$ tấn sản phẩm trong một tháng là $C\\left(x\\right)=%s+%sx$ (đơn vị triệu đồng), thuế giá trị gia tăng mà nhà máy A phải đóng cho nhà nước là $%s\\%%$ tổng doanh thu mỗi tháng. Hỏi mỗi tháng nhà máy A thu được lợi nhuận cao nhất là bao nhiêu triệu đồng (sau khi đã trừ thuế giá trị gia tăng)?'''
                                 % (M, a, b, C_0, C_1, tax_rate))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Doanh thu mỗi tháng của nhà máy A khi bán $x$ tấn sản phẩm là:\\\\ 
                $R\\left(x\\right) = x \\cdot p\\left(x\\right) = x\\left(%s - %sx^2\\right) = %sx - %sx^3$ (triệu đồng).\\\\
                Vì thuế giá trị gia tăng là $%s\\%%$ tổng doanh thu nên doanh thu thực tế nhà máy A nhận được là:\\\\
                $R_1\\left(x\\right) = R\\left(x\\right) \\cdot \\left(1 - \\frac{%s}{100}\\right) = %s \\cdot \\left(%sx - %sx^3\\right) = %sx - %sx^3$ (triệu đồng).\\\\
                Lợi nhuận nhà máy A thu được mỗi tháng là:\\\\
                $P\\left(x\\right) = R_1\\left(x\\right) - C\\left(x\\right) = \\left(%sx - %sx^3\\right) - \\left(%s + %sx\\right) = -%sx^3 + %sx - %s$ (triệu đồng).\\\\
                Xét hàm số $P\\left(x\\right) = -%sx^3 + %sx - %s$ với $0 < x \\le %s$.\\\\
                Đạo hàm $P'\\left(x\\right) = -%sx^2 + %s$. \\\\
                Cho $P'\\left(x\\right) = 0 \\Leftrightarrow -%sx^2 + %s = 0 \\Leftrightarrow x^2 = %s \\Rightarrow x = %s$ (do $x > 0$).\\\\
                Bảng biến thiên cho thấy hàm số $P\\left(x\\right)$ đạt giá trị lớn nhất tại $x = %s$ (thỏa mãn điều kiện).\\\\
                Vậy lợi nhuận cao nhất mỗi tháng nhà máy A thu được là $%s$ triệu đồng.'''
                % (a, b, a, b, 
                   tax_rate, tax_rate, T, a, b, Ta, Tb,
                   Ta, Tb, C_0, C_1, Tb, c3, C_0,
                   Tb, c3, C_0, M,
                   c4, c3,
                   c4, c3, x2, x_val,
                   x_val,
                   P_max))
                dapan='\\shortans[0]{$%s$}\n'%(P_max)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

