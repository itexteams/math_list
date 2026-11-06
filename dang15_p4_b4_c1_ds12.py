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


def bt_dang15_p4_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các tham số của hàm số bậc ba y = ax^3 + bx^2 + cx + d
                a = random.choice([1, 2])
                d = random.choice([-3, -2, -1, 1, 2])
                x1 = 1
                x2 = 3

                # f'(x) = 3a(x - 1)(x - 3) = 3a x^2 - 12a x + 9a
                b = -6 * a
                c = 9 * a

                # Tọa độ các điểm cực trị
                y1 = 4 * a + d  # Điểm cực đại (1; y1)
                y2 = d          # Điểm cực tiểu (3; y2)

                # Tìm hệ số lớn nhất trong các số a, b, c, d
                max_val = max(a, b, c, d)

                # Đáp án đúng
                du = ['$%s$' % (latex(max_val))]
                da = random.choice(du)

                # Khởi tạo các đáp án sai không trùng với đáp án đúng
                s_set = set()
                for offset in [1, -1, 2, -2, 3, -3, 4, -4, 5, 6, 8]:
                    val = max_val + offset
                    if val != max_val:
                        s_set.add('$%s$' % (latex(val)))

                s = list(s_set)
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Thiết lập giới hạn trục y cho hình vẽ TikZ
                y_min_axis = min(y1, y2, 0) - 2
                y_max_axis = max(y1, y2, 0) + 2

                # Mã TikZ vẽ đồ thị
                tikz_code = (
                    '\\begin{tikzpicture}[line join=round, line cap=round, >=stealth, line width=1pt]\n'
                    '\\tikzset{every node/.style={scale=0.9}}\n'
                    '\\draw[->, line width=1pt] (-1,0) -- (5,0) node[below left] {$x$};\n'
                    '\\draw[->, line width=1pt] (0,%s) -- (0,%s) node[below left] {$y$};\n'
                    '\\draw (0,0) node [below left] {$O$};\n'
                    '\\foreach \\x/\\nx in {1/1, 3/3}\n'
                    '\\draw[line width=1pt] (\\x, 1pt) -- (\\x, -1pt) node [below] {$\\nx$};\n'
                    '\\foreach \\y/\\ny in {%s/%s, %s/%s}\n'
                    '\\draw[line width=1pt] (1pt, \\y) -- (-1pt, \\y) node [left] {$\\ny$};\n'
                    '\\draw[dashed, line width=1pt] (3,0) -- (3,%s) -- (0,%s);\n'
                    '\\draw[dashed, line width=1pt] (1,0) -- (1,%s) -- (0,%s);\n'
                    '\\begin{scope}\n'
                    '\\clip (-1,%s) rectangle (5,%s);\n'
                    '\\draw[samples=200, domain=-0.5:4.2, smooth, variable=\\x, line width=1pt] plot (\\x, {%s*(\\x)^3 + (%s)*(\\x)^2 + (%s)*\\x + (%s)});\n'
                    '\\end{scope}\n'
                    '\\end{tikzpicture}'
                    % (
                        latex(y_min_axis), latex(y_max_axis),
                        latex(y1), latex(y1), latex(y2), latex(y2),
                        latex(y2), latex(y2),
                        latex(y1), latex(y1),
                        latex(y_min_axis), latex(y_max_axis),
                        latex(a), latex(b), latex(c), latex(d)
                    )
                )

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = f(x) = ax^3 + bx^2 + cx + d$ có đồ thị $(C)$ như hình vẽ ở bên dưới. \\\\
            \\begin{center}
            %s
            \\end{center}
            Tìm hệ số lớn nhất trong các số $a, b, c, d$.'''
                    % (tikz_code)
                )

                # Định dạng các phương án trả lời
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Tập xác định: $D = \\mathbb{R}$. \\\\
            Ta có: $y' = f'(x) = 3ax^2 + 2bx + c$. \\\\
            Từ đồ thị hàm số, ta thấy hàm số có hai điểm cực trị là $x = 1$ và $x = 3$. \\\\
            Do đó, $x = 1$ và $x = 3$ là hai nghiệm của phương trình $f'(x) = 0$. \\\\
            Suy ra: $f'(x) = 3a(x - 1)(x - 3) = 3a(x^2 - 4x + 3) = 3ax^2 - 12ax + 9a$. \\\\
            Đồng nhất hệ số với $f'(x) = 3ax^2 + 2bx + c$, ta được: \\\\
            $\\begin{cases} 2b = -12a \\\\ c = 9a \\end{cases} \\Rightarrow \\begin{cases} b = -6a \\\\ c = 9a \\end{cases}$. \\\\
            Đồ thị hàm số có hai điểm cực trị là điểm cực đại $(1; %s)$ và điểm cực tiểu $(3; %s)$. \\\\
            Mặt khác: \\\\
            $f(3) = %s \\Leftrightarrow a \\cdot 3^3 + b \\cdot 3^2 + c \\cdot 3 + d = %s \\Leftrightarrow 27a + 9b + 3c + d = %s$. \\\\
            Thay $b = -6a$ và $c = 9a$ vào phương trình trên: \\\\
            $27a + 9(-6a) + 3(9a) + d = %s \\Leftrightarrow d = %s$. \\\\
            Lại có: \\\\
            $f(1) = %s \\Leftrightarrow a \\cdot 1^3 + b \\cdot 1^2 + c \\cdot 1 + d = %s \\Leftrightarrow a + b + c + d = %s$. \\\\
            Thay $b = -6a$, $c = 9a$ và $d = %s$ vào phương trình trên: \\\\
            $a - 6a + 9a + (%s) = %s \\Leftrightarrow 4a + (%s) = %s \\Leftrightarrow 4a = %s \\Leftrightarrow a = %s$. \\\\
            Từ đó suy ra: \\\\
            $b = -6 \\cdot %s = %s$, $c = 9 \\cdot %s = %s$, $d = %s$. \\\\
            Các hệ số của hàm số là $a = %s$, $b = %s$, $c = %s$, $d = %s$. \\\\
            So sánh các số trên, ta thấy hệ số lớn nhất là $%s$.'''
                    % (
                        latex(y1), latex(y2),
                        latex(y2), latex(y2), latex(y2),
                        latex(y2), latex(y2),
                        latex(y1), latex(y1), latex(y1),
                        latex(d),
                        latex(d), latex(y1), latex(d), latex(y1), latex(y1 - d), latex(a),
                        latex(a), latex(b), latex(a), latex(c), latex(d),
                        latex(a), latex(b), latex(c), latex(d),
                        latex(max_val)
                    )
                )



            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

