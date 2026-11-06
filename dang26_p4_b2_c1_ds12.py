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


def bt_dang26_p4_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Ràng buộc 1: Hệ số của x^2 luôn âm (chọn a = -1 để y_max luôn là số nguyên đẹp)
                a = -1 

                # Ràng buộc 2: Phương trình bậc 2 trong căn luôn có 2 nghiệm nguyên x1, x2
                # Chọn x1 và x2 sao cho khoảng cách giữa chúng là số chẵn để x_0 (đỉnh) là số nguyên
                x1 = randint(-6, 2)
                khoang_cach = 2 * randint(1, 4)
                x2 = x1 + khoang_cach 

                # Tính toán b và c dựa trên định lý Vi-ét: a(x-x1)(x-x2) = ax^2 - a(x1+x2)x + a*x1*x2
                b = -a * (x1 + x2)
                c = a * x1 * x2

                # Biểu thức trong căn
                fx_inside = a*x**2 + b*x + c

                # Tử số của đạo hàm
                f_phay_tu = 2*a*x + b

                # Điểm cực trị x0
                x0 = (x1 + x2) // 2

                # Tính y_max
                y_max_val = (x2 - x1) // 2
                y_min_val = 0

                # Các đáp án trắc nghiệm
                ans_true = "Giá trị lớn nhất bằng $%s$, giá trị nhỏ nhất bằng $0$" % (latex(y_max_val))

                # Tạo các phương án sai (đảm bảo không trùng)
                val_s2 = y_max_val**2 if y_max_val > 1 else y_max_val + 2
                ans_s1 = "Giá trị lớn nhất bằng $%s$, giá trị nhỏ nhất bằng $-%s$" % (latex(y_max_val), latex(y_max_val))
                ans_s2 = "Giá trị lớn nhất bằng $%s$, giá trị nhỏ nhất bằng $0$" % (latex(val_s2))
                ans_s3 = "Giá trị lớn nhất bằng $%s$, không có giá trị nhỏ nhất" % (latex(y_max_val))

                da = ans_true
                das1 = ans_s1
                das2 = ans_s2
                das3 = ans_s3

                # Câu hỏi
                noidungcauhoi = ('''Tìm giá trị lớn nhất, giá trị nhỏ nhất của hàm số $y = \\sqrt{%s}$.''' 
                                 % (latex(fx_inside)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bảng biến thiên TikZ sao chép y hệt mẫu image_8ebb61.png
                bang_bien_thien = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, line width=1pt]
            \\def\\w{1.5}
            \\def\\c{2.6}
            \\draw (0,0) rectangle (\\w+4*\\c, -3.5);
            \\draw (0,-1) -- (\\w+4*\\c, -1);
            \\draw (0,-2) -- (\\w+4*\\c, -2);
            \\draw (\\w,0) -- (\\w,-3.5);
            \\node at (\\w/2, -0.5) {$x$};
            \\node at (\\w/2, -1.5) {$y'$};
            \\node at (\\w/2, -2.75) {$y$};
            \\node at (\\w+0.15*\\c, -0.5) {$-\\infty$};
            \\node at (\\w+1*\\c, -0.5) {$%s$};
            \\node at (\\w+2*\\c, -0.5) {$%s$};
            \\node at (\\w+3*\\c, -0.5) {$%s$};
            \\node at (\\w+3.8*\\c, -0.5) {$+\\infty$};
            \\begin{scope}
            \\clip (\\w, -1) rectangle (\\w+1*\\c, -3.5);
            \\foreach \\i in {10, 12, ..., 70}
            \\draw[thin] (\\i/10, -1) -- (\\i/10 - 2.5, -3.5);
            \\end{scope}
            \\begin{scope}
            \\clip (\\w+3*\\c+0.08, -1) rectangle (\\w+4*\\c, -3.5);
            \\foreach \\i in {85, 87, ..., 150}
            \\draw[thin] (\\i/10, -1) -- (\\i/10 - 2.5, -3.5);
            \\end{scope}
            \\draw (\\w+1*\\c, -1) -- (\\w+1*\\c, -3.5);
            \\draw (\\w+3*\\c, -1) -- (\\w+3*\\c, -3.5);
            \\draw (\\w+1*\\c+0.08, -1) -- (\\w+1*\\c+0.08, -2);
            \\draw (\\w+3*\\c+0.08, -1) -- (\\w+3*\\c+0.08, -2);
            \\node at (\\w+1.5*\\c, -1.5) {$+$};
            \\node at (\\w+2*\\c, -1.5) {$0$};
            \\node at (\\w+2.5*\\c, -1.5) {$-$};
            \\node (A) at (\\w+1*\\c+0.4, -3.1) {$0$};
            \\node (B) at (\\w+2*\\c, -2.4) {$%s$};
            \\node (C) at (\\w+3*\\c-0.4, -3.1) {$0$};
            \\draw[->] (A) -- (B);
            \\draw[->] (B) -- (C);
            \\end{tikzpicture}
            \\end{center}''' % (latex(x1), latex(x0), latex(x2), latex(y_max_val)))

                # Nội dung lời giải
                loigiai = ('''Tập xác định: $D = [%s; %s]$. \\\\
            Tính đạo hàm $y' = \\frac{%s}{2\\sqrt{%s}}$. \\\\
            Cho $y' = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow x = %s$. \\\\
            Bảng biến thiên tham khảo mẫu sau:
            %s 
            Dựa vào bảng biến thiên, ta kết luận: \\\\
            Hàm số đạt giá trị lớn nhất bằng $%s$ tại $x = %s$. \\\\
            Hàm số đạt giá trị nhỏ nhất bằng $0$ tại $x = %s$ hoặc $x = %s$.''' 
                           % (latex(x1), latex(x2), 
                              latex(f_phay_tu), latex(fx_inside), 
                              latex(f_phay_tu), latex(x0), 
                              bang_bien_thien, 
                              latex(y_max_val), latex(x0), 
                              latex(x1), latex(x2)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

