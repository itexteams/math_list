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


def bt_dang24_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Ta random tỉ lệ SA/AC để tạo ra các góc 30, 45, 60 độ
            list_scenarios = [
                {'sa': 'a\\sqrt{2}', 'tan': '1', 'goc': 45},
                {'sa': 'a\\sqrt{6}', 'tan': '\\sqrt{3}', 'goc': 60},
                {'sa': '\\frac{a\\sqrt{6}}{3}', 'tan': '\\frac{\\sqrt{3}}{3}', 'goc': 30}
            ]

            sce = random.choice(list_scenarios)
            sa_val = sce['sa']
            tan_val = sce['tan']
            kq_val = sce['goc']

            # B4: Điều chỉnh phương án sai không trùng đáp án đúng
            options = [30, 45, 60, 90]
            if kq_val in options:
                options.remove(kq_val)
            random.shuffle(options)

            # Câu hỏi
            noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh $a$, $SA$ vuông góc với mặt phẳng đáy và $SA = %s$. Góc giữa đường thẳng $SC$ và mặt phẳng đáy bằng'
                             % (sa_val))

            # Các đáp án
            da_d = ('\\True $%s^\\circ$' % (kq_val))
            da_s1 = ('$%s^\\circ$' % (options[0]))
            da_s2 = ('$%s^\\circ$' % (options[1]))
            da_s3 = ('$%s^\\circ$' % (options[2]))

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # B2: Lời giải chi tiết (Sửa lỗi %% và định dạng \left \right)
            # Lưu ý: Trong TikZ tọa độ vẫn dùng dấu chấm (2.5) để LaTeX hiểu, 
            # nhưng văn bản toán học dùng dấu phẩy theo yêu cầu.
            loigiai = ('\\begin{center}\n'
                       '\\begin{tikzpicture}[scale=1, line width=1pt, font=\\footnotesize]\n'
                       '\\coordinate (A) at (0,0);\n'
                       '\\coordinate (B) at (-1.5,-1);\n'
                       '\\coordinate (C) at (2.5,-1);\n'
                       '\\coordinate (D) at (4,0);\n'
                       '\\coordinate (S) at (0,3);\n'
                       '\\draw[dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C);\n'
                       '\\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D);\n'
                       '\\draw (0,0.3)--(0.3,0.3)--(0.3,0); %% Ky hieu goc vuong tai A\n'
                       '\\node[left] at (A) {$A$};\n'
                       '\\node[below left] at (B) {$B$};\n'
                       '\\node[below right] at (C) {$C$};\n'
                       '\\node[right] at (D) {$D$};\n'
                       '\\node[above] at (S) {$S$};\n'
                       '\\end{tikzpicture}\n'
                       '\\end{center}\n'
                       'Do $SA \\perp \\left(ABCD\\right)$ nên $AC$ là hình chiếu vuông góc của $SC$ lên mặt phẳng đáy $\\left(ABCD\\right)$. \\\\\n'
                       'Khi đó góc giữa đường thẳng $SC$ và mặt phẳng đáy bằng góc $\\widehat{SCA}$. \\\\\n'
                       'Vì đáy $ABCD$ là hình vuông cạnh $a$ nên đường chéo $AC = a\\sqrt{2}$. \\\\\n'
                       'Xét tam giác $SAC$ vuông tại $A$, ta có: \\\\\n'
                       '$\\tan \\widehat{SCA} = \\frac{SA}{AC} = \\frac{%s}{a\\sqrt{2}} = %s$. \\\\\n'
                       'Suy ra $\\widehat{SCA} = %s^\\circ$.'
                       % (sa_val, tan_val, kq_val))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

