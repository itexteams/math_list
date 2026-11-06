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


def bt_dang32_p1_b1_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Random bài toán bằng cách hoán đổi tên các đỉnh của tứ diện và các điểm trung điểm
                # Các bộ tên đỉnh phổ biến
                vertices_list = [['A', 'B', 'C', 'D'], ['S', 'A', 'B', 'C'], ['M', 'N', 'P', 'Q'], ['E', 'F', 'G', 'H']]
                verts = random.choice(vertices_list)
                v1, v2, v3, v4 = verts[0], verts[1], verts[2], verts[3]

                # Tập hợp các chữ cái cho trung điểm (loại bỏ các chữ cái đã dùng cho đỉnh)
                midpoints_list = ['I', 'J', 'K', 'L', 'X', 'Y', 'U', 'V']
                avail_midpoints = [m for m in midpoints_list if m not in verts]
                m1, m2 = random.sample(avail_midpoints, 2)

                # Tạo chuỗi vector để đưa vào đề và lời giải
                vec_v1v2 = '\\overrightarrow{%s%s}' % (v1, v2)
                vec_v4v3 = '\\overrightarrow{%s%s}' % (v4, v3)
                vec_m1m2 = '\\overrightarrow{%s%s}' % (m1, m2)
                vec_m2m1 = '\\overrightarrow{%s%s}' % (m2, m1)
                vec_v1v4 = '\\overrightarrow{%s%s}' % (v1, v4)
                vec_v2v3 = '\\overrightarrow{%s%s}' % (v2, v3)

                vec_v1m1 = '\\overrightarrow{%s%s}' % (v1, m1)
                vec_m1m2_sol = '\\overrightarrow{%s%s}' % (m1, m2)
                vec_m2v2 = '\\overrightarrow{%s%s}' % (m2, v2)
                vec_v4m1 = '\\overrightarrow{%s%s}' % (v4, m1)
                vec_m2v3 = '\\overrightarrow{%s%s}' % (m2, v3)

                # Các đáp án
                da = '2%s' % vec_m1m2
                das1 = '\\overrightarrow{0}'
                das2 = '2%s' % vec_v1v4
                das3 = '2%s' % vec_m2m1

                # B8: Hình vẽ bằng TikZ (đã sửa lỗi khoảng trắng trong thư viện calc)
                tikz_code = '''\\begin{tikzpicture}[scale=0.5, line join=round, line cap=round, line width=1pt]
            \\coordinate (%s) at (5,6);
            \\coordinate (%s) at (0,2);
            \\coordinate (%s) at (3,-2);
            \\coordinate (%s) at (9,2);
            \\coordinate (%s) at ($(%s)!0.5!(%s)$);
            \\coordinate (%s) at ($(%s)!0.5!(%s)$);
            \\draw (%s)--(%s) (%s)--(%s) (%s)--(%s) (%s)--(%s) (%s)--(%s);
            \\draw[dashed] (%s)--(%s) (%s)--(%s);
            \\fill (%s) circle (0pt) node[above] {$%s$};
            \\fill (%s) circle (0pt) node[left] {$%s$};
            \\fill (%s) circle (0pt) node[below] {$%s$};
            \\fill (%s) circle (0pt) node[right] {$%s$};
            \\fill (%s) circle (0pt) node[above right] {$%s$};
            \\fill (%s) circle (0pt) node[below left] {$%s$};
            \\end{tikzpicture}''' % (v1, v2, v3, v4, m1, v1, v4, m2, v2, v3,
                                v1, v2, v2, v3, v3, v4, v4, v1, v1, v3,
                                v2, v4, m1, m2,
                                v1, v1, v2, v2, v3, v3, v4, v4, m1, m1, m2, m2)

                # Câu hỏi
                noidungcauhoi = ('\\immini{Cho tứ diện $%s%s%s%s$. Gọi $%s$, $%s$ lần lượt là trung điểm của $%s%s$ và $%s%s$. Tổng $%s + %s$ bằng}{ %s}'
                                 %(v1, v2, v3, v4, m1, m2, v1, v4, v2, v3, vec_v1v2, vec_v4v3, tikz_code))

                # Các đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = '$%s$' % das1
                da_s2 = '$%s$' % das2 
                da_s3 = '$%s$' % das3 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Ta có: $%s + %s = %s + %s + %s + %s + %s + %s$ \\\\ \n'
                           '$= \\left(%s + %s\\right) + 2%s + \\left(%s + %s\\right) = 2%s$. \\\\ \n'
                           '(Vì $%s$, $%s$ lần lượt là trung điểm của $%s%s$ và $%s%s$ nên $%s + %s = \\overrightarrow{0}$, $%s + %s = \\overrightarrow{0}$).'
                           % (vec_v1v2, vec_v4v3, vec_v1m1, vec_m1m2_sol, vec_m2v2, vec_v4m1, vec_m1m2_sol, vec_m2v3,
                              vec_v1m1, vec_v4m1, vec_m1m2_sol, vec_m2v2, vec_m2v3, vec_m1m2_sol,
                              m1, m2, v1, v4, v2, v3, vec_v1m1, vec_v4m1, vec_m2v2, vec_m2v3))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

