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


def bt_dang63_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và chọn ngẫu nhiên tên cạnh
            lis_edge = ['a', 'x', 'b', 'c']
            e = random.choice(lis_edge)

            # Các phương án nhiễu
            ans_true = '\\frac{1}{3}'
            s = [
                '\\frac{\\sqrt{2}}{2}',
                '\\frac{\\sqrt{3}}{3}',
                '\\frac{2}{3}',
                '\\frac{1}{2}',
                '\\frac{\\sqrt{2}}{4}',
                '\\frac{\\sqrt{6}}{3}'
            ]

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$. Gọi $M$ là trung điểm của $SD$. '
                'Tang của góc giữa đường thẳng $BM$ và mặt phẳng $\\left(ABCD\\right)$ bằng'
                % (e)
            )

            # Các đáp án
            da_d = ('\\True $' + ans_true + '$')
            da_s1 = '$' + das1 + '$'
            da_s2 = '$' + das2 + '$'
            da_s3 = '$' + das3 + '$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ 100% giống ảnh
            hinh_ve = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth, line width=1pt]\n'
                '    \\tkzDefPoints{0/0/O, -1.2/0.8/A, -2.5/-1.2/B, 1.5/-1.2/C}\n'
                '    \\tkzDefPointBy[symmetry=center O](B)\\tkzGetPoint{D}\n'
                '    \\tkzDefShiftPoint[O](90:4){S}\n'
                '    \\tkzDefMidPoint(S,D)\\tkzGetPoint{M}\n'
                '    \\tkzDefMidPoint(O,D)\\tkzGetPoint{H}\n'
                '    \\tkzDrawSegments[dashed](S,A A,B A,D A,C B,D S,O M,H B,M)\n'
                '    \\tkzDrawSegments(S,B S,C S,D B,C C,D)\n'
                '    \\tkzLabelPoints[above](S)\n'
                '    \\tkzLabelPoints[below left](B)\n'
                '    \\tkzLabelPoints[below](O,C)\n'
                '    \\tkzLabelPoints[left](A)\n'
                '    \\tkzLabelPoints[right](D)\n'
                '    \\tkzLabelPoints[above right](M)\n'
                '    \\tkzLabelPoints[below right](H)\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            # Lời giải chi tiết
            loigiai = (
                'Gọi $O$ là tâm của hình vuông. Ta có $SO \\perp \\left(ABCD\\right)$ và '
                '$SO = \\sqrt{%s^2 - \\left(\\frac{%s\\sqrt{2}}{2}\\right)^2} = \\frac{%s\\sqrt{2}}{2}$. \\\\'
                'Gọi $M$ là trung điểm của $SD$, kẻ $MH // SO$ $\\left(H \\in OD\\right)$ nên $H$ là hình chiếu của $M$ lên mặt phẳng '
                '$\\left(ABCD\\right)$ và $MH = \\frac{1}{2} SO = \\frac{%s\\sqrt{2}}{4}$. \\\\'
                'Do đó góc giữa đường thẳng $BM$ và mặt phẳng $\\left(ABCD\\right)$ là góc giữa $BM$ và hình chiếu $BH$, chính là $\\widehat{MBH}$. \\\\'
                'Ta có $BH = BO + OH = \\frac{1}{2}BD + \\frac{1}{4}BD = \\frac{3}{4}BD = \\frac{3%s\\sqrt{2}}{4}$. \\\\'
                'Khi đó ta có $\\tan \\widehat{MBH} = \\frac{MH}{BH} = \\frac{\\frac{%s\\sqrt{2}}{4}}{\\frac{3%s\\sqrt{2}}{4}} = \\frac{1}{3}$. \\\\'
                'Vậy tang của góc giữa đường thẳng $BM$ và mặt phẳng $\\left(ABCD\\right)$ bằng $\\frac{1}{3}$.'
                % (e, e, e, e, e, e, e)
            )

            # Xuất nội dung theo cấu trúc mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'
                + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{\n' + str(hinh_ve) + '\n' + str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

