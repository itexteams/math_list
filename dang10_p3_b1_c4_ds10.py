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


def bt_dang10_p3_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hóa các tham số để tạo bài toán mới
                # k: hằng số dịch chuyển của x trong căn đầu tiên (Trong hình là k=0)
                # m: số chính phương trong căn thứ hai (Trong hình là m=4)
                k = random.randint(0, 2) 
                m_val = random.choice([4, 9, 16])
                m_sqrt = int(math.sqrt(m_val))

                # Biểu thức 1: sqrt(x + k + 2*sqrt(x + k - 1))
                # Điều kiện: x + k - 1 >= 0 => x >= 1 - k
                a = 1 - k

                # Biểu thức 2: sqrt(m_val + 1 - x^2 - 2*sqrt(m_val - x^2))
                # Điều kiện: m_val - x^2 >= 0 => -sqrt(m_val) <= x <= sqrt(m_val)
                # Kết hợp điều kiện, tập xác định là [a; b] với b = sqrt(m_val)
                b = m_sqrt

                # Tính tổng a + b
                tong_ab = a + b

                # Tạo đáp án đúng và sai
                kq = tong_ab
                da_dung = '$%s$' % (latex(kq))

                # Tạo danh sách các phương án sai (đảm bảo không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = kq + random.choice([-2, -1, 1, 2, 3, 4])
                    if sai != kq:
                        s.add('$%s$' % (latex(sai)))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Nội dung câu hỏi
                # Biểu thức hiển thị: y = sqrt(x + (k) + 2sqrt(x + k-1)) + sqrt((m+1) - x^2 - 2sqrt(m - x^2))
                part1_inside = "x" if k == 0 else f"x + {k}"
                part1_sub = "x - 1" if k == 0 else f"x + {k-1}"

                noidungcauhoi = (r"Tập xác định của hàm số $y = \sqrt{%s + 2\sqrt{%s}} + \sqrt{%s - x^2 - 2\sqrt{%s - x^2}}$ có dạng $[a;b]$. Tổng $a + b$ bằng"
                                 % (part1_inside, part1_sub, m_val + 1, m_val))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # f1 = sqrt(x+k-1) + 1, f2 = sqrt(m-x^2) - 1
                expr1_inside = "x-1" if k == 0 else f"x+{k-1}"
                expr2_inside = f"{m_val}-x^2"

                loigiai = (r'''Ta có $y = \sqrt{\left(\sqrt{%s} + 1\right)^2} + \sqrt{\left(\sqrt{%s} - 1\right)^2} = \left|\sqrt{%s} + 1\right| + \left|\sqrt{%s} - 1\right|$. \\
                             Do đó hàm số đã cho xác định $\Leftrightarrow \begin{cases} %s \ge 0 \\ %s \ge 0 \end{cases} \Leftrightarrow \begin{cases} x \ge %s \\ -%s \le x \le %s \end{cases} \Leftrightarrow %s \le x \le %s$. \\
                             Suy ra $a = %s, b = %s$. \\
                             Do đó $a + b = %s$.'''
                           % (expr1_inside, expr2_inside, expr1_inside, expr2_inside,
                              expr1_inside, expr2_inside, a, b, b, a, b, a, b, kq))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

