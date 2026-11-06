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


def bt_dang53_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random tham số. Trong đề gốc hệ số x^2 là -4. 
                # Ta chọn k là số dương sao cho y = x^4 - kx^2 + m
                k = random.choice([2, 4, 6, 8, 10, 12])

                # Bước 2: Tính toán m dựa trên điều kiện bài toán
                # Điều kiện để diện tích phần trên và phần dưới "cân bằng" dẫn đến tích phân từ 0 đến nghiệm dương lớn nhất bằng 0.
                # q^4/5 - k*q^2/3 + m = 0 (1) và q^4 - k*q^2 + m = 0 (2)
                # Từ đó q^2 = 5k/6 và m = 5*k^2/36
                m_frac = Rational(5 * k**2, 36)
                a = m_frac.p
                b = m_frac.q

                # Kết quả cần tìm S = a - b
                kq_val = a - b
                da = '$%s$' % (latex(kq_val))

                # Tạo các phương án sai
                s = []
                offsets = [-2, -1, 1, 2, 3, 5, -3]
                for offset in offsets:
                    wrong_val = kq_val + offset
                    if wrong_val != kq_val:
                        s.append('$%s$' % (latex(wrong_val)))

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = (r'''\immini{Cho hàm số $y = x^4 - %sx^2 + m$. Tìm $m$ để đồ thị hàm số cắt trục $Ox$ tại bốn điểm phân biệt sao cho hình phẳng giới hạn bởi đồ thị hàm số và $Ox$ có phần phía trên trục hoành là $S_1$, phần dưới trục hoành là $S_2$ và $S_3$ thỏa mãn $S_1 + S_2 = S_3$. Khi đó $m = \frac{a}{b}$ ($a, b$ là các số nguyên, $b > 0, \frac{a}{b}$ tối giản). Giá trị của biểu thức $S = a - b$ là}
                                 {\begin{tikzpicture}[>=stealth]
            	\coordinate (O) at (0,0);
            	\coordinate (Xmin) at (-3,0);
            	\coordinate (Xmax) at (3,0);
            	\coordinate (Ymin) at (0,-1.5);
            	\coordinate (Ymax) at (0,3);
            	\fill[pattern=north west lines, pattern color=green!50!black] 
            	plot[domain=-1:1, samples=100] (\x, {0.5*(\x)^4 - 2.5*(\x)^2 + 2}) -- (1,0) -- (-1,0) -- cycle;
            	\fill[pattern=north west lines, pattern color=green!50!black] 
            	plot[domain=-2:-1, samples=100] (\x, {0.5*(\x)^4 - 2.5*(\x)^2 + 2}) -- (-1,0) -- (-2,0) -- cycle;
            	\fill[pattern=north west lines, pattern color=green!50!black] 
            	plot[domain=1:2, samples=100] (\x, {0.5*(\x)^4 - 2.5*(\x)^2 + 2}) -- (2,0) -- (1,0) -- cycle;
            	\draw[->, line width=1pt] (Xmin) -- (Xmax) node[below] {$x$};
            	\draw[->, line width=1pt] (Ymin) -- (Ymax) node[left] {$y$};
            	\draw[line width=1pt, blue, smooth, samples=100] 
            	plot[domain=-2.317:2.317] (\x, {0.5*(\x)^4 - 2.5*(\x)^2 + 2});
            	\node[below left] at (O) {$O$};
            	\node at (0.2, 0.6) {$S_3$};
            	\node at (-1.5, -0.4) {$S_1$};
            	\node at (1.5, -0.4) {$S_2$};
            \end{tikzpicture}}'''
                                 % (latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Gọi $m, n, p, q$ ($m < n < 0 < p < q$) là hoành độ các giao điểm của đồ thị với $Ox$. \\
                             Do đồ thị hàm số nhận $Oy$ làm trục đối xứng nên \\
                             $S_1 + S_2 = S_3 \Leftrightarrow \frac{1}{2}S_3 = S_2 $ dẫn đến $ \int_{0}^{q} (x^4 - %sx^2 + m) \text{d}x = 0$ \\
                             $\Leftrightarrow \frac{q^5}{5} - \frac{%sq^3}{3} + mq = 0 \Leftrightarrow \frac{q^4}{5} - \frac{%sq^2}{3} + m = 0 \quad (1)$ \\
                             Mặt khác $q$ là nghiệm nên: $q^4 - %sq^2 + m = 0 \quad (2)$ \\
                             Từ (1) và (2) ta trừ vế theo vế: $\frac{4}{5}q^4 - \frac{2 \cdot %s}{3}q^2 = 0 \Rightarrow q^2 = \frac{5 \cdot %s}{6}$. \\
                             Thay vào (2): $m = %s \cdot \left(\frac{5 \cdot %s}{6}\right) - \left(\frac{5 \cdot %s}{6}\right)^2 = \frac{5 \cdot %s^2}{36} = %s$. \\
                             Vậy $a = %s, b = %s \Rightarrow a - b = %s$.'''
                           % (latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(m_frac), latex(a), latex(b), latex(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

