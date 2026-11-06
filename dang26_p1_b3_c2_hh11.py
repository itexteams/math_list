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


def bt_dang26_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1', '2', '3']
            dang = random.choice(lisdang)

            # Biến số a cố định là biểu tượng
            a = symbols('a')

            if dang == '1':
                # Trường hợp tam giác SBC đều (giống ảnh gốc)
                tan_val = 1
                dk_sbc = "tam giác $SBC$ là tam giác đều"
                kq_tex = "1"
                lg_sbc = "Vì $\\triangle SBC$ là tam giác đều cạnh $a$ nên đường cao $SH = \\frac{a\\sqrt{3}}{2}$."

                da_s1 = "$\\sqrt{3}$"
                da_s2 = "$0$"
                da_s3 = "$\\frac{1}{\\sqrt{3}}$"

            elif dang == '2':
                # Trường hợp SH = 3/2 * AH => tan = 3/2
                tan_val = Rational(3, 2)
                dk_sbc = "tam giác $SBC$ cân tại $S$ và có diện tích bằng $\\frac{3}{2}$ lần diện tích tam giác $ABC$"
                kq_tex = "\\frac{3}{2}"
                lg_sbc = "Ta có $S_{SBC} = \\frac{3}{2} S_{ABC} \\Rightarrow \\frac{1}{2}SH \\cdot BC = \\frac{3}{2} \\cdot \\frac{1}{2} AH \\cdot BC \\Rightarrow SH = \\frac{3}{2} AH$."

                da_s1 = "$1$"
                da_s2 = "$\\sqrt{3}$"
                da_s3 = "$\\frac{1}{2}$"

            else:
                # Trường hợp SH = sqrt(3) * AH => tan = sqrt(3)
                tan_val = sqrt(3)
                dk_sbc = "tam giác $SBC$ cân tại $S$ có góc $\\widehat{BSC} = 60^\\circ$ và $SH = \\frac{3a}{2}$"
                kq_tex = "\\sqrt{3}"
                lg_sbc = "Ta có $AH = \\frac{a\\sqrt{3}}{2}$ và $SH = \\frac{3a}{2}$."

                da_s1 = "$1$"
                da_s2 = "$\\frac{\\sqrt{3}}{3}$"
                da_s3 = "$2$"

            # Nội dung câu hỏi
            noidungcauhoi = ("Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$. Hình chiếu vuông góc của điểm $S$ lên mặt phẳng $\\left( ABC \\right)$ trùng với trung điểm $H$ của cạnh $BC$. Biết %s. Gọi $\\alpha$ là số đo của góc giữa đường thẳng $SA$ và mặt phẳng $\\left( ABC \\right)$. $\\tan \\alpha$ bằng" 
                             % (dk_sbc))

            # TikZ code
            tikz_code = ("\\begin{center}\n"
                         "\\begin{tikzpicture}[scale=0.8, line width=1pt, line cap=round, line join=round]\n"
                         "\\coordinate (H) at (0,0);\n"
                         "\\coordinate (B) at (-1.5,-1);\n"
                         "\\coordinate (C) at (1.5,1);\n"
                         "\\coordinate (A) at (4,0);\n"
                         "\\coordinate (S) at (0,4);\n"
                         "\\draw [dashed] (B)--(C) (H)--(A) (H)--(S) (A)--(C)--(S);\n"
                         "\\draw (S)--(B)  (S)--(A) (A)--(B);\n"
                         "\\node at (S) [above] {$S$};\n"
                         "\\node at (B) [left] {$B$};\n"
                         "\\node at (C) [right] {$C$};\n"
                         "\\node at (A) [right] {$A$};\n"
                         "\\node at (H) [below left] {$H$};\n"
                         "\\end{tikzpicture}\n"
                         "\\end{center}")

            # Lời giải chi tiết
            loigiai = ("Vì $SH \\perp \\left( ABC \\right)$ nên $AH$ là hình chiếu của $SA$ trên $\\left( ABC \\right)$. \\\\\n"
                       "Suy ra $\\left( SA, \\left( ABC \\right) \\right) = \\left( SA, AH \\right) = \\widehat{SAH} = \\alpha$. \\\\\n"
                       "Tam giác $ABC$ đều cạnh $a$ nên $AH = \\frac{a\\sqrt{3}}{2}$. \\\\\n"
                       "%s \\\\\n"
                       "Xét tam giác $SAH$ vuông tại $H$, ta có: \\\\\n"
                       "$\\tan \\alpha = \\frac{SH}{AH} = %s$." 
                       % (lg_sbc, kq_tex))

            # Xử lý đáp án
            da_d = '\\True $' + kq_tex + '$'
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

