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


def bt_dang20_p3_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tỷ lệ lợi nhuận k để tạo các bài toán khác nhau (giữ nguyên cấu trúc max tại C và D)
                k = random.choice([50, 60, 70, 80, 90, 100, 110, 120])
                px = 3 * k  # Lãi mỗi bàn
                py = 2 * k  # Lãi mỗi ghế

                # Tính toán các giá trị F(x, y) tại các đỉnh
                f_A = 3 * py
                f_B_float = 3.5 * px + 6.5 * py
                f_B = int(f_B_float) if f_B_float.is_integer() else f_B_float
                f_C = 4 * px + 6 * py
                f_D = 8 * px
                f_max = f_C

                # Định dạng số thập phân sử dụng dấu phẩy
                f_B_str = str(f_B).replace('.', ',')

                # Các đáp án trắc nghiệm
                da = '$%s$' % (f_max)

                # Tạo các phương án sai (nhiễu)
                s_set = set()
                multipliers = [10, -10, 20, -20, 15, -15, 5, -5]
                for m in multipliers:
                    val = f_max + m * k
                    s_set.add('$%s$' % val)

                # Đảm bảo không bị trùng đáp án đúng vào danh sách sai
                if da in s_set:
                    s_set.remove(da)

                s = list(s_set)
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một khách hàng cần đặt một thợ mộc một số bàn học và một số ghế. Để làm một cái bàn học người thợ mất $6$ giờ và mất $4$ giờ để làm một cái ghế. Người thợ mộc có tối đa $48$ giờ/tuần để làm bàn và ghế. Khách hàng yêu cầu người thợ mộc làm số ghế nhiều nhất là hơn số bàn $3$ cái. Số lượng bàn và ghế tối đa người thợ mộc có thể làm được trong một tuần là $10$ cái. Biết một cái bàn học bán ra lãi $%s$ nghìn đồng, mỗi cái ghế bán ra lãi $%s$ nghìn đồng. Khi đó số tiền lãi lớn nhất mà xưởng thu được trong một tuần là bao nhiêu nghìn đồng?''' % (px, py))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $x, y$ lần lượt là số bàn và số ghế mà người thợ này làm trong một tuần ($x, y \\in \\mathbb{N}^*$).\\\\
            Làm một cái bàn mất $6$ giờ, một cái ghế mất $4$ giờ. Tổng thời gian không quá $48$ giờ/tuần nên ta có bất phương trình: $6x + 4y \\le 48 \\Leftrightarrow 3x + 2y \\le 24 \\quad (1)$\\\\
            Tổng số bàn và số ghế không quá $10$ cái: $x + y \\le 10 \\quad (2)$\\\\
            Khách hàng yêu cầu người thợ mộc làm số ghế nhiều nhất là hơn số bàn $3$ cái (nghĩa là số ghế trừ số bàn không vượt quá $3$ cái): $y - x \\le 3 \\Leftrightarrow -x + y \\le 3 \\quad (3)$\\\\
            Số lượng sản phẩm không âm: $x \\ge 0, y \\ge 0 \\quad (4)$\\\\
            Từ $(1), (2), (3), (4)$ ta có hệ bất phương trình:
            $\\begin{cases} 3x + 2y \\le 24 \\\\ x + y \\le 10 \\\\ -x + y \\le 3 \\\\ x \\ge 0, y \\ge 0 \\end{cases}$\\\\
            Mỗi cái bàn lãi $%s$ nghìn đồng, mỗi cái ghế lãi $%s$ nghìn đồng.\\\\
            Tổng tiền lãi $F(x, y)$ là: $F(x, y) = %sx + %sy$\\\\
            \\begin{center}
            \\begin{tikzpicture}[scale=0.8, line width=1pt]
            \\clip (-1,-1) rectangle (9,8);
            \\fill[pattern=north east lines, pattern color=gray!70] (-2,-2) rectangle (10,10);
            \\fill[white] (0,0) -- (8,0) -- (4,6) -- (3.5,6.5) -- (0,3) -- cycle;
            \\draw[->] (-1,0) -- (9,0) node[below] {$x$};
            \\draw[->] (0,-1) -- (0,8) node[right] {$y$};
            \\node[below left] at (0,0) {$O$};
            \\draw[domain=-1:5] plot (\\x, {\\x+3});
            \\draw[domain=-1:10] plot (\\x, {10-\\x});
            \\draw[domain=-1:9] plot (\\x, {12 - 1.5*\\x});
            \\draw (0,0) -- (8,0) -- (4,6) -- (3.5,6.5) -- (0,3) -- cycle;
            \\fill (0,3) circle (1pt) node[below right] {$A(0; 3)$};
            \\fill (3.5,6.5) circle (1pt) node[left] {$B(3,5; 6,5)$};
            \\fill (4,6) circle (1pt) node[right] {$C(4; 6)$};
            \\fill (8,0) circle (1pt) node[above left] {$D(8; 0)$};
            \\fill (0,0) circle (1pt);
            \\end{tikzpicture}
            \\end{center}
            Ta có miền nghiệm của bất phương trình là ngũ giác $OABCD$\\\\
            Trong đó $O(0; 0), A(0; 3), B(3,5; 6,5), C(4; 6), D(8; 0)$\\\\
            Khi đó ta có: 
            $\\left\\{ \\begin{matrix} A(0; 3) \\Rightarrow F(x, y) = %s \\\\ B(3,5; 6,5) \\Rightarrow F(x, y) = %s \\\\ C(4; 6) \\Rightarrow F(x, y) = %s \\\\ D(8; 0) \\Rightarrow F(x, y) = %s \\end{matrix} \\right. \\Rightarrow F(x, y)_{\\max} = %s$''' % (px, py, px, py, f_A, f_B_str, f_C, f_D, f_max))
                dapan='\\shortans[0]{$%s$}\n'%(f_max)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

