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


def bt_dang6_p3_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số a (trong hình là a=2)
                a = random.randint(1, 5) 

                # Tính toán các thông số để bài toán có nghiệm đẹp m = -4a
                # Biểu thức: |ax^2 + mx + m + k| <= 1
                # m = -4a, k = 8a - 1
                m_val = -4 * a
                k_val = 8 * a - 1

                # Các giá trị trung gian cho lời giải
                # Tại x = 1: |a + m + m + k| = |2m + a + k|
                val_x1_m = 2 # Hệ số của m
                val_x1_const = a + k_val # Hệ số tự do

                # Tại x = 2: |4a + 2m + m + k| = |3m + 4a + k|
                val_x2_m = 3 # Hệ số của m
                val_x2_const = 4*a + k_val

                # Đáp án đúng
                kq = m_val
                da = '$m = %s$' % (latex(kq))

                # --- B4: Điều chỉnh phương án sai (không trùng đáp án đúng) ---
                s = set()
                while len(s) < 3:
                    sai = random.choice([kq+1, kq-1, kq+2, -kq, a, 0, 2*a])
                    if sai != kq:
                        s.add(sai)

                list_sai = list(s)
                das1 = '$m = %s$' % (latex(list_sai[0]))
                das2 = '$m = %s$' % (latex(list_sai[1]))
                das3 = '$m = %s$' % (latex(list_sai[2]))

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (r'Giá trị của $m$ để hàm số $y = \sqrt{1 - |%s x^2 + mx + m + %s|}$ xác định trên $[1; 3]$ là'
                                 % (latex(a) if a != 1 else '', latex(k_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải (Viết y hệt mẫu hình ảnh) ---
                # Tính toán biên cho m trong lời giải
                # |2m + const| <= 1 => -1-const <= 2m <= 1-const
                low1 = -1 - val_x1_const
                high1 = 1 - val_x1_const
                # |3m + const2| <= 1 => -1-const2 <= 3m <= 1-const2
                low2 = -1 - val_x2_const
                high2 = 1 - val_x2_const

                loigiai = (r'''Hàm số xác định khi $1 - |%s x^2 + mx + m + %s| \ge 0 \Leftrightarrow |%s x^2 + mx + m + %s| \le 1. (*)$ \\
                Bài toán được chuyển về việc tìm $m$ để $(*)$ nghiệm đúng với mọi $x \in [1; 3]$. \\
                \textbf{Điều kiện cần:} Bất phương trình nghiệm đúng với mọi $x \in [1; 3]$ nên nghiệm đúng với $x=1, x=2$ tức là ta có: \\
                $\begin{cases} |%sm + %s| \le 1 \\ |%sm + %s| \le 1 \end{cases} \Leftrightarrow 
                \begin{cases} %s \le %sm + %s \le 1 \\ -1 \le %sm + %s \le 1 \end{cases} \Leftrightarrow
                \begin{cases} %s \le m \le %s \\ %s \le m \le %s \end{cases} \Rightarrow m = %s$ \\
                \textbf{Điều kiện đủ:} Với $m = %s$, ta có: \\
                $(*) \Leftrightarrow |%s x^2 %s x + %s| \le 1 \Leftrightarrow -1 \le %s x^2 %s x + %s \le 1$ \\
                $\Leftrightarrow \begin{cases} %s x^2 %s x + %s \ge 0 \\ %s x^2 %s x + %s \le 0 \end{cases} \Leftrightarrow
                \begin{cases} %s(x-2)^2 \ge 0 \\ %s x^2 %s x + %s \le 0 \end{cases}$ \\
                $\Leftrightarrow x^2 - 4x + 3 \le 0 \Leftrightarrow (x-1)(x-3) \le 0 \Leftrightarrow 1 \le x \le 3$ (thỏa mãn). \\
                Vậy $m = %s$ thỏa mãn yêu cầu bài toán.'''
                % (latex(a) if a != 1 else '', latex(k_val), latex(a) if a != 1 else '', latex(k_val),
                   latex(val_x1_m), latex(val_x1_const), latex(val_x2_m), latex(val_x2_const),
                   latex(-1), latex(val_x1_m), latex(val_x1_const), latex(val_x2_m), latex(val_x2_const),
                   latex(Rational(low1, 2)), latex(Rational(high1, 2)), 
                   latex(Rational(low2, 3)), latex(Rational(high2, 3) if high2 % 3 != 0 else high2//3),
                   latex(kq), latex(kq), 
                   latex(a) if a != 1 else '', latex(m_val), latex(k_val), 
                   latex(a) if a != 1 else '', latex(m_val), latex(k_val),
                   latex(a) if a != 1 else '', latex(m_val), latex(k_val + 1),
                   latex(a) if a != 1 else '', latex(m_val), latex(k_val - 1),
                   latex(a) if a != 1 else '', 
                   latex(a) if a != 1 else '', latex(m_val//a), latex((k_val-1)//a),
                   latex(kq)
                  ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


