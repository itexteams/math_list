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


def bt_dang12_p3_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn số mặt xúc xắc (6, 12, 18, 24, 30)
                sides = random.choice([6, 12, 18, 24, 30])
                # Chọn bội của k (k thường là 2, 3, 4)
                k = random.choice([2, 3, 4])

                # Tính toán xác suất
                p_ngua = Rational(1, 2)

                # Số các kết quả thuận lợi cho biến cố C (mặt là bội của k)
                n_C = sides // k
                p_C = Rational(n_C, sides) 

                # Xác suất biến cố giao AC
                p_AC_val = p_ngua * p_C

                # Làm tròn đến hàng phần mười theo quy tắc ROUND_HALF_UP
                kq_float = float(p_AC_val)
                kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Định dạng hiển thị số thập phân dùng dấu phẩy
                kq_str = str(kq_decimal).replace('.', ',')

                # Đáp án đúng
                da = '$%s$' % (kq_str)

                # B4: Điều chỉnh các phương án sai
                s = []
                while len(s) < 3:
                    sai_so = random.choice([-0.2, -0.1, 0.1, 0.2, 0.3])
                    val_sai = float(kq_decimal) + sai_so
                    val_sai = round(max(0.1, val_sai), 1)
                    val_sai_str = str(val_sai).replace('.', ',')

                    opt = '$%s$' % (val_sai_str)
                    if opt != da and opt not in s:
                        s.append(opt)

                das1, das2, das3 = s

                # B2: Viết lại nội dung câu hỏi
                noidungcauhoi = ('''Tung đồng thời một đồng xu và một cục xúc xắc $%s$ mặt $\\left(1 \\text{đến} %s\\right)$. Xác suất xuất hiện mặt ngửa và mặt là bội của $%s$ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần mười).'''
                                 % (latex(sides), latex(sides), latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                boi_list = [i for i in range(1, sides + 1) if i % k == 0]
                boi_str = ", ".join(map(str, boi_list))

                loigiai = ('''Xác suất xuất hiện mặt ngửa là $P\\left(A\\right) = \\frac{1}{2}$. \\\\
                             Gọi $C$ là biến cố "Xúc xắc xuất hiện mặt là bội của $%s$". \\\\
                             Các mặt là bội của $%s$ trong tập hợp từ $1$ đến $%s$ là: $\\left\\{%s\\right\\}$. \\\\
                             Số kết quả thuận lợi cho $C$ là $%s$, do đó $P\\left(C\\right) = \\frac{%s}{%s} = \\frac{%s}{%s}$. \\\\
                             Vì việc tung đồng xu và xúc xắc là độc lập nên xác suất xuất hiện mặt ngửa và mặt là bội của $%s$ là: \\\\
                             $P\\left(AC\\right) = P\\left(A\\right) \\cdot P\\left(C\\right) = \\frac{1}{2} \\cdot \\frac{%s}{%s} = \\frac{%s}{%s} \\approx %s$.'''
                           % (latex(k), latex(k), latex(sides), boi_str,
                              latex(n_C), latex(n_C), latex(sides), latex(p_C.p), latex(p_C.q),
                              latex(k), latex(p_C.p), latex(p_C.q), latex(p_AC_val.p), latex(p_AC_val.q), kq_str))
                dapan=' \\shortans[0]{$%s$} '%(kq_str) 
            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

