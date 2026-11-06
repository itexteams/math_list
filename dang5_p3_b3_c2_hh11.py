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


def bt_dang5_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo các ký hiệu toán học
            a = symbols('a')

            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các trường hợp góc để bài toán đa dạng
                # Case 1: SA = a*sqrt(2) -> Góc 45 độ
                # Case 2: SA = a*sqrt(6) -> Góc 60 độ
                # Case 3: SA = a*sqrt(6)/3 -> Góc 30 độ

                case = random.choice(['45', '60', '30'])

                if case == '45':
                    val_sa = a * sqrt(2)
                    kq_doc = 45
                    tan_val = "1"
                elif case == '60':
                    val_sa = a * sqrt(6)
                    kq_doc = 60
                    tan_val = "\\sqrt{3}"
                else:
                    val_sa = a * Rational(1, 3) * sqrt(6)
                    kq_doc = 30
                    tan_val = "\\frac{\\sqrt{3}}{3}"

                # Đáp án đúng
                da_dung = "$%s^\\circ$" % (kq_doc)

                # Tạo danh sách đáp án sai
                s = ["$30^\\circ$", "$45^\\circ$", "$60^\\circ$", "$90^\\circ$"]
                if da_dung in s:
                    s.remove(da_dung)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ("Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABCD)$ và $SA = %s$. Góc giữa đường thẳng $SC$ và mặt phẳng $(ABCD)$ bằng bao nhiêu?"
                                 % (latex(val_sa)))

                # Nội dung lời giải chi tiết
                loigiai = ("\\begin{center}\n"
                             "\\begin{tikzpicture}[scale=0.8, line width=1pt, font=\\footnotesize]\n"
                             "\\coordinate (A) at (0,2.5);\n"
                             "\\coordinate (B) at (-1.5,0);\n"
                             "\\coordinate (C) at (2.5,0);\n"
                             "\\coordinate (D) at (4,2.5);\n"
                             "\\coordinate (S) at (0,5.5);\n"
                             "\\draw [dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C);\n"
                             "\\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D);\n"
                             "\\foreach \\p/\\pos in {S/above, A/left, B/below left, C/below right, D/right} \n"
                             "\\fill (\\p) node[\\pos] {$\\p$};\n"
                             "\\draw (0,2.8) -- (0.3,2.8) -- (0.3,2.5);\n" # Ký hiệu vuông góc tại A
                             "\\end{tikzpicture}\n"
                             "\\end{center}"
                    "Vì $SA \\perp (ABCD)$ nên $AC$ là hình chiếu vuông góc của $SC$ lên mặt phẳng $(ABCD)$. \\\\"
                           "Do đó, góc giữa đường thẳng $SC$ và mặt phẳng $(ABCD)$ là góc giữa $SC$ và $AC$, hay là góc $\\widehat{SCA}$. \\\\"
                           "Xét hình vuông $ABCD$ cạnh $a$, ta có độ dài đường chéo $AC = a\\sqrt{2}$. \\\\"
                           "Xét tam giác $SAC$ vuông tại $A$ (vì $SA \\perp (ABCD) \\Rightarrow SA \\perp AC$), ta có: \\\\"
                           "$\\tan \\widehat{SCA} = \\frac{SA}{AC} = \\frac{%s}{a\\sqrt{2}} = %s$. \\\\"
                           "Suy ra $\\widehat{SCA} = %s^\\circ$. \\\\"
                           "Vậy góc giữa đường thẳng $SC$ và mặt phẳng $(ABCD)$ bằng $%s^\\circ$."
                           % (latex(val_sa), tan_val, kq_doc, kq_doc))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_doc))

                # Đưa các đáp án vào danh sách shuffle
                da_d = "\\True " + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

