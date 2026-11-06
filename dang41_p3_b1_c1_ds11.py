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


def bt_dang41_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số nguyên dương n để bài toán đa dạng
                n = random.choice([60, 75, 80, 85, 90, 94, 95, 100, 105, 110, 120])

                # Tính toán chính xác giá trị góc
                val_exact = n * 180.0 / (n + 6)

                # Làm tròn kết quả đến hàng đơn vị
                kq_dec = Decimal(str(val_exact)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec)

                # Dạng số thập phân để hiển thị chi tiết bước giải (chỉ dùng hiển thị phụ)
                val_exact_str = str(Decimal(str(val_exact)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s^\\circ$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên
                s = []
                val_int = int(kq_dec)
                phi_sai = [val_int + 2, val_int - 2, val_int + 4, val_int - 4, val_int + 3, val_int - 3, val_int + 5]
                for v_sai in phi_sai:
                    if v_sai > 0 and ('$%s^\\circ$' % v_sai) != da and ('$%s^\\circ$' % v_sai) not in s:
                        s.append('$%s^\\circ$' % v_sai)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Với mỗi số nguyên dương $n$, lấy $n + 6$ điểm cách đều nhau trên đường tròn. Nối mỗi điểm với các điểm cách nó hai điểm trên đường tròn để tạo ra các ngôi sao như hình vẽ dưới đây. Số đo (đơn vị độ) của góc ở đỉnh của ngôi sao khi $n = %s$ (làm tròn kết quả đến hàng đơn vị) bằng bao nhiêu?
            \\begin{center}
            \\begin{tikzpicture}[scale=0.6, line width=1pt]
            \\begin{scope}[shift={(0,0)}]
            \\draw (0,0) circle (1);
            \\foreach \\i in {1,...,7} {
              \\fill (90-\\i*360/7:1) circle (1.5pt);
              \\draw (90-\\i*360/7:1) -- (90-\\i*360/7 - 3*360/7:1);
            } 
            \\node[below] at (0,-1.2) {$n = 1$};
            \\end{scope} 
            \\begin{scope}[shift={(2.5,0)}]
            \\draw (0,0) circle (1);
            \\foreach \\i in {1,...,8} {
              \\fill (90-\\i*360/8:1) circle (1.5pt);
              \\draw (90-\\i*360/8:1) -- (90-\\i*360/8 - 3*360/8:1);
            }
            \\node[below] at (0,-1.2) {$n = 2$};
            \\end{scope}
            \\begin{scope}[shift={(5,0)}]
            \\draw (0,0) circle (1);
            \\foreach \\i in {1,...,9} {
              \\fill (90-\\i*360/9:1) circle (1.5pt);
              \\draw (90-\\i*360/9:1) -- (90-\\i*360/9 - 3*360/9:1);
            }
            \\node[below] at (0,-1.2) {$n = 3$};
            \\end{scope}
            \\begin{scope}[shift={(7.5,0)}]
            \\draw (0,0) circle (1);
            \\foreach \\i in {1,...,10} {
              \\fill (90-\\i*360/10:1) circle (1.5pt);
              \\draw (90-\\i*360/10:1) -- (90-\\i*360/10 - 3*360/10:1);
            }
            \\node[below] at (0,-1.2) {$n = 4$};
            \\end{scope}
            \\begin{scope}[shift={(10,0)}]
            \\draw (0,0) circle (1);
            \\foreach \\i in {1,...,11} {
              \\fill (90-\\i*360/11:1) circle (1.5pt);
              \\draw (90-\\i*360/11:1) -- (90-\\i*360/11 - 3*360/11:1);
            }
            \\node[below] at (0,-1.2) {$n = 5$};
            \\end{scope}
            \\end{tikzpicture}
            \\end{center}''' % (n))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Khi $n + 6$ điểm chia đều đường tròn đơn vị thì mỗi cung nối hai điểm có số đo là $\\frac{360^\\circ}{n+6}$. \\\\
            Theo cách dựng hình ngôi sao thì mỗi góc ở đỉnh ngôi sao sẽ là góc nội tiếp chắn $n$ cung nhỏ. \\\\
            Do đó $\\varphi_n = \\frac{1}{2} \\cdot n \\cdot \\frac{360^\\circ}{n+6} = \\frac{n}{n+6} \\cdot 180^\\circ$. \\\\
            Với $n = %s$ thì $\\varphi_{%s} = \\frac{%s}{%s} \\cdot 180^\\circ = %s^\\circ \\approx %s^\\circ$.''' 
                           % (n, n, n, n+6, val_exact_str, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

