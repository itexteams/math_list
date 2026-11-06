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


def bt_dang38_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Sinh ngẫu nhiên các điểm x0 < x1 < x2 < x3 sao cho x1, x2 là điểm cực trị
                while True:
                    x1 = randint(-2, 1)
                    x2 = x1 + randint(1, 2)
                    x0 = x1 - randint(1, 2)
                    x3 = x2 + randint(1, 2)

                    ka = randint(1, 2)
                    d = randint(-5, 5)

                    # Hàm số f(x) = ka * (2x^3 - 3(x1+x2)x^2 + 6*x1*x2*x) + d
                    def f(val):
                        return ka * (2 * val**3 - 3 * (x1 + x2) * val**2 + 6 * x1 * x2 * val) + d

                    y0 = f(x0)
                    y1 = f(x1)
                    y2 = f(x2)
                    y3 = f(x3)

                    # Đảm bảo 4 giá trị y0, y1, y2, y3 phân biệt và thuộc khoảng hợp lý
                    if len({y0, y1, y2, y3}) == 4 and all(-50 <= val <= 50 for val in [y0, y1, y2, y3]):
                        break

                # Giá trị lớn nhất trên [x0; x3]
                da_val = max(y0, y1, y2, y3)
                x_max = x1 if y1 > y3 else x3

                # Đáp án đúng
                du = ['$%s$' % (latex(da_val))]
                da = random.choice(du)

                # Các phương án sai là các giá trị còn lại trong {y0, y1, y2, y3}
                wrong_vals = [v for v in [y0, y1, y2, y3] if v != da_val]
                das1 = '$%s$' % (latex(wrong_vals[0]))
                das2 = '$%s$' % (latex(wrong_vals[1]))
                das3 = '$%s$' % (latex(wrong_vals[2]))

                # Nội dung câu hỏi với bảng biến thiên vẽ bằng TikZ đóng khung
                noidungcauhoi = ('''Cho hàm số bậc ba $y=f(x)$ có bảng biến thiên trên đoạn $[%s; %s]$ như sau.
            \\begin{center}
            \\begin{tikzpicture}[scale=1, line width=1pt, >=stealth]
            \\draw (0,0) rectangle (8.5,3.2);
            \\draw (0,2.2) -- (8.5,2.2);
            \\draw (0,1.4) -- (8.5,1.4);
            \\draw (1.2,0) -- (1.2,3.2);
            \\node at (0.6, 2.7) {$x$};
            \\node at (1.7, 2.7) {$%s$};
            \\node at (3.8, 2.7) {$%s$};
            \\node at (5.9, 2.7) {$%s$};
            \\node at (8.0, 2.7) {$%s$};
            \\node at (0.6, 1.8) {$f'(x)$};
            \\node at (2.75, 1.8) {$+$};
            \\node at (3.8, 1.8) {$0$};
            \\node at (4.85, 1.8) {$-$};
            \\node at (5.9, 1.8) {$0$};
            \\node at (6.95, 1.8) {$+$};
            \\node at (0.6, 0.7) {$f(x)$};
            \\node (y0) at (1.7, 0.25) {$%s$};
            \\node (y1) at (3.8, 1.15) {$%s$};
            \\node (y2) at (5.9, 0.25) {$%s$};
            \\node (y3) at (8.0, 1.15) {$%s$};
            \\draw[->] (1.9, 0.35) -- (3.5, 1.05);
            \\draw[->] (4.1, 1.05) -- (5.7, 0.35);
            \\draw[->] (6.1, 0.35) -- (7.8, 1.05);
            \\end{tikzpicture}
            \\end{center}
            Giá trị lớn nhất của hàm số đã cho trên đoạn $[%s; %s]$ bằng'''
                                 % (latex(x0), latex(x3),
                                    latex(x0), latex(x1), latex(x2), latex(x3),
                                    latex(y0), latex(y1), latex(y2), latex(y3),
                                    latex(x0), latex(x3)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Dựa vào bảng biến thiên của hàm số $y=f(x)$ trên đoạn $[%s; %s]$, ta có:\\\\
            - Tại $x = %s$ thì $f(%s) = %s$.\\\\
            - Tại $x = %s$ thì $f(%s) = %s$.\\\\
            - Tại $x = %s$ thì $f(%s) = %s$.\\\\
            - Tại $x = %s$ thì $f(%s) = %s$.\\\\
            So sánh các giá trị trên, ta thấy giá trị lớn nhất của hàm số $y=f(x)$ trên đoạn $[%s; %s]$ bằng $%s$ (đạt được tại $x = %s$).'''
                           % (latex(x0), latex(x3),
                              latex(x0), latex(x0), latex(y0),
                              latex(x1), latex(x1), latex(y1),
                              latex(x2), latex(x2), latex(y2),
                              latex(x3), latex(x3), latex(y3),
                              latex(x0), latex(x3), latex(da_val), latex(x_max)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

