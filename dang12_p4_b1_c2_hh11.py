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


def bt_dang12_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Cách random: Thay đổi nhãn (tên) của các đỉnh tứ diện.
            list_vertices = [
                ('A', 'B', 'C', 'D'),
                ('S', 'A', 'B', 'C'),
                ('M', 'N', 'P', 'Q'),
                ('P', 'Q', 'R', 'S')
            ]
            v = random.choice(list_vertices)
            v1, v2, v3, v4 = v[0], v[1], v[2], v[3]

            # Đỉnh chung của hai tam giác đều là v1, v2. Cạnh cần tính góc là v1v2 và v3v4.
            # Trung điểm M của v1v2.

            # Các phương án nhiễu
            wrong_options = ['30^\\circ', '45^\\circ', '60^\\circ', '120^\\circ', '150^\\circ']
            random.shuffle(wrong_options)

            # BƯỚC 4: Điều chỉnh các phương án không trùng với đáp án đúng (90 độ)
            da_d = '\\True $90^\\circ$'
            da_s1 = '$' + wrong_options[0] + '$'
            da_s2 = '$' + wrong_options[1] + '$'
            da_s3 = '$' + wrong_options[2] + '$'

            # Đưa các đáp án vào danh sách và xáo trộn
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho tứ diện $%s%s%s%s$ có hai mặt $%s%s%s$ và $%s%s%s$ là các tam giác đều. '
                'Tính góc giữa hai đường thẳng $%s%s$ và $%s%s$.'
                % (v1, v2, v3, v4, v1, v2, v3, v1, v2, v4, v1, v2, v3, v4)
            )

            # Hình vẽ TikZ
            tikz_code = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round]\n'
                '\\coordinate (B) at (0,0); \n'
                '\\coordinate (C) at (1.5,-1.5); \n'
                '\\coordinate (D) at (4,0); \n'
                '\\coordinate (M) at ($(B)!0.5!(D)$); \n'
                '\\coordinate (A) at ($(M)+(0,3)$); \n'
                '\\draw (A)--(B)--(C)--cycle; \n'
                '\\draw (A)--(C)--(D)--(A); \n'
                '\\draw[dashed] (B)--(D) (A)--(M) (C)--(M); \n'
                '\\node[above] at (A) {$%s$}; \n'
                '\\node[left] at (B) {$%s$}; \n'
                '\\node[below] at (C) {$%s$}; \n'
                '\\node[right] at (D) {$%s$}; \n'
                '\\node[above left] at (M) {$M$}; \n'
                '\\end{tikzpicture}\n'
                '\\end{center}' % (v1, v2, v3, v4)
            )

            # Nội dung lời giải chi tiết
            loigiai = (
                tikz_code +
                'Gọi $M$ là trung điểm của $%s%s$. \\\\'
                'Vì hai mặt $%s%s%s$ và $%s%s%s$ là các tam giác đều nên $%sM \\perp %s%s$ và $%sM \\perp %s%s$. \\\\'
                'Khi đó: $\\vec{%s%s} \\cdot \\vec{%s%s} = \\vec{%s%s} \\cdot (\\vec{%sM} + \\vec{M%s}) = \\vec{%s%s} \\cdot \\vec{%sM} + \\vec{%s%s} \\cdot \\vec{M%s}$. \\\\'
                'Vì $%s%s \\perp %sM$ và $%s%s \\perp %sM$ nên $\\vec{%s%s} \\cdot \\vec{%sM} = 0$ và $\\vec{%s%s} \\cdot \\vec{M%s} = 0$. \\\\'
                'Suy ra $\\vec{%s%s} \\cdot \\vec{%s%s} = 0$. \\\\'
                'Vậy góc giữa hai đường thẳng $%s%s$ và $%s%s$ là $90^\\circ$.'
                % (v1, v2, v1, v2, v3, v1, v2, v4, v3, v1, v2, v4, v1, v2, 
                   v1, v2, v3, v4, v1, v2, v3, v4, v1, v2, v3, v1, v2, v4,
                   v1, v2, v3, v1, v2, v4, v1, v2, v3, v1, v2, v4,
                   v1, v2, v3, v4, v1, v2, v3, v4)
            )

            # Xuất câu trắc nghiệm (không dùng raw string r'' theo yêu cầu)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

