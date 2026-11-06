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


def bt_dang23_p1_b1_c1_ds10(self):
    # Khai báo biến
    # Cấu trúc: (Nội dung, Có phải mệnh đề toán học không?)
    pool_menh_de_toan_hoc = [
        ("Phương trình $x^2 - 3x + 1 = 0$ vô nghiệm.\\\\", True),
        ("16 không là số nguyên tố.\\\\", True),
        ("Hai phương trình $x^2 - 4x + 3 = 0$ và $x^2 - \\sqrt{x+3} + 1 = 0$ có nghiệm chung.\\\\", True),
        ("Italia vô địch Worldcup 2006.\\\\", False), # Mệnh đề logic/lịch sử, không phải mệnh đề TOÁN HỌC
        ("Hai tam giác bằng nhau khi và chỉ khi chúng có diện tích bằng nhau.\\\\", True),
        ("Một tứ giác là hình thoi khi và chỉ khi nó có hai đường chéo vuông góc với nhau.\\\\", True),
        ("Số $\\pi$ là một số hữu tỉ.\\\\", True),
        ("Tổng ba góc trong một tam giác bằng $180^\\circ$.\\\\", True),
        ("$\\sqrt{2}$ là số vô tỉ.\\\\", True),
        ("$22$ chia hết cho $4$.\\\\", True)
    ]

    pool_khong_phai_menh_de = [
        ("Ở đây đẹp quá!\\\\", False),
        ("Số $\\pi$ có lớn hơn 3 hay không?\\\\", False),
        ("Học lớp 10 thật vui!\\\\", False),
        ("Bạn có thích học Toán không?\\\\", False),
        ("Hãy cẩn thận đấy!\\\\", False),
        ("Trời hôm nay nắng đẹp quá!\\\\", False)
    ]

    # BƯỚC 2: Xử lý Random
    # Chọn ngẫu nhiên 5 câu từ nhóm mệnh đề toán học và 3 câu từ nhóm còn lại (Tổng 8 câu như ảnh)
    selected_math = random.sample(pool_menh_de_toan_hoc, 5)
    selected_non_math = random.sample(pool_khong_phai_menh_de, 3)

    all_sentences = selected_math + selected_non_math
    random.shuffle(all_sentences)

    # Xác định đáp án đúng (số lượng mệnh đề toán học)
    correct_count = sum(1 for _, is_math in all_sentences if is_math)

    # BƯỚC 3: Tạo nội dung hiển thị
    noidungcauhoi = "Các câu sau đây, có bao nhiêu câu là mệnh đề toán học?\\\\ \n"
    for i, (text, _) in enumerate(all_sentences, 1):
        noidungcauhoi += f"({i}) {text}\n"

    # Tạo danh sách liệt kê cho lời giải
    cac_cau_dung = [str(i+1) for i, (_, is_math) in enumerate(all_sentences) if is_math]
    loigiai = f"Các câu ({', '.join(cac_cau_dung)}) là những mệnh đề toán học. Vậy có tất cả ${correct_count}$ câu là mệnh đề toán học."

    # BƯỚC 4: Tạo các đáp án nhiễu
    da_d = '\\True ' + f'${correct_count}$'
    others = set()
    while len(others) < 3:
        fake = random.randint(2, 7)
        if fake != correct_count:
            others.add(f'${fake}$')
    others_list = list(others)

    da_s1 = others_list[0]
    da_s2 = others_list[1]
    da_s3 = others_list[2]

    # Trộn đáp án
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # BƯỚC 5: Xuất câu trắc nghiệm theo mẫu
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

