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


def bt_dang26_p1_b1_c1_ds10(self):
    # Khai báo biến
    # ---------------------------------------------------------
    kho_menh_de = []

    # Mệnh đề 1: x < 1/x (Đúng)
    val_I = random.randint(-5, -2)
    kho_menh_de.append({
        "noidung": r"$\exists x \in \mathbb{Z} : x < \frac{1}{x}$.",
        "loigiai": r"(I) Đúng vì $\exists x = %s \in \mathbb{Z}$ thỏa mãn." % val_I,
        "dung": True
    })

    # Mệnh đề 2: a^n > 0 (Đúng)
    base_II = random.choice([2, 3, 5])
    kho_menh_de.append({
        "noidung": r"$\forall n \in \mathbb{N} : %s^n > 0$." % base_II,
        "loigiai": r"(II) Đúng vì lũy thừa với cơ số dương luôn dương.",
        "dung": True
    })

    # Mệnh đề 3: x^2 - k = 0 (Đúng nếu k là số chính phương)
    k_III = random.choice([4, 9, 16])
    kho_menh_de.append({
        "noidung": r"$\exists x \in \mathbb{Q} : x^2 - %s = 0$." % k_III,
        "loigiai": r"(III) Đúng vì có nghiệm hữu tỷ $x = %s$." % int(k_III**0.5),
        "dung": True
    })

    # Mệnh đề 4: Chia hết (Đúng)
    c_IV = random.choice([2, 5])
    a_IV, b_IV = c_IV*2, c_IV*3
    kho_menh_de.append({
        "noidung": r"$\forall n \in \mathbb{N} : %sn^2 + %s$ chia hết cho $%s$." % (a_IV, b_IV, c_IV),
        "loigiai": r"(IV) Đúng vì $%sn^2 + %s = %s(%sn^2 + %s)$ chia hết cho %s." % (a_IV, b_IV, c_IV, a_IV//c_IV, b_IV//c_IV, c_IV),
        "dung": True
    })

    # Mệnh đề 5: x^2 + 1 = 0 (Sai)
    kho_menh_de.append({
        "noidung": r"$\exists x \in \mathbb{R} : x^2 + 1 = 0$.",
        "loigiai": r"(V) Sai vì $x^2 + 1 \ge 1 > 0$ với mọi $x$.",
        "dung": False
    })

    # Mệnh đề 6: Số nguyên tố (Sai)
    kho_menh_de.append({
        "noidung": r"Mọi số nguyên tố đều là số lẻ.",
        "loigiai": r"(VI) Sai vì số 2 là số nguyên tố chẵn.",
        "dung": False
    })

    # ---------------------------------------------------------
    # BƯỚC 2: RANDOM LẤY 4 MỆNH ĐỀ VÀ TÍNH TOÁN KẾT QUẢ
    # ---------------------------------------------------------
    # Lấy ngẫu nhiên 4 mệnh đề từ kho
    selected = random.sample(kho_menh_de, 4)

    # Xác định số lượng mệnh đề đúng
    count_true = sum(1 for item in selected if item['dung'])

    # Xây dựng nội dung hiển thị
    noidungcauhoi = "Số mệnh đề đúng trong các mệnh đề sau:\n\\begin{enumerate}[(I)]\n"
    loigiai_tong_hop = ""

    for i in range(4):
        noidungcauhoi += f"    \\item {selected[i]['noidung']}\n"
        loigiai_tong_hop += f"    \\item {selected[i]['loigiai']} \n"

    noidungcauhoi += "\\end{enumerate}"
    loigiai = f"Ta xét từng mệnh đề:\n\\begin{{itemize}}\n{loigiai_tong_hop}\\end{{itemize}}\nVậy có {count_true} mệnh đề đúng."

    # ---------------------------------------------------------
    # BƯỚC 3: TẠO ĐÁP ÁN TRẮC NGHIỆM
    # ---------------------------------------------------------
    da_dung = f"\\True {count_true}"
    # Tạo các đáp án nhiễu (0, 1, 2, 3, 4 trừ đáp án đúng)
    all_choices = [str(i) for i in range(5)]
    all_choices.remove(str(count_true))
    random.shuffle(all_choices)

    list_1 = [da_dung, all_choices[0], all_choices[1], all_choices[2]]
    random.shuffle(list_1)

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\n\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('--','+').replace('+-','-').replace('-+','-').replace('10x','10 x').replace('+0x','').replace('-0x','').replace('11x','11 x').replace('1x','x').replace('10y','10 y').replace('+0y','').replace('-0y','').replace('11y','11 y').replace('1y','y').replace('10t','10 t').replace('+0t','').replace('-0t','').replace('11t','11 t').replace('1t','t')
    return content

