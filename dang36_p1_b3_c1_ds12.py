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


def bt_dang36_p1_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Hàm số có dạng y = (\sqrt{x + b^2} - b) / (x^2 + c*x)
                # Nghiệm x = 0 luôn làm tử và mẫu bằng 0 (triệt tiêu nhân tử x, không là TCĐ)
                # Nghiệm x = -c là một nghiệm khác của mẫu, nằm trong TXĐ và không là nghiệm của tử (là TCĐ)

                b = randint(2, 4)
                a = b**2

                # Chọn nghiệm thứ hai x2 sao cho x2 nằm trong tập xác định và khác 0
                x2_choices = [i for i in range(-a + 2, 5) if i != 0]
                x2 = random.choice(x2_choices)
                c = -x2

                # Biểu diễn chuỗi các đại lượng dưới dạng latex
                str_num = "\\sqrt{x + %s} - %s" % (a, b)

                if c == 1:
                    str_den = "x^2 + x"
                elif c == -1:
                    str_den = "x^2 - x"
                elif c > 0:
                    str_den = "x^2 + %sx" % c
                else:
                    str_den = "x^2 - %sx" % abs(c)

                if x2 > 0:
                    str_den_fact = "x(x - %s)" % x2
                    str_x_minus_x2 = "x - %s" % x2
                else:
                    str_den_fact = "x(x + %s)" % abs(x2)
                    str_x_minus_x2 = "x + %s" % abs(x2)

                str_minus_x2 = latex(-x2)
                str_2b = latex(2*b)
                str_fraction_res = latex(Rational(1, -x2 * 2 * b))

                # Kết quả số tiệm cận đứng luôn luôn bằng 1
                kq = 1

                # Các đáp án trắc nghiệm
                da = '$1$'

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                options = [0, 2, 3]
                random.shuffle(options)

                das1 = '$%s$' % options[0]
                das2 = '$%s$' % options[1]
                das3 = '$%s$' % options[2]

                # Câu hỏi
                noidungcauhoi = ('''Số tiệm cận đứng của đồ thị hàm số $y = \\frac{%s}{%s}$ là''' % (str_num, str_den))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước theo bài mẫu
                loigiai = ('''Hàm số xác định khi và chỉ khi: \\\\
            $\\left\\{ \\begin{array}{l} x + %s \\ge 0 \\\\ %s \\neq 0 \\end{array} \\right. \\Leftrightarrow \\left\\{ \\begin{array}{l} x \\ge -%s \\\\ x \\neq 0 \\\\ x \\neq %s \\end{array} \\right.$. \\\\
            Tập xác định của hàm số là $D = [-%s; +\\infty) \\setminus \\{0; %s\\} $. \\\\
            Ta xét giới hạn của hàm số tại các điểm làm cho mẫu số bằng $0$: \\\\
            + Tại $x = 0$: \\\\
            $\\lim\\limits_{x \\to 0} y = \\lim\\limits_{x \\to 0} \\frac{\\sqrt{x + %s} - %s}{%s} = \\lim\\limits_{x \\to 0} \\frac{(\\sqrt{x + %s} - %s)(\\sqrt{x + %s} + %s)}{%s(\\sqrt{x + %s} + %s)}$ \\\\
            $= \\lim\\limits_{x \\to 0} \\frac{x}{%s(\\sqrt{x + %s} + %s)} = \\lim\\limits_{x \\to 0} \\frac{1}{(%s)(\\sqrt{x + %s} + %s)} = \\frac{1}{%s \\cdot %s} = %s$. \\\\
            Vì giới hạn là một số thực hữu hạn nên đường thẳng $x = 0$ không phải là tiệm cận đứng của đồ thị hàm số. \\\\
            + Tại $x = %s$: \\\\
            $\\lim\\limits_{x \\to %s} y = \\lim\\limits_{x \\to %s} \\frac{\\sqrt{x + %s} - %s}{%s} = \\infty$ (do tử số tiến về $\\sqrt{%s + %s} - %s \\neq 0$ và mẫu số tiến về $0$). \\\\
            Do đó, đường thẳng $x = %s$ là tiệm cận đứng của đồ thị hàm số. \\\\
            Vậy đồ thị hàm số đã cho có đúng $1$ tiệm cận đứng.''' % (
                    a, str_den, a, x2,
                    a, x2,
                    a, b, str_den, a, b, a, b, str_den_fact, a, b,
                    str_den_fact, a, b, str_x_minus_x2, a, b, str_minus_x2, str_2b, str_fraction_res,
                    x2, x2, x2, a, b, str_den, x2, a, b,
                    x2
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

