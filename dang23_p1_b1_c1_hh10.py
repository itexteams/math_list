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


def bt_dang23_p1_b1_c1_hh10(self):
            # Khai báo biến
            # B3: Suy nghĩ cách random
            # Khai báo dữ liệu chỉ cho 2 khoảng: (0; 90) và (90; 180)
            # Tích hợp danh sách các đáp án đúng (trues) và đáp án sai (falses) để random linh hoạt
            data_goc = [
                {
                    "goc": "(0^\\circ; 90^\\circ)",
                    "trues": [
                        "$\\sin\\alpha$ và $\\cos\\alpha$ cùng dấu",
                        "Tích $\\sin\\alpha.\\cos\\alpha$ mang dấu dương",
                        "$\\tan\\alpha > 0$",
                        "$\\cot\\alpha > 0$",
                        "$\\sin\\alpha$ và $\\tan\\alpha$ cùng dấu"
                    ],
                    "falses": [
                        "$\\sin\\alpha$ và $\\cos\\alpha$ trái dấu",
                        "Tích $\\sin\\alpha.\\cos\\alpha$ mang dấu âm",
                        "$\\tan\\alpha < 0$",
                        "$\\cot\\alpha < 0$",
                        "$\\cos\\alpha < 0$",
                        "$\\sin\\alpha$ và $\\tan\\alpha$ trái dấu"
                    ],
                    "loigiai_base": "Với $\\alpha \\in (0^\\circ; 90^\\circ)$, ta có $\\sin\\alpha > 0, \\cos\\alpha > 0$ suy ra $\\tan\\alpha > 0, \\cot\\alpha > 0$."
                },
                {
                    "goc": "(90^\\circ; 180^\\circ)",
                    "trues": [
                        "Tích $\\sin\\alpha.\\cot\\alpha$ mang dấu âm",
                        "$\\sin\\alpha$ và $\\cos\\alpha$ trái dấu",
                        "Tích $\\sin\\alpha.\\cos\\alpha$ mang dấu âm",
                        "$\\cos\\alpha < 0$",
                        "$\\tan\\alpha < 0$",
                        "$\\cot\\alpha < 0$"
                    ],
                    "falses": [
                        "$\\sin\\alpha$ và $\\cot\\alpha$ cùng dấu",
                        "Tích $\\sin\\alpha.\\cos\\alpha$ mang dấu dương",
                        "$\\sin\\alpha$ và $\\tan\\alpha$ cùng dấu",
                        "$\\cos\\alpha > 0$",
                        "$\\tan\\alpha > 0$",
                        "$\\sin\\alpha$ và $\\cos\\alpha$ cùng dấu"
                    ],
                    "loigiai_base": "Với $\\alpha \\in (90^\\circ; 180^\\circ)$, ta có $\\sin\\alpha > 0, \\cos\\alpha < 0$ suy ra $\\tan\\alpha < 0, \\cot\\alpha < 0$."
                }
            ]

            # Random chọn 1 trong 2 trường hợp góc
            bai_toan = random.choice(data_goc)

            # Bốc thăm ngẫu nhiên 1 đáp án đúng và 3 đáp án sai
            da_dung_text = random.choice(bai_toan["trues"])
            da_sai_list = random.sample(bai_toan["falses"], 3)

            # B2: Viết lại đề bài và lời giải
            # Câu hỏi
            noidungcauhoi = f"Cho góc $\\alpha \\in {bai_toan['goc']}$. Khẳng định nào sau đây đúng?"

            # Các đáp án
            da_d = '\\True ' + da_dung_text
            da_s1 = da_sai_list[0]
            da_s2 = da_sai_list[1]
            da_s3 = da_sai_list[2]

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên vị trí
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải: Nối phần giải thích gốc với mệnh đề đúng vừa được random
            loigiai = f"{bai_toan['loigiai_base']}\\\\\nVậy mệnh đề đúng là: {da_dung_text.replace('.', '')}"

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

