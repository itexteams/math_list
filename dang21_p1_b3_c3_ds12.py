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


def bt_dang21_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến và hằng số
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Ngẫu nhiên hóa cận trên b (trong hình là 2)
                # Chọn b sao cho b^4 chia hết cho 3 hoặc các số nhỏ để đáp án đẹp
                b = random.choice([2, 3, 4])

                # Tính toán diện tích thiết diện S(x)
                # Cạnh = x*sqrt(b-x)
                canh_latex = f"x\\sqrt{{{b}-x}}"
                canh_sq_latex = f"x^2({b}-x)"

                # Tính toán thể tích V bằng Sympy
                S_x = (x**2 * (b - x) * sqrt(3)) / 4
                V_val = integrate(S_x, (x, 0, b))
                da_dung = f"${latex(V_val)}$"

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = set()
                # Các trường hợp sai thường gặp: quên chia 4, sai mẫu số, quên sqrt(3)
                sai1 = integrate(x**2 * (b - x) * sqrt(3), (x, 0, b)) # Quên chia 4
                sai2 = integrate(S_x, (x, 0, b)) * 2 # Sai hệ số
                sai3 = integrate(x**2 * (b - x), (x, 0, b)) / 4 # Quên sqrt(3)
                sai4 = (b**3 * sqrt(3)) / 12 # Sai số mũ

                list_sai = [sai1, sai2, sai3, sai4]
                for val in list_sai:
                    latex_val = f"${latex(val)}$"
                    if latex_val != da_dung:
                        s.add(latex_val)

                # Lấy 3 đáp án sai từ set
                wrong_options = random.sample(list(s), 3)
                das1, das2, das3 = wrong_options

                # Câu hỏi
                noidungcauhoi = (f"Cho phần vật thể $(T)$ giới hạn bởi hai mặt phẳng có phương trình $x = 0$ và $x = {b}$. "
                                 f"Cắt phần vật thể $(T)$ bởi mặt phẳng vuông góc với trục $Ox$ tại điểm có hoành độ $x (0 \\le x \\le {b})$, "
                                 f"ta được thiết diện là một tam giác đều có độ dài cạnh bằng ${canh_latex}$. "
                                 f"Tthể tích $V$ của phần vật thể $(T)$ là")

                # Các đáp án
                da_d = '\\True ' + da_dung
                da_s1 = das1
                da_s2 = das2
                da_s3 = das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Thay dx bằng \\text{d}x)
                loigiai = (f"Ta có: diện tích thiết diện là $S(x) = \\frac{{{canh_sq_latex} \\sqrt{{3}}}}{{4}}$ \\\\ "
                           f"$\\Rightarrow V = \\int_{{0}}^{{{b}}} \\frac{{{canh_sq_latex} \\sqrt{{3}}}}{{4}} \\text{{d}}x$ \\\\ "
                           f"Sử dụng CASIO suy ra $V = {latex(V_val)}$.")

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
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

