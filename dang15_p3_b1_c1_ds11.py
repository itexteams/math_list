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


def bt_dang15_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số của biểu thức A = M*tan(m*pi/2 - x) + N*cot(p*pi + x)
                M = randint(1, 5)
                N = randint(2, 6)

                # Sinh số lẻ m có dạng 4n + 1 để tan(m*pi/2 - x) = cot(x)
                n1 = randint(2, 5)
                m = 4 * n1 + 1

                # Sinh số lẻ p bất kỳ để cot(p*pi + x) = cot(x)
                p = 2 * randint(2, 5) + 1

                # Tính toán kết quả k_val = M + N
                k_val = M + N

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(k_val))]
                da = random.choice(du)

                # Tạo phương án nhiễu không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = k_val + randint(-4, 4)
                    if sai != k_val and sai != 0:
                        s.add('$%s$' % (latex(sai)))

                s = list(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Thiết lập hiển thị chuỗi hệ số cho đẹp mắt
                M_str = '' if M == 1 else latex(M)
                N_str = latex(N)

                # Câu hỏi
                noidungcauhoi = ('''Biểu thức $A = %s\\tan\\left(\\frac{%s\\pi}{2} - x\\right) + %s\\cot(%s\\pi + x) = k\\cot x$, giá trị của $k$ bằng bao nhiêu?'''
                                 % (M_str, latex(m), N_str, latex(p)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                m_chu_ky = 2 * n1
                p_chu_ky = p - 1
                loigiai = ('''Ta sử dụng các công thức góc liên kết để rút gọn từng thành phần trong biểu thức $A$: \\\\
                           + $\\tan\\left(\\frac{%s\\pi}{2} - x\\right) = \\tan\\left(%s\\pi + \\frac{\\pi}{2} - x\\right) = \\tan\\left(\\frac{\\pi}{2} - x\\right) = \\cot x$. \\\\
                           + Do hàm số $\\cot$ có chu kỳ tuần hoàn là $\\pi$ nên: $\\cot(%s\\pi + x) = \\cot(%s\\pi + x) = \\cot x$. \\\\
                           Thay vào biểu thức $A$, ta được: \\\\
                           $A = %s\\cot x + %s\\cot x = (%s + %s)\\cot x = %s\\cot x$. \\\\
                           Đối chiếu với giả thiết $A = k\\cot x$, ta suy ra $k = %s$.'''
                           % (latex(m), latex(m_chu_ky), latex(p), latex(p_chu_ky),
                              latex(M), latex(N), latex(M), latex(N), latex(k_val), latex(k_val)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(k_val))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

