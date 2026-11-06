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


def bt_dang10_p4_b1_c2_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Random tần số sao cho tổng bằng 100 và điều kiện ngoại lệ ở câu b được thỏa mãn
        while True:
            f1 = random.randint(15, 23)
            cf2 = random.randint(55, 65) # Đảm bảo Q1 luôn nằm ở nhóm [18;21)
            f2 = cf2 - f1
            cf3 = random.randint(80, 90) # Đảm bảo Q3 luôn nằm ở nhóm [21;24)
            f3 = cf3 - cf2
            cf4 = random.randint(93, 96)
            f4 = cf4 - cf3
            f6 = 1                       # Giữ cố định 1 người ở nhóm cuối để hỏi câu b
            f5 = 100 - cf4 - f6

            # Tính toán Q1, Q3 và Delta Q bằng Sympy Rational để hiển thị phân số
            Q1 = 18 + Rational(25 - f1, f2) * 3
            Q3 = 21 + Rational(75 - cf2, f3) * 3
            DeltaQ = Q3 - Q1

            # Tính giá trị xấp xỉ
            Q3_plus_15_Delta = float(Q3) + 1.5 * float(DeltaQ)

            # Điều kiện để 32 luôn là giá trị ngoại lệ
            if Q3_plus_15_Delta < 30:
                break

        # Các chỉ số của x
        i_x1_end = f1
        i_x2_start = f1 + 1
        i_x2_end = f1 + f2
        i_x3_start = i_x2_end + 1
        i_x3_end = i_x3_start + f3 - 1
        i_x4_start = i_x3_end + 1
        i_x4_end = i_x4_start + f4 - 1
        i_x5_start = i_x4_end + 1
        i_x5_end = i_x5_start + f5 - 1

        # Format số thập phân dấu phẩy (làm tròn 2 chữ số)
        DeltaQ_approx = f"{float(DeltaQ):.2f}".replace('.', ',')
        Q3_plus_15_Delta_approx = f"{Q3_plus_15_Delta:.2f}".replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = (
            'Hằng ngày ông Thắng đều đi xe buýt từ nhà đến cơ quan. Dưới đây là bản thống kê thời gian của 100 lần ông Thắng đi xe buýt từ nhà đến cơ quan\n'
            '\\begin{center}\n'
            '\\begin{tabular}{|c|c|c|c|c|c|c|}\n'
            '\\hline\n'
            'Thời gian(phút) & $[15;18)$ & $[18;21)$ & $[21;24)$ & $[24;27)$ & $[27;30)$ & $[30;33)$ \\\\ \n'
            '\\hline\n'
            f'Số lần & {f1} & {f2} & {f3} & {f4} & {f5} & {f6} \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}\n'
            'a) Hãy tìm khoảng tứ phân vị của mẫu số liệu ghép nhóm phía trên (Làm tròn kết quả đến hàng phần trăm) \\\\'
            'b) Biết rằng trong 100 lần đi trên, chỉ có đúng một lần ông Thắng đi hết 32 phút. Thời gian của lần đi đó có phải giá trị ngoại lệ không?'
        )

        # Nội dung lời giải
        loigiai = (
            'a) Cỡ mẫu $n=100$. Gọi $x_1, x_2, x_3, \\dots, x_{100}$ là mẫu số liệu gốc gồm 100 lần đi xe buýt của ông Thắng. Khi đó ta có:'
            '\\begin{center}\n'
            '\\begin{tabular}{lll}\n'
            f'$x_1, \\dots, x_{{{i_x1_end}}} \\in [15;18)$ & $x_{{{i_x2_start}}}, \\dots, x_{{{i_x2_end}}} \\in [18;21)$ & $x_{{{i_x3_start}}}, \\dots, x_{{{i_x3_end}}} \\in [21;24)$ \\\\ \n'
            f'$x_{{{i_x4_start}}}, \\dots, x_{{{i_x4_end}}} \\in [24;27)$ & $x_{{{i_x5_start}}}, \\dots, x_{{{i_x5_end}}} \\in [27;30)$ & $x_{{100}} \\in [30;33)$ \n'
            '\\end{tabular}\n'
            '\\end{center}'
            'Tứ phân vị thứ nhất của mẫu số liệu gốc là $\\frac{1}{2}(x_{25} + x_{26}) \\in [18;21)$ \\\\'
            f'Do đó tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là: $Q_1 = 18 + \\frac{{\\frac{{100}}{{4}} - {f1}}}{{{f2}}}(21-18) = {latex(Q1)}$ \\\\'
            'Tứ phân vị thứ ba của mẫu số liệu gốc là $\\frac{1}{2}(x_{75} + x_{76}) \\in [21;24)$ \\\\'
            'Do đó tứ phân vị thứ ba của mẫu số liệu ghép nhóm là: \\\\'
            f'$$Q_3 = 21 + \\frac{{\\frac{{3.100}}{{4}} - ({f1} + {f2})}}{{{f3}}}(24-21) = {latex(Q3)}$$'
            f'Vậy khoảng tứ phân vị của mẫu số liệu ghép nhóm là $\\Delta_Q = {latex(Q3)} - {latex(Q1)} = {latex(DeltaQ)} \\approx {DeltaQ_approx}$. \\\\'
            'b) Trong lần duy nhất ông Thắng đi hết 32 phút, thời gian đi của ông thuộc nhóm $[30;33)$ \\\\'
            f'Vì $Q_3 + 1,5\\Delta_Q \\approx {Q3_plus_15_Delta_approx} < 30$ nên đây là giá trị ngoại lệ của mẫu số liệu ghép nhóm.'
        )

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \\').replace('\\frac', '\\dfrac')
    return content

