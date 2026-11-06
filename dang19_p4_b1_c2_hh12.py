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


def bt_dang19_p4_b1_c2_hh12(self):
            # Khai báo biến
            x, y, z = symbols('x y z')

            # Bước 1: Chọn bộ số đẹp
            triples = [[1, 2, 2], [2, 3, 6], [1, 4, 8], [4, 4, 7], [2, 6, 9]]
            abc = random.choice(triples)
            a, b, c = abc[0], abc[1], abc[2]

            dist = random.randint(1, 3)
            dq = random.randint(-10, 10)
            while dq == 0:
                dq = random.randint(-10, 10)

            denom = int(math.sqrt(a**2 + b**2 + c**2))
            k = dist * denom
            d1 = dq + k
            d2 = dq - k

            # Bước 2: Kiểm tra điều kiện (P) không qua O (d != 0) và (P) song song (Q) (d != dq)
            valid_d = []
            if d1 != 0 and d1 != dq: valid_d.append(d1)
            if d2 != 0 and d2 != dq: valid_d.append(d2)

            # Bước 3: Tạo nội dung phương trình mặt phẳng từ d
            def format_plane(d_val):
                res = latex(a*x).replace('1x', 'x')
                res += ('+' + latex(b*y).replace('1y', 'y')) if b > 0 else latex(b*y).replace('1y', 'y')
                res += ('+' + latex(c*z).replace('1z', 'z')) if c > 0 else latex(c*z).replace('1z', 'z')
                res += ('+' + str(d_val)) if d_val > 0 else str(d_val)
                return res + "=0"

            # Bước 4: Tạo đáp án đúng (bao gồm tất cả các d thỏa mãn)
            da_d_str = " \\text{ hoặc } ".join(["$%s$" % format_plane(d) for d in valid_d])
            da_d = '\\True ' + da_d_str

            # Bước 5: Tạo các phương án nhiễu (Lấy các d sai)
            wrong_d_candidates = {dq, 0, -d1, -d2, d1+1, d2-1, dq+k+1}
            # Loại bỏ các giá trị đúng khỏi danh sách nhiễu
            for v in valid_d:
                if v in wrong_d_candidates:
                    wrong_d_candidates.remove(v)

            wrong_samples = random.sample(list(wrong_d_candidates), 3)
            da_s1 = '$%s$' % format_plane(wrong_samples[0])
            da_s2 = '$%s$' % format_plane(wrong_samples[1])
            da_s3 = '$%s$' % format_plane(wrong_samples[2])

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            plane_q = format_plane(dq)
            noidungcauhoi = ('''Trong không gian $Oxyz$, cho mặt phẳng $(Q): %s$ và mặt phẳng $(P)$ không đi qua gốc tọa độ $O$, song song với mặt phẳng $(Q)$ sao cho $d((P);(Q)) = %s$. Lập phương trình mặt phẳng $(P)$.'''
                            % (plane_q, latex(dist)))

            # Lời giải chi tiết
            loigiai = ('''Mặt phẳng $(P)$ song song với $(Q)$ nên có dạng: $%s %s %s + d = 0$ ($d \\neq %s$). \\\\
                         Vì $(P)$ không đi qua $O(0;0;0)$ nên $d \\neq 0$. \\\\
                         Khoảng cách giữa hai mặt phẳng song song là: \\\\
                         $d((P);(Q)) = %s \\Leftrightarrow \\frac{|d - (%s)|}{\\sqrt{%s^2 + %s^2 + %s^2}} = %s$ \\\\
                         $\\Leftrightarrow \\frac{|d %s|}{%s} = %s \\Leftrightarrow |d %s| = %s$ \\\\
                         $\\Leftrightarrow \\left[ \\begin{aligned} d %s &= %s \\\\ d %s &= -%s \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} d &= %s \\\\ d &= %s \\end{aligned} \\right.$. \\\\
                         Đối chiếu điều kiện $d \\neq 0$ và $d \\neq %s$, ta nhận %s. \\\\
                         Vậy phương trình mặt phẳng $(P)$ là: %s.'''
                       % (latex(a*x).replace('1x', 'x'), '+' + latex(b*y).replace('1y', 'y') if b > 0 else latex(b*y).replace('1y', 'y'), 
                          '+' + latex(c*z).replace('1z', 'z') if c > 0 else latex(c*z).replace('1z', 'z'),
                          str(dq), str(dist), str(dq), str(a), str(b), str(c), str(dist),
                          '+' + str(-dq) if -dq > 0 else str(-dq), str(denom), str(dist),
                          '+' + str(-dq) if -dq > 0 else str(-dq), str(k),
                          '+' + str(-dq) if -dq > 0 else str(-dq), str(k), '+' + str(-dq) if -dq > 0 else str(-dq), str(k),
                          str(d1), str(d2), str(dq), 
                          "cả hai giá trị" if len(valid_d) == 2 else "giá trị thỏa mãn",
                          da_d_str
                          ))

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

