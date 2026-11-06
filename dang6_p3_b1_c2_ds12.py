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


def bt_dang6_p3_b1_c2_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Khởi tạo dữ liệu ngẫu nhiên cho bảng phân bố tần số
        # Để đơn giản, ta giữ nguyên các khoảng và thay đổi tần số
        m1 = random.randint(1, 3)
        m2 = random.randint(1, 4)
        m3 = random.randint(2, 6)
        m4 = random.randint(4, 8)
        m5 = random.randint(12, 18) # Nhóm chứa Q1
        m6 = random.randint(10, 15)
        m7 = random.randint(8, 12)  # Nhóm chứa Q3
        m8 = random.randint(4, 8)
        m9 = random.randint(1, 4)
        m10 = random.randint(0, 2)

        n = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10

        # Tính Q1
        pos_q1 = n / 4
        cf_q1 = m1 + m2 + m3 + m4 # Tần số tích lũy đến trước nhóm chứa Q1
        L_q1 = 39.5
        f_q1 = m5
        w = 10

        Q1 = L_q1 + ((pos_q1 - cf_q1) / f_q1) * w
        Q1_round = round(Q1, 2)

        # Tính Q3
        pos_q3 = (3 * n) / 4
        cf_q3 = m1 + m2 + m3 + m4 + m5 + m6 # Tần số tích lũy đến trước nhóm chứa Q3
        L_q3 = 59.5
        f_q3 = m7

        Q3 = L_q3 + ((pos_q3 - cf_q3) / f_q3) * w
        Q3_round = round(Q3, 2)

        # Tính Delta Q
        Delta_Q = Q3 - Q1
        Delta_Q_round = round(Delta_Q, 1)

        kq = str(Delta_Q_round).replace('.', ',')

        # Bảng số liệu
        table = '''\\begin{center}
    \\begin{tabular}{|c|c|c|c|c|c|}
    \\hline
    Điểm & $[0;9,5)$ & $[9,5;19,5)$ & $[19,5;29,5)$ & $[29,5;39,5)$ & $[39,5;49,5)$ \\\\
    \\hline
    Số thí sinh & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    Điểm & $[49,5;59,5)$ & $[59,5;69,5)$ & $[69,5;79,5)$ & $[79,5;89,5)$ & $[89,5;99,5)$ \\\\
    \\hline
    Số thí sinh & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (m1, m2, m3, m4, m5, m6, m7, m8, m9, m10)

        # Câu hỏi
        noidungcauhoi = ('''Điểm thi môn Toán (thang điểm 100, điểm được làm tròn đến 1) của $%s$ thí sinh được cho mẫu số liệu ghép nhóm như sau:
        %s
        Khoảng tứ phân vị của mẫu số liệu ghép nhóm bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                         %(n, table))
        # Nội dung lời giải
        # Chú ý: Cần xác định vị trí phần tử để viết x_i tương ứng
        idx_q1 = int(n/4)
        if n%4 == 0:
             q1_str = f"\\frac{{x_{{{idx_q1}}} + x_{{{idx_q1+1}}}}}{{2}}"
        else:
             q1_str = f"x_{{{idx_q1+1}}}"

        idx_q3 = int(3*n/4)
        if (3*n)%4 == 0:
             q3_str = f"\\frac{{x_{{{idx_q3}}} + x_{{{idx_q3+1}}}}}{{2}}"
        else:
             q3_str = f"x_{{{idx_q3+1}}}"

        loigiai=('''Cỡ mẫu là $n = %s$.\\\\
    Gọi $x_1, x_2, \\dots, x_{%s}$ là điểm thi môn Toán của $%s$ thí sinh và giả sử dãy này đã được sắp xếp theo thứ tự tăng dần.\\\\
    Tứ phân vị thứ nhất $Q_1$ là $%s$. Do các giá trị này đều thuộc nhóm $[39,5;49,5)$ nên nhóm này chứa $Q_1$. Do đó, $p=5; a_5=39,5; m_5=%s; m_1+m_2+m_3+m_4=%s; a_6-a_5=10$ và ta có:
    $$Q_1 = 39,5 + \\frac{\\frac{%s}{4} - %s}{%s} \\cdot 10 \\approx %s$$
    Tứ phân vị thứ ba $Q_3$ là $%s$. Do các giá trị này đều thuộc nhóm $[59,5;69,5)$ nên nhóm này chứa $Q_3$. \\\\
    Do đó, $p=7; a_7=59,5; m_7=%s; m_1+m_2+m_3+m_4+m_5+m_6=%s; a_8-a_7=10$ và ta có:
    $$Q_3 = 59,5 + \\frac{\\frac{3 \\cdot %s}{4} - %s}{%s} \\cdot 10 \\approx %s$$
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = Q_3 - Q_1 \\approx %s - %s = %s$'''
                 %(n, n, n, q1_str, m5, cf_q1, n, cf_q1, m5, str(Q1_round).replace('.', ','),
                   q3_str, m7, cf_q3, n, cf_q3, m7, str(Q3_round).replace('.', ','),
                   str(Q3_round).replace('.', ','), str(Q1_round).replace('.', ','), kq
                 ))

        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content

