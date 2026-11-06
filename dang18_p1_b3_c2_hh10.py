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


def bt_dang18_p1_b3_c2_hh10(self):
            # Khai báo biến
            # 1. Random đỉnh và trung tuyến tương ứng (Đỉnh, Trung điểm)
            list_vertices = [('A', 'M'), ('B', 'N'), ('C', 'P')]
            vertex, midpoint = random.choice(list_vertices)
            G = 'G' # Trọng tâm

            # Tìm 2 đỉnh còn lại để dựng hình (Ví dụ: chọn A thì còn B và C)
            vertices_set = {'A', 'B', 'C'}
            other_vertices = list(vertices_set - {vertex})
            v2, v3 = other_vertices[0], other_vertices[1]

            # 2. Kho các quan hệ đúng (vector 1, vector 2, hệ số k) theo đỉnh đã chọn
            relations = [
                (f"\\overrightarrow{{{vertex}{G}}}", f"\\overrightarrow{{{vertex}{midpoint}}}", "\\frac{2}{3}"),
                (f"\\overrightarrow{{{G}{vertex}}}", f"\\overrightarrow{{{vertex}{midpoint}}}", "-\\frac{2}{3}"),
                (f"\\overrightarrow{{{G}{midpoint}}}", f"\\overrightarrow{{{vertex}{midpoint}}}", "\\frac{1}{3}"),
                (f"\\overrightarrow{{{midpoint}{G}}}", f"\\overrightarrow{{{vertex}{midpoint}}}", "-\\frac{1}{3}"),
                (f"\\overrightarrow{{{vertex}{G}}}", f"\\overrightarrow{{{G}{midpoint}}}", "2"),
                (f"\\overrightarrow{{{G}{vertex}}}", f"\\overrightarrow{{{G}{midpoint}}}", "-2"),
                (f"\\overrightarrow{{{vertex}{midpoint}}}", f"\\overrightarrow{{{vertex}{G}}}", "\\frac{3}{2}")
            ]

            # Random chọn 1 quan hệ đúng làm đáp án
            vec1, vec2, true_ratio = random.choice(relations)

            # 3. Tạo các hệ số nhiễu phổ biến (Tránh lỗi +- bằng cách set thẳng text)
            distractors_pool = ["\\frac{1}{2}", "-\\frac{1}{2}", "\\frac{1}{3}", "-\\frac{1}{3}", "\\frac{2}{3}", "-\\frac{2}{3}", "2", "-2", "\\frac{3}{2}", "-\\frac{3}{2}"]

            # Loại bỏ hệ số đúng ra khỏi danh sách nhiễu
            if true_ratio in distractors_pool:
                distractors_pool.remove(true_ratio)

            # Bốc ngẫu nhiên 3 hệ số sai làm nhiễu
            distractors = random.sample(distractors_pool, 3)

            # 4. Nội dung câu hỏi
            noidungcauhoi = f"Cho $\\Delta ABC$ với trung tuyến ${vertex}{midpoint}$ và trọng tâm $G$. Khi đó đẳng thức nào dưới đây đúng?"

            # 5. Khởi tạo các đáp án
            da = f"${vec1} = {true_ratio}{vec2}$"
            das1 = f"${vec1} = {distractors[0]}{vec2}$"
            das2 = f"${vec1} = {distractors[1]}{vec2}$"
            das3 = f"${vec1} = {distractors[2]}{vec2}$"

            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # 6. Vẽ hình TikZ tự động theo đỉnh và đường trung tuyến được random
            tikz_code = f"""\\begin{{center}}
            \\begin{{tikzpicture}}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (1,2.5);
            \\coordinate (B) at (0,0);
            \\coordinate (C) at (4,0);
            \\path ({v2}) -- ({v3}) coordinate[midway] ({midpoint});
            \\path ({vertex}) -- ({midpoint}) coordinate[pos=0.667] (G);
            \\draw (A)--(B)--(C)--cycle;
            \\draw ({vertex})--({midpoint});
            \\fill (A) circle (1.2pt) node[above] {{$A$}};
            \\fill (B) circle (1.2pt) node[below left] {{$B$}};
            \\fill (C) circle (1.2pt) node[below right] {{$C$}};
            \\fill ({midpoint}) circle (1.2pt) node[below] {{${midpoint}$}};
            \\fill (G) circle (1.2pt) node[above right] {{$G$}};
            \\end{{tikzpicture}}
            \\end{{center}}"""

            # 7. Nội dung lời giải (Chèn kèm hình ảnh tikz_code)
            loigiai = (f"Vì $G$ là trọng tâm $\\Delta ABC$ nên xét trên trung tuyến ${vertex}{midpoint}$, "
                       f"ta có tỉ lệ các đoạn thẳng là ${vertex}{G} = 2{G}{midpoint}$ và ${vertex}{G} = \\frac{{2}}{{3}}{vertex}{midpoint}$.\\\\ "
                       f"Dựa vào hướng của vector, ta suy ra đẳng thức đúng là: ${vec1} = {true_ratio}{vec2}$."
                       f"{tikz_code}")


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

