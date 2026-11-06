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


def bt_dang38_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Ta chọn giao điểm của y = sqrt(x) và y = a - x là tại x = k^2
                # Khi đó sqrt(k^2) = a - k^2 => k = a - k^2 => a = k^2 + k
                k = random.randint(1, 4)  # Chọn k từ 1 đến 4 để số không quá lớn
                k_sq = k**2
                a = k**2 + k

                x = symbols('x')
                f1 = sqrt(x)
                f2 = a - x

                # Đáp án đúng (định dạng tích phân chưa tính toán để khớp với mẫu hình ảnh)
                # Thay dx bằng \text{d}x theo yêu cầu
                da_dung = r'\int_{0}^{%s} \sqrt{x} \text{d}x + \int_{%s}^{%s} (%s - x) \text{d}x' % (latex(k_sq), latex(k_sq), latex(a), latex(a))

                # B4: Điều chỉnh các phương án sai (không trùng với đáp án đúng)
                s = [
                    r'\int_{0}^{%s} \sqrt{x} \text{d}x - \int_{%s}^{%s} (%s - x) \text{d}x' % (latex(k_sq), latex(k_sq), latex(a), latex(a)),
                    r'\int_{0}^{%s} (\sqrt{x} + %s - x) \text{d}x' % (latex(a), latex(a)),
                    r'\int_{0}^{%s} \sqrt{x} \text{d}x + \int_{%s}^{%s} (%s - x) \text{d}x' % (latex(k), latex(k), latex(a), latex(a)),
                    r'\int_{0}^{%s} (%s - x) \text{d}x' % (latex(a), latex(a)),
                    r'\int_{0}^{%s} \sqrt{x} \text{d}x' % (latex(k_sq)),
                    r'\int_{0}^{%s} (\sqrt{x} - %s + x) \text{d}x' % (latex(k_sq), latex(a))
                ]

                # Lấy ngẫu nhiên 3 đáp án sai
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = (r'Diện tích hình phẳng giới hạn bởi các đường $y = \sqrt{x}, y = %s - x$ và trục $Ox$ được tính bởi công thức'
                                 % (latex(a)))

                # Các đáp án
                da_d = ('\\True $' + str(da_dung) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B1 & B2: Viết lại y hệt cấu trúc hình ảnh)
                loigiai = (r'''Ta có $\sqrt{x} = %s - x \Leftrightarrow x = %s$. \\
                          Diện tích $S = S_1 + S_2$ \\
                          Với $S_1$ là hình phẳng giới hạn bởi các đồ thị hàm số $y = \sqrt{x}$ và các đường thẳng $x = %s, y = 0$. \\
                          $S_2$ là hình phẳng giới hạn bởi các đồ thị hàm số $y = %s - x$ và các đường thẳng $x = %s, y = 0$ (với $%s - x = 0 \Leftrightarrow x = %s$). \\
                          Vậy $S = \int_{0}^{%s} \sqrt{x} \text{d}x + \int_{%s}^{%s} (%s - x) \text{d}x$.'''
                           % (latex(a), latex(k_sq), 
                              latex(k_sq), 
                              latex(a), latex(k_sq), latex(a), latex(a),
                              latex(k_sq), latex(k_sq), latex(a), latex(a)))

            # Xuất câu trắc nghiệm đúng mẫu 100%
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

