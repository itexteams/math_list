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


def bt_dang65_p3_b3_c3_ds12(self):
            # Khai báo biến
            # H (chiều cao), W (chiều rộng đáy), T (chiều dài phần cắt viền trên)
            setups = [(12, 24, 8), (24, 48, 16), (36, 72, 24), (48, 96, 32), (60, 120, 40)]
            setup = random.choice(setups)
            H, W, T = setup
            h = H // 2
            D = 4 * h**2 // T

            # Các tham số để vẽ hình TikZ
            c_float = T * (2 + math.sqrt(3)) / (2 * h**2)
            a_float = 3 * h - h * math.sqrt(3)

            # Rút gọn phân số cho phương trình đường thẳng
            num = 2 * T
            den = H
            g = math.gcd(num, den)
            num //= g
            den //= g
            if den == 1:
                frac_str = "%s" % num
            else:
                frac_str = "\\frac{%s}{%s}" % (num, den)

            # Tính diện tích chính xác và làm tròn
            S_exact_val = (W * H / 9) * (2 + math.sqrt(3))
            correct_ans = round(S_exact_val)
            S_decimal_str = str(round(S_exact_val, 1)).replace('.', ',') + ".."

            # Các đáp án trắc nghiệm
            du = ['$%s$' % correct_ans]
            da = random.choice(du)

            # Tạo phương án nhiễu
            distractors = [correct_ans + 1, correct_ans - 1, correct_ans + 2, correct_ans - 2, correct_ans + 3, correct_ans - 3]
            random.shuffle(distractors)
            s = ['$%s$' % d for d in distractors]

            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # TikZ code cho hình vẽ
            tikz_code = ('''\\begin{center} \\scalebox{0.6}{ 
            \\begin{tikzpicture}[scale=0.15, font=\\small, >=stealth]
            \\fill[cyan!30] (%s, %s) -- (%s, 0) -- plot[domain=0:%s, variable=\\y, samples=100] ({%s*(\\y-%s)*(\\y-%s)}, {\\y}) -- cycle;
            \\draw[blue, line width=1pt] (0,0) rectangle (%s,%s);
            \\draw[green!50!black, line width=1pt] (%s, %s) -- (%s, 0);
            \\draw[red, line width=1pt, domain=0:%s, variable=\\y, samples=100] plot ({%s*(\\y-%s)*(\\y-%s)}, {\\y});
            \\fill (0, %s) circle (1.5pt);
            \\fill (%s, %s) circle (1.5pt);
            \\fill (%s, 0) circle (1.5pt);
            \\fill (0, 0) circle (1.5pt);
            \\fill (0, %s) circle (1.5pt);
            \\fill (%s, %s) circle (1.5pt);
            \\draw[<->] (-1.5, 0) -- (-1.5, %s) node[midway, fill=white] {$%s$ cm};
            \\draw[<->] (0, -1.5) -- (%s, -1.5) node[midway, fill=white] {$%s$ cm};
            \\draw[<->] (0, %s) -- (%s, %s) node[midway, fill=white] {$%s$ cm};
            \\node at (%s, %s) {$(H)$};
            \\end{tikzpicture} }
            \\end{center}''' % (T, H, W, H, c_float, a_float, a_float, W, H, T, H, W, H, c_float, a_float, a_float, a_float, T, H, W, H, W, H, H, H, W, W, H + 1.5, T, H + 1.5, T, W/2, H/2))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình phẳng $(H)$ được giới hạn bởi một đường cong parabol và một đường thẳng có các kích thước như hình vẽ dưới đây. Diện tích hình phẳng $(H)$ là phần được tô màu bằng bao nhiêu centimet vuông? (Kết quả làm tròn đến hàng đơn vị)\\\\
            %s''' % tikz_code)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)
            tikz_code1 = ('''\\begin{center} \\scalebox{0.6}{ 
            \\begin{tikzpicture}[scale=0.15, font=\\small, >=stealth, rotate=-90]
            \\fill[cyan!30] (%s, %s) -- (%s, 0) -- plot[domain=0:%s, variable=\\y, samples=100] ({%s*(\\y-%s)*(\\y-%s)}, {\\y}) -- cycle;
            \\draw[blue, line width=1pt] (0,0) rectangle (%s,%s);
            \\draw[green!50!black, line width=1pt] (%s, %s) -- (%s, 0);
            \\draw[red, line width=1pt, domain=0:%s, variable=\\y, samples=100] plot ({%s*(\\y-%s)*(\\y-%s)}, {\\y});
            \\fill (0, %s) circle (1.5pt);
            \\fill (%s, %s) circle (1.5pt);
            \\fill (%s, 0) circle (1.5pt);
            \\fill (0, 0) circle (1.5pt);
            \\fill (0, %s) circle (1.5pt);
            \\fill (%s, %s) circle (1.5pt);
            \\draw[<->] (-1.5, 0) -- (-1.5, %s) node[midway, fill=white] {$%s$ cm};
            \\draw[<->] (0, -1.5) -- (%s, -1.5) node[midway, fill=white] {$%s$ cm};
            \\draw[<->] (0, %s) -- (%s, %s) node[midway, fill=white] {$%s$ cm};
            \\node at (%s, %s) {$(H)$};
            \\end{tikzpicture} }
            \\end{center}''' % (T, H, W, H, c_float, a_float, a_float, W, H, T, H, W, H, c_float, a_float, a_float, a_float, T, H, W, H, W, H, H, H, W, W, H + 1.5, T, H + 1.5, T, W/2, H/2))
            # Nội dung lời giải
            loigiai = ('''%s Tọa độ đỉnh của parabol là $I(a; %s)$, đi qua các điểm $O(0;0)$ và $A(%s; %s)$.\\\\
            Khi đó $y = k(x-a)^2 + %s$ nên $\\begin{cases} k a^2 + %s = 0 \\\\ k(%s-a)^2 + %s = %s \\end{cases} \\Rightarrow \\frac{(%s-a)^2}{a^2} = \\frac{1}{3} \\Leftrightarrow \\left[ \\begin{array}{l} a = %s - %s\\sqrt{3} \\\\ a = %s + %s\\sqrt{3} \\end{array} \\right.$\\\\
            Kiểm tra lại điều kiện: $-\\frac{b}{2a} < %s$ nên chọn $a = %s - %s\\sqrt{3}$ thỏa mãn $\\Rightarrow k = \\frac{-(\\sqrt{3}+1)^2}{%s}$.\\\\
            Vậy phương trình parabol là: $y = \\frac{-(\\sqrt{3}+1)^2}{%s}(x - %s + %s\\sqrt{3})^2 + %s$.\\\\
            Đường thẳng $OA$ đi qua $\\begin{cases} O(0;0) \\\\ A(%s; %s) \\end{cases}$ có phương trình $y = %s x$.\\\\
            Diện tích hình phẳng là: \\\\ $S = \\int_0^{%s} \\left[ \\frac{-(\\sqrt{3}+1)^2}{%s}(x - %s + %s\\sqrt{3})^2 + %s - %s x \\right] \\mathrm{d}x = %s \\approx %s (\\text{cm}^2)$.\\\\
            Vậy diện tích hình phẳng $(H)$ là phần được tô màu bằng $%s (\\text{cm}^2)$.'''
            % (tikz_code1,W, H, W-T, W, W, H, W, W-T, H, 3*h, h, 3*h, h, H, 3*h, h, D, D, 3*h, h, W, H, W-T, frac_str, H, D, 3*h, h, W, frac_str, S_decimal_str, correct_ans, correct_ans))
            dapan='\\shortans[0]{$%s$}\n'%(correct_ans)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

