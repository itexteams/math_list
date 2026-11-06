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


def bt_dang45_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random tham số bài toán
                # Chọn độ dài AB = k là một số nguyên từ 2 đến 10
                k = random.randint(2, 10)

                # Tính diện tích lớn nhất S_max = k^3 / 6
                kq_val = Rational(k**3, 6)
                da = '$%s$' % latex(kq_val)

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Tạo các giá trị sai quanh k^3/3, k^2/6, hoặc cộng trừ ngẫu nhiên
                    sai_val = random.choice([
                        Rational(k**3, 3), 
                        Rational(k**2, 6), 
                        Rational(k**3 + 6, 6),
                        Rational(k**3 - 3 if k**3 > 3 else 5, 6),
                        Rational(k**2, 2)
                    ])
                    if sai_val != kq_val:
                        s.add('$%s$' % latex(sai_val))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                noidungcauhoi = (r'''Cho parabol $(P): y=x^2$ và hai điểm $A, B$ thuộc $(P)$ sao cho $AB = %s$. Diện tích lớn nhất của hình phẳng giới hạn bởi $(P)$ và đường thẳng $AB$ là'''
                                 % (latex(k)))

                # Đáp án
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết lại y hệt logic hình ảnh nhưng với k biến thiên)
                # dx được thay bằng \text{d}x theo yêu cầu
                loigiai = (r'''Gọi phương trình đường thẳng $AB$ là: $y=ax+b$ ($a, b \in \mathbb{R}$). \\
                             Phương trình giao điểm của $AB$ và $(P)$ là: $x^2-ax-b=0$. \\
                             Để có $2$ điểm $A, B$ thì $a^2+4b > 0$. Khi đó: $\begin{cases} A(x_1; ax_1+b) \\ B(x_2; ax_2+b) \\ x_1+x_2=a \\ x_1x_2=-b \end{cases}$. \\
                             Nên $AB = %s \Leftrightarrow \sqrt{(a^2+1)}|x_2-x_1| = %s$. \\
                             Giả sử $x_2 > x_1$ ta có $|x_2-x_1| = \frac{%s}{\sqrt{a^2+1}} \le %s$. \\
                             Mặt khác: $|x_2-x_1| = \sqrt{(x_2+x_1)^2 - 4x_1x_2} = \sqrt{a^2+4b}$. \\
                             Khi đó $S = \int_{x_1}^{x_2} (ax+b-x^2) \text{d}x = \left[ \frac{a}{2}x^2 + bx - \frac{1}{3}x^3 \right]_{x_1}^{x_2}$ \\
                             $= (x_2-x_1) \left[ \frac{a}{2}(x_2+x_1) + b - \frac{1}{3}(x_2^2+x_1x_2+x_1^2) \right]$ \\
                             $= (x_2-x_1) \left[ \frac{a^2}{2} + b - \frac{1}{3}(a^2+b) \right] = (x_2-x_1) \frac{a^2+4b}{6}$ \\
                             $= \frac{(x_2-x_1)^3}{6} \le \frac{%s^3}{6} = %s$. \\
                             Suy ra: $S_{\max} = %s$ khi $a=0$.'''
                           % (latex(k), latex(k), latex(k), latex(k), latex(k), latex(kq_val), latex(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

