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


def bt_dang65_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Các cặp (n, a, b) tương ứng với:
                # n: tổng số ván
                # a: số ván thắng ít nhất
                # b: số ván thắng đúng
                pairs = [(5, 3, 4), (6, 4, 5), (7, 5, 6), (5, 2, 3), (6, 3, 4), (7, 4, 5)]
                n, a, b = random.choice(pairs)

                p_win = 0.3125
                q_lose = 0.6875

                def binom(n, k):
                    return math.comb(n, k)

                # Tính tử số: P(X=b)
                P_X_eq_b = binom(n, b) * (p_win**b) * (q_lose**(n-b))

                # Tính mẫu số: P(X >= a)
                sum_P = 0
                for k in range(a, n + 1):
                    sum_P += binom(n, k) * (p_win**k) * (q_lose**(n-k))

                # Tính xác suất điều kiện và làm tròn
                ans = P_X_eq_b / sum_P
                ans_rounded = round(ans, 2)
                kq_decimal = Decimal(str(ans_rounded)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')
                kq4 = float(kq_decimal)

                # Các đáp án trắc nghiệm sai (distractors)
                deltas = [0.02, -0.02, 0.05, -0.05, 0.08, -0.08, 0.12, -0.12]
                random.shuffle(deltas)
                s = []
                for d in deltas:
                    val = round(kq4 + d, 2)
                    if 0 < val < 1:
                        val_dec = Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                        s.append('$%s$' % str(val_dec).replace('.', ','))

                da = '$%s$' % kq_str
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                noidungcauhoi = '''Trong một lễ hội mùa hè, có một trò chơi mà mỗi lần chơi thì người chơi sẽ tung đồng thời $4$ đồng xu cân đối một cách ngẫu nhiên. Người chơi chỉ thắng cuộc nếu nhận được ít nhất $3$ mặt ngửa từ $4$ đồng xu đã tung. Một người chơi tham gia tổng cộng $%s$ ván với xác suất thắng một ván là $0,3125$. Ban tổ chức thông báo rằng người chơi này đã thắng ít nhất $%s$ ván. Tính xác suất để người chơi này thắng đúng $%s$ ván (Kết quả làm tròn đến hàng phần trăm).''' % (n, a, b)

                # Xây dựng các chuỗi động cho phần giải
                letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
                lines = []
                denom_sum_str_list = []
                letter_mapping = {}

                for idx, k in enumerate(range(a, n + 1)):
                    let = letters[idx]
                    letter_mapping[k] = let
                    line = 'Xác suất để thắng đúng $%s$ ván: $P(X = %s) = C_{%s}^{%s} \\cdot (0,3125)^{%s} \\cdot (0,6875)^{%s} \\rightarrow Sto %s$' % (k, k, n, k, k, n-k, let)
                    lines.append(line)
                    denom_sum_str_list.append('P(X = %s)' % k)

                prob_lines_str = '\\\\\\\\\n'.join(lines)

                num_let = letter_mapping[b]
                denom_str = ' + '.join(denom_sum_str_list)
                denom_lets = ' + '.join([letter_mapping[k] for k in range(a, n+1)])

                # Nội dung lời giải
                loigiai = '''Số ván chơi: $n = %s$\\\\
            Xác suất thắng một ván: $p = 0,3125$\\\\
            Xác suất thua một ván: $1 - p = 1 - 0,3125 = 0,6875$\\\\
            Gọi $X$ là số ván thắng trong $%s$ ván chơi.\\\\
            %s\\\\
            Xác suất để người chơi này thắng đúng $%s$ ván:\\\\
            $P(X = %s \\mid X \\ge %s) = \\frac{P(X = %s)}{P(X \\ge %s)} = \\frac{P(X = %s)}{%s} = \\frac{%s}{%s} \\approx %s.$''' % (n, n, prob_lines_str, b, b, a, b, a, b, denom_str, num_let, denom_lets, kq_str)
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

