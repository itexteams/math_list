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


def bt_dang37_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Bước 1 & 3: Nghiên cứu đề bài và thiết lập cơ chế random
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tọa độ điểm A
                xA = randint(-3, 3)
                yA = randint(-3, 6)

                # Chọn hệ số a, b cố định để đảm bảo mẫu số triệt tiêu (độ dài vector pháp tuyến bằng nhau)
                a, b = 2, 1 

                # Đường thẳng AC: a(x - xA) + b(y - yA) = 0 => ax + by + c1 = 0
                c1 = -a*xA - b*yA
                f_AC = a*x + b*y + c1

                # Đường thẳng AB: a(x - xA) - b(y - yA) = 0 => ax - by + c2 = 0
                c2 = -a*xA + b*yA
                f_AB = a*x - b*y + c2

                # Tìm điểm C trên AC và B trên AB
                k1 = random.choice([-2, -1, 1, 2, 3])
                k2 = random.choice([-2, -1, 1, 2, 3])

                # Tọa độ C
                xC, yC = xA + k1*b, yA - k1*a
                # Tọa độ B (Đã sửa lỗi yB -> yA ở đây)
                xB, yB = xA + k2*b, yA + k2*a

                # Hai đường phân giác: x - xA = 0 và y - yA = 0
                d1_expr = y - yA
                d2_expr = x - xA

                # Xét d1: Tính giá trị biểu thức tại B và C
                valB = d1_expr.subs({x: xB, y: yB})
                valC = d1_expr.subs({x: xC, y: yC})

                # Logic xác định trong/ngoài
                if valB * valC > 0:
                    pg_ngoai = "y - %s = 0" % (yA) if yA != 0 else "y = 0"
                    pg_trong = "x - %s = 0" % (xA) if xA != 0 else "x = 0"
                    loai_d1 = "phân giác ngoài"
                    loai_d2 = "phân giác trong"
                    tt_vi_tri = "cùng"
                else:
                    pg_trong = "y - %s = 0" % (yA) if yA != 0 else "y = 0"
                    pg_ngoai = "x - %s = 0" % (xA) if xA != 0 else "x = 0"
                    loai_d1 = "phân giác trong"
                    loai_d2 = "phân giác ngoài"
                    tt_vi_tri = "khác"

                # Làm đẹp chuỗi hiển thị
                def clean_str(s):
                    return s.replace("- -", "+ ").replace(" - 0", "").replace("+ -", "- ")

                pg_trong = clean_str(pg_trong)
                pg_ngoai = clean_str(pg_ngoai)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có $A(%s; %s)$, $B(%s; %s)$ và $C(%s; %s)$. Lập phương trình đường phân giác trong và phân giác ngoài của góc $A$.'''
                                 % (latex(xA), latex(yA), latex(xB), latex(yB), latex(xC), latex(yC)))

                da_dung = '$%s$ và $%s$' % (pg_trong, pg_ngoai)
                s1 = '$%s$ và $%s$' % (pg_ngoai, pg_trong)
                s2 = '$x + %s = 0$ và $y + %s = 0$' % (latex(xA+2), latex(yA-1))
                s3 = '$x - %s = 0$ và $y + %s = 0$' % (latex(xA+1), latex(yA))

                list_1 = ['\\True ' + da_dung, s1, s2, s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                str_AC = latex(f_AC).replace('1 y', 'y').replace('1*y', 'y')
                str_AB = latex(f_AB).replace('1 y', 'y').replace('1*y', 'y')
                mau_so = latex(a**2 + b**2)

                loigiai = ('''Đường thẳng $AC$ đi qua hai điểm $A, C$ nên $AC$ có phương trình $%s = 0$. \\\\
            Tương tự $AB: %s = 0$. \\\\
            Phương trình đường phân giác góc $A$ là: \\\\
            $\\frac{|%s|}{\\sqrt{%s}} = \\frac{|%s|}{\\sqrt{%s}} \\Leftrightarrow \\left[\\begin{array}{l} %s = 0 \\\\ %s = 0 \\end{array}\\right.$. \\\\
            Xét phân giác $d_1: %s = 0$. Ta có \\\\
            $P(B; d_1) = %s, P(C; d_1) = %s$ nên suy ra $B$ và $C$ nằm %s phía đối với $d_1$, suy ra $d_1$ là %s. \\\\
            Từ đó suy ra $d_2: %s = 0$ là %s góc $A$.'''
                           % (str_AC, str_AB, str_AC, mau_so, str_AB, mau_so,
                              latex(d1_expr), latex(d2_expr), latex(d1_expr),
                              latex(valB), latex(valC), tt_vi_tri, loai_d1,
                              latex(d2_expr), loai_d2))

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+').replace('+ -', '-')
            return content 

