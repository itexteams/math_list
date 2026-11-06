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


def bt_dang35_p1_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Hàm số dạng: y = (ax + n) + k / (x - x0)
                # Tiệm cận đứng: x = x0
                # Tiệm cận xiên: y = ax + n
                # Giao điểm: (x0, a*x0 + n)

                x0 = random.choice([-3, -2, -1, 1, 2, 3, 4])  # Hoành độ tiệm cận đứng
                a = random.choice([-3, -2, -1, 1, 2, 3])     # Hệ số góc của tiệm cận xiên
                n = random.randint(-4, 4)                     # Hệ số tự do của tiệm cận xiên
                k = random.choice([-3, -2, -1, 1, 2, 3])     # Phần dư để đảm bảo x0 không là nghiệm của tử số

                # Tạo tử số và mẫu số của hàm phân thức
                tu_so = expand((a*x + n)*(x - x0) + k)
                mau_so = x - x0

                # Tính tọa độ giao điểm đúng
                y0 = a*x0 + n

                # Chuyển đổi sang định dạng hiển thị latex
                str_tu = latex(tu_so)
                str_mau = latex(mau_so)
                str_x0 = latex(x0)
                str_y0 = latex(y0)
                str_tcx = latex(a*x + n)
                str_k = latex(k)

                # Đáp án đúng (Không có dấu chấm ở cuối)
                da = '$(%s; %s)$' % (str_x0, str_y0)

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                # Giữ nguyên hoành độ x0 giống như cấu trúc đề mẫu trong hình, chỉ thay đổi tung độ
                y_choices = [y0 + 1, y0 - 1, y0 + 2, y0 - 2, 0]
                # Lọc bỏ giá trị trùng với y0 nếu có
                y_choices = [y for y in y_choices if y != y0]
                # Lấy ra 3 giá trị tung độ sai độc lập
                wrong_ys = random.sample(y_choices, 3)

                s = [
                    '$(%s; %s)$' % (str_x0, latex(wrong_ys[0])),
                    '$(%s; %s)$' % (str_x0, latex(wrong_ys[1])),
                    '$(%s; %s)$' % (str_x0, latex(wrong_ys[2]))
                ]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Xác định toạ độ giao điểm của đường tiệm cận đứng và đường tiệm cận xiên của đồ thị hàm số $y = \\frac{%s}{%s}$''' % (str_tu, str_mau))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo đúng các bước bài toán gốc
                loigiai = ('''Tập xác định của hàm số đã cho là $D = \\mathbb{R} \\setminus \\{%s\\}$. \\\\
            Ta có $\\lim\\limits_{x \\to %s} y = \\infty$ nên đồ thị hàm số có đường tiệm cận đứng là $x = %s$. \\\\
            Mặt khác, thực hiện phép chia tử thức cho mẫu thức ta được: \\\\
            $y = %s + \\frac{%s}{%s}$. \\\\
            Vì $\\lim\\limits_{x \\to \\pm\\infty} \\frac{%s}{%s} = 0$ nên đồ thị hàm số có đường tiệm cận xiên là $y = %s$. \\\\
            Tọa độ giao điểm của hai đường tiệm cận là nghiệm của hệ phương trình: \\\\
            $\\left\\{ \\begin{array}{l} x = %s \\\\ y = %s \\end{array} \\right. \\Leftrightarrow \\left\\{ \\begin{array}{l} x = %s \\\\ y = %s \\end{array} \\right.$ \\\\
            Vậy tọa độ giao điểm của đường tiệm cận đứng và đường tiệm cận xiên là $(%s; %s)$''' % (
                    str_x0, str_x0, str_x0,
                    str_tcx, str_k, str_mau,
                    str_k, str_mau, str_tcx,
                    str_x0, str_tcx, str_x0, str_y0,
                    str_x0, str_y0
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

