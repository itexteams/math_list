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


def bt_dang20_p4_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp tìm bộ số ngẫu nhiên thỏa mãn lời giải đẹp và kết quả nguyên
                while True:
                    P0 = randint(10, 50)  # Số lượng tế bào ban đầu
                    V0 = randint(5, 30)   # Tốc độ tăng ban đầu

                    # Điều kiện để mô hình tăng trưởng hợp lý (b > 0 với k = 0,75)
                    if 3 * P0 > 4 * V0:
                        # Kiểm tra b và kết quả giới hạn L có phải là số đẹp không
                        if (3 * P0 * 100) % (4 * V0) == 0:  # b là số thập phân hữu hạn đẹp
                            num_L = 3 * P0 * P0
                            den_L = 3 * P0 - 4 * V0
                            if num_L % den_L == 0:  # Kết quả giới hạn là số nguyên
                                L = num_L // den_L
                                b_fraction = Rational(3 * P0, 4 * V0) - 1
                                a_fraction = P0 * (b_fraction + 1)
                                break

                # Chuyển đổi các giá trị số sang chuỗi định dạng dấu phẩy theo đúng quy định
                b_str = str(float(b_fraction)).replace('.', ',')
                if b_str.endswith(',0'):
                    b_str = b_str[:-2]

                b_plus_1_str = str(float(b_fraction + 1)).replace('.', ',')
                if b_plus_1_str.endswith(',0'):
                    b_plus_1_str = b_plus_1_str[:-2]

                a_str = str(float(a_fraction)).replace('.', ',')
                if a_str.endswith(',0'):
                    a_str = a_str[:-2]

                # Đáp án đúng
                da = '$%s$' % (latex(L))

                # Tạo danh sách các đáp án nhiễu logic
                s = [
                    '$%s$' % (latex(L + 20)),
                    '$%s$' % (latex(L - 20 if L > 20 else L + 40)),
                    '$%s$' % (latex(L + 50)),
                    '$%s$' % (latex(L - 50 if L > 50 else L + 60)),
                    '$%s$' % (latex(P0 * 4)),
                    '$%s$' % (latex(V0 * 10))
                ]

                # Xóa trùng và xóa đáp án đúng ra khỏi danh sách nhiễu
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Giả sử số lượng của một quần thể nấm men tại môi trường nuôi cấy trong phòng thí nghiệm được mô hình hoá bằng hàm số $P(t) = \\frac{a}{b + e^{-0,75t}}$, trong đó thời gian $t$ được tính bằng giờ. Tại thời điểm ban đầu $t = 0$, quần thể có $%s$ tế bào và tăng với tốc độ $%s$ tế bào/giờ. Theo mô hình này tính số lượng nấm men tối đa có thể có.'''
                                 % (latex(P0), latex(V0)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước
                loigiai = ('''Từ công thức mô hình hoá, tại thời điểm ban đầu $t = 0$, số lượng tế bào của quần thể là $%s$ nên ta có:\\\\
            $P(0) = \\frac{a}{b + e^0} = \\frac{a}{b + 1} = %s \\implies a = %s(b + 1)$ (1).\\\\
            Tốc độ tăng trưởng của quần thể nấm men tại thời điểm $t$ là đạo hàm bậc nhất của hàm số $P(t)$:\\\\
            $P'(t) = \\left(\\frac{a}{b + e^{-0,75t}}\\right)' = \\frac{-a \\cdot (b + e^{-0,75t})'}{(b + e^{-0,75t})^2} = \\frac{0,75a \\cdot e^{-0,75t}}{(b + e^{-0,75t})^2}$.\\\\
            Tại thời điểm ban đầu $t = 0$, tốc độ tăng trưởng của quần thể là $%s$ tế bào/giờ nên ta có:\\\\
            $P'(0) = \\frac{0,75a \\cdot e^0}{(b + e^0)^2} = \\frac{0,75a}{(b + 1)^2} = %s$ (2).\\\\
            Thay (1) vào (2), ta được:\\\\
            $\\frac{0,75 \\cdot %s(b + 1)}{(b + 1)^2} = \\frac{0,75 \\cdot %s}{b + 1} = %s \\implies b + 1 = \\frac{0,75 \\cdot %s}{%s} = %s \\implies b = %s$.\\\\
            Từ đó, ta tìm được $a = %s \\cdot (b + 1) = %s \\cdot %s = %s$.\\\\
            Khi đó, hàm số mô tả quần thể nấm men là $P(t) = \\frac{%s}{%s + e^{-0,75t}}$.\\\\
            Vì $e^{-0,75t} > 0$ với mọi $t$ nên $%s + e^{-0,75t} > %s$, suy ra:\\\\
            $P(t) = \\frac{%s}{%s + e^{-0,75t}} < \\frac{%s}{%s} = %s$.\\\\
            Mặt khác, khi $t \\to +\\infty$, ta có $e^{-0,75t} \\to 0$, do đó:\\\\
            $\\lim_{t \\to +\\infty} P(t) = \\lim_{t \\to +\\infty} \\frac{%s}{%s + e^{-0,75t}} = \\frac{%s}{%s} = %s$.\\\\
            Vậy theo mô hình này, số lượng nấm men không vượt quá $%s$ con.'''
                           % (latex(P0), latex(P0), latex(P0),
                              latex(V0), latex(V0),
                              latex(P0), latex(P0), latex(V0), latex(P0), latex(V0), b_plus_1_str, b_str,
                              latex(P0), latex(P0), b_plus_1_str, a_str,
                              a_str, b_str,
                              b_str, b_str,
                              a_str, b_str, a_str, b_str, latex(L),
                              a_str, b_str, a_str, b_str, latex(L),
                              latex(L)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

