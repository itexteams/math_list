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


def bt_dang23_p1_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp đảm bảo sinh số liệu hợp lệ và 4 đáp án phân biệt
                while True:
                    # 1. Sinh ngẫu nhiên giá trị của Tiệm cận đứng (x0) và Tiệm cận ngang (y0)
                    x0 = randint(-4, 4)
                    y0 = randint(-4, 4)

                    # Đảm bảo x0 và y0 khác nhau, và không đối nhau (và khác 0 để dễ nhìn)
                    if abs(x0) != abs(y0) and x0 != 0 and y0 != 0:
                        break

                # 2. Chọn ngẫu nhiên chiều biến thiên (dấu của đạo hàm y')
                dau_y_phay = random.choice(['+', '-'])

                # 3. Tạo mã LaTeX cho Bảng biến thiên sử dụng tkz-tab
                if dau_y_phay == '+':
                    # Hàm đồng biến
                    str_tkz = (
                        "\\begin{center}\n"
                        "\\begin{tikzpicture}\n"
                        f"\\tkzTabInit[lgt=1.2,espcl=3]{{$x$ /1, $y'$ /1, $y$ /2}}{{$-{{\\infty}}$, ${x0}$, $+{{\\infty}}$}}\n"
                        "\\tkzTabLine{, +, d, +, }\n"
                        f"\\tkzTabVar{{-/ ${y0}$, +D- / $+{{\\infty}}$ / $-{{\\infty}}$, +/ ${y0}$}}\n"
                        "\\end{tikzpicture}\n"
                        "\\end{center}"
                    )
                    lim_left = "+\\infty"
                    lim_right = "-\\infty"
                else:
                    # Hàm nghịch biến
                    str_tkz = (
                        "\\begin{center}\n"
                        "\\begin{tikzpicture}\n"
                        f"\\tkzTabInit[lgt=1.2,espcl=3]{{$x$ /1, $y'$ /1, $y$ /2}}{{$-{{\\infty}}$, ${x0}$, $+{{\\infty}}$}}\n"
                        "\\tkzTabLine{, -, d, -, }\n"
                        f"\\tkzTabVar{{+/ ${y0}$, -D+ / $-{{\\infty}}$ / $+{{\\infty}}$, -/ ${y0}$}}\n"
                        "\\end{tikzpicture}\n"
                        "\\end{center}"
                    )
                    lim_left = "-\\infty"
                    lim_right = "+\\infty"

                # 4. RANDOM LOẠI CÂU HỎI: Hỏi Tiệm cận đứng hay Tiệm cận ngang?
                loai_cau_hoi = random.choice(['TCD', 'TCN'])

                # Tập 4 phương án mặc định (đảo lộn vị trí x, y và x0, y0 để làm nhiễu)
                tap_dap_an = [f"$x = {x0}$", f"$x = {y0}$", f"$y = {x0}$", f"$y = {y0}$"]

                if loai_cau_hoi == 'TCN':
                    ten_duong = "ngang"
                    da_dung = f"$y = {y0}$"
                    tap_dap_an.remove(da_dung) # Rút đáp án đúng ra, 3 cái còn lại là nhiễu
                    loigiai_text = (
                        f"Dựa vào bảng biến thiên, ta quan sát giới hạn của hàm số khi $x$ tiến tới vô cực:\\\\ \n"
                        f"$\\lim\\limits_{{x \\to -\\infty}} y = {y0}$ và $\\lim\\limits_{{x \\to +\\infty}} y = {y0}$.\\\\ \n"
                        f"Do đó, đường tiệm cận ngang của đồ thị hàm số có phương trình là {da_dung}."
                    )
                else:
                    ten_duong = "đứng"
                    da_dung = f"$x = {x0}$"
                    tap_dap_an.remove(da_dung) # Rút đáp án đúng ra, 3 cái còn lại là nhiễu
                    loigiai_text = (
                        f"Dựa vào bảng biến thiên, ta quan sát giới hạn của hàm số khi $x$ tiến tới ${x0}$:\\\\ \n"
                        f"$\\lim\\limits_{{x \\to {x0}^-}} y = {lim_left}$ và $\\lim\\limits_{{x \\to {x0}^+}} y = {lim_right}$.\\\\ \n"
                        f"Do đó, đường tiệm cận đứng của đồ thị hàm số có phương trình là {da_dung}."
                    )

                # Gán đáp án đúng và nhiễu
                da = da_dung
                das1 = tap_dap_an[0]
                das2 = tap_dap_an[1]
                das3 = tap_dap_an[2]

                # Câu hỏi
                noidungcauhoi = (
                    f"Cho hàm số $y = \\frac{{ax+b}}{{cx+d}}$ ($c \\neq 0$, $ad - bc \\neq 0$) có bảng biến thiên như hình dưới đây:\n"
                    f"{str_tkz}\n"
                    f"Đường tiệm cận {ten_duong} của đồ thị hàm số đã cho có phương trình là"
                )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải đã được gán tự động ở trên
                loigiai = loigiai_text

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

