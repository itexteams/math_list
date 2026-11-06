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


def bt_dang46_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các giá trị giả định để tính toán (random hóa hệ số k trong AA' = k*a)
                # Trong đề gốc k = 1 (AB = AA' = a)
                # Ta có thể random k để bài toán đa dạng hơn: k = 1, sqrt(2), sqrt(3), 2...
                list_k = [1, sqrt(2), sqrt(3)]
                k_val = random.choice(list_k)

                # Tính toán giá trị tan
                # AC = a, AB = a
                # A'B = sqrt(AA'^2 + AB^2) = sqrt((k*a)^2 + a^2) = a*sqrt(k^2 + 1)
                # tan = AC / A'B = 1 / sqrt(k^2 + 1)

                tan_val = 1 / sqrt(k_val**2 + 1)
                kq_sym = simplify(tan_val)

                # Định dạng đáp án đúng
                da = '$' + latex(kq_sym) + '$'

                # Tạo các đáp án sai (distractors)
                s = [
                    '$' + latex(simplify(1/k_val)) + '$',
                    '$' + latex(simplify(sqrt(k_val**2 + 1))) + '$',
                    '$' + latex(simplify(sqrt(2)/2)) + '$',
                    '$' + latex(simplify(sqrt(6)/3)) + '$',
                    '$' + latex(simplify(sqrt(3)/3)) + '$',
                    '$' + latex(simplify(sqrt(2))) + '$'
                ]

                # Loại bỏ đáp án đúng khỏi danh sách đáp án sai nếu trùng
                if da in s:
                    s.remove(da)

                # Chọn ngẫu nhiên 3 đáp án sai
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Xử lý chuỗi latex cho đề bài dựa trên k_val
                str_k = ""
                if k_val == 1:
                    str_k = "AA' = a"
                else:
                    str_k = "AA' = a" + latex(k_val)

                # TikZ code cho hình lăng trụ đứng
                tikz_code = """\\begin{center} \\begin{tikzpicture}[line cap=round,line join=round,x=1.0cm,y=1.0cm,scale=0.7, line width=1pt]
                \\coordinate (A1) at (0,0);
                \\coordinate (B1) at (1.5,-1.2);
                \\coordinate (C1) at (4,0);
                \\coordinate (A) at (0,4);
                \\coordinate (B) at (1.5,2.8);
                \\coordinate (C) at (4,4);
                \\draw (A)--(B)--(C)--cycle;
                \\draw (A1)--(B1)--(C1);
                \\draw (A)--(A1) (B)--(B1) (C)--(C1);
                \\draw[dashed] (A1)--(C1);
                \\draw (B)--(A1);
                \\draw (B)--(C1);
                \\tkzMarkRightAngle(B,A,C)
                \\tkzMarkRightAngle(B1,A1,C1)
                \\tkzMarkRightAngle(A1,A,B)
                \\draw (A) node[left] {$A$} (B) node[below left] {$B$} (C) node[right] {$C$};
                \\draw (A1) node[left] {$A'$} (B1) node[below] {$B'$} (C1) node[right] {$C'$};
            \\end{tikzpicture} \\end{center}"""

                # Câu hỏi
                noidungcauhoi = ("Cho hình lăng trụ đứng $ABC.A'B'C'$ có đáy $ABC$ là tam giác vuông cân tại $A$, $AB = %s$. Tang của góc giữa đường thẳng $BC'$ và mặt phẳng $\\left( ABB'A' \\right)$ bằng"
                                 %(str_k))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ("""$\\triangle ABC$ vuông cân tại $A \\Rightarrow AB = AC = a$. \\\\
                            $\\triangle AA'B$ vuông tại $A \\Rightarrow A'B = \\sqrt{AA'^2 + AB^2} = \\sqrt{\\left( %s \\right)^2 + a^2} = a%s$. \\\\
                            Ta có $\\begin{cases} C'A' \\perp A'B' \\\\ C'A' \\perp AA' \\end{cases} \\Rightarrow C'A' \\perp \\left( ABB'A' \\right)$. \\\\
                            $\\Rightarrow BA'$ là hình chiếu của $BC'$ lên mặt phẳng $\\left( ABB'A' \\right)$. \\\\
                            $\\Rightarrow \\left( BC'; \\left( ABB'A' \\right) \\right) = \\left( BC'; BA' \\right) = \\widehat{C'BA'}$. \\\\
                            $\\triangle A'BC'$ vuông tại $A' \\Rightarrow \\tan \\widehat{A'BC'} = \\frac{A'C'}{A'B} = \\frac{a}{a%s} = %s$."""
                            %(latex(k_val*symbols('a')), latex(simplify(sqrt(k_val**2 + 1))), 
                              latex(simplify(sqrt(k_val**2 + 1))), latex(kq_sym)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

