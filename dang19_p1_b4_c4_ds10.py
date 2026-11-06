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


def bt_dang19_p1_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random giá trị t0 là nghiệm dương của phương trình theo t
                # Trong ảnh gốc t0 = 2. Ta có thể chọn t0 từ 2 đến 5 để số không quá lớn.
                t0 = random.randint(2, 5)

                # Biến đổi: 2x^2 + 2x - (sqrt(x^2+x-1) + 1) = C
                # Đặt t = sqrt(x^2 + x - 1) => x^2 + x = t^2 + 1
                # Phương trình trở thành: 2(t^2 + 1) - (t + 1) = C
                # => 2t^2 - t + 1 - C = 0. Để có nghiệm t0, C = 2*t0^2 - t0 + 1
                C = 2 * t0**2 - t0 + 1

                # Tính toán kết quả cuối cùng (Tổng bình phương nghiệm)
                # Phương trình x^2 + x - 1 = t0^2 => x^2 + x - (t0^2 + 1) = 0
                # Theo Vi-et: S = -1, P = -(t0^2 + 1)
                # Tổng bình phương = S^2 - 2P = (-1)^2 - 2*(-(t0^2 + 1)) = 1 + 2*t0^2 + 2 = 2*t0^2 + 3
                kq_val = 2 * t0**2 + 3
                da = '$%s$' % (latex(kq_val))

                # Tạo các đáp án sai
                s = set()
                while len(s) < 3:
                    sai = kq_val + random.choice([-2, -1, 1, 2, 3, 4, 5, 10])
                    if sai != kq_val and sai > 0:
                        s.add('$%s$' % (latex(sai)))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Tổng bình phương các nghiệm của phương trình $2x^2 + 2x - \\sqrt{x^2 + x + 2\\sqrt{x^2 + x - 1}} = %s$ là'''
                                 % (latex(C)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Nghiệm t thứ 2: t1 = (1 - 2*t0)/2 luôn âm
                t_phu = Rational(1 - 2*t0, 2)

                loigiai = ('''Biến đổi phương trình:
                             $2x^2 + 2x - \\sqrt{(\\sqrt{x^2 + x - 1} + 1)^2} = %s$ \\\\
                             $\\Leftrightarrow 2x^2 + 2x - (\\sqrt{x^2 + x - 1} + 1) = %s$ \\\\
                             $\\Leftrightarrow 2x^2 + 2x - \\sqrt{x^2 + x - 1} - %s = 0$. \\\\
                             Đặt $t = \\sqrt{x^2 + x - 1} \\ge 0 \\Leftrightarrow 2x^2 + 2x = 2(t^2 + 1)$. \\\\
                             Phương trình trở thành: $2t^2 - t - %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & t = %s (tm) \\\\ & t = %s (loại) \\end{aligned} \\right.$. \\\\
                             Với $t = %s$: $x^2 + x - 1 = %s \\Leftrightarrow x^2 + x - %s = 0$. \\\\
                             Áp dụng định lý Vi-ét ta có: $\\begin{cases} S = -1 \\\\ P = -%s \\end{cases} \\Rightarrow x_1^2 + x_2^2 = S^2 - 2P = 1 + 2 \\cdot %s = %s$.'''
                           % (latex(C), latex(C), latex(C + 1), latex(C - 1), latex(t0), latex(t_phu), 
                              latex(t0), latex(t0**2), latex(t0**2 + 1), latex(t0**2 + 1), latex(t0**2 + 1), latex(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

