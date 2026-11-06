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


def bt_dang28_p4_b3_c2_hh11(self):
            # Khai báo biến
            # Để random, ta thay đổi hệ số k của cạnh 'a'.

            list_k = [1, 2, 3, 4, 5]
            k = random.choice(list_k)
            side_val = str(k) + 'a' if k > 1 else 'a'

            # Tính toán các giá trị để tạo đáp án nhiễu
            # Đáp án đúng: sin = 1/sqrt(3) = sqrt(3)/3
            ans_correct = '$\\frac{1}{\\sqrt{3}}$'

            # Tạo danh sách đáp án nhiễu
            distractors = [
                '$\\frac{\\sqrt{6}}{3}$',
                '$\\frac{\\sqrt{2}}{2}$',
                '$\\frac{\\sqrt{3}}{2}$',
                '$\\frac{1}{2}$',
                '$\\frac{2}{3}$',
                '$\\frac{\\sqrt{5}}{3}$'
            ]
            random.shuffle(distractors)
            selected_distractors = distractors[:3]

            # --- BƯỚC 2 & 4: VIẾT LỜI GIẢI VÀ ĐIỀU CHỈNH ---

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho hình chóp $S.ABC$ có $SA, SB, SC$ đôi một vuông góc với nhau và $SA = SB = SC = %s$. '
                'Tính sin của góc giữa đường thẳng $SC$ và mặt phẳng $\\left( ABC \\right)$.'
                % (side_val)
            )

            # Hình vẽ TikZ
            hinh_ve = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1.2, line join=round, line cap=round, line width=1pt]\n'
                '\\coordinate (S) at (0,0);\n'
                '\\coordinate (C) at (0,3);\n'
                '\\coordinate (B) at (-1.5,-1.2);\n'
                '\\coordinate (A) at (2.5,-0.5);\n'
                '\\coordinate (F) at (0.5,-0.85);\n'
                '\\coordinate (K) at (-0.75, 0.9);\n'
                '\\coordinate (E) at (0.2, 0.4);\n'
                '\\draw[dashed] (B)--(S)--(A) (S)--(C) (B)--(A) (S)--(E) (S)--(F);\n'
                '\\draw (C)--(B)--(A)--cycle;\n'
                '\\draw (C)--(S);\n'
                '\\draw (A)--(K) (C)--(F);\n'
                '\\fill (S)  node[below left]{$S$};\n'
                '\\fill (A)  node[right]{$A$};\n'
                '\\fill (B)  node[left]{$B$};\n'
                '\\fill (C)  node[above]{$C$};\n'
                '\\fill (E)  node[above right]{$E$};\n'
                '\\fill (F)  node[below]{$F$};\n'
                '\\fill (K)  node[left]{$K$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            # Nội dung lời giải chi tiết
            # SE = a*k/sqrt(3), SC = a*k => sin = 1/sqrt(3)
            # Chú ý: Thay thế dấu . bằng , nếu có số thập phân (ở đây dùng k nguyên nên ít gặp)
            loigiai = (
                'Trong tam giác $ABC$ kẻ đường cao $AK$ và $CF$ và $AK \\cap CF = \\left\\{ E \\right\\}$ nên $E$ là trực tâm tam giác $ABC$.\\\\ '
                'Ta có: $\\begin{cases} SC \\perp SA \\\\ SC \\perp SB \\end{cases} \\Rightarrow SC \\perp \\left( SAB \\right)$ hay $SC \\perp AB$.\\\\ '
                'Mà $CF \\perp AB$ nên $AB \\perp \\left( SCF \\right) \\Rightarrow AB \\perp SE$. Chứng minh tương tự ta được '
                '$BC \\perp \\left( SAK \\right) \\Rightarrow BC \\perp SE$. Vậy $SE \\perp \\left( ABC \\right)$.\\\\ '
                'Ta có $CE$ là hình chiếu của $SC$ lên mặt phẳng $\\left( ABC \\right)$.\\\\ '
                '$\\Rightarrow \\left( SC, \\left( ABC \\right) \\right) = \\left( SC, CE \\right) = \\widehat{SCE}$.\\\\ '
                'Ta có tam giác $SCF$ vuông tại $S$ nên $\\frac{1}{SE^2} = \\frac{1}{SC^2} + \\frac{1}{SF^2}$. Mặt khác tam giác $SAB$ vuông tại $S$ '
                'nên $\\frac{1}{SF^2} = \\frac{1}{SA^2} + \\frac{1}{SB^2}$.\\\\ '
                'Suy ra $\\frac{1}{SE^2} = \\frac{1}{SC^2} + \\frac{1}{SA^2} + \\frac{1}{SB^2} = \\frac{3}{\\left( %s \\right)^2} \\Rightarrow SE = \\frac{%s}{\\sqrt{3}}$.\\\\ '
                'Xét tam giác $SCE$ vuông tại $E$: $\\sin \\widehat{SCE} = \\frac{SE}{SC} = \\frac{%s}{\\sqrt{3}} : %s = \\frac{1}{\\sqrt{3}}$.'
                % (side_val, side_val, side_val, side_val)
            ).replace('.', ',')

            # Chuẩn bị danh sách đáp án để shuffle
            da_d = '\\True ' + ans_correct
            list_ans = [da_d] + selected_distractors
            random.shuffle(list_ans)

            # Xuất nội dung theo cấu trúc mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\loigiai{' + hinh_ve+ loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

