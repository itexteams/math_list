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


def bt_dang29_p1_b1_c2_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random vectơ mục tiêu để đề bài luôn mới mẻ
                vectors = [
                    ('\\overrightarrow{MN}', '\\overrightarrow{QP}', '\\overrightarrow{AC}', 'AC'),
                    ('\\overrightarrow{NM}', '\\overrightarrow{PQ}', '\\overrightarrow{CA}', 'AC'),
                    ('\\overrightarrow{QP}', '\\overrightarrow{MN}', '\\overrightarrow{AC}', 'AC'),
                    ('\\overrightarrow{PQ}', '\\overrightarrow{NM}', '\\overrightarrow{CA}', 'AC'),
                    ('\\overrightarrow{MQ}', '\\overrightarrow{NP}', '\\overrightarrow{BD}', 'BD'),
                    ('\\overrightarrow{QM}', '\\overrightarrow{PN}', '\\overrightarrow{DB}', 'BD'),
                    ('\\overrightarrow{NP}', '\\overrightarrow{MQ}', '\\overrightarrow{BD}', 'BD'),
                    ('\\overrightarrow{PN}', '\\overrightarrow{QM}', '\\overrightarrow{DB}', 'BD')
                ]

                target, v1, v2, diag = random.choice(vectors)

                # Kết quả luôn là 2 vectơ (vì chỉ có các điểm A,B,C,D,M,N,P,Q)
                kq = '2'

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Phương án nhiễu
                s = ['$1$', '$3$', '$4$']

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho tứ giác $ABCD$. Gọi $M,N,P,Q$ lần lượt là trung điểm của $AB,BC,CD,DA$. Có bao nhiêu vectơ (khác vectơ-không) tạo thành từ các điểm đã cho cùng hướng với vectơ $%s$?''' % target)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý vẽ đường chéo tương ứng dựa trên diag
                if diag == 'AC':
                    draw_diag = "\\draw (A) -- (C);"
                else:
                    draw_diag = "\\draw (B) -- (D);"

                # Mã TikZ vẽ hình tứ giác
                code_hinh = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.9, >=stealth]
            \\coordinate (A) at (0,2);
            \\coordinate (B) at (2,4);
            \\coordinate (C) at (6,2);
            \\coordinate (D) at (2,0);
            \\coordinate (M) at (1,3);
            \\coordinate (N) at (4,3);
            \\coordinate (P) at (4,1);
            \\coordinate (Q) at (1,1);
            \\draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
            \\draw (M) -- (N) -- (P) -- (Q) -- cycle;
            %s
            \\node[left] at (A) {$A$};
            \\node[above] at (B) {$B$};
            \\node[right] at (C) {$C$};
            \\node[below] at (D) {$D$};
            \\node[above left] at (M) {$M$};
            \\node[above right] at (N) {$N$};
            \\node[below right] at (P) {$P$};
            \\node[below left] at (Q) {$Q$};
            \\end{tikzpicture}
            \\end{center}''' % draw_diag)

                # Nội dung lời giải
                if diag == 'AC':
                    loigiai = ('''%s
            Ta có $MN \\parallel PQ, MN = PQ$ (do cùng song song và bằng $\\frac{1}{2}AC$).\\\\
            Do đó $MNPQ$ là hình bình hành.\\\\
            Vậy các vectơ tạo thành từ các điểm đã cho cùng hướng với vectơ $%s$ là: $%s, %s$. Có tất cả $2$ vectơ thỏa mãn.''' % (code_hinh, target, v1, v2))
                else:
                    loigiai = ('''%s
            Ta có $MQ \\parallel NP, MQ = NP$ (do cùng song song và bằng $\\frac{1}{2}BD$).\\\\
            Do đó $MNPQ$ là hình bình hành.\\\\
            Vậy các vectơ tạo thành từ các điểm đã cho cùng hướng với vectơ $%s$ là: $%s, %s$. Có tất cả $2$ vectơ thỏa mãn.''' % (code_hinh, target, v1, v2))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

