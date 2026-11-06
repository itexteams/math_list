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


def bt_dang19_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các tỷ lệ thành phần sao cho tổng bằng 100%
                # p1: hút thuốc và mắc bệnh
                # p2: hút thuốc và không mắc bệnh
                # p4: không hút thuốc và mắc bệnh
                # p3: không hút thuốc và không mắc bệnh

                p1 = randint(12, 18)  # Ví dụ: 15%
                p2 = randint(22, 28)  # Ví dụ: 25%
                p4 = randint(8, 12)   # Ví dụ: 10%
                p3 = 100 - p1 - p2 - p4 # Phần còn lại (Ví dụ: 50%)

                # Tính toán theo logic của hình ảnh
                # Xác suất mắc bệnh P(B)
                pb_val = p1 + p4
                pb_rational = Rational(pb_val, 100)

                # P(A|B) = P(A n B) / P(B)
                pa_b_num = Rational(p1, 100)
                pa_b_val = float(pa_b_num / pb_rational)

                # P(not A|B) = P(not A n B) / P(B)
                pnot_a_b_num = Rational(p4, 100)
                pnot_a_b_val = float(pnot_a_b_num / pb_rational)

                # Tỉ lệ cuối cùng = P(A|B) / P(not A|B) = p1 / p4
                res_val = p1 / p4

                # Làm tròn đến hàng phần chục (0.1)
                kq_dec = Decimal(float(res_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                while len(s) < 3:
                    sai = float(kq_dec) + random.choice([-0.5, 0.5, 1.0, -1.0, 0.2, -0.2, 0.8])
                    sai_str = '$%s$' % (str(Decimal(sai).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','))
                    if sai_str != '$%s$' % (kq) and sai_str not in s:
                        s.append(sai_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Điều tra tình hình mắc bệnh ung thư phổi của một vùng thấy tỉ lệ người hút thuốc lá và mắc bệnh là $%s\\%%$. Tỉ lệ người hút thuốc lá và không mắc bệnh là $%s\\%%$, tỉ lệ người không hút thuốc lá và không mắc bệnh là $%s\\%%$ và $%s\\%%$ là người không hút thuốc nhưng mắc bệnh. Tỉ lệ mắc bệnh ung thư phổi giữa người hút thuốc lá và không hút thuốc lá là bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % (latex(p1), latex(p2), latex(p3), latex(p4)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi biến cố $A$: "Người hút thuốc" \\\\
                             $B$: "Bị mắc bệnh ung thư phổi" \\\\
                             Theo đề bài ta có: \\\\
                             $P(A \\cap B) = %s$; $P(A \\cap \\overline{B}) = %s$; $P(\\overline{A} \\cap \\overline{B}) = %s$; $P(\\overline{A} \\cap B) = %s$. \\\\
                             Suy ra: $P(B) = P(A \\cap B) + P(\\overline{A} \\cap B) = %s + %s = %s$. \\\\
                             Xác suất người đó hút thuốc lá biết họ mắc bệnh ung thư phổi là: \\\\
                             $P(A | B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{%s}{%s} = %s$. \\\\
                             Xác suất người đó không hút thuốc lá biết họ mắc bệnh ung thư phổi là: \\\\
                             $P(\\overline{A} | B) = \\frac{P(\\overline{A} \\cap B)}{P(B)} = \\frac{%s}{%s} = %s$. \\\\
                             Vậy tỉ lệ mắc bệnh ung thư phổi giữa người hút thuốc lá và người không hút thuốc lá là \\\\
                             $\\frac{%s}{%s} \\approx %s$.'''
                           % (latex(p1/100), latex(p2/100), latex(p3/100), latex(p4/100),
                              latex(p1/100), latex(p4/100), latex(pb_val/100),
                              latex(p1/100), latex(pb_val/100), str(round(pa_b_val, 2)).replace('.', ','),
                              latex(p4/100), latex(pb_val/100), str(round(pnot_a_b_val, 2)).replace('.', ','),
                              str(round(pa_b_val, 2)).replace('.', ','), str(round(pnot_a_b_val, 2)).replace('.', ','), kq))
                dapan=' \\shortans[0]{$%s$} '%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

