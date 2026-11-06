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


def bt_dang63_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random giá trị x (chiều rộng) để đảm bảo đáp án là số đẹp
                # Trong ảnh x = 5. Ta chọn x ngẫu nhiên trong khoảng từ 3 đến 8.
                x_val = random.randint(3, 8)

                # Bước 2: Tính toán các thông số dựa trên x_val
                # Theo đề bài: Chiều dài = 2x. Chiều cao h. 
                # V = x * 2x * h => h = V / (2x^2)
                # Để h có dạng phân số đẹp k/3 như trong ảnh, ta thiết lập V = (4 * x^3) / 3
                V = Rational(4 * x_val**3, 3)
                V_tex = latex(V)

                dai = 2 * x_val
                rong = x_val
                cao = Rational(2 * x_val, 3)

                # Chi phí nhân công (cố định hoặc có thể random)
                cost = 500000

                # Biểu thức diện tích S = 2x^2 + 500/x (với V = 500/3)
                # Tổng quát: S = 2x^2 + (2*V*3x) / (2x^2) = 2x^2 + 3V/x? 
                # Không, S = đáy + 2*(dài+rộng)*h = 2x^2 + 2*(3x)*h = 2x^2 + 6x * (V/(2x^2)) = 2x^2 + 3V/x
                # Với V = 4x^3/3 => 3V/x = 4x^2. 
                # Để giống hệt mẫu 500/x, ta tính hệ số k = 3*V
                k_val = 3 * V
                k_half = k_val / 2

                # Giá trị nhỏ nhất của S theo AM-GM (Cô-si)
                # S = 2x^2 + k_half/x + k_half/x >= 3 * cubert(2x^2 * k_half/x * k_half/x)
                min_S = 3 * (2 * k_half**2)**(Rational(1, 3))

                # Các đáp án trắc nghiệm (kích thước: dài, rộng, cao)
                da_dung = f"chiều dài ${dai}$m, chiều rộng ${rong}$m, chiều cao ${latex(cao)}$ m"

                s = [
                    f"chiều dài ${dai+2}$m, chiều rộng ${rong+1}$m, chiều cao ${latex(cao + 1)}$ m",
                    f"chiều dài ${rong}$m, chiều rộng ${dai}$m, chiều cao ${latex(cao)}$ m",
                    f"chiều dài ${dai}$m, chiều rộng ${rong}$m, chiều cao ${latex(cao + 2)}$ m",
                    f"chiều dài ${dai-1}$m, chiều rộng ${rong-1}$m, chiều cao ${latex(cao)}$ m",
                    f"chiều dài ${dai}$m, chiều rộng ${rong}$m, chiều cao ${x_val}$ m",
                ]

                random.shuffle(s)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Câu hỏi
                noidungcauhoi = (f"Người ta cần xây một chiếc bể chứa nước với dạng khối hộp chữ nhật không nắp có thể tích "
                                 f"bằng ${V_tex} m^3$. Đáy bể là hình chữ nhật có chiều dài gấp đôi chiều rộng. Giá thuê nhân công để "
                                 f"xây bể là ${cost:,}$ đồng/m$^2$ lòng bể. Khi đó, Tìm kích thước của bể nước sao cho chi phí thuê nhân "
                                 f"công thấp nhất.").replace(',', '.')

                # Nội dung lời giải (Bám sát ảnh 100%)
                loigiai = (f"Gọi $x$ là chiều rộng của bể chứa nước (đơn vị: m, điều kiện: $x > 0$). \\\\\n"
                           f"Khi đó chiều dài của bể chứa nước là $2x$ và chiều cao của bể chứa nước là "
                           f"$\\frac{{{V_tex}}}{{x \\cdot 2x}} = \\frac{{{latex(k_half)}}}{{3x^2}}$. \\\\\n"
                           f"Diện tích cần xây dựng là: \\\\\n"
                           f"$S = x \\cdot 2x + \\frac{{{latex(k_half)}}}{{3x^2}} \\cdot 2(x + 2x) = 2x^2 + \\frac{{{latex(k_val)}}}{{x}}$. \\\\\n"
                           f"Áp dụng bất đẳng thức Cô-si ta có: \\\\\n"
                           f"$S = 2x^2 + \\frac{{{latex(k_half)}}}{{x}} + \\frac{{{latex(k_half)}}}{{x}} \\ge 3\\sqrt[3]{{2x^2 \\cdot \\frac{{{latex(k_half)}}}{{x}} \\cdot \\frac{{{latex(k_half)}}}{{x}}}} = {int(min_S)}$ \\\\\n"
                           f"Dấu bằng xảy ra khi và chỉ khi: \\\\\n"
                           f"$2x^2 = \\frac{{{latex(k_half)}}}{{x}} \\Leftrightarrow x = {x_val}$ (TMĐK). \\\\\n"
                           f"Vậy kích thước của bể nước sao cho chi phí thuê nhân công thấp nhất là chiều dài ${dai}$m, chiều rộng ${rong}$m, chiều cao ${latex(cao)}$ m.")

            # Xuất câu trắc nghiệm
            list_ans = [f"\\True {da_dung}", da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

