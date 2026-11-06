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


def bt_dang24_p1_b2_c2_hh11(self):
            # Khai báo biến
            # Tuy nhiên, đỉnh S và vị trí chân đường cao (giả sử là đỉnh đầu tiên trong danh sách đáy) được giữ cố định logic
            v1='A'
            v2='B'
            v3='C'
            v4='D'
            S = 'S'

            # B2 & B4: Viết lại nội dung và điều chỉnh phương án
            # Các mệnh đề đúng:
            # 1. v2_v3 vuông góc (S_v1_v2)
            # 2. v4_v3 vuông góc (S_v1_v4)
            # 3. v2_v4 vuông góc (S_v1_v3)
            # Mệnh đề sai:
            # 4. v1_v3 vuông góc (S_v2_v4)

            # Định nghĩa các phương án
            # Lưu ý: Bài toán hỏi mệnh đề SAI, nên mệnh đề logic sai sẽ được đánh dấu \True
            da_d = f'\\True $ {v1}{v3} \\perp \\left({S}{v2}{v4}\\right)$'
            da_s1 = f'${v2}{v3} \\perp \\left({S}{v1}{v2}\\right)$'
            da_s2 = f'$ {v2}{v4} \\perp \\left({S}{v1}{v3}\\right)$'
            da_s3 = f'$ {v3}{v4} \\perp \\left({S}{v1}{v4}\\right)$'

            # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung câu hỏi
            noidungcauhoi = (f'Cho hình chóp ${S}.{v1}{v2}{v3}{v4}$ có đáy ${v1}{v2}{v3}{v4}$ là hình vuông và ${S}{v1}$ vuông góc với đáy. Mệnh đề nào sau đây sai?')



            # Nội dung lời giải chi tiết
            loigiai = (f'''\\begin{{center}} \\begin{{tikzpicture}}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (3.5,0);
                \\coordinate (D) at (-1.2,-1.2);
                \\coordinate (C) at ($(B)+(D)-(A)$);
                \\coordinate (S) at (0,3.5);
                \\draw [line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D);
                \\draw [line width=1pt] (S)--(D)--(C)--(B)--(S)--(C);
                \\fill (A) node[left] {{${v1}$}};
                \\fill (B) node[right] {{${v2}$}};
                \\fill (C) node[below right] {{${v3}$}};
                \\fill (D) node[below left] {{${v4}$}};
                \\fill (S) node[above] {{${S}$}};
            \\end{{tikzpicture}} \\end{{center}}'''
            f'''Ta có: \\\\
            + $\\begin{{cases}} {v2}{v3} \\perp {v1}{v2} \\\\ {v2}{v3} \\perp {S}{v1} \\end{{cases}} \\Rightarrow {v2}{v3} \\perp \\left({S}{v1}{v2}\\right)$.\\\\
            + $\\begin{{cases}} {v3}{v4} \\perp {v1}{v4} \\\\ {v3}{v4} \\perp {S}{v1} \\end{{cases}} \\Rightarrow {v3}{v4} \\perp \\left({S}{v1}{v4}\\right)$.\\\\
            + $\\begin{{cases}} {v2}{v4} \\perp {v1}{v3} \\\\ {v2}{v4} \\perp {S}{v1} \\end{{cases}} \\Rightarrow {v2}{v4} \\perp \\left({S}{v1}{v3}\\right)$.\\\\
            Suy ra mệnh đề ${v1}{v3} \\perp \\left({S}{v2}{v4}\\right)$ là mệnh đề sai (vì ${v1}{v3}$ vuông góc với ${v2}{v4}$ nhưng không vuông góc với bất kỳ đường thẳng nào khác trong mặt phẳng $\\left({S}{v2}{v4}\\right)$ mà có thể chứng minh được một cách trực tiếp).''')

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

