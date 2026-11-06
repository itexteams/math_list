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


def bt_dang38_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1 & 3: Nghiên cứu đề bài và Random các số để tạo nhiều câu hỏi khác nhau
                # Chọn n là số chẵn để kết quả cuối cùng (-1)^n luôn là 1 giống mẫu
                n = random.choice([10, 12, 14, 16, 18, 20, 22, 24])
                a = random.randint(2, 5)
                b = a + 1 # Để (a-b) = -1

                # Kết quả
                kq_val = (a - b)**n
                kq = str(kq_val).replace('.', ',')

                # Các đáp án trắc nghiệm
                da = '$%s$' % (kq)

                # Bước 4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s1 = '$%s^{%s}$' % (latex(a + b), latex(n))
                s2 = '$-%s^{%s}$' % (latex(a + b), latex(n))
                s3 = '$-1$' if kq_val == 1 else '$1$'

                # Trộn các phương án sai
                s = [s1, s2, s3]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (Sử dụng cấu trúc %s và định dạng LaTeX \left( \right))
                # Biểu thức K: a^n.C_n^0 - a^{n-1}.b.C_n^1 + ... - a.b^{n-1}.C_n^{n-1} + b^n.C_n^n
                noidungcauhoi = ('''Tính $K = %s^{%s} C_{%s}^0 - %s^{%s} \\cdot %s \\cdot C_{%s}^1 + %s^{%s} \\cdot %s^2 \\cdot C_{%s}^2 - \\dots - %s \\cdot %s^{%s} \\cdot C_{%s}^{%s-1} + %s^{%s} \\cdot C_{%s}^{%s}$.'''
                                 % (latex(a), latex(n), latex(n),
                                    latex(a), latex(n-1), latex(b), latex(n),
                                    latex(a), latex(n-2), latex(b), latex(n),
                                    latex(a), latex(b), latex(n-1), latex(n), latex(n),
                                    latex(b), latex(n), latex(n), latex(n)
                                    ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết từng bước như mẫu)
                loigiai = ('''Khai triển nhị thức Newton: \\\\
                             $\\left( %s+x \\right)^{%s} = %s^{%s} C_{%s}^0 + %s^{%s} C_{%s}^1 x + %s^{%s} C_{%s}^2 x^2 + \\dots + %s C_{%s}^{%s-1} x^{%s-1} + C_{%s}^{%s} x^{%s}$. \\\\
                             Chọn $x = -%s$, ta được: \\\\
                             $%s^{%s} C_{%s}^0 - %s^{%s} \\cdot %s \\cdot C_{%s}^1 + %s^{%s} \\cdot %s^2 \\cdot C_{%s}^2 - \\dots - %s \\cdot %s^{%s} \\cdot C_{%s}^{%s-1} + %s^{%s} \\cdot C_{%s}^{%s} = \\left( %s-%s \\right)^{%s} = \\left( -1 \\right)^{%s} = %s$.'''
                           % (latex(a), latex(n), latex(a), latex(n), latex(n), 
                              latex(a), latex(n-1), latex(n), 
                              latex(a), latex(n-2), latex(n),
                              latex(a), latex(n), latex(n), latex(n-1),
                              latex(n), latex(n), latex(n),
                              latex(b),
                              latex(a), latex(n), latex(n), 
                              latex(a), latex(n-1), latex(b), latex(n),
                              latex(a), latex(n-2), latex(b), latex(n),
                              latex(a), latex(b), latex(n-1), latex(n), latex(n),
                              latex(b), latex(n), latex(n), latex(n),
                              latex(a), latex(b), latex(n), latex(n), latex(kq)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

