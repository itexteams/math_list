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


def bt_dang25_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                s1_val = random.randint(1, 10)
                n_val = random.choice([50, 100, 150, 200])

                # Tính toán
                q_val = (3 + math.sqrt(5)) / 8
                sum_exact = s1_val * (2 * (5 + math.sqrt(5)) / 5)

                kq_dec = Decimal(float(sum_exact)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = ['$%s$' % (str(Decimal(float(sum_exact + 1.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                     '$%s$' % (str(Decimal(float(sum_exact + 2.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                     '$%s$' % (str(Decimal(float(sum_exact + 3.3)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                     '$%s$' % (str(Decimal(float(sum_exact - 1.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                     '$%s$' % (str(Decimal(float(sum_exact - 2.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                     '$%s$' % (str(Decimal(float(sum_exact - 0.5)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','))]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một ngũ giác đều $A_1B_1C_1D_1E_1$ có diện tích $S_1 = %s$ đơn vị diện tích. Nối $5$ trung điểm của $5$ cạnh liên tiếp ta được ngũ giác đều thứ hai là $A_2B_2C_2D_2E_2$ có diện tích $S_2$. Tiếp tục quá trình như thế ta được ngũ giác đều thứ ba có diện tích $S_3$ và cứ tiếp tục, ta được diện tích $S_4, S_5, \\dots$ Tổng $S = S_1 + S_2 + S_3 + \\dots + S_{%s}$ bằng bao nhiêu? (làm tròn đến hàng phần chục).
                                 \\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  (75,21.6) -- (131.49,62.64) -- (109.91,129.06) -- (40.09,129.06) -- (18.51,62.64) -- cycle ;
            		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  (225,21.6) -- (281.49,62.64) -- (259.91,129.06) -- (190.09,129.06) -- (168.51,62.64) -- cycle ;
            		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  (225,128.9) -- (179.44,95.8) -- (196.85,42.25) -- (253.15,42.25) -- (270.56,95.8) -- cycle ;
            		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  (375,21.6) -- (431.49,62.64) -- (409.91,129.06) -- (340.09,129.06) -- (318.51,62.64) -- cycle ;
            		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  (375,128.9) -- (329.44,95.8) -- (346.85,42.25) -- (403.15,42.25) -- (420.56,95.8) -- cycle ;
            		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  (375,42.4) -- (411.71,69.07) -- (397.69,112.23) -- (352.31,112.23) -- (338.29,69.07) -- cycle ;
            		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  (525.5,22.1) -- (581.99,63.14) -- (560.41,129.56) -- (490.59,129.56) -- (469.01,63.14) -- cycle ;
            		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  (525.5,129.4) -- (479.94,96.3) -- (497.35,42.75) -- (553.65,42.75) -- (571.06,96.3) -- cycle ;
            		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  (525.5,42.9) -- (562.21,69.57) -- (548.19,112.73) -- (502.81,112.73) -- (488.79,69.57) -- cycle ;
            		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  (525.5,112.4) -- (496.11,91.05) -- (507.34,56.5) -- (543.66,56.5) -- (554.89,91.05) -- cycle ;
            	\\end{tikzpicture}
            \\end{center}'''
                                 % (latex(s1_val), latex(n_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $a$ là độ dài cạnh của ngũ giác đều $A_1B_1C_1D_1E_1$. \\\\
                Góc trong của ngũ giác đều là $\\frac{(5-2)180^\\circ}{5} = 108^\\circ$. \\\\
                Nối các trung điểm ta cắt đi $5$ tam giác cân tại các đỉnh. Xét tam giác cân tại đỉnh $A_1$, nó có hai cạnh là $\\frac{a}{2}$ và góc xen giữa là $108^\\circ$. \\\\
                Diện tích $1$ tam giác nhỏ bị cắt đi là $S_{\\Delta} = \\frac{1}{2} \\cdot \\frac{a}{2} \\cdot \\frac{a}{2} \\cdot \\sin 108^\\circ = \\frac{a^2}{8} \\sin 108^\\circ$. \\\\
                Diện tích ngũ giác ban đầu là $S_1 = 5 \\cdot \\frac{1}{2} R^2 \\sin 72^\\circ$, có thể biểu diễn qua cạnh $a$ là: $S_1 = \\frac{5a^2}{4} \\cot 36^\\circ$. \\\\
                Tỉ số diện tích bị cắt đi so với ngũ giác ban đầu là: \\\\
                $\\frac{5 S_{\\Delta}}{S_1} = \\frac{\\frac{5a^2}{8} \\sin 108^\\circ}{\\frac{5a^2}{4} \\cot 36^\\circ} = \\frac{1}{2} \\sin 108^\\circ \\tan 36^\\circ = \\frac{1}{2} (2 \\sin 36^\\circ \\cos 36^\\circ) \\frac{\\sin 36^\\circ}{\\cos 36^\\circ} = \\sin^2 36^\\circ$. \\\\
                Ta có $\\sin^2 36^\\circ = 1 - \\cos^2 36^\\circ = 1 - \\left(\\frac{1+\\sqrt{5}}{4}\\right)^2 = 1 - \\frac{6+2\\sqrt{5}}{16} = \\frac{5-\\sqrt{5}}{8}$. \\\\
                Do đó, diện tích ngũ giác mới là $S_2 = S_1 - 5 S_{\\Delta} = S_1 \\left(1 - \\frac{5-\\sqrt{5}}{8}\\right) = S_1 \\cdot \\frac{3+\\sqrt{5}}{8}$. \\\\
                Các diện tích $S_1, S_2, S_3, \\dots$ tạo thành một cấp số nhân với số hạng đầu $S_1 = %s$ và công bội $q = \\frac{3+\\sqrt{5}}{8} \\approx 0,6545$. \\\\
                Tổng $n = %s$ số hạng đầu tiên là $S = S_1 \\frac{1 - q^{%s}}{1 - q}$. \\\\
                Vì $q \\approx 0,6545 < 1$ nên $q^{%s}$ rất nhỏ (gần tiến tới $0$), do đó $S \\approx \\frac{S_1}{1 - q} = \\frac{%s}{1 - \\frac{3+\\sqrt{5}}{8}} = %s \\cdot \\frac{8}{5-\\sqrt{5}} = \\frac{%s(5+\\sqrt{5})}{5}$. \\\\
                Thay số ta được $S \\approx %s$. \\\\
                Làm tròn đến hàng phần chục ta được kết quả là $%s$.'''
                           % (latex(s1_val), latex(n_val), latex(n_val), latex(n_val), latex(s1_val), latex(s1_val), latex(2 * s1_val), str(Decimal(float(sum_exact)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)).replace('.', ','), kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

