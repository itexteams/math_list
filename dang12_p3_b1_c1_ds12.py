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


def bt_dang12_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết kế bài toán để nghiệm cực đại là một số nguyên đẹp
                # Hàm doanh thu R(x) = p*x = (A * x) / (B * x^2 + 1)
                # R'(x) = A * (1 - B * x^2) / (B * x^2 + 1)^2
                # R'(x) = 0 <=> x = sqrt(1/B). Để x nguyên, ta chọn 1/B là số chính phương.
                # Gọi x_cucdai là vị trí đạt cực đại, chọn trong khoảng từ 5 đến 15
                x_cucdai = randint(5, 12)

                # B = 1 / (x_cucdai^2)
                # Để hiển thị dạng số thập phân đẹp giống 0,01x^2 + 1, ta có thể chọn trực tiếp x_cucdai từ tập hợp sao cho B đẹp
                # Hoặc biểu diễn B dưới dạng phân số/thập phân. 
                # Danh sách các cặp (x_cucdai, B_thap_phan, giới hạn đoạn x_max) đẹp:
                # 10 -> 0,01; 5 -> 0,04; 2 -> 0,25
                capphong = random.choice([
                    (10, "0,01", 0.01, 20),
                    (5, "0,04", 0.04, 10),
                    (4, "0,0625", 0.0625, 8)
                ])

                x_cucdai = capphong[0]
                B_str = capphong[1]
                B_val = capphong[2]
                x_max = capphong[3]

                # Chọn tử số A ngẫu nhiên để thay đổi số liệu đề bài
                A_val = random.choice([40, 50, 60, 80, 100])

                # Giá trị cực đại cần tìm
                kq = str(x_cucdai)

                # Các đáp án trắc nghiệm
                du = ['$%s$ nghìn chiếc'%(kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu không trùng đáp án đúng
                s = [
                    '$%s$ nghìn chiếc'%(str(x_cucdai + 2)),
                    '$%s$ nghìn chiếc'%(str(x_cucdai - 2 if x_cucdai > 2 else x_cucdai + 4)),
                    '$%s$ nghìn chiếc'%(str(x_cucdai * 2)),
                    '$%s$ nghìn chiếc'%(str(x_max)),
                    '$%s$ nghìn chiếc'%(str(x_cucdai + 5))
                ]
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Biểu diễn các thành phần trong chuỗi LaTeX
                A_latex = latex(A_val)
                x_max_latex = latex(x_max)

                # Câu hỏi
                noidungcauhoi = ('''Định mức cầu mỗi tháng của đồng hồ đeo tay Peget phụ thuộc vào giá đơn vị $p$ theo phương trình cầu $p = \\frac{%s}{%s x^2 + 1}$, $0 \\le x \\le %s$ trong đó $p$ tính bằng đô la và $x$ tính bằng nghìn chiếc. Hỏi nhà sản xuất phải bán bao nhiêu nghìn chiếc để doanh thu $R = px$ đạt cực đại?'''
                                 %(A_latex, B_str, x_max_latex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo phương pháp xét hàm và lập bảng biến thiên
                loigiai = ('''Hàm doanh thu của nhà sản xuất được xác định bởi công thức:
                           $$R(x) = p \\cdot x = \\frac{%s x}{%s x^2 + 1} \\text{ với } 0 \\le x \\le %s.$$
                           Ta tiến hành xét hàm số $R(x)$ trên đoạn $[0; %s]$.\\\\
                           Đạo hàm của hàm số là:
                           $$R'(x) = \\frac{(%s x)' \\cdot (%s x^2 + 1) - %s x \\cdot (%s x^2 + 1)'}{(%s x^2 + 1)^2}$$ 
                           $$R'(x) = \\frac{%s \\cdot (%s x^2 + 1) - %s x \\cdot (2 \\cdot %s x)}{(%s x^2 + 1)^2}$$ 
                           $$R'(x) = \\frac{%s - %s \\cdot %s x^2}{(%s x^2 + 1)^2}.$$ 
                           Cho $R'(x) = 0 \\Leftrightarrow %s - %s \\cdot %s x^2 = 0 \\Leftrightarrow x^2 = \\frac{%s}{%s \\cdot %s} \\Leftrightarrow x^2 = %s^2$ \\\\
                           Vì $0 \\le x \\le %s$ nên ta nhận nghiệm $x = %s$.\\\\
                           Ta lập bảng biến thiên của hàm số $R(x)$ trên đoạn $[0; %s]$ như sau:\\\\
                           \\begin{center}
                           \\begin{tikzpicture}[scale=1]
                           \\draw[line width=1pt] (0,3) -- (8,3);
                           \\draw[line width=1pt] (0,2) -- (8,2);
                           \\draw[line width=1pt] (2,0) -- (2,4);
                           \\node at (1,3.5) {$x$};
                           \\node at (2.3,3.5) {$0$};
                           \\node at (5,3.5) {$%s$};
                           \\node at (7.5,3.5) {$%s$};
                           \\node at (1,2.5) {$R'(x)$};
                           \\node at (3.6,2.5) {$+$};
                           \\node at (5,2.5) {$0$};
                           \\node at (6.4,2.5) {$-$};
                           \\node at (1,1) {$R(x)$};
                           \\draw[->,line width=1pt] (2.5,0.3) -- (4.6,1.7);
                           \\draw[->,line width=1pt] (5.4,1.7) -- (7.2,0.3);
                           \\end{tikzpicture}
                           \\end{center}
                           Dựa vào bảng biến thiên, ta thấy hàm số $R(x)$ đạt giá trị lớn nhất (cực đại) tại điểm $x = %s$.\\\\
                           Vậy nhà sản xuất phải bán $%s$ nghìn chiếc đồng hồ để doanh thu đạt cực đại.'''
                           %(A_latex, B_str, x_max_latex, x_max_latex,
                             A_latex, B_str, A_latex, B_str, B_str,
                             A_latex, B_str, A_latex, B_str, B_str,
                             A_latex, A_latex, B_str, B_str,
                             A_latex, A_latex, B_str, A_latex, A_latex, B_str, latex(x_cucdai**2),
                             x_max_latex, latex(x_cucdai), x_max_latex,
                             latex(x_cucdai), x_max_latex, latex(x_cucdai), latex(x_cucdai)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(x_cucdai))   
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

