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


def bt_dang29_p3_b2_c1_ds12(self):
            # Khai báo biến
            def round_SA(a): 
                # Kiểm tra nếu a là số nguyên
                if a == int(a):
                    return "", int(a)

                # Chuyển số thành chuỗi và tách phần nguyên, phần thập phân
                str_a = f"{a:.5f}".rstrip('0')  # Giữ tối đa 5 chữ số thập phân, loại bỏ số 0 dư
                integer_part, _, decimal_part = str_a.partition('.')  # Tách phần nguyên và thập phân

                # Xác định cách làm tròn
                if len(integer_part) > 2:
                    number = Decimal(float(a)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng đơn vị)."
                elif len(integer_part) == 2 and len(decimal_part) > 1:
                    number = Decimal(float(a)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần chục)."
                elif len(decimal_part) <= 2:
                    number = str_a  # Không cần làm tròn thêm
                    cirle = ""
                else:
                    number = Decimal(float(a)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần trăm)."

                # Chuyển dấu chấm thành dấu phẩy (nếu có)
                return cirle, str(number).replace('.', ',')

            # ------------------------------------------------------------------------------BÀI TOÁN
            for _ in range(1):
                # 1. Sinh ngẫu nhiên các giá trị gốc cho bài toán
                # Dùng chiến lược tạo ra các tham số để có kết quả đẹp
                n0 = random.randint(15, 25) # Số giếng ban đầu
                d = random.randint(8, 12)   # Lượng dầu giảm mỗi khi thêm giếng

                # Tạo ra sản lượng p0 sao cho bài toán có lời giải hợp lý
                x_max_target = random.uniform(8, 15)
                # p0/d - n0 = x_max_target => p0 = d * (x_max_target + n0)
                p0_ideal = d * (x_max_target + n0)
                p0 = round(p0_ideal / 5) * 5 # Làm tròn để số liệu đẹp hơn

                # 2. Giải bài toán dựa trên các số đã tạo
                x_max_float = (p0 - n0 * d) / d

                # Nếu x_max_float <= 0, bài toán vô nghiệm, ta tạo lại
                if x_max_float <= 0:
                    continue

                # Số giếng NGUYÊN tối đa có thể thêm vào
                ket_qua = math.floor(x_max_float)

            noidungcauhoi = f"""  Một công ty tiến hành khai thác {n0} giếng dầu trong khu vực được chỉ định. Trung bình mỗi giếng dầu chiết xuất được {p0} thùng dầu mỗi ngày. Công ty có thể khai thác nhiều hơn {n0} giếng dầu nhưng cứ khai thác thêm một giếng thì lượng dầu mỗi giếng chiết xuất được hằng ngày sẽ giảm {d} thùng.
             Để giám đốc công ty có thể quyết định số giếng cần thêm cho phù hợp với tài chính thì số giếng nguyên tối đa công ty có thể khai thác thêm để sản lượng dầu chiết xuất tăng lên là bao nhiêu? {round_SA(ket_qua)[0]} """
            loigiai = f""" 
                        Gọi $x$ là số giếng dầu công ty khai thác thêm ($x > 0$, $x$ là số nguyên). \\\\
                        Khi đó:\\\\
                        - Tổng số giếng dầu là: $n(x) = {n0} + x$.\\\\
                        - Sản lượng dầu mỗi giếng là: $p(x) = {p0} - {d}x$.  \\\\
                        Tổng sản lượng dầu hàng ngày của công ty là hàm số theo $x$:
                        $S(x) = n(x) \\cdot p(x) = ({n0} + x)({p0} - {d}x)$.    \\\\
                        Sản lượng dầu ban đầu khi chưa thêm giếng ($x=0$) là:
                        $S(0) = {n0} \\cdot {p0} = {n0*p0}$ thùng.    \\\\
                        Để sản lượng dầu tăng lên, ta cần tìm $x$ sao cho $S(x) > S(0)$:
                        $({n0} + x)({p0} - {d}x) > {n0*p0}$\\\\
                        $\\Leftrightarrow {n0*p0} - {n0*d}x + {p0}x - {d}x^2 > {n0*p0}$\\\\
                        $\\Leftrightarrow ({p0} - {n0*d})x - {d}x^2 > 0$\\\\
                        $\\Leftrightarrow x(({p0 - n0*d}) - {d}x) > 0$  \\\\
                        Vì $x > 0$, bất phương trình trở thành:
                        $({p0 - n0*d}) - {d}x > 0$
                        $\\Leftrightarrow {d}x < {p0 - n0*d}$
                        $\\Leftrightarrow x < \\frac{{{p0 - n0*d}}}{{{d}}} \\approx {x_max_float:.2f}$   \\\\
                        Vì $x$ phải là số nguyên dương, nên $x$ có thể nhận các giá trị từ $1$ đến ${math.floor(x_max_float)}$.
                        Vậy, số giếng nguyên tối đa công ty có thể khai thác thêm để sản lượng tăng là ${ket_qua}$.  """
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(round_SA(ket_qua)[1])              

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content     

