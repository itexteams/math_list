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


def bt_dang11_p1_b1_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lis_k = [2, 4, 6] # Chọn k chẵn để B và C luôn có phần tử chung (không xung khắc)
            k = random.choice(lis_k)

            # Thiết lập các tập hợp biến cố dưới dạng chuỗi LaTeX
            set_A = r"\{(1,1);(1,3);(1,5);(3,1);(3,3);(3,5);(5,1);(5,3);(5,5)\}"
            set_B = r"\{(2,2);(2,4);(2,6);(4,2);(4,4);(4,6);(6,2);(6,4);(6,6)\}"
            # Biến cố C phụ thuộc vào k
            elements_C = [f"({k},{i})" for i in range(1, 7)]
            set_C = r"\{" + ";".join(elements_C) + r"\}"

            # Các phần tử chung của B và C
            common_BC = [f"({k},{i})" for i in [2, 4, 6]]
            set_BC = r"\{" + ";".join(common_BC) + r"\}"

            # Câu hỏi
            noidungcauhoi = ('''Gieo một con xúc xắc cân đối và đồng chất $2$ lần. Xét các biến cố:\\\\
            $A$: "Số chấm xuất hiện trong hai lần gieo đều là số lẻ".\\\\
            $B$: "Số chấm xuất hiện trong hai lần gieo đều là số chẵn".\\\\
            $C$: "Số chấm xuất hiện trong lần gieo thứ nhất là $%s$".
            Khẳng định nào sau đây là \\textbf{sai}?''' % (latex(k)))

            # Các phương án
            # Đáp án sai (da_d) - khẳng định sai là "B và C xung khắc" trong khi thực tế chúng không xung khắc
            da_d = r'\True Hai biến cố $B$ và $C$ xung khắc'
            da_s1 = r'Hai biến cố $A$ và $B$ xung khắc'
            da_s2 = r'Hai biến cố $A$ và $C$ xung khắc'
            da_s3 = r'Hai biến cố $B$ và $C$ không xung khắc'

            # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = ('''Ta có: \\\\
            $A = %s$. \\\\
            $B = %s$. \\\\
            $C = %s$. \\\\
            Khi đó: \\\\
            $A \\cap B = \\emptyset$ nên $A$ và $B$ xung khắc. \\\\
            $A \\cap C = \\emptyset$ nên $A$ và $C$ xung khắc (vì $A$ chỉ gồm các số lẻ, mà lần gieo đầu của $C$ là số chẵn $%s$). \\\\
            $B \\cap C = %s \\neq \\emptyset$ nên $B$ và $C$ \\textbf{không xung khắc}. \\\\
            Vậy khẳng định "Hai biến cố $B$ và $C$ xung khắc" là khẳng định sai.''' 
            %(set_A, set_B, set_C, latex(k), set_BC))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

