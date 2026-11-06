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


def bt_dang82_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến ký hiệu
            x, y = symbols('x y')

            # Bước 1: Tạo các giá trị ngẫu nhiên cho tọa độ các đỉnh A, B, C
            # Để chân đường cao H có tọa độ nguyên "đẹp" như trong hình, 
            # ta có thể chọn ngẫu nhiên hoặc dùng bộ số đã biết.
            # Ở đây tôi thiết lập logic để H thường xuyên là số nguyên hoặc phân số gọn.

            def generate_data():
                while True:
                    xA, yA = random.randint(-5, 5), random.randint(-5, 5)
                    xB, yB = random.randint(-5, 5), random.randint(-5, 5)
                    xC, yC = random.randint(-10, 10), random.randint(-10, 10)

                    # Kiểm tra 3 điểm không thẳng hàng và B != C
                    if (xB - xC) != 0 and (yB - yC) != 0 and (xA-xB)*(yB-yC) != (yA-yB)*(xB-xC):
                        # Tính toán chân đường cao H
                        # Đường thẳng BC: (yB-yC)x - (xB-xC)y + xB*yC - yB*xC = 0
                        a1 = yB - yC
                        b1 = -(xB - xC)
                        c1 = xB*yC - yB*xC

                        # Đường thẳng AH vuông góc BC: (xB-xC)(x-xA) + (yB-yC)(y-yA) = 0
                        # <=> b1*x - a1*y + ... = 0 -> không, dùng vecto chỉ phương
                        # Vecto BC = (xC-xB, yC-yB). Vecto pháp tuyến AH là BC.
                        a2 = xC - xB
                        b2 = yC - yB
                        c2 = -(a2*xA + b2*yA)

                        # Giải hệ phương trình tìm H
                        sol = solve([a1*x + b1*y + c1, a2*x + b2*y + c2], [x, y])
                        xH, yH = sol[x], sol[y]

                        # Chọn bộ số sao cho tọa độ H là số nguyên để giống mẫu
                        if xH.is_integer and yH.is_integer:
                            return xA, yA, xB, yB, xC, yC, xH, yH, a1, b1, c1, a2, b2, c2

            xA, yA, xB, yB, xC, yC, xH, yH, a1, b1, c1, a2, b2, c2 = generate_data()

            # Bước 2: Chuẩn bị nội dung câu hỏi
            noidungcauhoi = (
                'Trong mặt phẳng với hệ trục tọa độ $Oxy$, cho tam giác $ABC$ có $A(%s;%s)$, $B(%s;%s)$, $C(%s;%s)$. '
                'Tìm tọa độ chân đường cao kẻ từ đỉnh $A$ xuống cạnh $BC$.'
                % (latex(xA), latex(yA), latex(xB), latex(yB), latex(xC), latex(yC))
            )

            # Bước 3: Tạo đáp án đúng và các đáp án nhiễu
            da_dung = '(%s;%s)' % (latex(xH), latex(yH))

            # Tạo danh sách đáp án sai (đảm bảo không trùng đáp án đúng)
            s = [
                '(%s;%s)' % (latex(-xH), latex(yH)),
                '(%s;%s)' % (latex(xH), latex(-yH)),
                '(%s;%s)' % (latex(yH), latex(xH)),
                '(%s;%s)' % (latex(xH + 1), latex(yH)),
                '(%s;%s)' % (latex(xH), latex(yH - 2)),
            ]
            # Loại bỏ nếu lỡ trùng đáp án đúng
            if da_dung in s:
                s.remove(da_dung)

            random.shuffle(s)
            da_s1, da_s2, da_s3 = s[0], s[1], s[2]

            # Bước 4: Trộn đáp án
            list_ans = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Bước 5: Viết lời giải chi tiết theo mẫu ảnh
            # Định dạng phương trình BC theo kiểu (x-x0)/(x1-x0) = (y-y0)/(y1-y0)
            tu_x = 'x' + ('+' + str(-xC) if xC < 0 else '-' + str(xC)).replace('+-', '+').replace('--', '+')
            tu_y = 'y' + ('+' + str(-yC) if yC < 0 else '-' + str(yC)).replace('+-', '+').replace('--', '+')
            mau_x = '%s' % (xB - xC)
            mau_y = '%s' % (yB - yC)

            # Chuẩn hóa phương trình tổng quát ax + by + c = 0
            def fmt_eq(a, b, c):
                res = ""
                if a != 0:
                    res += str(a) + "x"
                if b > 0:
                    res += "+" + str(b) + "y"
                elif b < 0:
                    res += str(b) + "y"
                if c > 0:
                    res += "+" + str(c)
                elif c < 0:
                    res += str(c)
                return res + "=0"

            eq_bc = fmt_eq(a1, b1, c1)
            eq_ah = fmt_eq(a2, b2, c2)

            # Lời giải chi tiết
            loigiai = (
                'Phương trình đường thẳng đi qua hai điểm $B$ và $C$ có dạng: '
                '$\\frac{%s}{%s} = \\frac{%s}{%s} \\Leftrightarrow %s$. \\\\'
                'Đường thẳng đi qua $A$ và vuông góc với $BC$ có phương trình: \\\\'
                '$%s(x-%s) %s (y-%s) = 0 \\Leftrightarrow %s$. \\\\'
                'Tọa độ chân đường cao kẻ từ đỉnh $A$ xuống cạnh $BC$ là nghiệm của hệ phương trình: \\\\'
                '$\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x=%s \\\\ y=%s \\end{cases}$. \\\\'
                'Vậy tọa độ chân đường cao hạ từ $A$ là $(%s;%s)$'
                % (tu_x, mau_x, tu_y, mau_y, eq_bc,
                   a2, xA, ('+' + str(b2) if b2 >= 0 else str(b2)), yA, eq_ah,
                   eq_bc, eq_ah, xH, yH, xH, yH)
            )

            # Bước 6: Xuất nội dung theo định dạng yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

