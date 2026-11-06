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


def bt_dang36_p3_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các thông số cho hàm C(x) = m*x + n
                # m là chi phí biến đổi (cũng là giới hạn a cần tìm)
                # n là chi phí cố định
                m = random.randint(3, 15)
                n = random.randint(10, 60)

                # Định nghĩa Symbol x cục bộ để tránh lỗi 'invalid input'
                x_sym = symbols('x')
                bieu_thuc_C = m * x_sym + n

                # Kết quả a chính là hệ số m
                kq_val = m
                da = '$a = %s$' % (latex(kq_val))

                # Tạo các đáp án nhiễu
                s = [
                    '$a = %s$' % (latex(kq_val + 1)),
                    '$a = %s$' % (latex(kq_val - 1) if kq_val > 1 else latex(kq_val + 5)),
                    '$a = %s$' % (latex(n)),
                    '$a = 0$',
                    '$a = %s$' % (latex(m + n)),
                    '$a = %s$' % (latex(n // 2))
                ]

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi
                noidungcauhoi = (
                    'Chi phí (đơn vị: triệu đồng) để sản xuất $x$ sản phẩm của một công ty được xác định bởi hàm số: '
                    '$C(x) = %s$ (triệu đồng). Khi số sản phẩm sản xuất ra càng lớn thì chi phí trung bình của mỗi sản phẩm '
                    'ngày càng giảm nhưng không vượt quá $a$ triệu đồng. Giá trị nhỏ nhất của $a$ bằng bao nhiêu?'
                    % (latex(bieu_thuc_C))
                )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Sử dụng chuỗi thô (f-string hoặc % format) để tránh lỗi ký tự thoát
                loigiai = (
                    'Chi phí trung bình của một sản phẩm là: $\\bar{C}(x) = \\frac{%s}{x} = %s + \\frac{%s}{x}$. \\\\'
                    'Khi số sản phẩm ngày càng lớn thì $x \\to +\\infty$, ta có: '
                    '$\\lim_{x \\to +\\infty} \\bar{C}(x) = \\lim_{x \\to +\\infty} \\left( %s + \\frac{%s}{x} \\right) = %s$. \\\\'
                    'Như vậy giá trị nhỏ nhất của $a$ là $a = %s$.'
                    % (latex(bieu_thuc_C), latex(m), latex(n), latex(m), latex(n), latex(m), latex(m))
                )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(m))

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+ '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

