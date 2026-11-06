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


def bt_dang29_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo các ký hiệu
            x, y, m = symbols('x y m')

            # --- BƯỚC 3: TƯ DUY RANDOM ---
            # Để đường thẳng x + y + m = 0 tiếp xúc với cả hai đường tròn, 
            # ta cần d(I1, d) = R1 và d(I2, d) = R2.
            # Với đường thẳng x + y + m = 0, khoảng cách là |x0 + y0 + m| / sqrt(2).
            # Vậy |x1 + y1 + m| = R1 * sqrt(2)  và |x2 + y2 + m| = R2 * sqrt(2).
            # Để m có nghiệm chung, ta chọn các giá trị sao cho các biểu thức này tương thích.

            def generate_data():
                # Chọn ngẫu nhiên R1_sqrt2 (là R1 * sqrt(2)), chọn số nguyên để m đẹp
                r1_val = random.randint(1, 3)
                R1 = r1_val * sqrt(2)

                # Chọn tâm I1(x1, y1) sao cho x1 + y1 là số nguyên
                x1, y1 = random.randint(-3, 3), random.randint(-3, 3)
                sum1 = x1 + y1

                # Giả sử ta chọn một trường hợp m + sum1 = r1_val * 2 (vì d*sqrt(2) = r1*sqrt(2)*sqrt(2))
                # m = 2*r1_val - sum1. Ta sẽ dùng m này để tạo I2 và R2.
                m_target = 2 * r1_val - sum1

                # Tạo I2 và R2 tương ứng
                r2_val = r1_val * random.choice([2, 3]) # R2 gấp 2 hoặc 3 lần R1
                R2 = r2_val * sqrt(2)

                # Để cùng m_target tiếp xúc I2, |x2 + y2 + m_target| = 2 * r2_val
                # Chọn sum2 = x2 + y2 sao cho x2 + y2 + m_target = 2 * r2_val (tiếp xúc cùng phía)
                sum2 = 2 * r2_val - m_target
                x2 = random.randint(4, 8)
                y2 = int(sum2 - x2)

                return (x1, y1), R1, (x2, y2), R2, m_target

            (x1, y1), R1, (x2, y2), R2, m_target = generate_data()

            # Tính toán các giá trị hiển thị trong lời giải
            sum1 = x1 + y1
            sum2 = x2 + y2
            R1_sq = int(R1**2)
            R2_sq = int(R2**2)

            # Nội dung câu hỏi
            noidungcauhoi = r'''Trong hệ trục $Oxy$, cho hai đường tròn $(C_1): (x-%s)^2 + (y-%s)^2 = %s$, $(C_2): (x-%s)^2 + (y-%s)^2 = %s$ và đường thẳng $d: x + y + m = 0$. Giá trị của $m$ để đường thẳng $d$ tiếp xúc với cả hai đường tròn $(C_1)$ và $(C_2)$ là''' % (
                latex(x1), latex(y1), latex(R1_sq), 
                latex(x2), latex(y2), latex(R2_sq)
            )

            # Xử lý hiển thị dấu +-
            def clean_sign(val):
                s = latex(val)
                return s.replace('+-', '-').replace('--', '+')

            # Đáp án
            da_dung = '$m = %s$' % latex(m_target)
            du = [da_dung]
            s = ['$m = %s$' % latex(m_target + i) for i in range(1, 5)] + \
                ['$m = %s$' % latex(m_target - i) for i in range(1, 5)]

            random.shuffle(s)
            das1, das2, das3 = s[:3]

            list_1 = ['\\True ' + da_dung, das1, das2, das3]
            random.shuffle(list_1)

            # Lời giải
            loigiai = r'''$(C_1)$ có tâm $I_1(%s;%s)$, bán kính $R_1 = %s$ và $(C_2)$ có tâm $I_2(%s;%s)$, bán kính $R_2 = %s$. \\
            Vì đường thẳng $d$ tiếp xúc với cả hai đường tròn $(C_1)$ và $(C_2)$ nên ta có: \\
            $\begin{cases} d(I_1,d) = R_1 \\ d(I_2,d) = R_2 \end{cases} \Leftrightarrow \begin{cases} \frac{|%s + %s + m|}{\sqrt{2}} = %s \\ \frac{|%s + %s + m|}{\sqrt{2}} = %s \end{cases} \Leftrightarrow \begin{cases} |m + %s| = %s \\ |m + %s| = %s \end{cases}$ \\
            Giải hệ trên ta thu được $m = %s$.''' % (
                latex(x1), latex(y1), latex(R1),
                latex(x2), latex(y2), latex(R2),
                latex(x1), latex(y1), latex(R1),
                latex(x2), latex(y2), latex(R2),
                latex(sum1), latex(int(R1*sqrt(2))),
                latex(sum2), latex(int(R2*sqrt(2))),
                latex(m_target)
            )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','+').replace('+-','-').replace('-+','-').replace('++','+').replace('- -','+').replace('+ -','-').replace('- +','-').replace('+ +','+')
            return content

