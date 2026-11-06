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


def bt_dang46_p1_b2_c4_ds11(self):
            # Khai báo biến
            # --- KHỞI TẠO BIẾN ---
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Random các thông số cho bài toán đẹp
                # Chọn x0 trong khoảng từ 1 đến 5
                x0 = randint(1, 5)
                # Chọn hệ số a của x sao cho biểu thức trong căn dương
                a_coeff = randint(-2, 4)
                while (x0**2 + a_coeff * x0) <= 0:
                    a_coeff = randint(-2, 4)

                # Biểu thức trong căn: f(x) = x^2 + ax
                f_x = x**2 + a_coeff * x
                # Giá trị hằng số C = sqrt(f(x0))
                C = sqrt(x0**2 + a_coeff * x0)

                # 2. Thiết lập các bước giải
                tu_so = sqrt(f_x) - C
                mau_so = x - x0

                # Tử số sau khi nhân liên hợp: (x^2 + ax) - C^2
                tu_sau_lien_hop = expand(f_x - C**2) 
                # Phân tích thành nhân tử: (x - x0)(x + x0 + a)
                tu_phan_tich = factor(tu_sau_lien_hop)
                # Phần còn lại sau khi triệt tiêu (x - x0)
                tu_con_lai = simplify(tu_sau_lien_hop / (x - x0))

                # Tính kết quả giới hạn cuối cùng
                kq_bieu_thuc = limit(tu_so / mau_so, x, x0)
                da = '$%s$' % latex(kq_bieu_thuc)

                # 3. Tạo các đáp án nhiễu (sao cho trông có vẻ hợp lý)
                s = [
                    '$%s$' % latex(kq_bieu_thuc * 2),
                    '$%s$' % latex(kq_bieu_thuc / 2),
                    '$%s$' % latex(kq_bieu_thuc + Rational(1, 2)),
                    '$%s$' % latex(-kq_bieu_thuc),
                    '$0$',
                    '$1$'
                ]
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # 4. Nội dung câu hỏi
                noidungcauhoi = (r'Giá trị $\lim_{x \to %s} \frac{\sqrt{%s} - %s}{%s}$ bằng'
                                 % (latex(x0), latex(f_x), latex(C), latex(mau_so)))

                # 5. Nội dung lời giải chi tiết (Dựa theo mẫu ảnh)
                loigiai = (r'''Ta có $\lim_{x \to %s} \frac{\sqrt{%s} - %s}{%s} = \lim_{x \to %s} \frac{%s}{(%s)(\sqrt{%s} + %s)}$ \\
                             $= \lim_{x \to %s} \frac{%s}{(%s)(\sqrt{%s} + %s)} = \lim_{x \to %s} \frac{%s}{\sqrt{%s} + %s}$ \\
                             $= \frac{%s + %s}{\sqrt{%s^2 + %s \cdot %s} + %s} = %s$.'''
                           % (latex(x0), latex(f_x), latex(C), latex(mau_so), 
                              latex(x0), latex(tu_sau_lien_hop), latex(mau_so), latex(f_x), latex(C),
                              latex(x0), latex(tu_phan_tich), latex(mau_so), latex(f_x), latex(C),
                              latex(x0), latex(tu_con_lai), latex(f_x), latex(C),
                              latex(x0), latex(x0 + a_coeff), latex(x0), latex(a_coeff), latex(x0), latex(C), 
                              latex(kq_bieu_thuc)
                             ))

            # 6. Xuất câu trắc nghiệm theo mẫu
            da_d = ('\\True ' + str(da))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # Xuất kết quả theo format mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

