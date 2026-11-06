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


def bt_dang29_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các tham số cho khoảng (alpha, beta) và hằng số k trong tử số
                alpha = random.randint(1, 3)
                beta = alpha + 2
                k = random.randint(1, 5)

                count = 0
                valid_b_list = []
                # Tìm các giá trị của b để đường tiệm cận đứng x = b không nằm trong (alpha; beta)
                for b in range(1, 7):
                    if b <= alpha or b >= beta:
                        valid_b_list.append(b)

                case_text = ""
                # Kiểm tra điều kiện g(x) <= 0 với từng giá trị b hợp lệ
                for b in valid_b_list:
                    valid_a = []
                    for a in range(1, 7):
                        if (alpha**2 - 2*b*alpha - a*b - k <= 0) and (beta**2 - 2*b*beta - a*b - k <= 0):
                            valid_a.append(a)

                    if len(valid_a) == 6:
                        case_text += f" + Với $b={b}$: ta có $\\left\\{{\\begin{{array}}{{l}} a \\cdot {b} + {2*alpha*b} + {k} \\ge {alpha**2} \\\\ a \\cdot {b} + {2*beta*b} + {k} \\ge {beta**2} \\end{{array}}\\right.$ luôn đúng với mọi $a \\in \\left\\{{1; 2; 3; 4; 5; 6\\right\\}}$. Có 6 cặp $\\left(a; b\\right)$. \\\\\n"
                        count += 6
                    elif len(valid_a) > 0:
                        list_a_str = "; ".join(map(str, valid_a))
                        case_text += f" + Với $b={b}$: ta có $\\left\\{{\\begin{{array}}{{l}} a \\cdot {b} + {2*alpha*b} + {k} \\ge {alpha**2} \\\\ a \\cdot {b} + {2*beta*b} + {k} \\ge {beta**2} \\end{{array}}\\right. \\Rightarrow a \\in \\left\\{{{list_a_str}\\right\\}} $. Có {len(valid_a)} cặp $\\left(a; b\\right)$. \\\\\n"
                        count += len(valid_a)
                    else:
                        case_text += f" + Với $b={b}$: ta có $\\left\\{{\\begin{{array}}{{l}} a \\cdot {b} + {2*alpha*b} + {k} \\ge {alpha**2} \\\\ a \\cdot {b} + {2*beta*b} + {k} \\ge {beta**2} \\end{{array}}\\right.$ không có $a$ thỏa mãn. \\\\\n"

                # Tính xác suất và phân số tối giản
                prob = frac(count, 36)
                m = prob.numerator
                n = prob.denominator
                kq = m**2 + n**2

                if prob == 1:
                    latex_prob = "1"
                else:
                    latex_prob = f"\\frac{{{m}}}{{{n}}}"

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu (distractors) đảm bảo không trùng với đáp án đúng
                s_set = set()
                s_set.add(m + n)
                s_set.add(abs(m**2 - n**2))
                s_set.add(kq + random.choice([-2, 2, 5, 10]))
                s_set.add(kq - random.choice([-1, 1, 3, 5]))
                s_set.add(m * n)
                if kq in s_set:
                    s_set.remove(kq)

                s = list(s_set)
                random.shuffle(s)

                das1 = '$%s$' % s[0]
                das2 = '$%s$' % s[1]
                das3 = '$%s$' % s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f\\left(x\\right) = \\frac{x^2 + ax + %s}{x - b}$ với $a$, $b$ lần lượt là số chấm trên mặt xuất hiện của hai lần tung một con xúc xắc cân đối đồng chất. Biết xác suất để hàm số $f\\left(x\\right)$ nghịch biến trên khoảng $\\left(%s; %s\\right)$ là $\\frac{m}{n}$ $\\left(m, n \\in \\mathbb{N}^*, \\frac{m}{n} \\text{ là phân số tối giản}\\right)$. Giá trị $m^2 + n^2$ bằng bao nhiêu?'''
                                 % (k, alpha, beta))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                str_valid_b = "; ".join(map(str, valid_b_list))

                loigiai = ('''Số phần tử của không gian mẫu: $n\\left(\\Omega\\right) = 36$. \\\\
            Tập xác định của hàm số: $D = \\mathbb{R} \\setminus \\left\\{b\\right\\}$. \\\\
            Ta có $f'\\left(x\\right) = \\frac{\\left(2x+a\\right)\\left(x-b\\right) - \\left(x^2+ax+%s\\right)}{\\left(x-b\\right)^2} = \\frac{x^2 - 2bx - ab - %s}{\\left(x-b\\right)^2}$. \\\\
            Hàm số $f\\left(x\\right)$ nghịch biến trên khoảng $\\left(%s; %s\\right)$ khi và chỉ khi: \\\\
            $\\left\\{\\begin{array}{l} f'\\left(x\\right) \\le 0, \\forall x \\in \\left(%s; %s\\right) \\\\ x = b \\notin \\left(%s; %s\\right) \\end{array}\\right. \\Leftrightarrow \\left\\{\\begin{array}{l} g\\left(x\\right) = x^2 - 2bx - ab - %s \\le 0, \\forall x \\in \\left(%s; %s\\right) \\\\ \\left[\\begin{array}{l} b \\le %s \\\\ b \\ge %s \\end{array}\\right. \\end{array}\\right.$ \\\\
            Vì đồ thị hàm số $g\\left(x\\right)$ là một parabol có bề lõm hướng lên trên nên $g\\left(x\\right) \\le 0, \\forall x \\in \\left(%s; %s\\right)$ khi và chỉ khi: \\\\
            $\\left\\{\\begin{array}{l} g\\left(%s\\right) \\le 0 \\\\ g\\left(%s\\right) \\le 0 \\end{array}\\right. \\Leftrightarrow \\left\\{\\begin{array}{l} %s - %s b - ab - %s \\le 0 \\\\ %s - %s b - ab - %s \\le 0 \\end{array}\\right. \\Leftrightarrow \\left\\{\\begin{array}{l} ab + %s b + %s \\ge %s \\\\ ab + %s b + %s \\ge %s \\end{array}\\right. (*)$ \\\\
            Các giá trị của $b \\in \\left\\{1; 2; 3; 4; 5; 6\\right\\}$ thỏa mãn $b \\le %s$ hoặc $b \\ge %s$ là $b \\in \\left\\{%s\\right\\}$. \\\\
            Thay lần lượt các giá trị của $b$ vào hệ điều kiện $(*)$ ta có: \\\\
            %s
            Vậy có tất cả $%s$ cặp $\\left(a;b\\right)$ thỏa mãn yêu cầu bài toán. \\\\
            Xác suất cần tìm là $P = \\frac{%s}{36} = %s$. \\\\
            Suy ra $m = %s, n = %s$. Khi đó $m^2 + n^2 = %s^2 + %s^2 = %s$.'''
                     % (k, k,
                        alpha, beta,
                        alpha, beta, alpha, beta, k, alpha, beta, alpha, beta,
                        alpha, beta,
                        alpha, beta, alpha**2, 2*alpha, k, beta**2, 2*beta, k, 2*alpha, k, alpha**2, 2*beta, k, beta**2,
                        alpha, beta, str_valid_b,
                        case_text,
                        count,
                        count, latex_prob,
                        m, n, m, n, kq
                       ))
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

