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


def bt_dang44_p4_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo ngẫu nhiên giá trị cos alpha = a/b sao cho hợp lệ lượng giác
                # Chọn ngẫu nhiên bộ số đảm bảo mẫu lớn hơn tử
                cac_bo_cos = [
                    [-2, 3], [-1, 3], [1, 3], [2, 3],
                    [-3, 4], [-1, 4], [1, 4], [3, 4],
                    [-4, 5], [-3, 5], [-2, 5], [2, 5], [3, 5], [4, 5]
                ]

                bo_cos = random.choice(cac_bo_cos)
                tu_cos = bo_cos[0]
                mau_cos = bo_cos[1]

                val_cos = Rational(tu_cos, mau_cos)
                val_cos_sq = Rational(tu_cos**2, mau_cos**2)

                # Tính tan^2(alpha) = 1/cos^2(alpha) - 1
                val_tan_sq = Rational(mau_cos**2 - tu_cos**2, tu_cos**2)

                # Sinh ngẫu nhiên hệ số k1 và k2 cho biểu thức P = (cot + k1*tan) / (k2*cot + tan)
                # Bài gốc k1 = 3, k2 = 2
                k1 = random.randint(2, 4)
                k2 = random.randint(2, 4)

                # Tính giá trị biểu thức P = (1 + k1 * tan^2) / (k2 + tan^2)
                val_P = Rational(1 + k1 * val_tan_sq, k2 + val_tan_sq)

                # Đáp án đúng
                da = '$P = %s$' % (latex(val_P))

                # Tạo các phương án sai ngẫu nhiên toán học đảm bảo không trùng với đáp án đúng
                s = [
                    '$P = -%s$' % (latex(val_P)),
                    '$P = %s$' % (latex(Rational(k1 + val_tan_sq, 1 + k2 * val_tan_sq))),
                    '$P = %s$' % (latex(Rational(1 - k1 * val_tan_sq, k2 - val_tan_sq))),
                    '$P = %s$' % (latex(val_P + Rational(1, 2))),
                    '$P = %s$' % (latex(val_P - Rational(1, 3)))
                ]
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Định dạng chuỗi hiển thị hệ số 1 đằng trước cot (nếu cần thiết)
                str_k1 = str(k1) if k1 > 1 else ''
                str_k2 = str(k2) if k2 > 1 else ''

                # Câu hỏi
                noidungcauhoi = ('''Cho biết $\\cos \\alpha = %s$. Tính giá trị của biểu thức $P = \\frac{\\cot \\alpha + %s \\tan \\alpha}{%s \\cot \\alpha + \\tan \\alpha}$.'''
                                 % (latex(val_cos), str_k1, str_k2))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuẩn bị chuỗi tử số và mẫu số cho phần biến đổi phân thức của P
                tu_bien_doi_1 = '1 + %s \\tan^2 \\alpha' % (str(k1)) if k1 > 1 else '1 + \\tan^2 \\alpha'
                mau_bien_doi_1 = '%s + \\tan^2 \\alpha' % (str(k2))

                tu_bien_doi_2 = '1 + %s \\cdot %s' % (str(k1), latex(val_tan_sq))
                mau_bien_doi_2 = '%s + %s' % (str(k2), latex(val_tan_sq))

                # Nội dung lời giải chi tiết từng bước bám sát cấu trúc của ảnh mẫu
                loigiai = ('''Ta có: $\\cos \\alpha = %s \\Rightarrow \\tan^2 \\alpha = \\frac{1}{\\cos^2 \\alpha} - 1 = \\frac{1}{\\left(%s\\right)^2} - 1 = %s$ \\\\
            $P = \\frac{\\cot \\alpha + %s \\tan \\alpha}{%s \\cot \\alpha + \\tan \\alpha} = \\frac{\\frac{1}{\\tan \\alpha} + %s \\tan \\alpha}{\\frac{%s}{\\tan \\alpha} + \\tan \\alpha} = \\frac{\\frac{%s}{\\tan \\alpha}}{\\frac{%s}{\\tan \\alpha}} = \\frac{%s}{%s} = \\frac{%s}{%s} = %s$.'''
                           % (latex(val_cos), latex(val_cos), latex(val_tan_sq), str(k1), str(k2), str(k1), str(k2), tu_bien_doi_1, mau_bien_doi_1, tu_bien_doi_1, mau_bien_doi_1, tu_bien_doi_2, mau_bien_doi_2, latex(val_P)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

