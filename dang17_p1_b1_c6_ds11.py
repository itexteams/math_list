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


def bt_dang17_p1_b1_c6_ds11(self):
            # Khai báo biến
            # Ta có thể random t1, t2 là "lẻ" hoặc "chẵn"

            tinh_chat = ["lẻ", "chẵn"]
            t1 = random.choice(tinh_chat) # Tính chất lần gieo 1
            t2 = random.choice(tinh_chat) # Tính chất lần gieo 2

            # Xác định tập hợp các số tương ứng
            set_le = [1, 3, 5]
            set_chan = [2, 4, 6]

            s1 = set_le if t1 == "lẻ" else set_chan
            s2 = set_le if t2 == "lẻ" else set_chan

            # Tính tập hợp AB
            res_list = []
            for i in s1:
                for j in s2:
                    res_list.append(f"\\left({i},{j}\\right)")

            kq = len(res_list) # kq luôn bằng 9 đối với xúc sắc 6 mặt chia đôi chẵn lẻ

            # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
            s = [8, 10, 11, 12, 6, 7]
            random.shuffle(s)

            das1 = s.pop()
            das2 = s.pop()
            das3 = s.pop()

            # Câu hỏi
            noidungcauhoi = (
                "Gieo một con xúc xắc cân đối, đồng nhất hai lần liên tiếp. Xét các biến cố: \\\\"
                "A: “số chấm xuất hiện ở lần gieo thứ nhất là số " + t1 + "” \\\\"
                "B: “số chấm xuất hiện ở lần gieo thứ hai là số " + t2 + "” .\\\\"
                "Phát biểu nào sau đây là đúng?"
            )

            # Các đáp án
            da_d = "\\True $n\\left(AB\\right) = " + str(kq) + "$"
            da_s1 = "$n\\left(AB\\right) = " + str(das1) + "$"
            da_s2 = "$n\\left(AB\\right) = " + str(das2) + "$"
            da_s3 = "$n\\left(AB\\right) = " + str(das3) + "$"

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # B2: Nội dung lời giải chi tiết theo mẫu
            chuoi_tap_hop = ", ".join(res_list)
            loigiai = (
                "Tập hợp các kết quả thuận lợi cho biến cố $A$ là $S_1 = \\left\\{" + ", ".join(map(str, s1)) + "\\right\\}$. \\\\"
                "Tập hợp các kết quả thuận lợi cho biến cố $B$ là $S_2 = \\left\\{" + ", ".join(map(str, s2)) + "\\right\\}$.\\\\"
                "Biến cố giao $AB$ là tập hợp các cặp số chấm $\\left(i,j\\right)$ trong đó $i \\in S_1$ và $j \\in S_2$.\\\\"
                "Ta có: $AB = \\left\\{" + chuoi_tap_hop + "\\right\\}$.\\\\"
                "Vậy $n\\left(AB\\right) = " + str(kq) + "$."
            )

            # Xuất câu trắc nghiệm (Không dùng tiền tố r, dùng \left( \right))
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\choice \n'
                '{' + list_1[0] + '}\n'
                '{' + list_1[1] + '}\n'
                '{' + list_1[2] + '}\n'
                '{' + list_1[3] + '}\n'
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

