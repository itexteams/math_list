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


def bt_dang42_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (Ở đây tập trung vào bài toán hình lập phương)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Danh sách các cặp đường thẳng chéo nhau tạo góc 60 độ trong hình lập phương
                # Cấu trúc: (Đường 1, Đường 2, Đường song song với Đ1, Tam giác đều tạo thành)
                pairs = [
                    ('AC', "DA'", "A'C'", "A'C'D"),
                    ('BD', "A'B", "B'D'", "AB'D'"),
                    ("BC'", "CD'", "AD'", "ACD'"),
                    ("A'B", "B'C", "D'A", "D'AC"),
                ]

                selected = random.choice(pairs)
                d1, d2, d_parallel, triangle = selected

                # Đáp án đúng luôn là 60 độ cho các cặp này
                kq = '60^\\circ'
                da_d = '\\True $' + kq + '$'

                # Các phương án nhiễu
                s = ['$30^\\circ$', '$45^\\circ$', '$90^\\circ$', '$120^\\circ$']
                if '$' + kq + '$' in s:
                    s.remove('$' + kq + '$')

                random.shuffle(s)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai đường thẳng $%s$ và $%s$ bằng'''
                                 % (d1, d2))

                # Vẽ hình bằng TikZ (Mô phỏng hình lập phương và các đường liên quan)
                hinh_ve = '''\\begin{center}
            \\begin{tikzpicture}[scale=2, line join=round, line cap=round, >=stealth]
                \\coordinate (A) at (0,1,0);
                \\coordinate (B) at (0,0,0);
                \\coordinate (C) at (1,0,0);
                \\coordinate (D) at (1,1,0);
                \\coordinate (A1) at (0,1,1);
                \\coordinate (B1) at (0,0,1);
                \\coordinate (C1) at (1,0,1);
                \\coordinate (D1) at (1,1,1);
                \\draw (B1)--(C1)--(D1)--(A1)--cycle;
                \\draw (C1)--(C)--(D)--(D1);
                \\draw (A1)--(A)--(D);
                \\draw[dashed] (A)--(B)--(C);
                \\draw[dashed] (B)--(B1);
                \\draw[dashed] (A)--(C);
                \\draw (D)--(A1);
                \\draw(A1)--(C1);
                \\draw (D)--(C1);
                \\node[left] at (A) {$A$}; \\node[left] at (B) {$B$}; \\node[right] at (C) {$C$}; \\node[right] at (D) {$D$};
                \\node[left] at (A1) {$A'$}; \\node[left] at (B1) {$B'$}; \\node[right] at (C1) {$C'$}; \\node[right] at (D1) {$D'$};
            \\end{tikzpicture}
            \\end{center}'''

                # Nội dung lời giải chi tiết
                loigiai = ('''Ta có $%s \\parallel %s$ nên góc giữa hai đường thẳng $%s$ và $%s$ bằng góc giữa hai đường thẳng $%s$ và $%s$. \\\\
                             Mà $%s = %s = %s$ (độ dài các đường chéo của các mặt hình vuông bằng nhau). \\\\
                             Suy ra tam giác $\\triangle %s$ là tam giác đều $\\Rightarrow \\widehat{%s} = 60^\\circ$. \\\\
                             Vậy góc giữa hai đường thẳng $%s$ và $%s$ bằng $60^\\circ$.'''
                           % (d1, d_parallel, d1, d2, d_parallel, d2,
                              d_parallel, d2, "DC'" if d2 == "DA'" else "\\text{đường chéo còn lại}", # Logic hóa độ dài cạnh
                              triangle, triangle[0]+triangle[1]+triangle[2], # Tên góc
                              d1, d2))

                # Các đáp án đưa vào danh sách shuffle
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xuất nội dung theo cấu trúc yêu cầu
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n'  + str(noidungcauhoi) + '\n'
                           '\\choice \n'
                           '{' + str(list_1[0]) + '}\n'
                           '{' + str(list_1[1]) + '}\n'
                           '{' + str(list_1[2]) + '}\n'
                           '{' + str(list_1[3]) + '}\n'
                           '\\loigiai{' + hinh_ve + '\n'+ str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

