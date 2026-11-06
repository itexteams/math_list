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


def bt_dang77_p3_b2_c1_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        x = symbols('x')

        c_cost = randint(20, 30)
        profit_old = randint(4, 8)
        p_old = c_cost + profit_old


        delta_opt = randint(1, profit_old - 1)
        k_inc = random.choice([100, 150, 200, 250])
        # q_old = k_inc * profit_old - 2 * k_inc * delta_opt = k_inc * (profit_old - 2 * delta_opt)

        delta_opt = randint(1, 3)
        profit_old = 2 * delta_opt + randint(2, 4)
        p_old = c_cost + profit_old
        q_old = k_inc * (profit_old - 2 * delta_opt)

        # Giá bán mới tối ưu
        p_new = p_old - delta_opt


        f_func = sp.expand((profit_old - x) * (q_old + k_inc * x))
        df = sp.diff(f_func, x)

        # Giá trị lợi nhuận tại các mốc
        f_0 = f_func.subs(x, 0)
        f_opt = f_func.subs(x, delta_opt)
        f_max_x = f_func.subs(x, profit_old)

        # Định dạng kết quả
        kq_str = str(p_new).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một doanh nghiệp tư nhân A chuyên kinh doanh xe gắn máy các loại. Hiện nay, doanh nghiệp đang tập trung chiến lược kinh doanh một loại xe máy với chi phí mua vào là $%s$ triệu đồng/chiếc và giá bán ra là $%s$ triệu đồng/chiếc. Với giá bán này thì số lượng xe bán ra mỗi năm là $%s$ chiếc. Nhằm tiêu thụ dòng xe đang ăn khách này, doanh nghiệp dự định giảm giá bán. Ước tính rằng cứ giảm $1$ triệu đồng/chiếc thì số lượng xe bán ra trong một năm tăng thêm $%s$ chiếc. Vậy doanh nghiệp phải định giá bán mới là bao nhiêu triệu đồng/chiếc để thu được lợi nhuận cao nhất?'''
                         %(str(c_cost),
                           str(p_old),
                           str(q_old),
                           str(k_inc)
                         ))

        # Nội dung lời giải
        loigiai = ('''Gọi $x$ (triệu đồng) là số tiền giảm giá cho mỗi chiếc xe máy ($0 < x < %s$). \\\\
    Khi đó: \\\\
    - Giá bán mới của mỗi chiếc xe là: $%s - x$ (triệu đồng). \\\\
    - Lợi nhuận thu được trên mỗi chiếc xe là: $(%s - x) - %s = %s - x$ (triệu đồng). \\\\
    - Số lượng xe bán ra trong một năm là: $%s + %s x$ (chiếc). \\\\
    Tổng lợi nhuận của doanh nghiệp thu được trong một năm là hàm số: \\\\
    $f(x) = (%s - x)(%s + %s x) = %s$ (triệu đồng). \\\\
    Xét hàm số $f(x)$ trên khoảng $(0; %s)$: \\\\
    Ta có: $f'(x) = %s$. \\\\
    Cho $f'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow x = %s$ (thỏa mãn $0 < x < %s$). \\\\
    Bảng biến thiên của hàm số $f(x)$ trên khoảng $(0; %s)$:
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\tkzTabInit[lgt=1.5, espcl=3]{$x$/0.8, $f'(x)$/0.8, $f(x)$/2}{$0$, $%s$, $%s$}
    \\tkzTabLine{,+,0,-,}
    \\tkzTabVar{-/$%s$, +/$%s$, -/$%s$}
    \\end{tikzpicture}
    \\end{center}
    Căn cứ vào bảng biến thiên, hàm số đạt giá trị lớn nhất tại $x = %s$. \\\\
    Vậy để thu được lợi nhuận cao nhất, doanh nghiệp phải định giá bán mới là: \\\\
    $%s - %s = %s$ (triệu đồng/chiếc).'''
                   %(str(profit_old),
                     str(p_old),
                     str(p_old), str(c_cost), str(profit_old),
                     str(q_old), str(k_inc),
                     str(profit_old), str(q_old), str(k_inc), latex(f_func),
                     str(profit_old),
                     latex(df),
                     latex(df), str(delta_opt), str(profit_old),
                     str(profit_old),
                     str(delta_opt), str(profit_old),
                     str(f_0), str(f_opt), str(f_max_x),
                     str(delta_opt),
                     str(p_old), str(delta_opt), str(p_new)
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n' +
               '\\end{minipage} \n\n')
    return content

