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


def bt_dang17_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Sinh tần số ngẫu nhiên cho các điểm từ 0 đến 10
                f0 = random.randint(0, 2)
                f1 = random.randint(0, 3)
                f2 = random.randint(1, 5)
                f3 = random.randint(3, 8)
                f4 = random.randint(5, 12)
                f5 = random.randint(10, 20)
                f6 = random.randint(15, 25)
                f7 = random.randint(15, 30)
                f8 = random.randint(10, 20)
                f9 = random.randint(5, 15)
                f10 = random.randint(1, 5)

                freqs = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
                N = sum(freqs)

                # Tạo mảng dữ liệu thô để tìm trung vị
                data = []
                for score, f in enumerate(freqs):
                    data.extend([score] * f)

                # Xác định giá trị trung vị
                if N % 2 != 0:
                    pos = (N + 1) // 2
                    Me = data[pos - 1]
                    Me_str = str(Me)
                    loigiai_calc = f"giá trị ở vị trí thứ {pos} là {Me} nên $M_e = {Me_str}$."
                else:
                    pos1 = N // 2
                    pos2 = N // 2 + 1
                    val1 = data[pos1 - 1]
                    val2 = data[pos2 - 1]
                    Me = (val1 + val2) / 2

                    # Sửa lỗi: Chuyển về float trước khi dùng is_integer()
                    if float(Me).is_integer():
                        Me = int(Me)
                        Me_str = str(Me)
                    else:
                        Me_str = str(Me).replace('.', ',')

                    if val1 == val2:
                        loigiai_calc = f"giá trị ở vị trí thứ {pos1} và {pos2} đều là {val1} nên $M_e = {Me_str}$."
                    else:
                        loigiai_calc = f"giá trị ở vị trí thứ {pos1} và {pos2} là {val1} và {val2} nên $M_e = \\frac{{{val1}+{val2}}}{{2}} = {Me_str}$."

                # Đáp án đúng
                da = f"$M_e = {Me_str}$"

                # Sinh các đáp án nhiễu
                distractors = set()
                while len(distractors) < 3:
                    delta = random.choice([-1.5, -1, -0.5, 0.5, 1, 1.5])
                    fake_Me = Me + delta
                    if 0 <= fake_Me <= 10:
                        # Sửa lỗi: Chuyển fake_Me về float trước khi gọi is_integer()
                        if float(fake_Me).is_integer():
                            fake_Me_str = str(int(fake_Me))
                        else:
                            fake_Me_str = str(fake_Me).replace('.', ',')

                        fake_ans = f"$M_e = {fake_Me_str}$"
                        if fake_ans != da:
                            distractors.add(fake_ans)

                distractors = list(distractors)
                das1 = distractors[0]
                das2 = distractors[1]
                das3 = distractors[2]

                # Tạo bảng LaTeX
                table_str = "\\begin{center}\n\\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|}\n\\hline\n"
                table_str += "Điểm & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\\\\n\\hline\n"
                table_str += "Tần số & " + " & ".join(map(str, freqs)) + " \\\\\n\\hline\n\\end{tabular}\n\\end{center}"

                # Câu hỏi
                noidungcauhoi = (f"Để khảo sát kết quả thi tuyển sinh môn Toán trong kì thi tuyển sinh đại học năm vừa qua của trường A, "
                                 f"người ta chọn một mẫu gồm {N} học sinh tham gia kì thi tuyển sinh đó. Điểm môn Toán của các học sinh được cho ở bảng tần số sau đây:\n"
                                 f"{table_str}\n"
                                 f"Số trung vị của mẫu số liệu trên là bao nhiêu?")

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f"Cỡ mẫu $N={N}$.\\\\\n"
                           f"Sắp xếp điểm của {N} học sinh theo thứ tự không giảm thì {loigiai_calc}")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

