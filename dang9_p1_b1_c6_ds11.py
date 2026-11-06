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


def bt_dang9_p1_b1_c6_ds11(self):
            # Khai báo biến
            # B1 & B3: Phân tích và thiết lập logic random
            lis_names = ['An', 'Bình', 'Hùng', 'Dũng', 'Mai', 'Lan', 'Nam', 'Việt', 'Cường', 'Tuấn']
            name1, name2 = random.sample(lis_names, 2)

            # Randomize tính chất của biến cố A: số lẻ hoặc số chẵn
            # Cả hai trường hợp đều có n(A) = 3
            props = [('số lẻ', '{1, 3, 5}'), ('số chẵn', '{2, 4, 6}')]
            prop_selected = random.choice(props)
            prop_text = prop_selected[0]
            set_A_str = prop_selected[1]

            # Biến cố A mô tả trong câu hỏi
            A_desc = '“' + name1 + ' gieo được mặt có ' + prop_text + ' chấm”'

            # --- Tạo các phương án ---

            # Đáp án đúng (D): Người thứ hai gieo được mặt có n=3 (lẻ hoặc chẵn)
            # Để đảm bảo độc lập, biến cố phải thuộc về lần gieo của người thứ hai (name2)
            da_dung_str = name2 + ' gieo được mặt có ' + prop_text + ' chấm'

            # Đáp án sai 1: Người thứ nhất gieo được mặt cụ thể (n=1, phụ thuộc)
            face1 = random.randint(1, 6)
            da_sai1_str = name1 + ' gieo được mặt ' + str(face1) + ' chấm'

            # Đáp án sai 2: Người thứ nhất gieo được mặt cụ thể khác (n=1, phụ thuộc)
            face2 = random.randint(1, 6)
            while face2 == face1:
                face2 = random.randint(1, 6)
            da_sai2_str = name1 + ' gieo được mặt ' + str(face2) + ' chấm'

            # Đáp án sai 3: Người thứ hai gieo được mặt cụ thể (n=1, độc lập nhưng số phần tử sai)
            face3 = random.randint(1, 6)
            da_sai3_str = name2 + ' gieo được mặt ' + str(face3) + ' chấm'

            # --- Thiết lập nội dung theo mẫu ---

            # Câu hỏi
            noidungcauhoi = (name1 + ' và ' + name2 + ' mỗi người gieo một con xúc xắc cân đối và đồng chất. '
                             'Gọi $A$ là biến cố ' + A_desc + ', biến cố nào sau đây vừa độc lập '
                             'với biến cố $A$ vừa có số phần tử bằng với số phần tử của biến cố $A$?')

            # Gán đáp án
            da_d = ('\\True ' + da_dung_str)
            da_s1 = da_sai1_str
            da_s2 = da_sai2_str
            da_s3 = da_sai3_str

            # Xáo trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết không viết tắt
            loigiai = ('Ta có $A = ' + set_A_str + ' \\Rightarrow n(A) = 3$. \\\\ '
                       'Biến cố “' + da_sai1_str[:-1] + '” không độc lập với biến cố $A$ và có số phần tử bằng 1. \\\\ '
                       'Biến cố “' + da_sai2_str[:-1] + '” không độc lập với biến cố $A$ và có số phần tử bằng 1. \\\\ '
                       'Biến cố “' + da_sai3_str[:-1] + '” độc lập với biến cố $A$ (' + name2 + ' gieo nên xác suất xảy ra không làm ảnh hưởng đến xác suất biến cố $A$) và có số phần tử bằng 1. \\\\ '
                       'Biến cố “' + da_dung_str[:-1] + '” độc lập với biến cố $A$ (' + name2 + ' gieo nên xác suất xảy ra không làm ảnh hưởng đến xác suất biến cố $A$) và có số phần tử bằng 3. \\\\ '
                       'Do đó chọn “' + da_dung_str[:-1] + '” thỏa mãn yêu cầu bài toán.')

            # B2: Xuất câu trắc nghiệm theo đúng cấu trúc mẫu (không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

