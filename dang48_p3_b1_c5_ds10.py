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


def bt_dang48_p3_b1_c5_ds10(self):
            # Chọn ngẫu nhiên 5 chữ số khác nhau từ 1 đến 9
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng màu từ 5 đến 9
                n = random.randint(5, 9)

                # Tính toán
                m = n - 1
                # Trường hợp 1: A và C cùng màu
                case1 = m * 1 * (m - 1) * (m - 1)
                # Trường hợp 2: A và C khác màu
                case2 = m * (m - 1) * (m - 2) * (m - 2)
                # Tổng số cách tô cho 4 miền A, B, C, D
                ways_ABCD = case1 + case2
                # Tổng số cách tô toàn bộ hình
                kq = n * ways_ABCD

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(latex(kq))]
                da = random.choice(du)

                # Sinh các đáp án sai (đảm bảo không trùng với đáp án đúng)
                fake_set = set()
                while len(fake_set) < 3:
                    f1 = n * m * m * m * m # Hiểu lầm các ô chọn độc lập
                    f2 = n * m * (m-1) * (m-2) * (m-3) # Hiểu lầm A,B,C,D hoàn toàn khác nhau
                    f3 = n * m * (m-1)**3 # Hiểu lầm chỉ có 1 điều kiện khác nhau
                    f4 = kq + random.randint(1, 9) * 10 # Sai số tính toán
                    f5 = abs(kq - random.randint(1, 9) * 10)
                    f6 = ways_ABCD # Quên nhân với số cách tô vùng O

                    choices = [f1, f2, f3, f4, f5, f6]
                    c = random.choice(choices)
                    if c != kq and c > 0:
                        fake_set.add(c)

                s = ['$%s$'%(latex(val)) for val in fake_set]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''\\immini{Bác Huy định tô màu hình vẽ là hình tròn được chia thành 5 phần $O, A, B, C, D$ bằng $%s$ màu khác nhau (mỗi phần tô một màu) sao cho hai phần hình cạnh nhau thì không được tô cùng màu (2 phần có chung biên được gọi là cạnh nhau: $C$ và $D$ được gọi là cạnh nhau; $C$ và $A$ gọi là không cạnh nhau...). Bác Huy có bao nhiêu cách tô màu thoả mãn yêu cầu trên?}{
            \\scalebox{0.6}{  \\begin{tikzpicture}[thick, line width=1pt]
            \\draw (0,0) circle (1.5);
            \\draw (0,0) circle (3);
            \\draw (1.5,0) -- (3,0);
            \\draw (-1.5,0) -- (-3,0);
            \\draw (0,1.5) -- (0,3);
            \\draw (0,-1.5) -- (0,-3);
            \\fill (1.5,0) circle (2pt);
            \\fill (-1.5,0) circle (2pt);
            \\fill (0,1.5) circle (2pt);
            \\fill (0,-1.5) circle (2pt);
            \\fill (3,0) circle (2pt);
            \\fill (-3,0) circle (2pt);
            \\fill (0,3) circle (2pt);
            \\fill (0,-3) circle (2pt);
            \\node at (0,0) {$O$};
            \\node at (45:2.25) {$A$};
            \\node at (-45:2.25) {$B$};
            \\node at (-135:2.25) {$C$};
            \\node at (135:2.25) {$D$};
            \\end{tikzpicture}} }'''
                                 %(latex(n)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Tô màu phần $O$: có $%s$ cách.\\\\
            Còn lại $%s$ màu để tô cho các phần $A, B, C, D$.\\\\
            Chia làm 2 trường hợp:\\\\
            Trường hợp 1: Phần $A$ và phần $C$ tô cùng màu.\\\\
            - Tô phần $A$ và $C$: có $%s$ cách.\\\\
            - Tô phần $B$ (khác màu $O$ và $A, C$): có $%s - 1 = %s$ cách.\\\\
            - Tô phần $D$ (khác màu $O$ và $A, C$): có $%s - 1 = %s$ cách.\\\\
            Số cách tô trong trường hợp này là: $%s \\cdot %s \\cdot %s = %s$ cách.\\\\
            Trường hợp 2: Phần $A$ và phần $C$ tô khác màu.\\\\
            - Tô phần $A$: có $%s$ cách.\\\\
            - Tô phần $C$ (khác màu $O$ và $A$): có $%s - 1 = %s$ cách.\\\\
            - Tô phần $B$ (khác màu $O, A, C$): có $%s - 2 = %s$ cách.\\\\
            - Tô phần $D$ (khác màu $O, A, C$): có $%s - 2 = %s$ cách.\\\\
            Số cách tô trong trường hợp này là: $%s \\cdot %s \\cdot %s \\cdot %s = %s$ cách.\\\\
            Tổng số cách tô phần $A, B, C, D$ là: $%s + %s = %s$ cách.\\\\
            Vậy số cách tô màu thoả mãn yêu cầu là: $%s \\cdot %s = %s$ cách.'''
                         %(latex(n), latex(m),
                           latex(m), latex(m), latex(m-1), latex(m), latex(m-1), latex(m), latex(m-1), latex(m-1), latex(case1),
                           latex(m), latex(m), latex(m-1), latex(m), latex(m-2), latex(m), latex(m-2), latex(m), latex(m-1), latex(m-2), latex(m-2), latex(case2),
                           latex(case1), latex(case2), latex(ways_ABCD),
                           latex(n), latex(ways_ABCD), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

