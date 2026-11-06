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


def bt_dang27_p4_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp tìm bộ số ngẫu nhiên thỏa mãn đồ thị có tiệm cận đứng và xiên đẹp
                while True:
                    A = random.choice([1, 2, 3, 4])
                    B = randint(-5, 5)
                    C = randint(-10, 10)
                    D = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])

                    # Phần dư của phép chia tử số cho mẫu số x + D chính là giá trị tử số tại x = -D
                    rem = A * (-D)**2 + B * (-D) + C
                    if rem != 0:
                        x0 = -D
                        y0 = A * (-D) + B - A * D
                        kq_val = x0 + y0
                        break

                # Đáp án đúng
                da = '$%s$' % (latex(kq_val))

                # Tạo danh sách các đáp án nhiễu logic
                s = [
                    '$%s$' % (latex(y0)),
                    '$%s$' % (latex(x0 - y0)),
                    '$%s$' % (latex(D + A * D + B - A * D)),
                    '$%s$' % (latex(kq_val + 2)),
                    '$%s$' % (latex(kq_val - 2)),
                    '$%s$' % (latex(kq_val + 5)),
                    '$%s$' % (latex(kq_val - 5))
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
                noidungcauhoi = ('''Biết giao điểm đường tiệm cận xiên và tiệm cận đứng của đồ thị hàm số $y = \\frac{%s}{%s}$ là $(x_0; y_0)$. Tính $x_0 + y_0$.'''
                                 % (latex(A*x**2 + B*x + C), latex(x + D)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                B_minus_AD = B - A * D
                linear_part = A * x + B_minus_AD
                loigiai = ('''Đồ thị hàm số $y = \\frac{%s}{%s}$ có:\\\\
            - Tiệm cận đứng: Mẫu số bằng $0 \\iff %s = 0 \\iff x = %s$. Do đó, giao điểm có hoành độ $x_0 = %s$.\\\\
            - Tiệm cận xiên: Thực hiện phép chia đa thức ở tử số cho mẫu số, ta biến đổi hàm số về dạng:\\\\
            $$y = %s + \\frac{%s}{%s}$$
            Vì $\\lim_{x \\to \\pm\\infty} \\frac{%s}{%s} = 0$ nên đường tiệm cận xiên của đồ thị hàm số là $y = %s$.\\\\
            Giao điểm $(x_0; y_0)$ của hai đường tiệm cận là nghiệm của hệ phương trình gồm đường tiệm cận đứng và tiệm cận xiên:\\\\
            $$\\begin{cases} x = %s \\\\ y = %s \\end{cases} \\implies \\begin{cases} x_0 = %s \\\\ y_0 = %s \\end{cases}$$\\\\
            Thay giá trị hoành độ và tung độ vừa tìm được vào biểu thức, ta tính được:\\\\
            $x_0 + y_0 = %s + (%s) = %s$.'''
                           % (latex(A*x**2 + B*x + C), latex(x + D),
                              latex(x + D), latex(x0), latex(x0),
                              latex(linear_part), latex(rem), latex(x + D),
                              latex(rem), latex(x + D), latex(linear_part),
                              latex(x0), latex(linear_part), latex(x0), latex(y0),
                              latex(x0), latex(y0), latex(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

